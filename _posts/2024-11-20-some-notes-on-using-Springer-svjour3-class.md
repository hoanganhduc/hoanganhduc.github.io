---
layout: blog-post
title: "Some notes on using Springer svjour3 class"
author: "Duc A. Hoang"
categories:
  - tex
last_modified_at: 2024-11-27
description: This post contains some notes on using Springer svjour3 class to prepare manuscripts and submissions in some Springer journals
keywords: LaTeX, Springer, svjour3, author, tips
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This page contains some notes I find useful when using Springer `svjour3` class to prepare manuscripts and submissions in some journals. You can find [here](https://latextemplates.github.io/LNCS/) a more customized version with several additional features that you can use to prepare your draft. You can find [here]({% post_url 2018-05-26-some-tex-tips %}) some more tips for using TeX and [here]({% post_url 2019-11-20-some-tips-for-using-springer-lncs-style %}) some tips for using Springer LNCS style.

* TOC
{:toc}

</div>

# Download

You can download the `svjour3` class from [here](https://media.springer.com/full/springer-instructions-for-authors-assets/zip/468198_LaTeX_DL_468198_240419.zip). I also downloaded a copy {% include files.html name="468198_LaTeX_DL_468198_240419.zip" text="here" %}. (MD5SUM: `89998b8a6754c5f2349c141a7595c64f`)

# Some Configurations

## Add Statements and Declarations

In the file `svjour3.cls`, there is already a definition for the `acknowledgements` environment. You can use it to add your acknowledgements. Furthermore, some journals require you to add some statements and declarations. To achieve this, one way is to define a new `\declare` command as follows:

```latex
\newcommand{\declare}[2]{
    \renewcommand{\ackname}{#1} % Change the title "Acknowledgements" to #1
    {\begin{acknowledgements}% #2 is the content of the declaration/statement
        #2 
    \end{acknowledgements}}
}
```

And then you can use it as follows:

```latex
\declare{Conflict of interest}{
    The authors declare that they have no conflict of interest.
}
```

## Author-year Citation

To use author-year citation, you can use the `natbib` package with the `svjour3` class. You can use the following commands to set the citation style:

```latex
\usepackage{natbib} 
% show citations like (Author1 et al. 2019; Author2 2020) 
% that is, no comma between the author and the year
\setcitestyle{round,sort&compress,aysep={},yysep={;}} 
\let\cite\citep % Make \cite behave like \citep

% Some other configurations

\begin{document}

% Some contents

% BibTeX users please use one of
\bibliographystyle{spbasic}      % basic style, author-year citations
% \bibliographystyle{spmpsci}      % mathematics and physical sciences
% \bibliographystyle{spphys}       % APS-like style for physics
\bibliography{<your-bib-file>}

\end{document}
```

To display the URLs in the bibliography with blue color, you can use the following configuration in addition to the `hyperref` package:

```latex
% Redefine the \urlstyle command to change the style of URLs in bibliography 
% by setting the URL font color to blue and applies a specific style based on the argument provided
\renewcommand\urlstyle[1]{\renewcommand\UrlFont{\color{blue}\csname url#1style\endcsname}}
```

## `hyperref` Package Settings

```latex
\usepackage{hyperref}
% Hyperref options
\hypersetup{
    hidelinks,          % This option hides the colored boxes around links
    colorlinks=true,    % This option colors the text of links instead of using colored boxes
    allcolors=blue,     % This sets the color of all types of links (e.g., citations, URLs) to blue
    unicode,            % This allows the use of Unicode characters in PDF bookmarks
    bookmarks,          % This enables the creation of bookmarks in the PDF
    bookmarksopen,      % This option makes all bookmarks visible when the PDF is opened
    bookmarksdepth=2    % This sets the depth of the bookmarks tree to 2 levels
}
```
