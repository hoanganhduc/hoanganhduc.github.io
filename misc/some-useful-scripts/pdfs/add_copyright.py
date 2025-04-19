#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from typing import List, Optional, Tuple

# Check required libraries before importing
def check_libraries() -> List[str]:
    """Check if required libraries are installed."""
    import importlib.util
    
    required_libraries = ["PyPDF2", "reportlab", "tqdm"]
    missing_libraries = []
    
    for lib in required_libraries:
        if importlib.util.find_spec(lib) is None:
            missing_libraries.append(lib)
    
    return missing_libraries

# Import optional dependencies only if available
missing_deps = check_libraries()
if not missing_deps:
    import PyPDF2
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.colors import HexColor
    from tqdm import tqdm
    import fnmatch
else:
    # Define tqdm as a no-op if not available
    def tqdm(iterable=None, **kwargs):
        return iterable if iterable is not None else []

def print_progress(message: str, verbose: bool = True) -> None:
    """Print progress message to the screen if verbose is True."""
    if verbose:
        print(message)

def print_usage(parser=None) -> None:
    """
    Print usage information.
    
    Args:
        parser: Optional argparse parser object to use for printing help
    """
    if parser:
        parser.print_help()
        return
        
    usage = """
    Usage: python add_copyright.py [options] path
    
    Description:
      Add copyright and licensing notices to PDF files.
      
    Options:
      -h, --help            Show this help message and exit
      -o, --overwrite       Overwrite original PDF files
      -v, --verbose         Print progress information
      -e, --engine          Specify the rendering engine: "latex", "reportlab", or "auto" (default: "auto")
      -i, --ignore          Patterns to ignore (e.g., '*_copyright.pdf'). Can be used multiple times.
    
    Arguments:
      path                  Path to a PDF file or a directory containing PDF files
    
    Examples:
      python add_copyright.py -o -v document.pdf
      python add_copyright.py -o -v -e latex /path/to/pdf_directory
      python add_copyright.py --engine reportlab document.pdf
      python add_copyright.py -i '*_copyright.pdf' -i 'draft_*.pdf' /path/to/pdf_directory
      
    Requirements:
      PyPDF2, reportlab, and tqdm libraries
      (LaTeX rendering engine requires pdflatex to be installed and accessible)
    """
    print(usage)

def get_file_modified_date(file_path: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract the last modified date of a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        tuple: (formatted_date, year) or (None, None) if error
    """
    try:
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return None, None
        
        # Get the modification time as seconds since epoch
        mod_time_seconds = os.path.getmtime(file_path)
        
        # Convert to a datetime object and format as a string
        mod_time = datetime.fromtimestamp(mod_time_seconds)
        formatted_date = mod_time.strftime("%Y-%m-%d")
        year = mod_time.strftime("%Y")
        
        return formatted_date, year
    
    except Exception as e:
        print(f"Error getting file modification date for {file_path}: {str(e)}")
        return None, None

def find_suitable_font() -> str:
    """Find a suitable font for Vietnamese text."""
    font_name = 'Helvetica'  # Default fallback
    try:
        # Check common font locations on different platforms
        font_paths = [
            # Windows fonts
            "C:/Windows/Fonts/Arial.ttf", 
            "C:/Windows/Fonts/calibri.ttf",
            # Linux fonts
            "/usr/share/fonts/TTF/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
        
        for path in font_paths:
            if os.path.exists(path):
                font_base = os.path.basename(path).split('.')[0]
                pdfmetrics.registerFont(TTFont(font_base, path))
                return font_base
    except Exception as e:
        print(f"Font registration error: {e}. Using Helvetica as fallback.")
        
    return font_name

def create_english_copyright_notice(copyright_year: str, mod_date: str) -> str:
    """
    Create the English copyright notice text.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        
    Returns:
        str: Formatted English copyright notice text
    """
    return (
        "COPYRIGHT (English):\n"
        "This document is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0). You are free to share and adapt this material with appropriate attribution and under the same license.\n"
        "This document is not up to date and may contain several errors or outdated information.\n"
        f"Last revision date: {mod_date}"
    )

def create_vietnamese_copyright_notice(copyright_year: str, mod_date: str) -> str:
    """
    Create the Vietnamese copyright notice text.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        
    Returns:
        str: Formatted Vietnamese copyright notice text
    """
    return (
        "BẢN QUYỀN (Tiếng Việt):\n"
        "Tài liệu này được cấp phép theo Giấy phép Quốc tế Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA 4.0). Bạn được tự do chia sẻ và chỉnh sửa tài liệu này với điều kiện ghi nguồn phù hợp và sử dụng cùng loại giấy phép.\n"
        "Tài liệu này không được cập nhật và có thể chứa nhiều lỗi hoặc thông tin cũ.\n"
        f"Ngày sửa đổi cuối cùng: {mod_date}"
    )

def create_copyright_notice(copyright_year: str, mod_date: str) -> str:
    """
    Create the complete copyright notice text by combining English and Vietnamese notices.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        
    Returns:
        str: Formatted copyright notice text in both languages
    """
    english_notice = create_english_copyright_notice(copyright_year, mod_date)
    vietnamese_notice = create_vietnamese_copyright_notice(copyright_year, mod_date)
    
    return (
        "COPYRIGHT NOTICE / THÔNG BÁO BẢN QUYỀN\n"
        f"© {copyright_year} Duc A. Hoang (Hoàng Anh Đức)\n\n"
        f"{english_notice}\n\n"
        f"{vietnamese_notice}"
    )

def create_copyright_page(copyright_notice: str, engine: str = "auto") -> io.BytesIO:
    """
    Create a PDF page with the copyright notice.
    
    Args:
        copyright_notice: The copyright text
        engine: The rendering engine to use:
                "latex" - use LaTeX (falls back to ReportLab if LaTeX fails)
                "reportlab" - use ReportLab
                "auto" - try LaTeX first, then fall back to ReportLab (default)
        
    Returns:
        io.BytesIO: Buffer containing the PDF page
    """
    if engine.lower() == "reportlab":
        return create_reportlab_copyright_page(copyright_notice)
    
    if engine.lower() in ["latex", "auto"]:
        # Try LaTeX first
        latex_page = create_latex_copyright(copyright_notice)
        if latex_page:
            return latex_page
        
        # Fall back to ReportLab if LaTeX fails or if LaTeX was specified but failed
        if engine.lower() == "auto":
            return create_reportlab_copyright_page(copyright_notice)
        else:
            print("LaTeX rendering failed. Please ensure pdflatex is installed and accessible.")
            return create_reportlab_copyright_page(copyright_notice)
    
    # Invalid engine type - use ReportLab as default
    print(f"Warning: Unknown rendering engine '{engine}'. Using ReportLab instead.")
    return create_reportlab_copyright_page(copyright_notice)

def create_english_latex_section(copyright_year: str, mod_date: str) -> str:
    """
    Create simple LaTeX code for the English copyright section.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        
    Returns:
        str: LaTeX formatted English copyright section
    """
    english_notice = create_english_copyright_notice(copyright_year, mod_date)
    latex_content = ""
    
    lines = english_notice.split("\n")
    # Simple section header
    latex_content += r"""
\section*{""" + lines[0] + r"""}
\noindent """  # Add \noindent to remove paragraph indentation
    
    # Format content with simple paragraph style
    for j, line in enumerate(lines[1:]):
        # Escape special LaTeX characters
        line = (line.replace("&", r"\&")
                   .replace("_", r"\_")
                   .replace("#", r"\#")
                   .replace("%", r"\%")
                   .replace("$", r"\$")
                   .replace("{", r"\{")
                   .replace("}", r"\}"))
        
        latex_content += line
        if j < len(lines) - 2:
            latex_content += r" \\" + "\n\n\\noindent "  # Add \noindent for each new paragraph
    
    return latex_content

def create_vietnamese_latex_section(copyright_year: str, mod_date: str) -> str:
    """
    Create simple LaTeX code for the Vietnamese copyright section.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        
    Returns:
        str: LaTeX formatted Vietnamese copyright section
    """
    vietnamese_notice = create_vietnamese_copyright_notice(copyright_year, mod_date)
    latex_content = ""
    
    lines = vietnamese_notice.split("\n")
    # Simple section header
    latex_content += r"""
\section*{""" + lines[0] + r"""}
\noindent """  # Add \noindent to remove paragraph indentation
    
    # Format content with simple paragraph style
    for j, line in enumerate(lines[1:]):
        # Escape special LaTeX characters
        line = (line.replace("&", r"\&")
                   .replace("_", r"\_")
                   .replace("#", r"\#")
                   .replace("%", r"\%")
                   .replace("$", r"\$")
                   .replace("{", r"\{")
                   .replace("}", r"\}"))
        
        latex_content += line
        if j < len(lines) - 2:
            latex_content += r" \\" + "\n\n\\noindent "  # Add \noindent for each new paragraph
    
    return latex_content

def create_latex_copyright(copyright_notice: str) -> Optional[io.BytesIO]:
    """
    Create a simple copyright page using LaTeX.
    
    Args:
        copyright_notice: The copyright text
        
    Returns:
        Optional[io.BytesIO]: Buffer containing the PDF page, or None if failed
    """
    try:
        # Check if pdflatex is available
        if not shutil.which("pdflatex"):
            return None
        
        # Extract copyright year and date from the notice
        lines = copyright_notice.split('\n')
        copyright_line = next((line for line in lines if "© " in line), "")
        copyright_year = copyright_line.split("© ")[1].split(" ")[0] if copyright_line else ""
        
        mod_date = ""
        for line in lines:
            if "Last revision date:" in line:
                mod_date = line.split(": ")[1]
                break
        
        # Create temp directory for LaTeX files
        with tempfile.TemporaryDirectory(dir="C:/Windows/Temp" if os.name == 'nt' else None) as temp_dir:
            tex_file_path = os.path.join(temp_dir, "copyright.tex")
            pdf_file_path = os.path.join(temp_dir, "copyright.pdf")
            
            # Create simple LaTeX content
            latex_content = r"""
\documentclass[12pt,a4paper]{article}
\usepackage{lmodern}
\usepackage{ccicons}
\usepackage[utf8]{vietnam}
\usepackage[left=2cm,right=2cm,top=2.5cm,bottom=2cm]{geometry}
\setlength{\parindent}{0pt}  % Remove all paragraph indentation globally

\begin{document}
\pagestyle{empty}

\begin{center}
\Large\textbf{COPYRIGHT NOTICE}\\
\large\textbf{THÔNG BÁO BẢN QUYỀN}
\end{center}

\vspace*{1cm}

\begin{center}
\large\textbf{© """ + copyright_year + r""" Duc A. Hoang (Hoàng Anh Đức)}
\end{center}

\vspace{0.8cm}
"""
            
            # Add the English section
            latex_content += create_english_latex_section(copyright_year, mod_date)
            
            # Add spacing between sections
            latex_content += r"\vspace{1cm}" + "\n"
            
            # Add the Vietnamese section
            latex_content += create_vietnamese_latex_section(copyright_year, mod_date)
            
            # Add CC license info at the bottom
            latex_content += r"""
\vfill
\begin{center}
\ccbysa\\
\small Creative Commons Attribution-ShareAlike 4.0 International
\end{center}

\end{document}
"""
            
            # Write LaTeX file
            with open(tex_file_path, "w", encoding="utf-8") as tex_file:
                tex_file.write(latex_content)
            
            # Run pdflatex without showing output
            try:
                # Change to the temp directory before running pdflatex
                current_dir = os.getcwd()
                os.chdir(temp_dir)
                
                process = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "copyright.tex"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=30
                )
                
                # Change back to original directory
                os.chdir(current_dir)
                
                if process.returncode != 0 or not os.path.exists(pdf_file_path):
                    return None
                
                # Read the PDF into BytesIO
                buffer = io.BytesIO()
                with open(pdf_file_path, "rb") as pdf_file:
                    buffer.write(pdf_file.read())
                buffer.seek(0)
                return buffer
                
            except Exception:
                # Ensure we return to the original directory
                os.chdir(current_dir)
                return None
            
    except Exception:
        return None

def create_reportlab_english_section(c, width, font_name, y_position):
    """
    Create the English section of the copyright notice using ReportLab without decorative elements.
    
    Args:
        c: Canvas object
        width: Width of the page
        font_name: Font to use
        y_position: Current Y position on the page
        
    Returns:
        int: Updated Y position after drawing the content
    """
    # Get copyright notice English section
    copyright_year = datetime.now().strftime("%Y")
    mod_date = datetime.now().strftime("%Y-%m-%d")
    english_notice = create_english_copyright_notice(copyright_year, mod_date)
    
    # Define text area width
    text_width = width - 120
    margin = 40
    
    # Process English section
    lines = english_notice.split('\n')
    
    # Draw header
    c.setFont(font_name, 14)
    c.drawString(margin, y_position, lines[0])  # Title
    y_position -= 30
    
    # Draw content
    for i, line in enumerate(lines[1:]):
        text_object = c.beginText(margin, y_position)
        text_object.setFont(font_name, 12)
        
        words = line.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_width_pixels = c.stringWidth(test_line, font_name, 12)
            
            if text_width_pixels <= text_width:
                current_line = test_line
            else:
                text_object.textLine(current_line)
                y_position -= 20
                current_line = word
        
        if current_line:
            text_object.textLine(current_line)
            y_position -= 20
        
        c.drawText(text_object)
    
    # Add space after section
    y_position -= 20
    
    return y_position

def create_reportlab_vietnamese_section(c, width, font_name, y_position):
    """
    Create the Vietnamese section of the copyright notice using ReportLab without decorative elements.
    
    Args:
        c: Canvas object
        width: Width of the page
        font_name: Font to use
        y_position: Current Y position on the page
        
    Returns:
        int: Updated Y position after drawing the content
    """
    # Get copyright notice Vietnamese section
    copyright_year = datetime.now().strftime("%Y")
    mod_date = datetime.now().strftime("%Y-%m-%d")
    vietnamese_notice = create_vietnamese_copyright_notice(copyright_year, mod_date)
    
    # Define text area width
    text_width = width - 120
    margin = 40
    
    # Process Vietnamese section
    lines = vietnamese_notice.split('\n')
    
    # Draw header
    c.setFont(font_name, 14)
    c.drawString(margin, y_position, lines[0])  # Title
    y_position -= 30
    
    # Draw content
    for i, line in enumerate(lines[1:]):
        text_object = c.beginText(margin, y_position)
        text_object.setFont(font_name, 12)
        
        words = line.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_width_pixels = c.stringWidth(test_line, font_name, 12)
            
            if text_width_pixels <= text_width:
                current_line = test_line
            else:
                text_object.textLine(current_line)
                y_position -= 20
                current_line = word
        
        if current_line:
            text_object.textLine(current_line)
            y_position -= 20
        
        c.drawText(text_object)
    
    return y_position

def create_reportlab_copyright_page(copyright_notice: str) -> io.BytesIO:
    """
    Create a simple PDF page with the copyright notice using ReportLab.
    
    Args:
        copyright_notice: The copyright text
        
    Returns:
        io.BytesIO: Buffer containing the PDF page
    """
    packet = io.BytesIO()
    font_name = find_suitable_font()
    c = canvas.Canvas(packet, pagesize=letter)
    
    width, height = letter
    
    # Set initial position
    y_position = height - 60
    
    # Draw title
    title_text = "COPYRIGHT NOTICE / THÔNG BÁO BẢN QUYỀN"
    c.setFont(font_name, 18)
    c.drawCentredString(width/2, y_position, title_text)
    y_position -= 50
    
    # Extract and draw copyright year line
    lines = copyright_notice.split('\n')
    copyright_line = next((line for line in lines if "© " in line), "")
    if copyright_line:
        c.setFont(font_name, 14)
        c.drawCentredString(width/2, y_position, copyright_line)
        y_position -= 60
    
    # Draw English section
    y_position = create_reportlab_english_section(c, width, font_name, y_position)
    
    # Add spacing between sections
    y_position -= 30
    
    # Draw Vietnamese section
    y_position = create_reportlab_vietnamese_section(c, width, font_name, y_position)
    
    # Draw CC notice
    c.setFont(font_name, 10)
    c.drawCentredString(width/2, 20, "Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)")
    
    c.save()
    packet.seek(0)
    return packet

def merge_pdfs(copyright_page: io.BytesIO, input_path: str, output_path: str) -> bool:
    """
    Merge the copyright page with the existing PDF.
    
    Args:
        copyright_page: Buffer containing the copyright PDF page
        input_path: Path to the original PDF
        output_path: Path to save the modified PDF
        
    Returns:
        bool: True if successful
    """
    try:
        new_pdf = PyPDF2.PdfReader(copyright_page)
        
        with open(input_path, "rb") as f:
            existing_pdf = PyPDF2.PdfReader(f)
            output = PyPDF2.PdfWriter()
            
            # Add the copyright page
            output.add_page(new_pdf.pages[0])
            
            # Add all pages from existing PDF
            for page in existing_pdf.pages:
                output.add_page(page)
                
            # Write the output PDF
            with open(output_path, "wb") as output_file:
                output.write(output_file)
                
        return True
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False

def add_copyright_to_pdf(input_path: str, output_path: str, engine: str = "auto") -> bool:
    """
    Add copyright notice and warning to a PDF file.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path to save the modified PDF file
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get the file's last modification date
        mod_date, copyright_year = get_file_modified_date(input_path)
        if not mod_date:
            mod_date = "Unknown"
            copyright_year = str(datetime.now().year)
            
        # Create the copyright notice
        notice = create_copyright_notice(copyright_year, mod_date)
        
        # Create a PDF page with the notice using the specified engine
        copyright_page = create_copyright_page(notice, engine)
        
        # Merge the copyright page with the existing PDF
        return merge_pdfs(copyright_page, input_path, output_path)
            
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False

def process_pdf(pdf_path: str, overwrite: bool = False, verbose: bool = True, engine: str = "auto") -> bool:
    """
    Process a single PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        overwrite: Whether to overwrite the original file
        verbose: Whether to print progress messages
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        
    Returns:
        bool: True if successful, False otherwise
    """
    print_progress(f"Processing {pdf_path}...", verbose)
    
    if overwrite:
        temp_path = pdf_path + ".temp"
        success = add_copyright_to_pdf(pdf_path, temp_path, engine)
        
        if success:
            try:
                # Try to replace the original file, with up to 3 retries
                max_retries = 3
                retry_count = 0
                while retry_count < max_retries:
                    try:
                        os.replace(temp_path, pdf_path)
                        print_progress(f"Overwritten: {pdf_path}", verbose)
                        break
                    except PermissionError:
                        retry_count += 1
                        if retry_count < max_retries:
                            print_progress(f"File appears to be locked. Retrying in 2 seconds... (Attempt {retry_count}/{max_retries})", verbose)
                            time.sleep(2)
                        else:
                            print(f"Error: Could not overwrite {pdf_path} - file may be in use by another application.")
                            print(f"The modified file has been saved as {temp_path}")
                            return False
            except Exception as e:
                print(f"Error replacing file {pdf_path}: {str(e)}")
                print(f"The modified file has been saved as {temp_path}")
                return False
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return False
    else:
        output_path = pdf_path.replace(".pdf", "_copyright.pdf")
        success = add_copyright_to_pdf(pdf_path, output_path, engine)
        
        if success:
            print_progress(f"Created: {output_path}", verbose)
        
    return success

def process_directory(directory_path: str, overwrite: bool = False, verbose: bool = True, 
                     engine: str = "auto", ignore: List[str] = None) -> int:
    """
    Process all PDF files in a directory and its subdirectories.
    
    Args:
        directory_path: Path to the directory
        overwrite: Whether to overwrite original files
        verbose: Whether to print progress messages
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        ignore: List of file patterns to ignore
        
    Returns:
        int: Number of successfully processed files
    """
    success_count = 0
    pdf_files = []
    ignore = ignore or []  # Default to empty list if None
    
    # First, collect all PDF files
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_path = os.path.join(root, file)
                # Check if file matches any ignore patterns
                if any(fnmatch.fnmatch(file, pattern) for pattern in ignore):
                    if verbose:
                        print(f"Skipping {full_path} (matches ignore pattern)")
                    continue
                pdf_files.append(full_path)
    
    if verbose:
        print(f"Found {len(pdf_files)} PDF files to process.")
    
    # Process files with a progress bar
    for pdf_path in tqdm(pdf_files, disable=not verbose):
        if process_pdf(pdf_path, overwrite, False, engine):  # Set verbose to False to avoid double-printing
            success_count += 1
    
    print_progress(f"Successfully processed {success_count} out of {len(pdf_files)} PDF files.", verbose)
    return success_count

def parse_arguments():
    """Parse command line arguments.
    
    Returns:
        argparse.Namespace: The parsed command line arguments
    """
    parser = argparse.ArgumentParser(description="Add copyright notice to PDF files.")
    parser.add_argument("path", help="Path to a PDF file or directory containing PDF files")
    parser.add_argument("-o", "--overwrite", action="store_true", 
                        help="Overwrite original PDF files")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print progress information")
    parser.add_argument("-e", "--engine", type=str, choices=["latex", "reportlab", "auto"],
                        default="auto", help="Specify the rendering engine: 'latex', 'reportlab', or 'auto' (default: 'auto')")
    parser.add_argument("-i", "--ignore", action="append", default=[],
                        help="Patterns to ignore (e.g., '*_copyright.pdf'). Can be used multiple times.")
    
    return parser.parse_args()

def main() -> int:
    """Main function to handle command line arguments and process PDFs."""
    args = parse_arguments()
    
    # Check for required libraries
    missing_libs = check_libraries()
    if missing_libs:
        print(f"Error: Missing required libraries: {', '.join(missing_libs)}")
        print("Please install the required libraries using pip:")
        print(f"pip install {' '.join(missing_libs)}")
        return 1
    
    # Check if path exists
    if not os.path.exists(args.path):
        print(f"Error: Path does not exist: {args.path}")
        print_usage()
        return 1
    
    # Process the path
    if os.path.isfile(args.path):
        if not args.path.lower().endswith('.pdf'):
            print(f"Error: Not a PDF file: {args.path}")
            print_usage()
            return 1
        
        # Check if file matches any ignore patterns
        filename = os.path.basename(args.path)
        if any(fnmatch.fnmatch(filename, pattern) for pattern in args.ignore):
            if args.verbose:
                print(f"Skipping {args.path} (matches ignore pattern)")
            return 0
            
        success = process_pdf(args.path, args.overwrite, args.verbose, args.engine)
        return 0 if success else 1
    
    elif os.path.isdir(args.path):
        count = process_directory(args.path, args.overwrite, args.verbose, args.engine, args.ignore)
        if count == 0:
            print(f"No PDF files were processed in {args.path}")
            return 1
        return 0
    
    else:
        print(f"Error: Path is neither a file nor a directory: {args.path}")
        print_usage()
        return 1


if __name__ == "__main__":
    sys.exit(main())