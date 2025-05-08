import argparse
import os
import re
import fitz  # PyMuPDF

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

def remove_watermark(input_pdf, output_pdf, watermark_patterns=None, verbose=False):
    if watermark_patterns is None:
        watermark_patterns = [
            # IEEE Xplore style watermarks
            re.compile(r"Authorized licensed use limited to:.*?Restrictions apply\.", re.IGNORECASE | re.DOTALL),
            re.compile(r"Downloaded on.*?from IEEE Xplore", re.IGNORECASE | re.DOTALL),
            re.compile(r"Downloaded from .* on \w+ \d{1,2},\d{4} at \d{2}:\d{2}:\d{2} UTC", re.IGNORECASE),
            re.compile(r"Downloaded from .* on \w+ \d{1,2}, \d{4}", re.IGNORECASE),
            re.compile(r"Downloaded from .*", re.IGNORECASE),
            re.compile(r"Authorized licensed use limited to:.*?downloaded.*", re.IGNORECASE | re.DOTALL),
            
            # Additional publisher watermarks
            re.compile(r"Downloaded from ScienceDirect.*", re.IGNORECASE),
            re.compile(r"© \d{4} Elsevier Ltd\.", re.IGNORECASE),
            re.compile(r"Provided by .* Library", re.IGNORECASE),
            re.compile(r"Downloaded on .* from SpringerLink", re.IGNORECASE),
            re.compile(r"Copyright ACM.*For personal use", re.IGNORECASE | re.DOTALL),
            re.compile(r"This content downloaded from", re.IGNORECASE),
            re.compile(r"Downloaded by .* at ", re.IGNORECASE),
            re.compile(r"© \d{4} .* All rights reserved", re.IGNORECASE),
            re.compile(r"Downloaded from Cambridge Core", re.IGNORECASE),
            re.compile(r"Downloaded from Wiley Online Library", re.IGNORECASE),
            re.compile(r"For Review Only", re.IGNORECASE),
            
            # Standard document watermarks
            re.compile(r"CONFIDENTIAL", re.IGNORECASE),
            re.compile(r"DRAFT\s+DOCUMENT", re.IGNORECASE),
            re.compile(r"DO NOT DISTRIBUTE", re.IGNORECASE),
            re.compile(r"SAMPLE|PREVIEW", re.IGNORECASE),
            re.compile(r"INTERNAL USE ONLY", re.IGNORECASE),
            re.compile(r"PROPRIETARY AND CONFIDENTIAL", re.IGNORECASE),
            re.compile(r"NOT FOR DISTRIBUTION", re.IGNORECASE),
            re.compile(r"RESTRICTED ACCESS", re.IGNORECASE),
            re.compile(r"PREPRINT", re.IGNORECASE),
            re.compile(r"PROOF COPY", re.IGNORECASE),
            
            # MR reference review watermark
            re.compile(r"\[\s*MR\d+.*?for reviewing purposes only\s*\]", re.IGNORECASE),
            re.compile(r"\[\s*Review\s+Copy\s+Only\s*\]", re.IGNORECASE),
            
            # Additional review watermarks
            re.compile(r"Under Review", re.IGNORECASE),
            re.compile(r"Submitted to .*", re.IGNORECASE),
            re.compile(r"Manuscript submitted to .*", re.IGNORECASE),
            re.compile(r"For Peer Review", re.IGNORECASE),
            re.compile(r"Confidential: For Review Purposes Only", re.IGNORECASE),
            re.compile(r"REVIEW COPY", re.IGNORECASE),
            re.compile(r"For Conference Review", re.IGNORECASE),
            re.compile(r"Not for Public Release", re.IGNORECASE),
            re.compile(r"Submitted for Publication", re.IGNORECASE),
            re.compile(r"Under Consideration for Publication", re.IGNORECASE),
            re.compile(r"Pending Review", re.IGNORECASE),
            re.compile(r"Manuscript ID:.*", re.IGNORECASE),
            re.compile(r"Paper #\d+", re.IGNORECASE),
            re.compile(r"arXiv:\d+\.\d+v\d+", re.IGNORECASE),
            re.compile(r"This article has not been peer[ -]reviewed", re.IGNORECASE),
            re.compile(r"Preliminary version", re.IGNORECASE),
            re.compile(r"Version for peer review", re.IGNORECASE),
            re.compile(r"Unpublished manuscript", re.IGNORECASE),
        ]
    
    # Enhanced DOI pattern to match any DOI format (with or without prefix)
    doi_pattern = re.compile(r'(?:doi:?\s*|DOI\s+|https?://(?:dx\.)?doi\.org/)?10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+', re.IGNORECASE)

    if verbose:
        print(f"Reading input PDF: {input_pdf}")
    
    doc = fitz.open(input_pdf)
    
    for i in range(len(doc)):
        page = doc[i]
        if verbose:
            print(f"Processing page {i+1}/{len(doc)}")
        
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
                
                # Search for the text on the page and redact it
                text_instances = page.search_for(matched_text)
                for inst in text_instances:
                    page.add_redact_annot(inst, fill=(1, 1, 1))  # White fill
        
        # Apply redactions
        page.apply_redactions()
    
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove metadata and watermarks from PDF while preserving clickable URLs and selectable text.")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("--inplace", action="store_true", help="Overwrite the input PDF file")
    parser.add_argument("--remove-watermark", action="store_true", help="Attempt to remove watermark text indicating download source/date")
    parser.add_argument("--verbose", action="store_true", help="Print progress details")
    args = parser.parse_args()

    print(f"Processing file: {args.input_pdf}")

    if args.inplace:
        output_pdf = args.input_pdf
    else:
        base, ext = os.path.splitext(args.input_pdf)
        output_pdf = f"{base}_no_metadata{ext}"

    try:
        # Always remove watermark since that's what the user wants
        remove_watermark(args.input_pdf, output_pdf, verbose=args.verbose)
        print(f"Successfully processed PDF. Output saved to: {output_pdf}")
    except Exception as e:
        print(f"Failed to process PDF: {e}")