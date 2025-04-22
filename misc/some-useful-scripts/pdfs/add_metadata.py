import argparse
import os
import subprocess
from PyPDF2 import PdfReader, PdfWriter
import bibtexparser
import json
import rispy
import re

def parse_args():
    parser = argparse.ArgumentParser(description="Insert metadata as a PDF page into an existing PDF file.")
    parser.add_argument('-i', '--input_pdf', required=True, help='Path to the input PDF file')
    parser.add_argument('-o', '--output_pdf', help='Path to the output PDF file')
    parser.add_argument('-s', '--sources', help='Comma-separated list of metadata sources (e.g., file paths or "input_pdf")')
    parser.add_argument('-e', '--entries', help='Comma-separated list of additional entries in the form "field:value"')
    parser.add_argument('-w', '--overwrite', action='store_true', help='Overwrite input PDF if no output is specified')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print detailed progress information')
    parser.add_argument('-n', '--no-metadata-page', action='store_true', help='Only update PDF metadata without inserting a metadata page')
    return parser.parse_args()

def extract_from_pdf(pdf_path, verbose=False):
    """Extract metadata from the input PDF."""
    if verbose:
        print(f"Reading PDF metadata from: {pdf_path}")
    reader = PdfReader(pdf_path)
    metadata = {}
    if reader.metadata:
        for key, value in reader.metadata.items():
            # Remove leading '/' from PDF metadata keys and use as is
            field = key.lstrip('/')
            metadata[field] = value or "None"
            if verbose:
                print(f"  Found field: {field} = {value or 'None'}")
    elif verbose:
        print("  No metadata found in PDF")
    return metadata

def parse_bibtex(bib_path, verbose=False):
    """Parse a BibTeX file and return its entries."""
    if verbose:
        print(f"Parsing BibTeX file: {bib_path}")
    with open(bib_path, 'r', encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    if bib_database.entries:
        # Take the first entry; assumes the file describes one document
        entry = bib_database.entries[0]
        if verbose:
            print(f"  Found {len(entry)} fields in BibTeX")
        # Set missing fields to None
        return {k: v if v else "None" for k, v in entry.items()}
    if verbose:
        print("  No entries found in BibTeX file")
    return {}

def parse_json(json_path, verbose=False):
    """Parse a JSON file and return its dictionary."""
    if verbose:
        print(f"Parsing JSON file: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    if verbose:
        print(f"  Found {len(data)} fields in JSON")
    # Assume JSON is a flat dictionary; set missing values to None
    return {k: v if v else "None" for k, v in data.items()}

def parse_txt(txt_path, verbose=False):
    """Parse a text file assuming 'field: value' per line."""
    if verbose:
        print(f"Parsing TXT file: {txt_path}")
    metadata = {}
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            if ':' in line:
                field, value = line.split(':', 1)
                metadata[field.strip()] = value.strip() or "None"
                if verbose:
                    print(f"  Found field: {field.strip()} = {value.strip() or 'None'}")
    if verbose:
        print(f"  Found {len(metadata)} fields in text file")
    return metadata

def parse_ris(ris_path, verbose=False):
    """Parse an RIS file and return its entries."""
    if verbose:
        print(f"Parsing RIS file: {ris_path}")
    with open(ris_path, 'r', encoding='utf-8') as ris_file:
        entries = rispy.load(ris_file)
    if entries:
        # Take the first entry; assumes one document
        entry = entries[0]
        if verbose:
            print(f"  Found {len(entry)} fields in RIS")
        # Set missing fields to None
        return {k: v if v else "None" for k, v in entry.items()}
    if verbose:
        print("  No entries found in RIS file")
    return {}

def escape_latex(text):
    """
    Escape LaTeX special characters in a string to display correctly in LaTeX documents.
    
    This function handles special characters by converting them to their LaTeX representation.
    Distinguishes between backslashes in Windows paths and regular backslashes.
    """
    if text is None:
        return "None"
    
    # Convert to string if it's not already
    text = str(text)
    
    
    # Function to detect if a string looks like a Windows path
    def is_likely_windows_path(s):
        # Check for drive letter pattern (e.g., C:\) or UNC path pattern (e.g., \\server)
        return bool(re.match(r'^[A-Za-z]:[\\]', s) or re.match(r'^[\\]{2}', s))
    
    # If the text looks like a Windows path, handle backslashes differently
    if is_likely_windows_path(text):
        # For Windows paths, convert backslashes to forward slashes which are more LaTeX-friendly
        text = text.replace('\\', '/')
    
    # Define replacements for special characters
    replacements = [
        # Only include backslash replacement if not identified as a Windows path
        *([('\\', r'\textbackslash{}')] if not is_likely_windows_path(text) else []),
        ('_', r'\_'),
        ('&', r'\&'),
        ('#', r'\#'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('^', r'\textasciicircum{}'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('<', r'\textless{}'),
        ('>', r'\textgreater{}'),
        ('|', r'\textbar{}'),
    ]
    
    # Apply replacements in the specific order
    for old, new in replacements:
        text = text.replace(old, new)
    
    return text

def create_latex_preamble():
    """Generate the LaTeX document preamble."""
    return r"""\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{margin=1cm}
\usepackage{tabularx}
\usepackage[table]{xcolor}
\begin{document}
\pagestyle{empty}
"""

def create_latex_table_header():
    """Generate the LaTeX table header."""
    return r"""\begin{center}
    \textbf{\Large Metadata}
\end{center}
\rowcolors{2}{gray!15}{white}
\begin{tabularx}{\textwidth}{p{0.3\textwidth}X}
    \hline
    \textbf{Field} & \textbf{Value} \\
    \hline
"""

def create_latex_table_rows(metadata):
    """Generate the LaTeX table rows from metadata."""
    rows = ""
    for field, value in sorted(metadata.items()):
        field_safe = escape_latex(field)
        value_safe = escape_latex(str(value))
        rows += f"    {field_safe} & {value_safe} \\\\\n"
    return rows

def create_latex_footer():
    """Generate the LaTeX document footer."""
    return r"""    \hline
\end{tabularx}
\end{document}
"""

def create_latex(metadata):
    """Generate LaTeX code to display metadata in a table with alternating row colors."""
    latex_code = create_latex_preamble()
    latex_code += create_latex_table_header()
    latex_code += create_latex_table_rows(metadata)
    latex_code += create_latex_footer()
    return latex_code

def compile_latex(verbose=False):
    """Compile the LaTeX file to PDF using latexmk."""
    try:
        # First check if latexmk is installed
        try:
            if verbose:
                print("Checking for latexmk installation...")
            subprocess.run(['latexmk', '--version'], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print("Error: latexmk is not installed or not in the PATH.")
            print("Please install LaTeX with latexmk or make sure it's in your system PATH.")
            raise RuntimeError("latexmk command not found")
        
        # Try compiling the LaTeX file using latexmk
        if verbose:
            print("Compiling LaTeX document...")
            result = subprocess.run(['latexmk', '-pdf', 'metadata.tex'], 
                        check=True)
        else:
            result = subprocess.run(['latexmk', '-pdf', 'metadata.tex'], 
                      check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if metadata.pdf was actually created
        if not os.path.exists('metadata.pdf'):
            print("Error: latexmk did not produce metadata.pdf.")
            print(f"latexmk output: {result.stdout.decode() if hasattr(result, 'stdout') else ''}")
            raise RuntimeError("latexmk did not produce the output file")
        elif verbose:
            print("  Successfully generated metadata.pdf")
            
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX: {e}")
        print(f"latexmk output: {e.stdout.decode() if hasattr(e, 'stdout') else ''}")
        raise

def merge_pdfs(metadata_pdf_path, input_pdf_path, output_pdf_path, verbose=False):
    """Merge the metadata PDF with the input PDF."""
    if verbose:
        print(f"Merging PDFs...")
        print(f"  Metadata PDF: {metadata_pdf_path}")
        print(f"  Input PDF: {input_pdf_path}")
        print(f"  Output PDF: {output_pdf_path}")
    
    metadata_pdf = PdfReader(metadata_pdf_path)
    input_pdf = PdfReader(input_pdf_path)
    output_pdf = PdfWriter()
    
    # Add metadata page(s) first
    if verbose:
        print(f"  Adding {len(metadata_pdf.pages)} metadata page(s)")
    for page in metadata_pdf.pages:
        output_pdf.add_page(page)
    
    # Add original PDF pages
    if verbose:
        print(f"  Adding {len(input_pdf.pages)} pages from original PDF")
    for page in input_pdf.pages:
        output_pdf.add_page(page)
    
    if verbose:
        print(f"  Writing to {output_pdf_path}")
    with open(output_pdf_path, 'wb') as f:
        output_pdf.write(f)

def cleanup(verbose=False):
    """Remove temporary files."""
    temp_files = ['metadata.tex', 'metadata.aux', 'metadata.log', 'metadata.pdf', 
                 'metadata.fls', 'metadata.fdb_latexmk']
    if verbose:
        print("Cleaning up temporary files...")
    for file in temp_files:
        if os.path.exists(file):
            if verbose:
                print(f"  Removing {file}")
            os.remove(file)

def insert_pdf_metadata_complete(pdf_path, metadata, verbose=False):
    """Insert metadata into both Document Information Dictionary and XMP metadata"""
    if verbose:
        print(f"Inserting metadata fields into PDF: {pdf_path}")
    
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)
    
    # Prepare metadata dictionary
    metadata_dict = {}
    for key, value in metadata.items():
        # Skip non-standard fields
        if key.lower() in ['note', 'id', 'file', 'mendeley-tags', 'mendeley-groups', 'type']:
            continue
        
        # Sanitize key by removing square brackets and other invalid characters
        sanitized_key = re.sub(r'[\[\]\(\)\<\>\{\}\#\%]', '_', key)
            
        # Map common fields to standard PDF metadata keys
        if sanitized_key.lower() == 'title':
            pdf_key = '/Title'
        elif sanitized_key.lower() in ['author', 'authors']:
            pdf_key = '/Author'
        elif sanitized_key.lower() == 'subject':
            pdf_key = '/Subject'
        elif sanitized_key.lower() == 'keywords':
            pdf_key = '/Keywords'
        elif sanitized_key.lower() == 'creator':
            pdf_key = '/Creator'
        elif sanitized_key.lower() == 'producer':
            pdf_key = '/Producer'
        elif sanitized_key.lower() == 'creationdate':
            pdf_key = '/CreationDate'
        elif sanitized_key.lower() == 'moddate':
            pdf_key = '/ModDate'
        else:
            # Add leading slash for PDF metadata convention
            pdf_key = f"/{sanitized_key}" if not sanitized_key.startswith('/') else sanitized_key
        
        metadata_dict[pdf_key] = str(value)
        
        if verbose:
            print(f"  Setting {pdf_key} = {str(value)}")
    
    # Add metadata to PDF
    writer.add_metadata(metadata_dict)
    
    # Add XMP metadata (limited support in PyPDF2)
    # Note: PyPDF2 has limited XMP support through the metadata dictionary
    # For full XMP metadata support, consider using pikepdf:
    # 
    try:
        import pikepdf
        # Write the PDF with PyPDF2 first
        temp_output = f"{pdf_path}.temp"
        with open(temp_output, 'wb') as output_file:
            writer.write(output_file)
            
        # Then enhance with pikepdf's XMP support
        with pikepdf.open(temp_output) as pdf:
            with pdf.open_metadata() as meta:
                for key, value in metadata.items():
                    # Sanitize key for XMP metadata too
                    sanitized_key = re.sub(r'[\[\]\(\)\<\>\{\}\#\%]', '_', key)
                    if sanitized_key.lower() == 'title':
                        meta['dc:title'] = str(value)
                    elif sanitized_key.lower() in ['author', 'authors']:
                        meta['dc:creator'] = [str(value)]
                    elif sanitized_key.lower() == 'subject':
                        meta['dc:description'] = str(value)
                    elif sanitized_key.lower() == 'keywords':
                        # Split keywords by commas and add as subjects
                        keywords = [k.strip() for k in str(value).split(',')]
                        if 'dc:subject' not in meta:
                            meta['dc:subject'] = keywords
                        else:
                            # Append to existing subjects
                            subjects = meta['dc:subject']
                            if isinstance(subjects, str):
                                subjects = [subjects]
                            meta['dc:subject'] = subjects + keywords
            pdf.save(pdf_path)
        os.remove(temp_output)
        if verbose:
            print("  Enhanced metadata added with pikepdf (XMP)")
        return  # Skip the PyPDF2 write below
    except ImportError:
        if verbose:
            print("  For enhanced XMP support, install pikepdf: pip install pikepdf")
    
    # Write updated PDF
    with open(pdf_path, 'wb') as output_file:
        writer.write(output_file)
    
    if verbose:
        print(f"  Metadata successfully inserted into {pdf_path}")

def main():
    args = parse_args()
    metadata = {}

    if args.verbose:
        print("Starting metadata insertion process...")

    # Determine output path
    output_pdf = args.output_pdf
    if not output_pdf:
        # No output specified, create a new path or overwrite
        input_base, input_ext = os.path.splitext(args.input_pdf)
        if args.overwrite:
            output_pdf = args.input_pdf
            if args.verbose:
                print(f"No output specified. Will overwrite input PDF: {output_pdf}")
        else:
            output_pdf = f"{input_base}_metadata_included{input_ext}"
            if args.verbose:
                print(f"No output specified. Creating: {output_pdf}")
    elif args.verbose:
        print(f"Output will be saved to: {output_pdf}")

    # Process sources
    if args.sources:
        sources = args.sources.split(',')
        if args.verbose:
            print(f"Processing {len(sources)} metadata source(s)...")
        for source in sources:
            source = source.strip()
            if source == "input_pdf":
                metadata.update(extract_from_pdf(args.input_pdf, args.verbose))
            elif source.endswith('.bib'):
                metadata.update(parse_bibtex(source, args.verbose))
            elif source.endswith('.json'):
                metadata.update(parse_json(source, args.verbose))
            elif source.endswith('.txt'):
                metadata.update(parse_txt(source, args.verbose))
            elif source.endswith('.ris'):
                metadata.update(parse_ris(source, args.verbose))
            else:
                print(f"Warning: Unknown source type '{source}', skipping.")

    # Process additional entries (override previous values)
    if args.entries:
        entries = args.entries.split(',')
        if args.verbose:
            print(f"Processing {len(entries)} additional entries...")
        for entry in entries:
            if ':' in entry:
                field, value = entry.split(':', 1)
                metadata[field.strip()] = value.strip() or "None"
                if args.verbose:
                    print(f"  Added: {field.strip()} = {value.strip() or 'None'}")

    # If no metadata collected, add a note
    if not metadata:
        metadata['Note'] = 'No metadata provided'
        if args.verbose:
            print("No metadata collected. Adding default note.")

    if args.no_metadata_page:
        # Skip adding metadata page, just copy input to output if needed
        if args.verbose:
            print("Skipping metadata page insertion as requested")
        
        if output_pdf != args.input_pdf:
            if args.verbose:
                print(f"Copying input PDF to output: {output_pdf}")
            reader = PdfReader(args.input_pdf)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            with open(output_pdf, 'wb') as f:
                writer.write(f)
    else:
        # Create and compile LaTeX document
        if args.verbose:
            print(f"Creating LaTeX document with {len(metadata)} metadata fields...")
        latex_code = create_latex(metadata)
        with open('metadata.tex', 'w', encoding='utf-8') as f:
            f.write(latex_code)
        compile_latex(args.verbose)

        # Merge PDFs
        merge_pdfs('metadata.pdf', args.input_pdf, output_pdf, args.verbose)
        
        # Clean up temporary files
        cleanup(args.verbose)

    # Insert metadata into the PDF document information dictionary
    insert_pdf_metadata_complete(output_pdf, metadata, args.verbose)
    
    if args.verbose:
        print(f"Process completed successfully! Output saved to: {output_pdf}")

if __name__ == "__main__":
    main()