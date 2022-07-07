---
layout: blog-post
title: "Some tips for using Springer LNCS style"
author: "Duc A. Hoang"
categories:
  - tex
last_modified_at: 2022-07-07
description: This post contains some tips for using Springer LNCS style
keywords: LaTeX, Springer, LNCS, author, tips
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This page contains some tips I collected when using Springer LNCS style to prepare manuscripts and submissions in some international conferences. Many of these tips are from [here](http://lata2019.irdta.eu/finalpaperinstructions/).
</div>


* Follow the [instructions for LNCS authors](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines).
* Use the latest [TeXLive system](https://www.tug.org/texlive/), or maybe [Overleaf](https://www.overleaf.com/latex/templates/springer-lecture-notes-in-computer-science/kzwwpvhwnvfj#.WuA4JS5uZpi).
* Include your [ORCID identifier](https://orcid.org/) using the `\orcidID{...}` command. In the published version, the ORCID identifier will be replaced by ORCID icon linked to the corresponding entry in the ORCID database.
* When submitting the camera-ready version, pack your working files (`.tex` file(s), pictures, `splncs04.bst`, a bibliography (`.bib`) file) into a ZIP archive. Make minimal ZIP archives when submitting, do not add `llncs.cls`, the PDF version of the paper or the copyright form.
* Pay a special attention to **overfull boxes**! Use the option `draft` when specifying `\documentclass` to identify such issues.
* Make sure that the figures included in your manuscript look good when printed in **black and white**.
* Do not change the default font of the document, or use too many variations on fonts.
* Use `\documentclass[runningheads, envcountsame, a4paper]{llncs}`; some packages modify the paper format to `letter` if `a4` is not specified.
* Do not use a complicated directory structure for your document. Use as few `.tex` files as possible, a single file is best, name it `main.tex`, it helps the assembling task.
* In English, the first word and the last word of titles should be capitalized. In addition, all nouns, pronouns, adjectives, verbs, adverbs, and subordinate conjunctions should be capitalized. Articles and coordinating conjunctions are not capitalized. Traditionally, prepositions are not capitalized. Use the same conventions for all titles of sections, subsection, etc. If you are not sure, [this tool](https://individed.com/code/to-title-case/) may help.
* LNCS recommends keywords to be added after the abstract using the `\keywords{...}` command, each keyword must be separated by commas or `\and`. Do not use `\newcommand{\keywords}`.
* In `\author{...}` use `\and` as separator between authors names.
* Give all the affiliation (the entries in this order, one entry per line), department, university, street address (including country), e-mail. Do not use comma or dot at the end of each affiliation line.
* Inside the `\authorrunning{}` field of your article, please use only the initial of your first name, followed by a dot. The word "and" between two authors is used without a comma. If there are three or more authors, there is a comma before "and". If headings with author names are not fitting well in the page, then you should use "et al." after the first author.
* Use `\toctitle` and `\tocauthor`, they are important fields defining your paper in the proceedings "Table Of Contents".
* Use `~` between first name and name to avoid a break line inside author's names.
* After `\maketitle`, `\setcounter{footnote}{0}` to start footnotes from 1 after `\thanks`.
* Normally, captions of tables, figures, should end without a dot. If you feel that dots are needed, please be consistent along the whole article. Table captions are **above** the tables, while figures have captions **below**.
* Do not use frames around figures, algorithms, other elements of your paper.
* For "Acknowledge" please use `\section*{Acknowledgments}`.
* Please use [BibTeX](http://www.bibtex.org/Using/). LNCS recommends to include the [DOI](https://www.doi.org/) of each reference if possible. Use `\_` instead of `_` in a DOI number. Or, better, use [bibtex-tidy](https://flamingtempura.github.io/bibtex-tidy/) to produce a nicer BibTeX file. Especially, using the `Escape special characters` option will automatically convert all `_` in a DOI number to `\_`.
* To prevent line breaking in unwanted places, we can use `\mbox{...}`.
* To break a long inline math formula manually, use `\allowbreak` between two `$`s. We can use `\usepackage{breqn}` to break line in equations.
* Do not use `\usepackage[...]{babel}`.
* Do not use whatever fancy signs as in `mathabx`.
* Do not modify `\qed`. It is recommended to use `\begin{proof} <some text> \qed \end{proof}`.
* Do not use `a4wide` or `geometrix`.
* Avoid using `\vspace`, and in any case `\vspace` with a negative argument. If things are not going as we wish, instead of negative `\vspace` there should be another solution.
* Do not use `\newpage` for formatting reasons, trying to fit floating figures or tables.
* Do not `\usepackage{hyperref}`. If you want to use `hyperref`, use `\usepackage[hidelinks]{hyperref}`.
* Do not `\usepackage{caption}`.
* Do not use `\mainmatter`; this is a command only for the whole volume, for papers inside the volume this is rather undesirable.
* Do not use `\sloppy`; a simple solution for overfull errors could be to rephrase the sentences causing problems; in many cases `\usepackage{microtype}` helps too.
* Use `\email{...}` to include author's email. If you want `{author1,author2,...}@...` in your manuscript, please use `\email{$\{$author1,... $\}$@...}`.
* Use `\fnmsep` (i.e. footnote mark separator) to separate `\thanks` by `\inst`.
* Use `algorithm2e` for listings of algorithms. I often use the options `linesnumbered,ruled,noend` for the `algorithm2e` package.
* Use `\figurename~\ref{fig:a}` instead of `Fig.~\ref{fig:a}`.
* `pdflatex` processes a bit better than the sequence `latex`, `dvips`, `pspdf`. Thus, using together
```bash
\usepackage[pdftex]{graphicx}
\usepackage{epstopdf}
```
could help to switch from `latex` to `pdflatex`.
* `\usepackage[hyphens]{url}` improves the aspects of hyperlinks in the final document.
* Use
```bash
\makeatletter
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                       {-12\p@ \@plus -4\p@ \@minus -4\p@}%
                       {-0.5em \@plus -0.22em \@minus -0.1em}%
                       {\normalfont\normalsize\bfseries}}
\makeatother
```
to re-define `\paragraph` with **bold** text style instead of *italic*.
* Use
```bash
\let\claim\relax % undefined 'claim' environment
\spnewtheorem{claim}{Claim}{\itshape}{\rmfamily}
```
if you want to number the "Claim" environment.
* In case we wish to avoid the warning message `Package amsmath Warning: Unable to redefine math accent \vec`, use
```bash
\let\accentvec\vec
\documentclass[runningheads, envcountsame, a4paper]{llncs}
\let\spvec\vec
\let\vec\accentvec
```
* For tables giving an Overfull Errors, we can simply correct with `\resizebox{\textwidth}{!}{\begin{tabular}{|l||c|c|c|c|c|}...\end{tabular}}`. Another way is to use the `adjustbox` package and place the `tabular` environment between `\begin{adjustbox}{max width=\textwidth}` and `\end{adjustbox}`.
* If we need subfigures, then we could
`\usepackage[caption=false]{subfig}` ...and when needed the subfigures...
```bash
\begin{figure}
\centering
\subfloat[label (a)\label{fig:label:a}]{
\includegraphics[width=.48\textwidth]{subfig_a}
}
\subfloat[label (b)) \label{fig:label:b}]{
\includegraphics[width=.48\textwidth]{subfig_b}
}
\caption{general caption}
\end{figure}
```
