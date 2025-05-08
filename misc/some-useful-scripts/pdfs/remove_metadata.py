import argparse
import os
import re
import tempfile
import shutil
import fitz  # PyMuPDF

def parse_page_range(page_range_str, num_pages):
    """
    Parse a page range string like "1-3,5,7-9" into a set of zero-based page indices.
    """
    pages = set()
    for part in page_range_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            start = int(start) - 1
            end = int(end) - 1
            pages.update(range(max(start, 0), min(end + 1, num_pages)))
        else:
            idx = int(part) - 1
            if 0 <= idx < num_pages:
                pages.add(idx)
    return pages

def remove_metadata(input_pdf, output_pdf, verbose=False):
    if verbose:
        print(f"Reading input PDF: {input_pdf}")
    
    doc = fitz.open(input_pdf)
    
    if verbose:
        print("Removing metadata...")
    
    # Clear all metadata
    doc.set_metadata({})
    
    if verbose:
        print(f"Writing output PDF: {output_pdf}")
    
    doc.save(output_pdf)
    doc.close()
    
    if verbose:
        print("Done.")

def remove_watermark(input_pdf, output_pdf, watermark_patterns=None, verbose=False, page_range=None):
    if watermark_patterns is None:
        watermark_patterns = [
            # IEEE Xplore style watermarks
            re.compile(r"Authorized\s*licensed\s*use\s*limited\s*to:.*?Restrictions\s*apply\.", re.IGNORECASE | re.DOTALL),
            re.compile(r"Downloaded\s*on.*?from\s*IEEE\s*Xplore", re.IGNORECASE | re.DOTALL),
            re.compile(r"Downloaded\s*from\s*.+?\s*on\s*\w+\s*\d{1,2},\s*\d{4}\s*at\s*\d{2}:\d{2}:\d{2}\s*UTC", re.IGNORECASE),
            re.compile(r"Downloaded\s*from\s*.+?\s*on\s*\w+\s*\d{1,2},\s*\d{4}", re.IGNORECASE),
            re.compile(r"Downloaded\s*from\s*.*", re.IGNORECASE),
            re.compile(r"Authorized\s*licensed\s*use\s*limited\s*to:.*?downloaded.*", re.IGNORECASE | re.DOTALL),

            # Licensed to ... Prepared on ... for download from IP ...
            re.compile(
            r"Licensed\s+to\s+.+?\.\s+Prepared\s+on\s+\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\w+\s+\d{4}for\s+download\s+from\s+IP\s+\d{1,3}(?:\.\d{1,3}){3}\.",
            re.IGNORECASE
            ),
            re.compile(
            r"Licensed\s+to\s+.+?\.\s+Prepared\s+on\s+\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\w+\s+\d{4}.*?download\s+from\s+IP\s+\d{1,3}(?:\.\d{1,3}){3}\.",
            re.IGNORECASE
            ),

            # Additional publisher watermarks
            re.compile(r"Downloaded\s*from\s*ScienceDirect.*", re.IGNORECASE),
            re.compile(r"©\s*\d{4}\s*Elsevier\s*Ltd\.", re.IGNORECASE),
            re.compile(r"Provided\s*by\s*.+?\s*Library", re.IGNORECASE),
            re.compile(r"Downloaded\s*on\s*.+?\s*from\s*SpringerLink", re.IGNORECASE),
            re.compile(r"Copyright\s*ACM.*For\s*personal\s*use", re.IGNORECASE | re.DOTALL),
            re.compile(r"This\s*content\s*downloaded\s*from", re.IGNORECASE),
            re.compile(r"Downloaded\s*by\s*.+?\s*at\s*", re.IGNORECASE),
            re.compile(r"©\s*\d{4}\s*.+?\s*All\s*rights\s*reserved", re.IGNORECASE),
            re.compile(r"Downloaded\s*from\s*Cambridge\s*Core", re.IGNORECASE),
            re.compile(r"Downloaded\s*from\s*Wiley\s*Online\s*Library", re.IGNORECASE),
            re.compile(r"For\s*Review\s*Only", re.IGNORECASE),

            # SIAM watermarks
            re.compile(r"Downloaded\s*\d{2}/\d{2}/\d{2}\s*to\s*\d+\.\d+\.\d+\.\d+.*Redistribution\s*subject\s*to\s*SIAM\s*license\s*or\s*copyright;\s*see\s*https://epubs\.siam\.org/terms-privacy", re.IGNORECASE),
            re.compile(r"Copyright.*by\s*SIAM\.\s*Unauthorized\s*reproduction\s*of\s*this\s*article\s*is\s*prohibited", re.IGNORECASE),

            # MR reference review watermark
            re.compile(r"\[\s*MR\d+.*?for\s*reviewing\s*purposes\s*only\s*\]", re.IGNORECASE),
            re.compile(r"\[\s*Review\s+Copy\s+Only\s*\]", re.IGNORECASE),

            # Additional review watermarks
            re.compile(r"Under\s*Review", re.IGNORECASE),
            re.compile(r"Submitted\s*to\s*.*", re.IGNORECASE),
            re.compile(r"Manuscript\s*submitted\s*to\s*.*", re.IGNORECASE),
            re.compile(r"For\s*Peer\s*Review", re.IGNORECASE),
            re.compile(r"Confidential:\s*For\s*Review\s*Purposes\s*Only", re.IGNORECASE),
            re.compile(r"REVIEW\s*COPY", re.IGNORECASE),
            re.compile(r"For\s*Conference\s*Review", re.IGNORECASE),
            re.compile(r"Not\s*for\s*Public\s*Release", re.IGNORECASE),
            re.compile(r"Submitted\s*for\s*Publication", re.IGNORECASE),
            re.compile(r"Under\s*Consideration\s*for\s*Publication", re.IGNORECASE),
            re.compile(r"Pending\s*Review", re.IGNORECASE),
            re.compile(r"Manuscript\s*ID:\s*.*", re.IGNORECASE),
            re.compile(r"Paper\s*#\s*\d+", re.IGNORECASE),
            re.compile(r"arXiv:\s*\d+\.\d+v\d+", re.IGNORECASE),
            re.compile(r"This\s*article\s*has\s*not\s*been\s*peer[\s-]reviewed", re.IGNORECASE),
            re.compile(r"Preliminary\s*version", re.IGNORECASE),
            re.compile(r"Version\s*for\s*peer\s*review", re.IGNORECASE),
            re.compile(r"Unpublished\s*manuscript", re.IGNORECASE),
        ]
    
    # Enhanced DOI pattern to match any DOI format (with or without prefix)
    doi_pattern = re.compile(r'(?:doi:?\s*|DOI\s+|https?://(?:dx\.)?doi\.org/)?10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+', re.IGNORECASE)

    if verbose:
        print(f"Reading input PDF: {input_pdf}")
    
    doc = fitz.open(input_pdf)
    num_pages = len(doc)
    pages_to_process = set(range(num_pages))
    if page_range:
        pages_to_process = parse_page_range(page_range, num_pages)
        if verbose:
            print(f"Processing only pages: {sorted([p+1 for p in pages_to_process])}")

    for i in range(num_pages):
        if i not in pages_to_process:
            continue
        page = doc[i]
        if verbose:
            print(f"Processing page {i+1}/{num_pages}")
        
        # Extract text
        text = page.get_text()
        
        # Search for watermark patterns
        for pattern in watermark_patterns:
            for match in pattern.finditer(text):
                matched_text = match.group()
                
                # Skip if the text contains a DOI
                if doi_pattern.search(matched_text):
                    if verbose:
                        print(f"Skipping watermark containing DOI: {matched_text}")
                    continue
                
                if verbose:
                    print(f"Found watermark: {matched_text}")
                
                # Search for the text on the page
                text_instances = page.search_for(matched_text)
                
                # To avoid white boxes, use redaction with fill=None and keep_appearance=True,
                # which tries to preserve the background as much as possible.
                for inst in text_instances:
                    annot = page.add_redact_annot(inst)
                    annot.set_colors(stroke=None, fill=None)
                    annot.update()
                
                # Apply all redactions on the page
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
    
    # Remove metadata
    if verbose:
        print("Removing metadata...")
    doc.set_metadata({})
    
    if verbose:
        print(f"Writing output PDF: {output_pdf}")
    
    doc.save(output_pdf)
    doc.close()
    
    if verbose:
        print("Done.")

def main():
    parser = argparse.ArgumentParser(
        description="Remove metadata and watermarks from PDF while preserving clickable URLs and selectable text."
    )
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument(
        "-i", "--inplace", action="store_true", help="Overwrite the input PDF file"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print progress details"
    )
    parser.add_argument(
        "-p", "--watermark-pages", type=str, default=None,
        help="Page range to remove watermarks, e.g. '1-3,5,7-9' (1-based)"
    )
    args = parser.parse_args()

    print(f"Processing file: {args.input_pdf}")

    try:
        # Create a temporary file for output
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            temp_output = tmp_file.name

        # Always remove watermarks (option --remove-watermark is ignored)
        remove_watermark(
            args.input_pdf,
            temp_output,
            verbose=args.verbose,
            page_range=args.watermark_pages
        )

        if args.inplace:
            # Replace original file with processed file
            shutil.move(temp_output, args.input_pdf)
            output_pdf = args.input_pdf
        else:
            # Create new file with _no_metadata suffix
            base, ext = os.path.splitext(args.input_pdf)
            output_pdf = f"{base}_no_metadata{ext}"
            shutil.move(temp_output, output_pdf)

        print(f"Successfully processed PDF. Output saved to: {output_pdf}")
    except Exception as e:
        # Clean up temporary file if something went wrong
        if 'temp_output' in locals():
            try:
                os.unlink(temp_output)
            except:
                pass
        print(f"Failed to process PDF: {e}")

if __name__ == "__main__":
    main()