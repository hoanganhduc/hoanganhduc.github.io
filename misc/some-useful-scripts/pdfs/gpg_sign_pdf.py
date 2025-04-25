import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional
import tempfile
import datetime

SIGNATURE_MARKER = b"\n%%GPG_SIGNATURE_START%%\n"
SIGNATURE_END_MARKER = b"\n%%GPG_SIGNATURE_END%%\n"

def verbose_print(verbose, *args, **kwargs):
    if verbose:
        print(*args, **kwargs)

def sign_pdf(pdf_path: Path, gpg_key: Optional[str], verbose=False) -> bytes:
    verbose_print(verbose, f"📝 Signing PDF: {pdf_path}")
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    gpg_cmd = ["gpg", "--detach-sign", "--armor", "--output", "-", "--sign"]
    if gpg_key:
        gpg_cmd.extend(["--local-user", gpg_key])
    proc = subprocess.run(gpg_cmd, input=pdf_data, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(f"❌ GPG signing failed: {proc.stderr.decode()}")
    signature = proc.stdout
    verbose_print(verbose, f"✍️ Signature size: {len(signature)} bytes")
    return signature

def embed_signature(pdf_path: Path, signature: bytes, output_path: Path, overwrite=False, verbose=False):
    if output_path.exists() and not overwrite:
        raise FileExistsError(f"⚠️ {output_path} exists. Use --overwrite to replace.")
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    # Add sign time in ISO format (UTC), using timezone-aware datetime and print timezone
    sign_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    sign_time_bytes = sign_time.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(pdf_data)
        f.write(SIGNATURE_MARKER)
        f.write(b"sign_time:")
        f.write(sign_time_bytes)
        f.write(b"\n")
        f.write(signature)
        f.write(SIGNATURE_END_MARKER)
    verbose_print(verbose, f"📎 Signature embedded into {output_path} at {sign_time} (timezone: UTC)")

def _find_signature_markers(data: bytes):
    start = data.find(SIGNATURE_MARKER)
    end = data.find(SIGNATURE_END_MARKER, start + len(SIGNATURE_MARKER))
    if start == -1 or end == -1:
        raise ValueError("❗ Signature markers not found in PDF.")
    return start, end

def _extract_key_id_from_signature(signature: bytes) -> Optional[str]:
    # Try to find keyid in the signature using gpg --list-packets
    with tempfile.NamedTemporaryFile(delete=False, mode="wb") as sig_tmp:
        sig_tmp.write(signature)
        sig_tmp.flush()
        sig_tmp_path = sig_tmp.name
    key_id = None
    try:
        proc = subprocess.run(
            ["gpg", "--list-packets", sig_tmp_path],
            capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        for line in proc.stdout.splitlines():
            if "keyid" in line:
                parts = line.split("keyid")
                if len(parts) > 1:
                    key_id = parts[1].strip().split()[0]
                    break
    finally:
        os.unlink(sig_tmp_path)
    return key_id

def _ensure_key_present(key_id: str, verbose=False):
    proc = subprocess.run(
        ["gpg", "--list-keys", key_id],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if proc.returncode == 0 and key_id in proc.stdout:
        verbose_print(verbose, f"🔑 GPG key {key_id} is already present locally.")
        return
    print(f"ℹ️ GPG key {key_id} not found locally. Attempting to import from keyservers...")
    
    # First try without specifying a keyserver
    recv_proc = subprocess.run(
        ["gpg", "--recv-keys", key_id],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    
    if recv_proc.returncode == 0:
        verbose_print(verbose, f"✅ Imported public key {key_id} using default keyserver.")
        return
        
    # If the default keyserver failed, try specific keyservers
    keyservers = [
            "hkps://keyserver.ubuntu.com",
            "hkps://keys.openpgp.org",
            "hkps://keyring.debian.org",
            "hkps://pgp.mit.edu",
            "hkps://keys.fedoraproject.org",
            "hkps://keyserver.opensuse.org"
        ]
    imported = False
    for ks in keyservers:
        verbose_print(verbose, f"Trying keyserver: {ks}...")
        recv_proc = subprocess.run(
            ["gpg", "--keyserver", ks, "--recv-keys", key_id],
            capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        if recv_proc.returncode == 0:
            print(f"✅ Imported public key {key_id} from {ks}.")
            imported = True
            break
        else:
            verbose_print(verbose, f"⚠️ Failed to import key {key_id} from {ks}: {recv_proc.stderr.strip()}")
    
    if not imported:
        print(f"❌ Could not import key {key_id} from any keyserver. You may need to import it manually.")

def extract_signature(pdf_path: Path, verbose=False):
    with open(pdf_path, "rb") as f:
        data = f.read()
    start, end = _find_signature_markers(data)
    signature = data[start + len(SIGNATURE_MARKER):end]
    original_pdf = data[:start]
    verbose_print(verbose, f"🔍 Extracted signature ({len(signature)} bytes) and original PDF ({len(original_pdf)} bytes)")

    key_id = _extract_key_id_from_signature(signature)
    if key_id:
        _ensure_key_present(key_id, verbose)
    else:
        verbose_print(verbose, "⚠️ Could not extract key ID from signature.")

    return original_pdf, signature

def verify_signed_pdf(pdf_path: Path, verbose=False) -> bool:
    """
    Verifies the signature embedded in a signed PDF.
    Returns True if valid, False otherwise.
    Prints information about the GPG key used for signing and the sign time.
    Adds icons to make output prettier.
    Handles the case where no signature is embedded.
    Prints more information in case of failure.
    """
    try:
        original_pdf, signature = extract_signature(pdf_path, verbose)
    except ValueError as e:
        print(f"❌ No signature embedded in PDF: {e}")
        return False
    except Exception as e:
        print(f"❌ Failed to extract signature: {e}")
        return False

    # Extract sign time from the signature block
    sign_time = None
    for line in signature.splitlines():
        if line.startswith(b"sign_time:"):
            try:
                sign_time = line[len(b"sign_time:"):].decode("utf-8")
            except Exception:
                sign_time = None
            break
    if sign_time:
        verbose_print(True, f"⏰ Sign time: {sign_time}")

    with tempfile.NamedTemporaryFile(delete=False, mode="wb") as pdf_tmp, tempfile.NamedTemporaryFile(delete=False, mode="wb") as sig_tmp:
        pdf_tmp.write(original_pdf)
        pdf_tmp.flush()
        # Remove the sign_time line from the signature before verifying
        sig_lines = signature.splitlines(keepends=True)
        filtered_sig = b"".join(line for line in sig_lines if not line.startswith(b"sign_time:"))
        sig_tmp.write(filtered_sig)
        sig_tmp.flush()
        pdf_tmp_path = pdf_tmp.name
        sig_tmp_path = sig_tmp.name

    gpg_cmd = ["gpg", "--status-fd", "1", "--verify", sig_tmp_path, pdf_tmp_path]
    proc = subprocess.run(gpg_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.unlink(pdf_tmp_path)
    os.unlink(sig_tmp_path)

    key_id = None
    user_name = None
    user_email = None

    if proc.returncode == 0:
        verbose_print(verbose, "✅ Signature is valid.")
        # Extract key info from GPG status output
        for line in proc.stdout.splitlines():
            if line.startswith("[GNUPG:] GOODSIG"):
                parts = line.split()
                if len(parts) >= 4:
                    key_id = parts[2]
                    name_email = " ".join(parts[3:])
                    verbose_print(True, f"🔑 Signed by key ID: {key_id}")
                    verbose_print(True, f"👤 Name/Email: {name_email}")
                    if "<" in name_email and ">" in name_email:
                        user_name = name_email.split("<")[0].strip()
                        user_email = name_email[name_email.find("<"):].strip()
                        verbose_print(True, f"   Name: {user_name}")
                        verbose_print(True, f"   Email: {user_email}")
            elif line.startswith("[GNUPG:] VALIDSIG"):
                parts = line.split()
                if len(parts) >= 10:
                    fingerprint = parts[2]
                    verbose_print(True, f"🖊️ Key fingerprint: {fingerprint}")
            elif line.startswith("[GNUPG:] TRUST_ULTIMATE"):
                verbose_print(True, "🌟 Trust level: ULTIMATE")
            elif line.startswith("[GNUPG:] TRUST_FULLY"):
                verbose_print(True, "👍 Trust level: FULLY TRUSTED")
            elif line.startswith("[GNUPG:] TRUST_MARGINAL"):
                verbose_print(True, "⚠️ Trust level: MARGINAL")
            elif line.startswith("[GNUPG:] TRUST_UNDEFINED"):
                verbose_print(True, "❓ Trust level: UNDEFINED")
            elif line.startswith("[GNUPG:] TRUST_NEVER"):
                verbose_print(True, "🚫 Trust level: NEVER TRUSTED")
        return True
    else:
        if "no signature found" in proc.stderr.lower() or "no signature found" in proc.stdout.lower():
            print("❌ No signature found in the PDF for verification.")
        elif "can't open" in proc.stderr.lower() or "can't open" in proc.stdout.lower():
            print("❌ Cannot extract signature for verification.")
        else:
            print("❌ Signature is not valid.")
            verbose_print(verbose, f"❌ Signature verification failed: {proc.stderr.strip() or proc.stdout.strip()}")
        return False

def batch_sign_pdfs(directory: Path, gpg_key: Optional[str], overwrite=False, verbose=False):
    pdf_files = list(directory.glob("*.pdf"))
    verbose_print(verbose, f"📂 Found {len(pdf_files)} PDF(s) in {directory}")
    for pdf_path in pdf_files:
        output_path = pdf_path.with_suffix(".gpgsigned.pdf")
        if output_path.exists() and not overwrite:
            verbose_print(verbose, f"⏭️ Skipping {output_path} (already exists)")
            print(f"⏭️ Skipped {pdf_path} (output exists)")
            continue
        try:
            signature = sign_pdf(pdf_path, gpg_key, verbose)
            embed_signature(pdf_path, signature, output_path, overwrite, verbose)
            print(f"✅ Signed {pdf_path} -> {output_path}")
        except Exception as e:
            print(f"❌ Error signing {pdf_path}: {e}", file=sys.stderr)
            print(f"❌ Failed to sign {pdf_path}")

def handle_sign(args):
    output = args.output or args.pdf.with_suffix(".gpgsigned.pdf")
    # Check if input PDF is already signed
    try:
        with open(args.pdf, "rb") as f:
            if SIGNATURE_MARKER in f.read():
                print(f"⏭️ Skipped {args.pdf} (already signed)")
                return
    except Exception as e:
        verbose_print(args.verbose, f"⚠️ Could not check if {args.pdf} is signed: {e}")
    try:
        signature = sign_pdf(args.pdf, args.key, args.verbose)
        embed_signature(args.pdf, signature, output, args.overwrite, args.verbose)
        print(f"✅ Signed PDF saved to {output}")
        if args.inplace:
            args.pdf.write_bytes(output.read_bytes())
            print(f"♻️ Input file {args.pdf} overwritten with signed PDF.")
    except Exception as e:
        print(f"❌ Failed to sign PDF: {e}", file=sys.stderr)

def handle_batch(args):
    pdf_files = list(args.directory.rglob("*.pdf"))
    verbose_print(args.verbose, f"📂 Found {len(pdf_files)} PDF(s) in {args.directory} (recursively)")
    for pdf_path in pdf_files:
        output_path = pdf_path.with_suffix(".gpgsigned.pdf")
        # Skip if already signed (contains signature marker)
        try:
            with open(pdf_path, "rb") as f:
                if SIGNATURE_MARKER in f.read():
                    verbose_print(args.verbose, f"⏭️ Skipping {pdf_path} (already signed)")
                    print(f"⏭️ Skipped {pdf_path} (already signed)")
                    continue
        except Exception as e:
            verbose_print(args.verbose, f"⚠️ Could not check if {pdf_path} is signed: {e}")
        if output_path.exists() and not args.overwrite:
            verbose_print(args.verbose, f"⏭️ Skipping {output_path} (already exists)")
            print(f"⏭️ Skipped {pdf_path} (output exists)")
            continue
        try:
            signature = sign_pdf(pdf_path, args.key, args.verbose)
            embed_signature(pdf_path, signature, output_path, args.overwrite, args.verbose)
            print(f"✅ Signed {pdf_path} -> {output_path}")
            if args.inplace:
                pdf_path.write_bytes(output_path.read_bytes())
                print(f"♻️ Input file {pdf_path} overwritten with signed PDF.")
                try:
                    output_path.unlink()
                    verbose_print(args.verbose, f"🗑️ Removed signed output file {output_path} after inplace overwrite.")
                except Exception as e:
                    verbose_print(args.verbose, f"⚠️ Could not remove {output_path}: {e}")
        except Exception as e:
            print(f"❌ Error signing {pdf_path}: {e}", file=sys.stderr)
            print(f"❌ Failed to sign {pdf_path}")

def handle_extract(args):
    original_pdf, signature = extract_signature(args.pdf, args.verbose)
    orig_path = args.pdf.with_suffix(".orig.pdf")
    sig_path = args.pdf.with_suffix(".asc")
    with open(orig_path, "wb") as f:
        f.write(original_pdf)
    with open(sig_path, "wb") as f:
        f.write(signature)
    verbose_print(args.verbose, f"📄 Original PDF saved to {orig_path}")
    verbose_print(args.verbose, f"🔏 Signature saved to {sig_path}")

def handle_verify(args):
    result = verify_signed_pdf(args.pdf, args.verbose)
    if result:
        print("✅ Signature is VALID.")
    else:
        print("❌ Signature is INVALID or not present.")

def main():
    parser = argparse.ArgumentParser(description="🔏 Sign PDF with GPG and embed signature.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sign_parser = subparsers.add_parser("sign", help="✍️ Sign a single PDF")
    sign_parser.add_argument("pdf", type=Path, help="PDF file to sign")
    sign_parser.add_argument("-k", "--key", type=str, help="GPG key ID/email")
    sign_parser.add_argument("-o", "--output", type=Path, help="Output file (default: <pdf>.gpgsigned.pdf)")
    sign_parser.add_argument("--overwrite", action="store_true", help="Overwrite output file")
    sign_parser.add_argument("--inplace", action="store_true", help="After signing, overwrite the input file with the signed output")
    sign_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    batch_parser = subparsers.add_parser("batch", help="🔁 Batch sign all PDFs in a directory")
    batch_parser.add_argument("directory", type=Path, help="Directory containing PDFs")
    batch_parser.add_argument("-k", "--key", type=str, help="GPG key ID/email")
    batch_parser.add_argument("--overwrite", action="store_true", help="Overwrite output files")
    batch_parser.add_argument("--inplace", action="store_true", help="After signing, overwrite each input file with the signed output")
    batch_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    extract_parser = subparsers.add_parser("extract", help="📤 Extract signature and original PDF")
    extract_parser.add_argument("pdf", type=Path, help="Signed PDF file")
    extract_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    verify_parser = subparsers.add_parser("verify", help="🔎 Verify the signature of a signed PDF")
    verify_parser.add_argument("pdf", type=Path, help="Signed PDF file")
    verify_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    if args.command == "sign":
        handle_sign(args)
    elif args.command == "batch":
        handle_batch(args)
    elif args.command == "extract":
        handle_extract(args)
    elif args.command == "verify":
        handle_verify(args)

if __name__ == "__main__":
    main()