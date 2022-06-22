---
layout: blog-post
title: "Writing a KAKENHI grant proposal using LaTeX"
author: "Duc A. Hoang"
categories:
  - tex
  - linux
  - windows
last_modified_at: 2021-09-27
description: This post contains some tips for using LaTeX to write a KAKENHI grant proposal 
keywords: LaTeX, KAKENHI, grant proposal, tips
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This page contains some tips I collected when using LaTeX to write a [KAKENHI](https://www.jsps.go.jp/english/e-grants/) grant proposal. Please note that **this is not a guide on how to write a KAKENHI grant proposal**.

* TOC
{:toc}
</div>

# Some available templates

## 科研費LaTeX templates (in Japanese)

The page [科研費LaTeX](http://osksn2.hep.sci.osaka-u.ac.jp/~taku/kakenhiLaTeX/) contains a collection of templates for writing KAKENHI grant proposals. You can also find the templates on [Overleaf](https://www.overleaf.com/gallery/tagged/japanese+grant-application). Using Japanese templates to write proposals in English seems to be a reasonable option.

## English templates I modified from 科研費LaTeX

In case you want everything to be in English, you can find some templates I modified from 科研費LaTeX at [https://github.com/hoanganhduc/TeX-Templates#kakenhiLaTeX](https://github.com/hoanganhduc/TeX-Templates#kakenhiLaTeX). If you are familiar with LaTeX, you can modify them to fit your requirements.

## Use the PDF template provided by JSPS as "background"

With the [pdfoverlay](https://ctan.org/pkg/pdfoverlay) package, you can include the PDF template provided by JSPS (which may be obtained by exporting the corresponding DOC version after deleting all unnecessary comments) as "background", and then start writing. 
To see an example I created with `pdfoverlay` and other packages, download {% include files.html name="s-21_e-2021_fall.tar.gz" text="s-21_e-2021_fall.tar.gz" %}.

# Convert PDF to grayscale using Ghostscript

This is useful when you want to convert color PDF to a grayscale (black and white) one. You will need [Ghostscript](https://www.ghostscript.com/download/gsdnld.html).
In Linux, you can use something like
```bash
gs -q -r600 -dNOPAUSE \
	-sDEVICE=pdfwrite \
	-o <input-file>.pdf \
	-dPDFSETTINGS=/prepress \
	-dOverrideICC \
	-sProcessColorModel=DeviceGray \
	-sColorConversionStrategy=Gray \
	-sColorConversionStrategyForImage=Gray \
	-dGrayImageResolution=600 \
	-dMonoImageResolution=600 \
	-dColorImageResolution=600 \
	-f <output-file>.pdf
```
Replace `<input-file>` and `<output-file>` appropriately.

In Windows 10 64bit, you can use a similar command, just replacing `gs` by something like `"C:\Program Files\gs\gs9.54.0\bin\gswin64c.exe"`, or simply just `gswin64c` if the directory `C:\Program Files\gs\gs9.54.0\bin\` (or other directory, depending on the version of Ghostscript you installed) was already specified in the `PATH` environment variable.

# Some TeX tips

## Page layout

You can `\usepackage{geometry}` to customize page layout. From the JSPS guidelines for preparing and entering a research proposal document: "The margin of style is set with upper 20mm, lower 20mm, left 25mm, and right 25mm." 

```latex
%% Adjust paper size and margins
\usepackage{geometry}
\geometry{
	a4paper,
	left=25mm,
	right=25mm,
	top=20mm,
	bottom=20mm
}
```

## Page style

Use `\pagestyle{empty}` to remove page numbering.

## Using `hyperref`

For example, some `hyperref` options can be:

```latex
\usepackage{hyperref}
\hypersetup{
%	bookmarks=true, % show bookmarks bar?
	bookmarksnumbered, % put section numbers in bookmarks
	hidelinks, % hide links (removing color and border)
	unicode=true, % non-Latin characters in Acrobat’s bookmarks
	pdftitle={Form S-21: Research Proposal Document (forms to be uploaded)}, % title
	pdfauthor={<your-name>}, % author
	pdfsubject={Grant Proposal}, % subject of the document
	pdfcreator={LaTeX}, % creator of the document
	pdfproducer={pdfTeX}, % producer of the document
	pdfkeywords={grant proposal, kakenhi, early-career scientists}, % list of keywords
	pdfstartview={FitH} % fits the width of the page to the window
}
```

## Fonts

* See [this page](https://en.wikibooks.org/wiki/LaTeX/Fonts) for more details on fonts in LaTeX. 
* A recommendation is to use **Times New Roman** font with size **11pt** for the **main text** and (probably) 9pt for references. There is no actual Times New Roman font in native LaTeX, but you can `\usepackage{newtxtext}` or `\usepackage{newtxtext,newtxmath}`.

## Improving full justification with `microtype`

You can `\usepackage{microtype}`. See [this blog post](https://texblog.net/latex-archive/latex-general/pdflatex-microtype/) for an example of what `microtype` can do.

## Figures/Tables

* <span style="color:red;">[Important]</span> Make sure that your figures/tables can be viewed clearly when the proposal is printed in **black and white**.
* To utilize spaces, you can `\usepackage{wrapfig}` to wrap text around figures. To adjust the space around the `wrapfigure` environment (see [this page](https://tex.stackexchange.com/a/111397) for more details), use
  ```latex
  %% Adjust space around wrapfigure
  \setlength{\intextsep}{0pt}%
  \setlength{\columnsep}{5pt}%
  ```
* To reduce the space between caption and figure/table (default is 10pt, see [this page](https://tex.stackexchange.com/a/94018)), use
  ```latex
  %% Reduce space between caption and figure/table (default=10pt)
  \usepackage{caption} 
  \captionsetup[figure]{skip=3pt} % figure
  \captionsetup[table]{skip=3pt} % table
  ```
* Avoid using `\begin{center}` and `\end{center}` to center the figure/table, it adds extra space. Use `\centering` instead.
* Caption name of figures can be changed by `\renewcommand{\figurename}{Fig.}`.
* [TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) produces nice figures. Another choice is [Ipe](https://ipe.otfried.org/).

## Adjusting space

Use `\vspace` to adjust vertical spaces. Basically, `\vspace` inserts space after the *current line*. Additionally, `\vspace*` inserts spaces even at the start of the page, while `\vspace` does not. For adjusting horizontal spaces, use `\hspace` or `\hspace*`.

## Using fake sections

See [this page](https://tex.stackexchange.com/a/129985) for more details.
Basically, "a `\fakesection` does all the things the regular `\section` does except print the actual heading".

```latex
{% raw %}\newcommand{\fakesection}[1]{%
	\par\refstepcounter{section}% Increase section counter
	\sectionmark{#1}% Add section mark (header)
	\addcontentsline{toc}{section}{\protect\numberline{\thesection}#1}% Add section to ToC
	% Add more content here, if needed.{% endraw %}
}
```

## Redefine `\subsection` and `\subsubsection` formats with the `titlesec` package

```latex
%% Redefine \subsection and \subsubsection formats
\usepackage{titlesec}
\renewcommand\thesubsection{\arabic{subsection}} % numbering subsections by 1, 2, 3
\titleformat{\subsection}[runin]
{\normalfont\normalsize\bfseries}{\thesubsection.}{0.5em}{}[]
\titlespacing{\subsection}{0pt}{1pt}{0.4em}
\titleformat{\subsubsection}[runin]
{\normalfont\normalsize\bfseries}{\thesubsubsection.}{0.5em}{}[]
\titlespacing{\subsubsection}{0pt}{1pt}{0.4em}
```

## Bibliography

* <span style="color:red;">[Important]</span> Remember to <u>underline your name</u> in **all of your publications**. To underline texts, you can `\usepackage[normalem]{ulem}`. The option `normalem` prevents `ulem` from replaceing *italics* with <u>underlining</u> in text emphasized by `\emph`.
* You can simply use `thebibliography` environment. For example:
  ```latex
  {\footnotesize
   \begin{thebibliography}{99}
       \bibitem{citekey} Author A. "A nice article", Journal X, YYYY.
   \end{thebibliography}
  }
  ```
* Another way is to use `biblatex` with `refsection` to print a bibliography for each section. For example, in the preamble, use
  ```latex
  %% Biblatex
  \usepackage[backend=biber, sorting=none, style=numeric-comp, firstinits=true, url=false, doi=false, isbn=false]{biblatex}
  \addbibresource{refs.bib}
  \renewcommand*{\bibfont}{\footnotesize} % default: article=11pt => footnotesize=9pt 
  ```
  and then in the body of the document, you can use something like
  ```latex
  \fakesection{Research Objectives, Research Method, etc.}
  
  \begin{refsection}
  
  %%% content goes here
  
  %% bibliography with biblatex (uncomment and modify)
  \printbibliography[heading=subbibliography]
  \end{refsection}
  ```
  You can also `\setlength\bibitemsep{0pt}` to remove the space between two consecutive bibentries.
  Adding `\AtBeginBibliography{\vspace*{-5pt}}` to the preamble to reduce the space between the bibliography heading and the first bibentry by 5pt. 

## Compiling TeX files

* Use [TeX Live](https://www.tug.org/texlive/) or [Overleaf](https://www.overleaf.com/).
* Use [latexmk](https://ctan.org/pkg/latexmk/) to avoid manually running `pdflatex` and `biber` multiple times. 
* Use a `.latexmkrc` or `latexmkrc` file if you use the `jarticle` class instead of `article`. Some examples of `.latexmkrc` for Japanese documents are available in [this page](https://qiita.com/ymfj/items/088fa556c94fc9ab460f) or [this page](https://doratex.hatenablog.jp/entry/20180503/1525338512). You can also [use a `.latexmkrc` file on Overleaf](https://www.overleaf.com/learn/latex/Articles/How_to_use_latexmkrc_with_Overleaf:_examples_and_techniques).

## Revising TeX files

* You can keep track of what you have been written by using [Overleaf](https://www.overleaf.com/).
* You can `\usepackage{lineno}` to display line numbers (see [this page](https://ctan.org/pkg/lineno) for more details).
* You can use [latexdiff](https://ctan.org/pkg/latexdiff) or [git-latexdiff](https://ctan.org/pkg/git-latexdiff) to produce a PDF file showing what you have editted.
