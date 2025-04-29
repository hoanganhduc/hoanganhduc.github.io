import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional
import tempfile
import datetime
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import threading
import webbrowser
import io
import contextlib
from tkinter import messagebox

def check_pdf_formal_digital_signature(pdf_path: Path, verbose=False):
    """
    Checks if the PDF contains a formal digital signature (not GPG).
    Prints details if verbose.
    Returns True if a digital signature is found, False otherwise.
    """
    try:
        # Attempt to use PdfReader (already imported at the top)
        pass
    except ImportError:
        print("❌ PyPDF2 is required for digital signature detection. Install with: pip install PyPDF2")
        return False

    try:
        reader = PdfReader(str(pdf_path))
        if "/AcroForm" in reader.trailer["/Root"]:
            acroform = reader.trailer["/Root"]["/AcroForm"]
            sig_fields = []
            if "/Fields" in acroform:
                for field in acroform["/Fields"]:
                    field_obj = field.get_object()
                    ft = None
                    if hasattr(field_obj, "get"):
                        ft = field_obj.get("/FT")
                    if ft == "/Sig" or "/Sig" in str(ft or ""):
                        sig_fields.append(field_obj)
                if sig_fields:
                    if verbose:
                        print(f"🔏 PDF {pdf_path} contains {len(sig_fields)} formal digital signature field(s).")
                    else:
                        print(f"🔏 {len(sig_fields)} formal digital signature(s) found in {pdf_path}")
                    for idx, sig in enumerate(sig_fields, 1):
                        sig_dict = None
                        if hasattr(sig, "get"):
                            sig_dict = sig.get("/V")
                            if hasattr(sig_dict, "get_object"):
                                sig_dict = sig_dict.get_object()
                        if sig_dict and hasattr(sig_dict, "get"):
                            signer = sig_dict.get("/Name", "Unknown")
                            location = sig_dict.get("/Location", "Unknown")
                            reason = sig_dict.get("/Reason", "Unknown")
                            contact = sig_dict.get("/ContactInfo", "Unknown")
                            date = sig_dict.get("/M", "Unknown")
                            if verbose:
                                print(f"  📝 Signature {idx}:")
                                print(f"    👤 Signer: {signer}")
                                print(f"    📍 Location: {location}")
                                print(f"    💡 Reason: {reason}")
                                print(f"    📧 Contact: {contact}")
                                print(f"    📅 Date: {date}")
                        else:
                            if verbose:
                                print(f"  📝 Signature {idx}: ⚠️ No signature dictionary found.")
                    return True
        if verbose:
            print(f"❌ PDF {pdf_path} does not contain a formal digital signature field.")
        else:
            print(f"❌ 0 formal digital signature(s) found in {pdf_path}")
        return False
    except Exception as e:
        if verbose:
            print(f"❌ Error checking digital signature: {e}")
        else:
            print(f"❌ 0 formal digital signature(s) found in {pdf_path}")
        return False
    
def batch_check_pdf_formal_digital_signatures(directory: Path, verbose=False):
    """
    Batch check all PDFs in a directory (recursively) for formal digital signatures (not GPG).
    Prints details for each PDF if verbose.
    """
    pdf_files = list(directory.rglob("*.pdf"))
    found_count = 0
    not_found_count = 0
    for pdf_path in pdf_files:
        try:
            has_sig = check_pdf_formal_digital_signature(pdf_path, verbose)
            if has_sig:
                print(f"✅ {pdf_path}: FORMAL DIGITAL SIGNATURE FOUND")
                found_count += 1
            else:
                print(f"❌ {pdf_path}: No formal digital signature")
                not_found_count += 1
        except Exception as e:
            print(f"❌ {pdf_path}: Error checking signature: {e}")
            not_found_count += 1
    print(f"\nSummary: {found_count} with formal digital signature, {not_found_count} without, out of {len(pdf_files)} PDF(s).")

SIGNATURE_MARKER = b"\n%%GPG_SIGNATURE_START%%\n"
SIGNATURE_END_MARKER = b"\n%%GPG_SIGNATURE_END%%\n"

def verbose_print(verbose, *args, **kwargs):
    if verbose:
        print(*args, **kwargs)

def gpg_sign_pdf(pdf_path: Path, gpg_key: Optional[str], verbose=False) -> bytes:
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

def gpg_embed_signature(pdf_path: Path, signature: bytes, output_path: Path, overwrite=False, verbose=False):
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

def _find_gpg_signature_markers(data: bytes):
    """
    Find GPG signature markers in PDF data.
    Handles signatures embedded by this tool as well as potentially other software.
    
    Returns:
        tuple: (start position, end position) of the signature block
        
    Raises:
        ValueError: If no recognizable signature format is found
    """
    # Check for our standard markers
    start = data.find(SIGNATURE_MARKER)
    if start != -1:
        end = data.find(SIGNATURE_END_MARKER, start + len(SIGNATURE_MARKER))
        if end != -1:
            return start, end
    
    # Try alternative signature formats
    # Common PGP/GPG markers
    pgp_markers = [
        (b"-----BEGIN PGP SIGNATURE-----", b"-----END PGP SIGNATURE-----"),
        (b"-----BEGIN GPG SIGNATURE-----", b"-----END GPG SIGNATURE-----"),
        # Additional common markers from various tools and standards
        (b"-----BEGIN PGP SIGNED MESSAGE-----", b"-----END PGP SIGNATURE-----"),
        (b"-----BEGIN DIGITAL SIGNATURE-----", b"-----END DIGITAL SIGNATURE-----"),
        (b"-----BEGIN SIGNED MESSAGE-----", b"-----END SIGNED MESSAGE-----"),
        (b"-----BEGIN DETACHED SIGNATURE-----", b"-----END DETACHED SIGNATURE-----"),
        (b"-----BEGIN PGP MESSAGE-----", b"-----END PGP MESSAGE-----"),
        (b"%%GPG-SIG-START%%", b"%%GPG-SIG-END%%"),
        (b"<!-- GPG SIGNATURE -->", b"<!-- END GPG SIGNATURE -->"),
        (b"%%%SIGNATURE_START%%%", b"%%%SIGNATURE_END%%%"),
        (b"<SIGNATURE>", b"</SIGNATURE>"),
        (b"##PGP_SIG_BEGIN##", b"##PGP_SIG_END##"),
        (b"=====BEGIN PGP SIGNATURE=====", b"=====END PGP SIGNATURE====="),
        (b"[SIG_START]", b"[SIG_END]"),
        (b"<<<GPG SIGNATURE>>>", b"<<<END GPG SIGNATURE>>>"),
        (b"__SIG_BEGIN__", b"__SIG_END__"),
    ]
    
    for start_marker, end_marker in pgp_markers:
        start = data.find(start_marker)
        if start != -1:
            end = data.find(end_marker, start)
            if end != -1:
                # Include the end marker in the result
                return start, end + len(end_marker)
    
    # No recognized signature format found
    raise ValueError("❗ No GPG signature markers found in PDF. If this PDF is signed, it may use an unsupported signature format.")

def _extract_key_id_from_gpg_signature(signature: bytes) -> Optional[str]:
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

def _ensure_gpg_key_present(key_id: str, verbose=False):
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

def gpg_extract_signature(pdf_path: Path, verbose=False):
    """
    Extracts GPG signatures from a signed PDF.
    Returns the original PDF content and a list of extracted signatures.
    
    Args:
        pdf_path: Path to the signed PDF file
        verbose: Whether to print verbose information
        
    Returns:
        Tuple of (original_pdf_bytes, signatures_list)
        If multiple signatures exist, signatures_list will contain multiple items
    """
    with open(pdf_path, "rb") as f:
        data = f.read()
    
    # Original data before we start removing signatures
    original_data = data
    signatures = []
    
    # Extract all signatures iteratively
    while True:
        try:
            start, end = _find_gpg_signature_markers(data)
            signature = data[start + len(SIGNATURE_MARKER):end]
            signatures.append(signature)
            
            # Remove this signature block from data for next iteration
            data = data[:start]
            
            key_id = _extract_key_id_from_gpg_signature(signature)
            if key_id:
                _ensure_gpg_key_present(key_id, verbose)
                verbose_print(verbose, f"🔑 Found signature with key ID: {key_id}")
            else:
                verbose_print(verbose, "⚠️ Could not extract key ID from signature.")
        except ValueError:
            # No more signatures found
            break
    
    if not signatures:
        raise ValueError("No GPG signatures found in the PDF")
    
    # The original PDF is what remains after removing all signatures
    original_pdf = data
    
    verbose_print(verbose, f"🔍 Extracted {len(signatures)} signature(s) from PDF")
    verbose_print(verbose, f"📄 Original PDF size: {len(original_pdf)} bytes")
    
    return original_pdf, signatures[0] if len(signatures) == 1 else signatures

def gpg_verify_signed_pdf(pdf_path: Path, verbose=False) -> bool:
    """
    Verifies the signature embedded in a signed PDF.
    Returns True if valid, False otherwise.
    Prints information about the GPG key used for signing and the sign time.
    Adds icons to make output prettier.
    Handles the case where no signature is embedded.
    Prints more information in case of failure.
    Also prints the name of the input PDF.
    """
    print(f"🔎 GPG signature verification: {pdf_path}")
    try:
        original_pdf, signature = gpg_extract_signature(pdf_path, verbose)
        # Handle case where multiple signatures are returned (as a list)
        valid_signatures = 0
        signatures_to_verify = []
        if isinstance(signature, list):
            if verbose:
                verbose_print(True, f"📝 Found {len(signature)} signatures, verifying each one.")
            signatures_to_verify = signature
        else:
            signatures_to_verify = [signature]
        
        total_signatures = len(signatures_to_verify)
    except ValueError as e:
        print(f"❌ No GPG signature embedded in PDF: {e}")
        print(f"❌ 0 valid GPG signatures found in {pdf_path}")
        return False
    except Exception as e:
        print(f"❌ Failed to extract GPG signature: {e}")
        print(f"❌ 0 valid GPG signatures found in {pdf_path}")
        return False

    # Verify each signature
    for idx, sig in enumerate(signatures_to_verify, 1):
        if verbose and total_signatures > 1:
            verbose_print(True, f"🔍 Verifying signature {idx} of {total_signatures}")

        # Extract sign time from the signature block
        sign_time = None
        for line in sig.splitlines():
            if line.startswith(b"sign_time:"):
                try:
                    sign_time = line[len(b"sign_time:"):].decode("utf-8")
                except Exception:
                    sign_time = None
                break
        if sign_time and verbose:
            verbose_print(True, f"⏰ GPG sign time: {sign_time}")

        with tempfile.NamedTemporaryFile(delete=False, mode="wb") as pdf_tmp, tempfile.NamedTemporaryFile(delete=False, mode="wb") as sig_tmp:
            pdf_tmp.write(original_pdf)
            pdf_tmp.flush()
            # Remove the sign_time line from the signature before verifying
            sig_lines = sig.splitlines(keepends=True)
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
            valid_signatures += 1
            if verbose:
                verbose_print(verbose, f"✅ GPG signature {idx} is valid.")
                # Extract key info from GPG status output
                for line in proc.stdout.splitlines():
                    if line.startswith("[GNUPG:] GOODSIG"):
                        parts = line.split()
                        if len(parts) >= 4:
                            key_id = parts[2]
                            name_email = " ".join(parts[3:])
                            verbose_print(True, f"🔑 GPG signed by key ID: {key_id}")
                            verbose_print(True, f"👤 Name/Email: {name_email}")
                            if "<" in name_email and ">" in name_email:
                                user_name = name_email.split("<")[0].strip()
                                user_email = name_email[name_email.find("<"):].strip()
                                verbose_print(True, f"   👤 Name: {user_name}")
                                verbose_print(True, f"   📧 Email: {user_email}")
                    elif line.startswith("[GNUPG:] VALIDSIG"):
                        parts = line.split()
                        if len(parts) >= 10:
                            fingerprint = parts[2]
                            verbose_print(True, f"🖊️ GPG key fingerprint: {fingerprint}")
                    elif line.startswith("[GNUPG:] TRUST_ULTIMATE"):
                        verbose_print(True, "🌟 GPG trust level: ULTIMATE")
                    elif line.startswith("[GNUPG:] TRUST_FULLY"):
                        verbose_print(True, "👍 GPG trust level: FULLY TRUSTED")
                    elif line.startswith("[GNUPG:] TRUST_MARGINAL"):
                        verbose_print(True, "⚠️ GPG trust level: MARGINAL")
                    elif line.startswith("[GNUPG:] TRUST_UNDEFINED"):
                        verbose_print(True, "❓ GPG trust level: UNDEFINED")
                    elif line.startswith("[GNUPG:] TRUST_NEVER"):
                        verbose_print(True, "🚫 GPG trust level: NEVER TRUSTED")
        else:
            if verbose:
                if "no signature found" in proc.stderr.lower() or "no signature found" in proc.stdout.lower():
                    verbose_print(True, f"❌ Signature {idx} - No GPG signature found for verification.")
                elif "can't open" in proc.stderr.lower() or "can't open" in proc.stdout.lower():
                    verbose_print(True, f"❌ Signature {idx} - Cannot extract GPG signature for verification.")
                else:
                    verbose_print(True, f"❌ Signature {idx} - GPG signature verification failed: {proc.stderr.strip() or proc.stdout.strip()}")

    # Print summary
    if valid_signatures > 0:
        print(f"✅ {valid_signatures} valid GPG signature(s) found in {pdf_path}")
        return True
    else:
        print(f"❌ 0 valid GPG signatures found in {pdf_path}")
        return False

def batch_gpg_sign_pdfs(directory: Path, gpg_key: Optional[str], overwrite=False, verbose=False):
    pdf_files = list(directory.glob("*.pdf"))
    verbose_print(verbose, f"📂 Found {len(pdf_files)} PDF(s) in {directory}")
    for pdf_path in pdf_files:
        output_path = pdf_path.with_suffix(".gpgsigned.pdf")
        if output_path.exists() and not overwrite:
            verbose_print(verbose, f"⏭️ Skipping {output_path} (already exists)")
            print(f"⏭️ Skipped {pdf_path} (output exists)")
            continue
        try:
            signature = gpg_sign_pdf(pdf_path, gpg_key, verbose)
            gpg_embed_signature(pdf_path, signature, output_path, overwrite, verbose)
            print(f"✅ Signed {pdf_path} -> {output_path}")
        except Exception as e:
            print(f"❌ Error signing {pdf_path}: {e}", file=sys.stderr)
            print(f"❌ Failed to sign {pdf_path}")

def handle_gpg_sign(args):
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
        signature = gpg_sign_pdf(args.pdf, args.key, args.verbose)
        gpg_embed_signature(args.pdf, signature, output, args.overwrite, args.verbose)
        print(f"✅ Signed PDF saved to {output}")
        if args.inplace:
            args.pdf.write_bytes(output.read_bytes())
            print(f"♻️ Input file {args.pdf} overwritten with signed PDF.")
            try:
                output.unlink()
                verbose_print(args.verbose, f"🗑️ Removed signed output file {output} after inplace overwrite.")
            except Exception as e:
                verbose_print(args.verbose, f"⚠️ Could not remove {output}: {e}")
    except Exception as e:
        print(f"❌ Failed to sign PDF: {e}", file=sys.stderr)

def handle_gpg_batch_sign(args):
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
            signature = gpg_sign_pdf(pdf_path, args.key, args.verbose)
            gpg_embed_signature(pdf_path, signature, output_path, args.overwrite, args.verbose)
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

def handle_gpg_extract(args):
    original_pdf, signature = gpg_extract_signature(args.pdf, args.verbose)
    orig_path = args.pdf.with_suffix(".orig.pdf")
    sig_path = args.pdf.with_suffix(".asc")
    with open(orig_path, "wb") as f:
        f.write(original_pdf)
    with open(sig_path, "wb") as f:
        f.write(signature)
    verbose_print(args.verbose, f"📄 Original PDF saved to {orig_path}")
    verbose_print(args.verbose, f"🔏 GPG signature saved to {sig_path}")

def handle_gpg_verify(args):
    try:
        result = gpg_verify_signed_pdf(args.pdf, args.verbose)
        
        # Try to extract the original PDF and signatures to get the count
        try:
            _, signatures = gpg_extract_signature(args.pdf, False)  # Don't show verbose output here
            # Handle if signatures is returned as a single signature or a list
            sig_count = len(signatures) if isinstance(signatures, list) else 1
            if result:
                print(f"✅ {sig_count} GPG signature(s) verified as VALID. The PDF is authentic.")
            else:
                print(f"❌ Found {sig_count} GPG signature(s), but verification FAILED. The PDF may have been tampered with.")
        except:
            # Fall back to simple message if we can't determine signature count
            if result:
                print("✅ The GPG signature is VALID and the PDF is authentic.")
            else:
                print("❌ The GPG signature is INVALID, missing, or the PDF has been tampered with.")
    except Exception as e:
        print(f"❌ Error during verification: {e}")

def handle_gpg_batch_verify(args):
    pdf_files = list(args.directory.rglob("*.pdf"))
    verbose_print(args.verbose, f"🔎 Found {len(pdf_files)} PDF(s) in {args.directory} (recursively)")
    valid_count = 0
    invalid_count = 0
    for pdf_path in pdf_files:
        try:
            result = gpg_verify_signed_pdf(pdf_path, args.verbose)
            
            # Try to determine the number of signatures for better reporting
            sig_count = "unknown number of"
            try:
                _, signatures = gpg_extract_signature(pdf_path, False)  # Don't show verbose output here
                # Handle if signatures is returned as a single signature or a list
                sig_count = len(signatures) if isinstance(signatures, list) else 1
            except Exception:
                pass
                
            if result:
                print(f"✅ {pdf_path}: {sig_count} GPG SIGNATURE(S) VALID")
                valid_count += 1
            else:
                print(f"❌ {pdf_path}: GPG SIGNATURE(S) INVALID or not signed")
                invalid_count += 1
        except Exception as e:
            print(f"❌ {pdf_path}: Error during GPG signature verification: {e}")
            invalid_count += 1
    print(f"\nSummary: {valid_count} files with valid GPG signature(s), {invalid_count} with invalid or no signatures out of {len(pdf_files)} PDF(s).")

def handle_gui_mode():

    def run_in_thread(fn):
        def wrapper(*args, **kwargs):
            threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True).start()
        return wrapper

    class PDFGPGGui(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("🔏 PDF GPG Sign/Verify Tool")
            self.geometry("900x750")
            self.configure(bg="#f5f6fa")
            self.pdf_path = tk.StringVar()
            self.key_id = tk.StringVar()
            self.verbose = tk.BooleanVar()
            self.dir_path = tk.StringVar()
            self.inplace = tk.BooleanVar()
            self.batch_inplace = tk.BooleanVar()
            self.create_widgets()
            self.style_widgets()

        def create_widgets(self):
            # Header
            header = tk.Label(self, text="PDF GPG Sign/Verify Tool", font=("Segoe UI", 22, "bold"), fg="#273c75", bg="#f5f6fa")
            header.pack(pady=(18, 8))

            # PDF File Selection
            file_frame = tk.Frame(self, bg="#f5f6fa")
            file_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Label(file_frame, text="PDF File:", font=("Segoe UI", 12), bg="#f5f6fa").pack(side="left")
            tk.Entry(file_frame, textvariable=self.pdf_path, width=60, font=("Segoe UI", 11)).pack(side="left", padx=(8, 0))
            tk.Button(file_frame, text="Browse...", command=self.browse_pdf, font=("Segoe UI", 10, "bold"), bg="#00a8ff", fg="white", activebackground="#0097e6").pack(side="left", padx=8)

            # Directory Selection for batch
            dir_frame = tk.Frame(self, bg="#f5f6fa")
            dir_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Label(dir_frame, text="PDF Directory (batch):", font=("Segoe UI", 12), bg="#f5f6fa").pack(side="left")
            tk.Entry(dir_frame, textvariable=self.dir_path, width=50, font=("Segoe UI", 11)).pack(side="left", padx=(8, 0))
            tk.Button(dir_frame, text="Browse...", command=self.browse_dir, font=("Segoe UI", 10, "bold"), bg="#00a8ff", fg="white", activebackground="#0097e6").pack(side="left", padx=8)

            # GPG Key ID
            key_frame = tk.Frame(self, bg="#f5f6fa")
            key_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Label(key_frame, text="GPG Key ID/Email (optional):", font=("Segoe UI", 12), bg="#f5f6fa").pack(side="left")
            tk.Entry(key_frame, textvariable=self.key_id, width=40, font=("Segoe UI", 11)).pack(side="left", padx=(8, 0))

            # Verbose Checkbox
            verbose_frame = tk.Frame(self, bg="#f5f6fa")
            verbose_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Checkbutton(verbose_frame, text="Verbose Output", variable=self.verbose, font=("Segoe UI", 11), bg="#f5f6fa").pack(side="left")

            # Inplace Checkbox for single sign
            inplace_frame = tk.Frame(self, bg="#f5f6fa")
            inplace_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Checkbutton(inplace_frame, text="Inplace (overwrite input PDF after signing)", variable=self.inplace, font=("Segoe UI", 11), bg="#f5f6fa").pack(side="left")

            # Action Buttons
            btn_frame = tk.Frame(self, bg="#f5f6fa")
            btn_frame.pack(pady=10)
            tk.Button(btn_frame, text="✍️ Sign PDF", command=self.sign_pdf, font=("Segoe UI", 12, "bold"), bg="#44bd32", fg="white", width=15, activebackground="#4cd137").grid(row=0, column=0, padx=8, pady=4)
            tk.Button(btn_frame, text="🔎 Verify PDF", command=self.verify_pdf, font=("Segoe UI", 12, "bold"), bg="#273c75", fg="white", width=15, activebackground="#40739e").grid(row=0, column=1, padx=8, pady=4)
            tk.Button(btn_frame, text="📤 Extract Signature", command=self.extract_signature, font=("Segoe UI", 12, "bold"), bg="#e1b12c", fg="white", width=15, activebackground="#fbc531").grid(row=0, column=2, padx=8, pady=4)
            # Removed "Check Formal Signature" button

            # Batch Inplace Checkbox
            batch_inplace_frame = tk.Frame(self, bg="#f5f6fa")
            batch_inplace_frame.pack(fill="x", padx=30, pady=(0, 10))
            tk.Checkbutton(batch_inplace_frame, text="Batch Inplace (overwrite input PDFs after signing)", variable=self.batch_inplace, font=("Segoe UI", 11), bg="#f5f6fa").pack(side="left")

            # Batch Action Buttons
            batch_btn_frame = tk.Frame(self, bg="#f5f6fa")
            batch_btn_frame.pack(pady=10)
            tk.Button(batch_btn_frame, text="🔁 Batch Sign PDFs", command=self.batch_sign_pdfs, font=("Segoe UI", 12, "bold"), bg="#00b894", fg="white", width=18, activebackground="#00cec9").grid(row=0, column=0, padx=8, pady=4)
            tk.Button(batch_btn_frame, text="🔎 Batch Verify PDFs", command=self.batch_verify_pdfs, font=("Segoe UI", 12, "bold"), bg="#636e72", fg="white", width=18, activebackground="#b2bec3").grid(row=0, column=1, padx=8, pady=4)

            # Output Frame
            output_label = tk.Label(self, text="Output Log:", font=("Segoe UI", 12, "bold"), bg="#f5f6fa", fg="#353b48")
            output_label.pack(anchor="w", padx=30, pady=(10, 0))

            output_frame = tk.Frame(self, bg="#f5f6fa")
            output_frame.pack(fill="both", expand=True, padx=30, pady=(0, 10))
            self.output_text = tk.Text(output_frame, height=16, wrap="word", font=("Consolas", 11), bg="#f0f0f0", fg="#353b48", borderwidth=2, relief="groove")
            self.output_text.pack(side="left", fill="both", expand=True)
            scrollbar = tk.Scrollbar(output_frame, command=self.output_text.yview)
            scrollbar.pack(side="right", fill="y")
            self.output_text.config(yscrollcommand=scrollbar.set)

            # Footer
            footer = tk.Frame(self, bg="#f5f6fa")
            footer.pack(fill="x", side="bottom", pady=(0, 8))
            tk.Label(footer, text="Made with ❤️ | ", font=("Segoe UI", 10), bg="#f5f6fa", fg="#718093").pack(side="left")
            link = tk.Label(footer, text="GitHub Project", font=("Segoe UI", 10, "underline"), fg="#0097e6", bg="#f5f6fa", cursor="hand2")
            link.pack(side="left")
            link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/your-repo/pdf-gpg-sign"))
            tk.Label(footer, text=" | 2024", font=("Segoe UI", 10), bg="#f5f6fa", fg="#718093").pack(side="left")

        def style_widgets(self):
            try:
                import tkinter.ttk as ttk
                style = ttk.Style()
                style.theme_use("clam")
            except Exception:
                pass

        def browse_pdf(self):
            path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if path:
                self.pdf_path.set(path)

        def browse_dir(self):
            path = filedialog.askdirectory()
            if path:
                self.dir_path.set(path)

        def log(self, msg):
            self.output_text.insert("end", msg + "\n")
            self.output_text.see("end")

        def clear_log(self):
            self.output_text.delete("1.0", "end")

        def verbose_log(self, *args, **kwargs):
            if self.verbose.get():
                msg = " ".join(str(a) for a in args)
                self.log(msg)

        @run_in_thread
        def sign_pdf(self):
            self.clear_log()
            pdf = self.pdf_path.get()
            key = self.key_id.get() or None
            verbose = self.verbose.get()
            inplace = self.inplace.get()
            if not pdf:
                messagebox.showerror("Error", "Please select a PDF file.")
                return
            try:
                self.log(f"✍️ Signing PDF: {pdf}")
                signature = gpg_sign_pdf(Path(pdf), key, verbose)
                output_path = Path(pdf).with_suffix(".gpgsigned.pdf")
                gpg_embed_signature(Path(pdf), signature, output_path, overwrite=True, verbose=verbose)
                self.log(f"✅ Signed PDF saved to {output_path}")
                if inplace:
                    Path(pdf).write_bytes(output_path.read_bytes())
                    self.log(f"♻️ Input file {pdf} overwritten with signed PDF.")
                    try:
                        output_path.unlink()
                        self.verbose_log(f"🗑️ Removed signed output file {output_path} after inplace overwrite.")
                    except Exception as e:
                        self.verbose_log(f"⚠️ Could not remove {output_path}: {e}")
                if verbose:
                    self.log("Signature created and embedded successfully.")
            except Exception as e:
                self.log(f"❌ Failed to sign PDF: {e}")

        @run_in_thread
        def verify_pdf(self):
            self.clear_log()
            pdf = self.pdf_path.get()
            verbose = self.verbose.get()
            if not pdf:
                messagebox.showerror("Error", "Please select a PDF file.")
                return
            try:
                self.log(f"🔎 Verifying PDF: {pdf}")
                # Patch verbose_print to log to GUI if verbose
                orig_verbose_print = globals().get("verbose_print")
                def gui_verbose_print(v, *args, **kwargs):
                    if v:
                        self.log(" ".join(str(a) for a in args))
                globals()["verbose_print"] = gui_verbose_print
                
                # Get the verification result
                result = gpg_verify_signed_pdf(Path(pdf), verbose)
                
                # Try to extract signatures to count them
                try:
                    original_pdf, signatures = gpg_extract_signature(Path(pdf), False)
                    # Handle if signatures is returned as a single signature or a list
                    sig_count = len(signatures) if isinstance(signatures, list) else 1
                    if result:
                        self.log(f"✅ {sig_count} GPG signature(s) verified as VALID. The PDF is authentic.")
                    else:
                        self.log(f"❌ Found {sig_count} GPG signature(s), but verification FAILED. The PDF may have been tampered with.")
                except Exception as e:
                    # Fall back to simple message if we can't determine signature count
                    if result:
                        self.log("✅ The GPG signature is VALID and the PDF is authentic.")
                    else:
                        self.log("❌ The GPG signature is INVALID, missing, or the PDF has been tampered with.")
                        self.verbose_log(f"Error extracting signatures: {e}")
                
                # Also check for formal digital signature
                formal_result = False
                formal_info = []
                try:
                    reader = PdfReader(str(pdf))
                    if "/AcroForm" in reader.trailer["/Root"]:
                        acroform = reader.trailer["/Root"]["/AcroForm"]
                        sig_fields = []
                        if "/Fields" in acroform:
                            for field in acroform["/Fields"]:
                                field_obj = field.get_object()
                                ft = None
                                if hasattr(field_obj, "get"):
                                    ft = field_obj.get("/FT")
                                if ft == "/Sig" or "/Sig" in str(ft or ""):
                                    sig_fields.append(field_obj)
                            if sig_fields:
                                formal_result = True
                                for idx, sig in enumerate(sig_fields, 1):
                                    sig_dict = None
                                    if hasattr(sig, "get"):
                                        sig_dict = sig.get("/V")
                                        if hasattr(sig_dict, "get_object"):
                                            sig_dict = sig_dict.get_object()
                                    if sig_dict and hasattr(sig_dict, "get"):
                                        signer = sig_dict.get("/Name", "Unknown")
                                        location = sig_dict.get("/Location", "Unknown")
                                        reason = sig_dict.get("/Reason", "Unknown")
                                        contact = sig_dict.get("/ContactInfo", "Unknown")
                                        date = sig_dict.get("/M", "Unknown")
                                        formal_info.append(
                                            f"  📝 Signature {idx}:\n"
                                            f"    👤 Signer: {signer}\n"
                                            f"    📍 Location: {location}\n"
                                            f"    💡 Reason: {reason}\n"
                                            f"    📧 Contact: {contact}\n"
                                            f"    📅 Date: {date}"
                                        )
                                    else:
                                        formal_info.append(f"  📝 Signature {idx}: ⚠️ No signature dictionary found.")
                except Exception as e:
                    if verbose:
                        self.log(f"❌ Error checking digital signature: {e}")
                globals()["verbose_print"] = orig_verbose_print
                
                if formal_result:
                    self.log(f"🔏 {len(formal_info)} formal digital signature(s) FOUND in PDF.")
                    if verbose and formal_info:
                        self.log("Formal digital signature details:")
                        for info in formal_info:
                            self.log(info)
                else:
                    self.log("❌ No formal digital signature found in PDF.")
            except Exception as e:
                self.log(f"❌ Verification failed: {e}")

        @run_in_thread
        def extract_signature(self):
            self.clear_log()
            pdf = self.pdf_path.get()
            verbose = self.verbose.get()
            if not pdf:
                messagebox.showerror("Error", "Please select a PDF file.")
                return
            try:
                self.log(f"📤 Extracting signature from: {pdf}")
                # Patch verbose_print to log to GUI if verbose
                orig_verbose_print = globals().get("verbose_print")
                def gui_verbose_print(v, *args, **kwargs):
                    if v:
                        self.log(" ".join(str(a) for a in args))
                globals()["verbose_print"] = gui_verbose_print
                
                original_pdf, signatures = gpg_extract_signature(Path(pdf), verbose)
                globals()["verbose_print"] = orig_verbose_print
                
                # Handle multiple signatures
                if isinstance(signatures, list):
                    self.log(f"Found {len(signatures)} GPG signatures in the PDF")
                    for i, sig in enumerate(signatures, 1):
                        sig_path = Path(pdf).with_suffix(f".sig{i}.asc")
                        with open(sig_path, "wb") as f:
                            f.write(sig)
                        self.log(f"🔏 GPG signature {i} saved to {sig_path}")
                else:
                    # Single signature
                    sig_path = Path(pdf).with_suffix(".asc")
                    with open(sig_path, "wb") as f:
                        f.write(signatures)
                    self.log(f"🔏 GPG signature saved to {sig_path}")
                
                # Save the original PDF
                orig_path = Path(pdf).with_suffix(".orig.pdf")
                with open(orig_path, "wb") as f:
                    f.write(original_pdf)
                self.log(f"📄 Original PDF saved to {orig_path}")
                
                if verbose:
                    self.log("Signature(s) extracted and saved successfully.")
            except Exception as e:
                self.log(f"❌ Extraction failed: {e}")

        @run_in_thread
        def batch_sign_pdfs(self):
            self.clear_log()
            dir_path = self.dir_path.get()
            key = self.key_id.get() or None
            verbose = self.verbose.get()
            inplace = self.batch_inplace.get()
            if not dir_path:
                messagebox.showerror("Error", "Please select a directory for batch signing.")
                return
            try:
                self.log(f"🔁 Batch signing PDFs in: {dir_path}")
                pdf_files = list(Path(dir_path).rglob("*.pdf"))
                self.log(f"Found {len(pdf_files)} PDF(s) to sign.")
                for pdf_path in pdf_files:
                    try:
                        self.log(f"✍️ Signing: {pdf_path}")
                        signature = gpg_sign_pdf(pdf_path, key, verbose)
                        output_path = pdf_path.with_suffix(".gpgsigned.pdf")
                        gpg_embed_signature(pdf_path, signature, output_path, overwrite=True, verbose=verbose)
                        self.log(f"✅ Signed {pdf_path} -> {output_path}")
                        if inplace:
                            pdf_path.write_bytes(output_path.read_bytes())
                            self.log(f"♻️ Input file {pdf_path} overwritten with signed PDF.")
                            try:
                                output_path.unlink()
                                self.verbose_log(f"🗑️ Removed signed output file {output_path} after inplace overwrite.")
                            except Exception as e:
                                self.verbose_log(f"⚠️ Could not remove {output_path}: {e}")
                        if verbose:
                            self.log("Signature created and embedded successfully.")
                    except Exception as e:
                        self.log(f"❌ Failed to sign {pdf_path}: {e}")
                self.log("🔁 Batch signing completed.")
            except Exception as e:
                self.log(f"❌ Batch signing failed: {e}")

        @run_in_thread
        def batch_verify_pdfs(self):
            self.clear_log()
            dir_path = self.dir_path.get()
            verbose = self.verbose.get()
            if not dir_path:
                messagebox.showerror("Error", "Please select a directory for batch verification.")
                return
            try:
                self.log(f"🔎 Batch verifying PDFs in: {dir_path}")
                pdf_files = list(Path(dir_path).rglob("*.pdf"))
                self.log(f"Found {len(pdf_files)} PDF(s) to verify.")
                valid_count = 0
                invalid_count = 0
                formal_sig_count = 0
                
                for pdf_path in pdf_files:
                    try:
                        # Patch verbose_print to log to GUI if verbose
                        orig_verbose_print = globals().get("verbose_print")
                        def gui_verbose_print(v, *args, **kwargs):
                            if v:
                                self.log(" ".join(str(a) for a in args))
                        globals()["verbose_print"] = gui_verbose_print
                        
                        # Verify GPG signatures
                        result = gpg_verify_signed_pdf(pdf_path, verbose)
                        
                        # Try to get the signature count
                        sig_count = "unknown number of"
                        try:
                            _, signatures = gpg_extract_signature(pdf_path, False)
                            sig_count = len(signatures) if isinstance(signatures, list) else 1
                        except Exception:
                            pass
                        
                        # Also check for formal digital signature and collect info
                        formal_result = False
                        formal_info = []
                        try:
                            reader = PdfReader(str(pdf_path))
                            if "/AcroForm" in reader.trailer["/Root"]:
                                acroform = reader.trailer["/Root"]["/AcroForm"]
                                sig_fields = []
                                if "/Fields" in acroform:
                                    for field in acroform["/Fields"]:
                                        field_obj = field.get_object()
                                        ft = None
                                        if hasattr(field_obj, "get"):
                                            ft = field_obj.get("/FT")
                                        if ft == "/Sig" or "/Sig" in str(ft or ""):
                                            sig_fields.append(field_obj)
                                    if sig_fields:
                                        formal_result = True
                                        formal_sig_count += 1
                                        for idx, sig in enumerate(sig_fields, 1):
                                            sig_dict = None
                                            if hasattr(sig, "get"):
                                                sig_dict = sig.get("/V")
                                                if hasattr(sig_dict, "get_object"):
                                                    sig_dict = sig_dict.get_object()
                                            if sig_dict and hasattr(sig_dict, "get"):
                                                signer = sig_dict.get("/Name", "Unknown")
                                                location = sig_dict.get("/Location", "Unknown")
                                                reason = sig_dict.get("/Reason", "Unknown")
                                                contact = sig_dict.get("/ContactInfo", "Unknown")
                                                date = sig_dict.get("/M", "Unknown")
                                                formal_info.append(
                                                    f"  📝 Signature {idx}:\n"
                                                    f"    👤 Signer: {signer}\n"
                                                    f"    📍 Location: {location}\n"
                                                    f"    💡 Reason: {reason}\n"
                                                    f"    📧 Contact: {contact}\n"
                                                    f"    📅 Date: {date}"
                                                )
                                            else:
                                                formal_info.append(f"  📝 Signature {idx}: ⚠️ No signature dictionary found.")
                        except Exception as e:
                            if verbose:
                                self.log(f"❌ Error checking digital signature: {e}")
                        
                        globals()["verbose_print"] = orig_verbose_print
                        
                        # Show results for this file
                        if result:
                            self.log(f"✅ {pdf_path}: {sig_count} GPG SIGNATURE(S) VALID")
                            valid_count += 1
                        else:
                            self.log(f"❌ {pdf_path}: GPG SIGNATURE(S) INVALID or not signed")
                            invalid_count += 1
                        
                        if formal_result:
                            self.log(f"🔏 {pdf_path}: {len(formal_info)} formal digital signature(s) FOUND")
                            if verbose and formal_info:
                                self.log("Formal digital signature details:")
                                for info in formal_info:
                                    self.log(info)
                        else:
                            self.log(f"❌ {pdf_path}: No formal digital signature found")
                            
                    except Exception as e:
                        self.log(f"❌ {pdf_path}: Error during verification: {e}")
                        invalid_count += 1
                
                # Show summary
                self.log(f"\nSummary:")
                self.log(f"✅ {valid_count} PDFs with valid GPG signature(s)")
                self.log(f"❌ {invalid_count} PDFs with invalid or no GPG signature")
                self.log(f"🔏 {formal_sig_count} PDFs with formal digital signature(s)")
                self.log(f"📄 {len(pdf_files)} total PDF(s) processed")
                self.log("🔎 Batch verification completed.")
            except Exception as e:
                self.log(f"❌ Batch verification failed: {e}")

    app = PDFGPGGui()
    app.mainloop()

def check_requirements(verbose=False):
    """
    Checks for required external software and Python libraries.
    Prints missing dependencies and returns True if all are present, False otherwise.
    """
    import importlib.util
    required_software = ["gpg"]
    required_python_libs = ["PyPDF2"]

    # Check external software
    missing_software = []
    for sw in required_software:
        if not any(
            os.access(os.path.join(path, sw), os.X_OK)
            or os.access(os.path.join(path, sw + ".exe"), os.X_OK)
            for path in os.environ.get("PATH", "").split(os.pathsep)
        ):
            missing_software.append(sw)

    # Check Python libraries
    missing_libs = []
    for lib in required_python_libs:
        if importlib.util.find_spec(lib) is None:
            missing_libs.append(lib)

    if missing_software:
        print("❌ Missing required software:", ", ".join(missing_software))
    if missing_libs:
        print("❌ Missing required Python libraries:", ", ".join(missing_libs))
        print("   Install with: pip install " + " ".join(missing_libs))
    if not missing_software and not missing_libs:
        if verbose:
            print("✅ All required software and libraries are present.")
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="🔏 Sign PDF with GPG and embed GPG signature.")
    subparsers = parser.add_subparsers(dest="command")

    sign_parser = subparsers.add_parser("sign", help="✍️ Sign a single PDF with GPG and embed the GPG signature")
    sign_parser.add_argument("pdf", type=Path, help="PDF file to sign with GPG")
    sign_parser.add_argument("-k", "--key", type=str, help="GPG key ID/email to use for signing")
    sign_parser.add_argument("-o", "--output", type=Path, help="Output file (default: <pdf>.gpgsigned.pdf)")
    sign_parser.add_argument("--overwrite", action="store_true", help="Overwrite output file if it exists")
    sign_parser.add_argument("--inplace", action="store_true", help="After GPG signing, overwrite the input file with the signed output")
    sign_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for GPG operations")

    batch_parser = subparsers.add_parser("batch", help="🔁 Batch sign all PDFs in a directory (recursively) with GPG")
    batch_parser.add_argument("directory", type=Path, help="Directory containing PDFs to GPG sign")
    batch_parser.add_argument("-k", "--key", type=str, help="GPG key ID/email to use for signing")
    batch_parser.add_argument("--overwrite", action="store_true", help="Overwrite output files if they exist")
    batch_parser.add_argument("--inplace", action="store_true", help="After GPG signing, overwrite each input file with the signed output")
    batch_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for GPG operations")

    extract_parser = subparsers.add_parser("extract", help="📤 Extract embedded GPG signature and original PDF")
    extract_parser.add_argument("pdf", type=Path, help="Signed PDF file with embedded GPG signature")
    extract_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for GPG extraction")

    verify_parser = subparsers.add_parser("verify", help="🔎 Verify the embedded GPG signature of a signed PDF")
    verify_parser.add_argument("pdf", type=Path, help="Signed PDF file with embedded GPG signature")
    verify_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for GPG verification")

    batch_verify_parser = subparsers.add_parser("batch-verify", help="🔎 Batch verify embedded GPG signatures in all PDFs in a directory (recursively)")
    batch_verify_parser.add_argument("directory", type=Path, help="Directory containing PDFs with embedded GPG signatures")
    batch_verify_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for GPG verification")

    gui_parser = subparsers.add_parser("gui", help="🖥️ Launch the GUI for PDF GPG signing and verification")

    args = parser.parse_args()

    # Check requirements before running any command except help
    if args.command is not None and args.command != "gui":
        if not check_requirements(getattr(args, "verbose", False)):
            print("❌ Please install the missing requirements and try again.")
            sys.exit(1)
    elif args.command == "gui":
        # For GUI, check requirements and show error if missing
        if not check_requirements():
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Missing Requirements", "Some required software or Python libraries are missing.\nPlease install them and try again.")
            sys.exit(1)

    if args.command == "sign":
        handle_gpg_sign(args)
    elif args.command == "batch":
        handle_gpg_batch_sign(args)
    elif args.command == "extract":
        handle_gpg_extract(args)
    elif args.command == "verify":
        handle_gpg_verify(args)
        check_pdf_formal_digital_signature(args.pdf, args.verbose)
    elif args.command == "batch-verify":
        handle_gpg_batch_verify(args)
        batch_check_pdf_formal_digital_signatures(args.directory, args.verbose)
    elif args.command == "gui":
        handle_gui_mode()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()