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
    script_name = os.path.basename(sys.argv[0])
    
    if parser:
        parser.print_help()
        return
        
    usage = f"""
    Usage: python {script_name} [options] path
    
    Description:
      Add copyright and licensing notices to PDF files.
      
    Options:
      -h, --help            Show this help message and exit
      -o, --overwrite       Overwrite original PDF files
      -v, --verbose         Print progress information
      -e, --engine          Specify the rendering engine: "latex", "reportlab", or "auto" (default: "auto")
      -i, --ignore          Patterns to ignore (e.g., '*_copyright.pdf'). Can be used multiple times.
      -c, --copyright-pdf   Use a custom PDF file as the copyright notice instead of generating one
      -d, --decoration      Create a more beautiful and colorful version of the copyright notice
      -t, --title           Custom title for the copyright notice
      -H, --holder          Custom copyright holder name
      -E, --english-notice  Custom English copyright notice
      -V, --vietnamese-notice Custom Vietnamese copyright notice
      -n, --no-default      Use only custom content provided, no default text
    
    Arguments:
      path                  Path to a PDF file or a directory containing PDF files
    
    Examples:
      python {script_name} -o -v document.pdf
      python {script_name} -t "CUSTOM COPYRIGHT" -H "Company Name" document.pdf
      python {script_name} -n -E "Custom English notice" document.pdf
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

def create_english_copyright_notice(copyright_year: str, mod_date: str, 
                                   custom_notice: str = None, no_default: bool = False) -> str:
    """
    Create the English copyright notice text.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        custom_notice: Custom English notice text
        no_default: If True, use only custom content
        
    Returns:
        str: Formatted English copyright notice text
    """
    if no_default:
        if custom_notice:
            return custom_notice
        else:
            return None
    
    default_notice = (
        "COPYRIGHT (English):\n"
        "This document is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0). You are free to share and adapt this material with appropriate attribution and under the same license.\n"
        "This document is not up to date and may contain several errors or outdated information.\n"
        f"Last revision date: {mod_date}"
    )
    
    if custom_notice and not no_default:
        return default_notice + "\n\n" + custom_notice
    
    return default_notice

def create_vietnamese_copyright_notice(copyright_year: str, mod_date: str, 
                                      custom_notice: str = None, no_default: bool = False) -> str:
    """
    Create the Vietnamese copyright notice text.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        custom_notice: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
    Returns:
        str: Formatted Vietnamese copyright notice text
    """
    if no_default:
        if custom_notice:
            return custom_notice
        else:
            return None
    
    default_notice = (
        "BẢN QUYỀN (Tiếng Việt):\n"
        "Tài liệu này được cấp phép theo Giấy phép Quốc tế Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA 4.0). Bạn được tự do chia sẻ và chỉnh sửa tài liệu này với điều kiện ghi nguồn phù hợp và sử dụng cùng loại giấy phép.\n"
        "Tài liệu này không được cập nhật và có thể chứa nhiều lỗi hoặc thông tin cũ.\n"
        f"Ngày sửa đổi cuối cùng: {mod_date}"
    )
    
    if custom_notice and not no_default:
        return default_notice + "\n\n" + custom_notice
    
    return default_notice

def create_copyright_notice(copyright_year: str, mod_date: str, 
                           custom_title: str = None, custom_holder: str = None,
                           custom_english: str = None, custom_vietnamese: str = None,
                           no_default: bool = False) -> str:
    """
    Create the complete copyright notice text by combining English and Vietnamese notices.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        custom_title: Custom title for the notice
        custom_holder: Custom copyright holder name
        custom_english: Custom English notice text
        custom_vietnamese: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
    Returns:
        str: Formatted copyright notice text in both languages
    """
    english_notice = create_english_copyright_notice(copyright_year, mod_date, custom_english, no_default)
    vietnamese_notice = create_vietnamese_copyright_notice(copyright_year, mod_date, custom_vietnamese, no_default)
    
    if no_default and not custom_title:
        title = None
    else:
        title = custom_title if custom_title else "COPYRIGHT NOTICE / THÔNG BÁO BẢN QUYỀN"
    
    if no_default and not custom_holder:
        holder = None
    else:
        holder = custom_holder if custom_holder else f"Duc A. Hoang (Hoàng Anh Đức)"
    
    return (
        f"{title}\n"
        f"© {copyright_year} {holder}\n\n"
        f"{english_notice}\n\n"
        f"{vietnamese_notice}"
    )

def create_copyright_page(copyright_notice: str, engine: str = "auto", decoration: bool = False) -> io.BytesIO:
    """
    Create a PDF page with the copyright notice.
    
    Args:
        copyright_notice: The copyright text
        engine: The rendering engine to use:
                "latex" - use LaTeX (falls back to ReportLab if LaTeX fails)
                "reportlab" - use ReportLab
                "auto" - try LaTeX first, then fall back to ReportLab (default)
        decoration: Whether to add decorative elements to make the notice more visually appealing
        
    Returns:
        io.BytesIO: Buffer containing the PDF page
    """
    if engine.lower() == "reportlab":
        return create_reportlab_copyright_page(copyright_notice, decoration)
    
    if engine.lower() in ["latex", "auto"]:
        # Try LaTeX first
        latex_page = create_latex_copyright(copyright_notice, decoration)
        if latex_page:
            return latex_page
        
        # Fall back to ReportLab if LaTeX fails or if LaTeX was specified but failed
        if engine.lower() == "auto":
            return create_reportlab_copyright_page(copyright_notice, decoration)
        else:
            print("LaTeX rendering failed. Please ensure pdflatex is installed and accessible.")
            return create_reportlab_copyright_page(copyright_notice, decoration)
    
    # Invalid engine type - use ReportLab as default
    print(f"Warning: Unknown rendering engine '{engine}'. Using ReportLab instead.")
    return create_reportlab_copyright_page(copyright_notice, decoration)

def create_english_latex_section(copyright_year: str, mod_date: str, custom_notice: str = None, no_default: bool = False) -> str:
    """
    Create simple LaTeX code for the English copyright section.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        custom_notice: Custom English notice text
        no_default: If True, use only custom content
        
    Returns:
        str: LaTeX formatted English copyright section
    """
    english_notice = create_english_copyright_notice(copyright_year, mod_date, custom_notice, no_default)
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

def create_vietnamese_latex_section(copyright_year: str, mod_date: str, custom_notice: str = None, no_default: bool = False) -> str:
    """
    Create simple LaTeX code for the Vietnamese copyright section.
    
    Args:
        copyright_year: Year for copyright
        mod_date: Last modification date
        custom_notice: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
    Returns:
        str: LaTeX formatted Vietnamese copyright section
    """
    vietnamese_notice = create_vietnamese_copyright_notice(copyright_year, mod_date, custom_notice, no_default)
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

def create_latex_copyright(copyright_notice: str, decoration: bool = False) -> Optional[io.BytesIO]:
    """
    Create a simple copyright page using LaTeX.
    
    Args:
        copyright_notice: The copyright text
        decoration: Whether to add decorative elements to make the notice more visually appealing
        
    Returns:
        Optional[io.BytesIO]: Buffer containing the PDF page, or None if failed
    """
    try:
        # Check if pdflatex is available
        if not shutil.which("pdflatex"):
            return None
        
        # Extract copyright year and date from the notice
        lines = copyright_notice.split('\n')
        title_line = lines[0] if lines else "COPYRIGHT NOTICE / THÔNG BÁO BẢN QUYỀN"
        
        copyright_line = next((line for line in lines if "© " in line), "")
        copyright_year = copyright_line.split("© ")[1].split(" ")[0] if copyright_line else ""
        copyright_holder = copyright_line.split(copyright_year + " ")[1] if copyright_line and " " in copyright_line.split("© ")[1] else ""
        
        mod_date = ""
        for line in lines:
            if "Last revision date:" in line:
                mod_date = line.split(": ")[1]
                break
            elif "Ngày sửa đổi cuối cùng:" in line:
                mod_date = line.split(": ")[1]
                break
        
        # Extract English and Vietnamese notices
        english_start = -1
        vietnamese_start = -1
        
        for i, line in enumerate(lines):
            if "COPYRIGHT (English):" in line:
                english_start = i
            elif "BẢN QUYỀN (Tiếng Việt):" in line:
                vietnamese_start = i
                
        english_notice = None
        vietnamese_notice = None
        
        if english_start >= 0 and vietnamese_start >= 0:
            english_notice = "\n".join(lines[english_start:vietnamese_start-1])
            vietnamese_notice = "\n".join(lines[vietnamese_start:])
        
        # Create temp directory for LaTeX files
        with tempfile.TemporaryDirectory(dir="C:/Windows/Temp" if os.name == 'nt' else None) as temp_dir:
            tex_file_path = os.path.join(temp_dir, "copyright.tex")
            pdf_file_path = os.path.join(temp_dir, "copyright.pdf")
            
            # Create LaTeX content based on decoration flag
            if decoration:
                latex_content = r"""
\documentclass[12pt,a4paper]{article}
\usepackage{lmodern}
\usepackage{fontawesome}
\usepackage{ccicons}
\usepackage[utf8]{vietnam}
\usepackage[left=2cm,right=2cm,top=2.5cm,bottom=2cm]{geometry}
\usepackage{xcolor}
\usepackage{mdframed}
\usepackage{fancyhdr}
\usepackage{tikz}
\usepackage{tikzpagenodes}
\usetikzlibrary{decorations.pathmorphing,calc,positioning}

\definecolor{primarycolor}{HTML}{6A1B9A}
\definecolor{secondarycolor}{HTML}{9C27B0}
\definecolor{accentcolor}{HTML}{E91E63}
\definecolor{bglight}{HTML}{F3E5F5}
\definecolor{bgdark}{HTML}{D1C4E9}

\setlength{\parindent}{0pt}  % Remove all paragraph indentation globally

\begin{document}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}

% Page decorations - corners and dashed border
\begin{tikzpicture}[remember picture, overlay]
    % Fancy corners
    \foreach \corner in {north east, north west, south east, south west}{
        \begin{scope}
            \clip (current page.\corner) rectangle +(-4cm,-4cm);
            \fill[primarycolor, opacity=0.2] (current page.\corner) circle (3cm);
        \end{scope}
    }
    
    % Dashed border
    \draw[dashed, line width=1.5pt, primarycolor] 
        ($(current page.north west) + (1.5cm,-1.5cm)$) 
        rectangle ($(current page.south east) + (-1.5cm,1.5cm)$);
        
    % Side decorations
    \draw[secondarycolor, opacity=0.15, line width=12pt] 
        ($(current page.west) + (0.5cm,0)$) -- ($(current page.east) + (-0.5cm,0)$);
\end{tikzpicture}

\begin{center}
\vspace*{1cm}
{\color{primarycolor}\Large\textbf{""" + title_line.replace("&", r"\&").replace("%", r"\%") + r"""}}\\[0.3cm]
\end{center}

\begin{center}
\vspace{0.8cm}
{\color{accentcolor}\large\textbf{© """ + copyright_year + " " + copyright_holder.replace("&", r"\&").replace("%", r"\%") + r"""}}\\
\vspace{0.2cm}
\faBook \quad \faFileTextO \quad \faGraduationCap
\end{center}

\vspace{0.7cm}
\begin{mdframed}[
    linewidth=1.5pt,
    linecolor=primarycolor,
    backgroundcolor=bglight,
    roundcorner=10pt,
    leftmargin=1cm,
    rightmargin=1cm,
    innerleftmargin=15pt,
    innerrightmargin=15pt,
    innertopmargin=10pt,
    innerbottommargin=10pt
]
"""
                # Add English section with colorful formatting
                if english_notice:
                    english_lines = english_notice.split('\n')
                    latex_content += r"""
\begin{center}
{\color{primarycolor}\Large\textbf{""" + english_lines[0].replace("&", r"\&").replace("%", r"\%") + r"""}}
\end{center}
"""
                    for line in english_lines[1:]:
                        escaped_line = (line.replace("&", r"\&")
                                         .replace("_", r"\_")
                                         .replace("#", r"\#")
                                         .replace("%", r"\%")
                                         .replace("$", r"\$")
                                         .replace("{", r"\{")
                                         .replace("}", r"\}"))
                        if escaped_line.strip():
                            latex_content += escaped_line + r"\\" + "\n\n"
                
                latex_content += r"""
\end{mdframed}

\vspace{1cm}
\begin{mdframed}[
    linewidth=1.5pt,
    linecolor=secondarycolor,
    backgroundcolor=bgdark,
    roundcorner=10pt,
    leftmargin=1cm,
    rightmargin=1cm,
    innerleftmargin=15pt,
    innerrightmargin=15pt,
    innertopmargin=10pt,
    innerbottommargin=10pt
]
"""
                # Add Vietnamese section with colorful formatting
                if vietnamese_notice:
                    vietnamese_lines = vietnamese_notice.split('\n')
                    latex_content += r"""
\begin{center}
{\color{secondarycolor}\Large\textbf{""" + vietnamese_lines[0].replace("&", r"\&").replace("%", r"\%") + r"""}}
\end{center}
"""
                    for line in vietnamese_lines[1:]:
                        escaped_line = (line.replace("&", r"\&")
                                        .replace("_", r"\_")
                                        .replace("#", r"\#")
                                        .replace("%", r"\%")
                                        .replace("$", r"\$")
                                        .replace("{", r"\{")
                                        .replace("}", r"\}"))
                        if escaped_line.strip():
                            latex_content += escaped_line + r"\\" + "\n\n"
                
                latex_content += r"""
\end{mdframed}

\vfill
\begin{center}
\begin{tikzpicture}
\node[draw=accentcolor, rounded corners, line width=1pt, fill=bglight, inner sep=10pt] {
\ccbysa \quad {\color{accentcolor}\small Creative Commons Attribution-ShareAlike 4.0 International}
};
\end{tikzpicture}
\end{center}

\end{document}
"""
            else:
                # Original plain version
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
\Large\textbf{""" + title_line.replace("&", r"\&").replace("%", r"\%") + r"""}
\end{center}

\vspace*{1cm}

\begin{center}
\large\textbf{© """ + copyright_year + " " + copyright_holder.replace("&", r"\&").replace("%", r"\%") + r"""}
\end{center}

\vspace{0.8cm}
"""
            
                # Add the English section
                if english_notice:
                    english_lines = english_notice.split('\n')
                    latex_content += r"""
\section*{""" + english_lines[0].replace("&", r"\&").replace("%", r"\%") + r"""}
\noindent """
                    for j, line in enumerate(english_lines[1:]):
                        escaped_line = (line.replace("&", r"\&")
                                        .replace("_", r"\_")
                                        .replace("#", r"\#")
                                        .replace("%", r"\%")
                                        .replace("$", r"\$")
                                        .replace("{", r"\{")
                                        .replace("}", r"\}"))
                        latex_content += escaped_line
                        if j < len(english_lines) - 2:
                            latex_content += r" \\" + "\n\n\\noindent "
                
                # Add spacing between sections
                latex_content += r"\vspace{1cm}" + "\n"
                
                # Add the Vietnamese section
                if vietnamese_notice:
                    vietnamese_lines = vietnamese_notice.split('\n')
                    latex_content += r"""
\section*{""" + vietnamese_lines[0].replace("&", r"\&").replace("%", r"\%") + r"""}
\noindent """
                    for j, line in enumerate(vietnamese_lines[1:]):
                        escaped_line = (line.replace("&", r"\&")
                                        .replace("_", r"\_")
                                        .replace("#", r"\#")
                                        .replace("%", r"\%")
                                        .replace("$", r"\$")
                                        .replace("{", r"\{")
                                        .replace("}", r"\}"))
                        latex_content += escaped_line
                        if j < len(vietnamese_lines) - 2:
                            latex_content += r" \\" + "\n\n\\noindent "
                
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

def create_reportlab_copyright_page(copyright_notice: str, decoration: bool = False) -> io.BytesIO:
    """
    Create a simple PDF page with the copyright notice using ReportLab.
    
    Args:
        copyright_notice: The copyright text
        decoration: Whether to add decorative elements to make the notice more visually appealing
        
    Returns:
        io.BytesIO: Buffer containing the PDF page
    """
    packet = io.BytesIO()
    font_name = find_suitable_font()
    c = canvas.Canvas(packet, pagesize=letter)
    
    width, height = letter
    
    # Extract information from the copyright notice
    lines = copyright_notice.split('\n')
    title_line = lines[0] if lines else "COPYRIGHT NOTICE / THÔNG BÁO BẢN QUYỀN"
    
    copyright_line = next((line for line in lines if "© " in line), "")
    
    english_start = -1
    vietnamese_start = -1
    
    for i, line in enumerate(lines):
        if "COPYRIGHT (English):" in line:
            english_start = i
        elif "BẢN QUYỀN (Tiếng Việt):" in line:
            vietnamese_start = i
            
    english_section = None
    vietnamese_section = None
    
    if english_start >= 0 and vietnamese_start >= 0:
        english_section = "\n".join(lines[english_start:vietnamese_start-1])
        vietnamese_section = "\n".join(lines[vietnamese_start:])
    
    if decoration:
        # Draw decorative border
        border_color = HexColor('#3E97FF')
        c.setStrokeColor(border_color)
        c.setLineWidth(3)
        c.rect(30, 30, width-60, height-60, stroke=1, fill=0)
        
        # Set initial position
        y_position = height - 80
        
        # Draw title with decorative styling
        title_color = HexColor('#0F4C81')
        c.setFillColor(title_color)
        c.setFont(font_name, 20)
        c.drawCentredString(width/2, y_position, title_line)
        y_position -= 50
        
        # Draw copyright line with color
        if copyright_line:
            c.setFillColor(HexColor('#1E73BE'))
            c.setFont(font_name, 16)
            c.drawCentredString(width/2, y_position, copyright_line)
            y_position -= 60
        
        # Draw English section if available
        if english_section:
            # Draw box background for English section
            section_color = HexColor('#007ACC')
            bg_color = HexColor('#EBF5FF')
            english_lines = english_section.split("\n")
            english_title = english_lines[0] if english_lines else "COPYRIGHT (English):"
            c.setFillColor(bg_color)
            c.rect(50, y_position-150, width-100, 200, stroke=0, fill=1)
            
            # Draw English section title
            c.setFillColor(section_color)
            c.setFont(font_name, 16)
            c.drawString(60, y_position, english_title)
            y_position -= 30
            
            # Draw English content
            c.setFillColor(HexColor('#000000'))  # Black text
            text = c.beginText(60, y_position)
            text.setFont(font_name, 12)
            
            for line in english_lines[1:]:
                words = line.split()
                current_line = ""
                for word in words:
                    test_line = current_line + " " + word if current_line else word
                    if c.stringWidth(test_line, font_name, 12) <= width-130:
                        current_line = test_line
                    else:
                        text.textLine(current_line)
                        current_line = word
                if current_line:
                    text.textLine(current_line)
                text.textLine("")  # Extra line between paragraphs
            
            c.drawText(text)
            y_position = text.getY() - 60
        
        # Draw Vietnamese section if available
        if vietnamese_section:
            # Draw Vietnamese section box
            c.setFillColor(bg_color)
            c.rect(50, y_position-150, width-100, 200, stroke=0, fill=1)
            
            # Draw Vietnamese section title
            c.setFillColor(section_color)
            c.setFont(font_name, 16)
            vietnamese_lines = vietnamese_section.split("\n")
            vietnamese_title = vietnamese_lines[0] if vietnamese_lines else "BẢN QUYỀN (Tiếng Việt):"
            c.drawString(60, y_position, vietnamese_title)
            y_position -= 30
            
            # Draw Vietnamese content
            c.setFillColor(HexColor('#000000'))  # Black text
            text = c.beginText(60, y_position)
            text.setFont(font_name, 12)
            
            for line in vietnamese_lines[1:]:
                words = line.split()
                current_line = ""
                for word in words:
                    test_line = current_line + " " + word if current_line else word
                    if c.stringWidth(test_line, font_name, 12) <= width-130:
                        current_line = test_line
                    else:
                        text.textLine(current_line)
                        current_line = word
                if current_line:
                    text.textLine(current_line)
                text.textLine("")  # Extra line between paragraphs
            
            c.drawText(text)
        
        # Draw CC notice with color
        c.setFillColor(HexColor('#1E73BE'))
        c.setFont(font_name, 10)
        c.drawCentredString(width/2, 50, "Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)")
    else:
        # Original non-decorated version
        # Set initial position
        y_position = height - 60
        
        # Draw title
        c.setFont(font_name, 18)
        c.drawCentredString(width/2, y_position, title_line)
        y_position -= 50
        
        # Draw copyright line
        if copyright_line:
            c.setFont(font_name, 14)
            c.drawCentredString(width/2, y_position, copyright_line)
            y_position -= 60
        
        # Draw English section
        if english_section:
            english_lines = english_section.split("\n")
            c.setFont(font_name, 14)
            c.drawString(40, y_position, english_lines[0])  # Title
            y_position -= 30
            
            # Draw content
            for line in english_lines[1:]:
                text_object = c.beginText(40, y_position)
                text_object.setFont(font_name, 12)
                
                words = line.split()
                current_line = ""
                
                for word in words:
                    test_line = current_line + " " + word if current_line else word
                    text_width_pixels = c.stringWidth(test_line, font_name, 12)
                    
                    if text_width_pixels <= width-80:
                        current_line = test_line
                    else:
                        text_object.textLine(current_line)
                        y_position -= 20
                        current_line = word
                
                if current_line:
                    text_object.textLine(current_line)
                    y_position -= 20
                
                c.drawText(text_object)
            
            # Add spacing between sections
            y_position -= 30
        
        # Draw Vietnamese section
        if vietnamese_section:
            vietnamese_lines = vietnamese_section.split("\n")
            c.setFont(font_name, 14)
            c.drawString(40, y_position, vietnamese_lines[0])  # Title
            y_position -= 30
            
            # Draw content
            for line in vietnamese_lines[1:]:
                text_object = c.beginText(40, y_position)
                text_object.setFont(font_name, 12)
                
                words = line.split()
                current_line = ""
                
                for word in words:
                    test_line = current_line + " " + word if current_line else word
                    text_width_pixels = c.stringWidth(test_line, font_name, 12)
                    
                    if text_width_pixels <= width-80:
                        current_line = test_line
                    else:
                        text_object.textLine(current_line)
                        y_position -= 20
                        current_line = word
                
                if current_line:
                    text_object.textLine(current_line)
                    y_position -= 20
                
                c.drawText(text_object)
        
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

def add_copyright_to_pdf(input_path: str, output_path: str, engine: str = "auto", 
                         copyright_pdf: str = None, decoration: bool = False,
                         custom_title: str = None, custom_holder: str = None,
                         custom_english: str = None, custom_vietnamese: str = None,
                         no_default: bool = False) -> bool:
    """
    Add copyright notice and warning to a PDF file.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path to save the modified PDF file
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        copyright_pdf: Optional path to a custom PDF to use as copyright notice
        decoration: Whether to add decorative elements to the copyright notice
        custom_title: Custom title for the notice
        custom_holder: Custom copyright holder name
        custom_english: Custom English notice text
        custom_vietnamese: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # If a custom copyright PDF is specified and exists, use it directly
        if copyright_pdf and os.path.exists(copyright_pdf):
            try:
                with open(copyright_pdf, "rb") as f:
                    copyright_page = io.BytesIO(f.read())
                return merge_pdfs(copyright_page, input_path, output_path)
            except Exception as e:
                print(f"Error using custom copyright PDF: {str(e)}")
                print(f"Falling back to generated copyright notice...")
                # Fall through to generate a copyright notice
        elif copyright_pdf:
            print(f"Custom copyright PDF not found: {copyright_pdf}. Using generated notice instead.")
        
        # Get the file's last modification date
        mod_date, copyright_year = get_file_modified_date(input_path)
        if not mod_date:
            mod_date = "Unknown"
            copyright_year = str(datetime.now().year)
            
        # Create the copyright notice with custom content if provided
        notice = create_copyright_notice(
            copyright_year, 
            mod_date, 
            custom_title, 
            custom_holder, 
            custom_english, 
            custom_vietnamese, 
            no_default
        )
        
        # Create a PDF page with the notice using the specified engine
        copyright_page = create_copyright_page(notice, engine, decoration)
        
        # Merge the copyright page with the existing PDF
        return merge_pdfs(copyright_page, input_path, output_path)
            
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False

def process_pdf(pdf_path: str, overwrite: bool = False, verbose: bool = True, engine: str = "auto", 
               copyright_pdf: str = None, decoration: bool = False,
               custom_title: str = None, custom_holder: str = None,
               custom_english: str = None, custom_vietnamese: str = None,
               no_default: bool = False) -> bool:
    """
    Process a single PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        overwrite: Whether to overwrite the original file
        verbose: Whether to print progress messages
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        copyright_pdf: Optional path to a custom PDF to use as copyright notice
        decoration: Whether to add decorative elements to the copyright notice
        custom_title: Custom title for the notice
        custom_holder: Custom copyright holder name
        custom_english: Custom English notice text
        custom_vietnamese: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
    Returns:
        bool: True if successful, False otherwise
    """
    print_progress(f"Processing {pdf_path}...", verbose)
    
    # Determine output path based on overwrite flag
    if overwrite:
        output_path = pdf_path + ".temp"
    else:
        output_path = pdf_path.replace(".pdf", "_copyright.pdf")
    
    # Process with appropriate method
    success = False
    if copyright_pdf and os.path.exists(copyright_pdf):
        # Use custom copyright PDF
        print_progress(f"Using custom copyright PDF: {copyright_pdf}", verbose)
        try:
            with open(copyright_pdf, "rb") as f:
                copyright_buffer = io.BytesIO(f.read())
            success = merge_pdfs(copyright_buffer, pdf_path, output_path)
        except Exception as e:
            print(f"Error using custom copyright PDF: {str(e)}")
            print_progress("Falling back to generated copyright notice...", verbose)
            success = add_copyright_to_pdf(pdf_path, output_path, engine, copyright_pdf, decoration,
                                         custom_title, custom_holder, custom_english, custom_vietnamese, no_default)
    else:
        # Generate copyright notice
        if copyright_pdf:
            print_progress(f"Custom copyright PDF not found: {copyright_pdf}. Using generated notice instead.", verbose)
        success = add_copyright_to_pdf(pdf_path, output_path, engine, copyright_pdf, decoration,
                                     custom_title, custom_holder, custom_english, custom_vietnamese, no_default)
    
    # Handle overwrite case if successful
    if success and overwrite:
        try:
            # Try to replace the original file, with up to 3 retries
            max_retries = 3
            retry_count = 0
            while retry_count < max_retries:
                try:
                    os.replace(output_path, pdf_path)
                    print_progress(f"Overwritten: {pdf_path}", verbose)
                    break
                except PermissionError:
                    retry_count += 1
                    if retry_count < max_retries:
                        print_progress(f"File appears to be locked. Retrying in 2 seconds... (Attempt {retry_count}/{max_retries})", verbose)
                        time.sleep(2)
                    else:
                        print(f"Error: Could not overwrite {pdf_path} - file may be in use by another application.")
                        print(f"The modified file has been saved as {output_path}")
                        return False
        except Exception as e:
            print(f"Error replacing file {pdf_path}: {str(e)}")
            print(f"The modified file has been saved as {output_path}")
            return False
    elif success and not overwrite:
        print_progress(f"Created: {output_path}", verbose)
    
    # Clean up temp file if processing failed
    if not success and overwrite and os.path.exists(output_path):
        os.remove(output_path)
        
    return success

def process_directory(directory_path: str, overwrite: bool = False, verbose: bool = True, 
                     engine: str = "auto", ignore: List[str] = None, copyright_pdf: str = None,
                     decoration: bool = False, custom_title: str = None, custom_holder: str = None,
                     custom_english: str = None, custom_vietnamese: str = None, 
                     no_default: bool = False) -> int:
    """
    Process all PDF files in a directory and its subdirectories.
    
    Args:
        directory_path: Path to the directory
        overwrite: Whether to overwrite original files
        verbose: Whether to print progress messages
        engine: The rendering engine to use: 'latex', 'reportlab', or 'auto'
        ignore: List of file patterns to ignore
        copyright_pdf: Optional path to a custom PDF to use as copyright notice
        decoration: Whether to add decorative elements
        custom_title: Custom title for the notice
        custom_holder: Custom copyright holder name
        custom_english: Custom English notice text
        custom_vietnamese: Custom Vietnamese notice text
        no_default: If True, use only custom content
        
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
        if process_pdf(pdf_path, overwrite, False, engine, copyright_pdf, decoration,
                     custom_title, custom_holder, custom_english, custom_vietnamese, no_default):
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
    parser.add_argument("-c", "--copyright-pdf", type=str, metavar="FILE",
                        help="Use a custom PDF file as the copyright notice instead of generating one")
    parser.add_argument("-d", "--decoration", action="store_true",
                        help="Create a more beautiful and colorful version of the copyright notice")
    # New arguments with shortcuts
    parser.add_argument("-t", "--title", type=str, help="Custom title for the copyright notice")
    parser.add_argument("-H", "--holder", type=str, help="Custom copyright holder name")
    parser.add_argument("-E", "--english-notice", type=str, help="Custom English copyright notice")
    parser.add_argument("-V", "--vietnamese-notice", type=str, help="Custom Vietnamese copyright notice")
    parser.add_argument("-n", "--no-default", action="store_true",
                        help="Use only custom content provided, no default text")
    
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
    
    # Check if no-default is set but no custom content is provided
    if args.no_default and not any([args.title, args.holder, args.english_notice, args.vietnamese_notice]):
        print("No action taken: --no-default specified but no custom content provided.")
        return 0
    
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
            
        success = process_pdf(args.path, args.overwrite, args.verbose, args.engine, 
                            args.copyright_pdf, args.decoration, args.title, args.holder,
                            args.english_notice, args.vietnamese_notice, args.no_default)
        return 0 if success else 1
    
    elif os.path.isdir(args.path):
        count = process_directory(args.path, args.overwrite, args.verbose, args.engine, 
                               args.ignore, args.copyright_pdf, args.decoration, args.title,
                               args.holder, args.english_notice, args.vietnamese_notice, args.no_default)
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