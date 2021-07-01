---
layout: blog-post
title: "Some TeX Tips"
author: "Duc A. Hoang"
categories:
  - tex
<!--comment: true-->
description: This post contains some tips of Duc A. Hoang on using LaTeX
keywords: tex, beamer, usage, tips, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some tips for using TeX that I collected from different sources.

</div>

# BibTeX Tidy

[BibTeX Tidy](https://github.com/FlamingTempura/bibtex-tidy), as introduced in its [web version](https://flamingtempura.github.io/bibtex-tidy/), tidies bibtex files by fixing inconsistent whitespace, removing duplicates, removing unwanted fields, and sorting entries.

# Beamer: bibliography icon with `biblatex`

The original source is at [https://tex.stackexchange.com/a/68084](https://tex.stackexchange.com/a/68084).

Add the followings to the preamble.

```latex
\documentclass{beamer}
\usepackage[style=authoryear,backend=bibtex]{biblatex}
\usepackage{hyperref}

\setbeamertemplate{bibliography item}{
  \ifboolexpr{ test {\ifentrytype{book}} or test {\ifentrytype{mvbook}}
    or test {\ifentrytype{collection}} or test {\ifentrytype{mvcollection}}
    or test {\ifentrytype{reference}} or test {\ifentrytype{mvreference}} }
    {\setbeamertemplate{bibliography item}[book]}
    {\ifentrytype{online}
       {\setbeamertemplate{bibliography item}[online]}
       {\setbeamertemplate{bibliography item}[article]}}%
  \usebeamertemplate{bibliography item}}

\defbibenvironment{bibliography}
  {\list{}
     {\settowidth{\labelwidth}{\usebeamertemplate{bibliography item}}%
      \setlength{\leftmargin}{\labelwidth}%
      \setlength{\labelsep}{\biblabelsep}%
      \addtolength{\leftmargin}{\labelsep}%
      \setlength{\itemsep}{\bibitemsep}%
      \setlength{\parsep}{\bibparsep}}}
  {\endlist}
  {\item}

\addbibresource{biblatex-examples.bib}

\nocite{glashow,markey,knuth:ct:a,knuth:ct:b,companion,bertram,ctan}
\begin{frame}[noframenumbering,plain,allowframebreaks]{References}
\printbibliography
\end{frame}

```

# Beamer: Insert logo on the upper right corner of every frame

Add the followings to the preamble.

```latex
\newcommand\AtPagemyUpperLeft[1]{\AtPageLowerLeft{
\put(\LenToUnit{0.88\paperwidth},\LenToUnit{0.92\paperheight}){#1}}}
\AddToShipoutPictureFG{
	\AtPagemyUpperLeft{
	{
		\includegraphics[width=1.5cm,keepaspectratio]{fig/logo.jpg}
	}
	}
}%
```

It is better to re-define ``frametitle'' to put logo on the upper-right corner, as follows:

```latex
\setbeamertemplate{frametitle}
{
    \begin{beamercolorbox}[rounded=true,sep=0.3cm,ht=1.7em,wd=\paperwidth]{frametitle}
        \insertframetitle
        \hfill
        \raisebox{-0.8mm}{\includegraphics[width=1cm]{fig/logo.png}}
    \end{beamercolorbox}
}
```

# Beamer: Table of contents at the beginning of every section and subsection

```latex
\AtBeginSection[]
{
\begin{frame}
\frametitle{Outline}
\tableofcontents[currentsection]
\end{frame}
}
\AtBeginSubsection[]
{
\begin{frame}
\frametitle{Outline}
\tableofcontents[currentsection,
		 currentsubsection,
		 hideothersubsections,
		 sectionstyle=show/shaded,
		 subsectionstyle=show/shaded,]
\end{frame}
}
```

# `tcolorbox`: Some boxes I defined

A manual for the `tcolorbox` package can be found [here](http://mirror.hmc.edu/ctan/macros/latex/contrib/tcolorbox/tcolorbox.pdf).

```latex
\usepackage[most]{tcolorbox}
% Highlight Oval Box
\newtcbox{\xmybox}[1][red]{on line,
arc=7pt,colback=#1!10!white,colframe=#1!50!black,
before upper={\rule[-3pt]{0pt}{10pt}},boxrule=1pt,
boxsep=0pt,left=6pt,right=6pt,top=2pt,bottom=2pt}
%% Usage: \xmybox[green]{<some content>}
% Box for stating problems
\newtcolorbox{defbox}[1]{
    enhanced,
    attach boxed title to top   left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
    colback=blue!5!white,
    colframe=blue!75!black,
    coltitle=blue!80!black,
    left=1mm,right=1mm,top=2mm,bottom=0mm,
    title={#1},
    fonttitle=\bfseries,
    boxed title style={size=small,colback=blue!5!white,colframe=blue!75!black}
}%
%% Usage \begin{defbox}{<title>} <some content> \end{defbox}
% Box for announcement
\newtcolorbox{infobox}[1]{
    enhanced,
    attach boxed title to top   left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
    colback=green!5!white,
    colframe=green!75!black,
    coltitle=green!80!black,
    left=1mm,right=1mm,top=2mm,bottom=0mm,
    title={#1},
    fonttitle=\bfseries,
    boxed title style={size=small,colback=green!5!white,colframe=green!75!black}
}%
%% Usage \begin{infobox}{<title>} <some content> \end{infobox}
% Theorem Box
\newtcbtheorem[number within=section]{thrm}%
  {Theorem}{theorem style=plain,
    enhanced jigsaw,
    top=0mm,bottom=0mm,
     fonttitle=\bfseries\upshape,fontupper=\slshape,
     colframe=blue!75!black,colback=blue!5!white,coltitle=blue!50!blue!75!black}{thrm}%
%% Usage \begin{thrm}{<title>}{<label>} <some content> \end{thrm}
%% For citation, use ref{thrm:<label>}
%% If you don't want to use numbering: \begin{thrm*}{<title>}{<label>} <some content> \end{thrm*}
```

Some other boxes I used are:

```latex
{% raw %}
%% Boxes with tcolorbox
%%% Highlight Oval Box
\newtcbox{\xmybox}[1][red]{on line,
	arc=7pt,colback=#1!10!white,colframe=#1!50!black,
	before upper={\rule[-3pt]{0pt}{10pt}},boxrule=1pt,
	boxsep=0pt,left=6pt,right=6pt,top=2pt,bottom=2pt}
%%% Box for stating problems
%%%%%%%%
%Usage: (similar for infobox)
%	\begin{defbox}{title}
%		contents
%	\end{defbox}
%%%%%%%%
\newtcolorbox{defbox}[1]{%
	enhanced,
	attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	colback=cyan!5!white,
	colframe=cyan!75!black,
	coltitle=cyan!80!black,
	left=0mm,right=0mm,top=2mm,bottom=0mm,
	title={#1},
	fonttitle=\bfseries,
	boxed title style={size=small,colback=cyan!5!white,colframe=cyan!75!black}
}%
%%% Box for announcement
\newtcolorbox{infobox}[1]{%
	enhanced,
	attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	colback=yellow,
	colframe=red!75!black,
	coltitle=red!75!black,
	left=0mm,right=0mm,top=2mm,bottom=0mm,
	title={#1},
	fonttitle=\bfseries,
	boxed title style={size=small,colback=yellow,colframe=red!75!black}
}%
%%% Theorem Box
%%%%%%%%
%Usage: (similar for conjecture, lemma, etc.)
%	\begin{thm}{title}{nameref}
%		contents
%	\end{thm}
% Use \ref{thm:nameref} to refer to the theorem
%%%%%%%%
%%%% Use \newtcbtheorem[number within=section]{thm} to number within each section
\newtcbtheorem[]{thm}%
{Theorem}{attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	enhanced jigsaw,
	top=2mm,bottom=0mm,left=0mm,right=0mm,
	fonttitle=\bfseries,fontupper=\itshape,
	colframe=green!75!black,colback=green!5!white,coltitle=green!50!green!75!black,
	boxed title style={size=small,colback=green!5!white,coltitle=green!50!green!75!black}}{thm}%
%%% Proposition Box
\newtcbtheorem[use counter from=thm]{prop}%
{Proposition}{attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	enhanced jigsaw,
	top=2mm,bottom=0mm,left=0mm,right=0mm,
	fonttitle=\bfseries,fontupper=\itshape,
	colframe=gray!75!black,colback=gray!5!white,coltitle=gray!50!gray!75!black,
	boxed title style={size=small,colback=gray!5!white,coltitle=gray!50!gray!75!black}}{prop}%
%%% Conjecture Box
\newtcbtheorem[use counter from=thm]{conj}%
{Conjecture}{attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	enhanced jigsaw,
	top=2mm,bottom=0mm,left=0mm,right=0mm,
	fonttitle=\bfseries,fontupper=\slshape,
	colframe=orange!75!black,colback=orange!5!white,coltitle=orange!50!orange!75!black,
	boxed title style={size=small,colback=orange!5!white,coltitle=orange!50!orange!75!black}}{conj}%
%%% Lemma Box
\newtcbtheorem[use counter from=thm]{lem}%
{Lemma}{attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	enhanced jigsaw,
	top=2mm,bottom=0mm,left=0mm,right=0mm,
	fonttitle=\bfseries,fontupper=\itshape,
	colframe=blue!75!black,colback=blue!5!white,coltitle=blue!50!blue!75!black,
	boxed title style={size=small,colback=blue!5!white,coltitle=blue!50!blue!75!black}}{lem}%
%%% Claim Box
\newtcbtheorem[use counter from=thm]{clm}%
{Claim}{attach boxed title to top 	left={xshift=2mm,yshift=-3mm,yshifttext=-1mm},
	enhanced jigsaw,
	top=2mm,bottom=0mm,left=0mm,right=0mm,
	fonttitle=\bfseries,fontupper=\itshape,
	colframe=pink!75!black,colback=pink!5!white,coltitle=pink!50!pink!75!black,
	boxed title style={size=small,colback=pink!5!white,coltitle=pink!50!pink!75!black}}{clm}%
{% endraw %}
```

Note that the Lemma, Claim, Conjecture, Proposition Boxes use the same counter as the Theorem Box (because I use option `use counter from=thm`). Note that in Beamer, you also need to add 

```latex
{% raw %}
%% Reset counter on overlays
\resetcounteronoverlays{tcb@cnt@thm}
{% endraw %}
```

to get the correct numbering when using overlays (see [this page](https://tex.stackexchange.com/a/330064)).

# Beamer: Creating handout with `pgfpages`

```latex
\documentclass[handout]{beamer}
\usepackage{pgfpages}
\pgfpagesuselayout{4 on 1}[a4paper,landscape=true]
```

# Beamer: Several authors with different institutions

The original source is at [https://tex.stackexchange.com/a/17963](https://tex.stackexchange.com/a/17963).

```latex
\author[shortname]{author1 \inst{1} \and author2 \inst{2}}
\institute[shortinst]{\inst{1} affiliation for author1 \and %
                      \inst{2} affiliation for author2}
```

# Beamer: Remove footer in the title page

```latex
{
\setbeamertemplate{footline}{}  % Remove footer in the title page
 
}
\addtocounter{framenumber}{-1} % Do not count the title page in frame numbering
```

# Beamer: Customize titlepage

The original tutorial is at [https://tex.stackexchange.com/a/25318](https://tex.stackexchange.com/a/25318). The idea is to use `\defbeamertemplate`.

```latex
\documentclass{beamer}
\defbeamertemplate*{title page}{customized}[1][]
{
  \usebeamerfont{title}\inserttitle\par
  \usebeamerfont{subtitle}\usebeamercolor[fg]{subtitle}\insertsubtitle\par
  
  \usebeamerfont{author}\insertauthor\par
  \usebeamerfont{institute}\insertinstitute\par
  \usebeamerfont{date}\insertdate\par
  \usebeamercolor[fg]{titlegraphic}\inserttitlegraphic
}
\title{A customized title page}
\subtitle{for demonstration}
\author{Stefan Kottwitz}
\date{\today}

```

# Beamer: Adjust space between frametitle and content

The original source is at [https://latex.org/forum/viewtopic.php?t=15137](https://latex.org/forum/viewtopic.php?t=15137).

You can set the distances that fit your need.

```latex
% The first \vspace* moves the frametitle, and the second one moves the text coming after the frame title
\addtobeamertemplate{frametitle}{\vspace*{0cm}}{\vspace*{-0.5cm}}
```

You can also use `\vspace` command to manually ``adjust'' your Beamer frames when using overlay and other animation stuffs.

# Beamer: Different contents in presentation slide and handout 

```latex

\mode<beamer|second|trans|article>{
\setbeamercolor{background canvas}{bg=}
% insert stuffs used in the presentation slide only
}

\mode<handout>{
\setbeamercolor{background canvas}{bg=}
% insert stuffs used in the handout only
}
```

# Insert PDF file

To insert a PDF file, in the preamble, add the `pdfpages` package.

```latex
% Include PDF
\usepackage{pdfpages}
```

For instance, to insert all pages in `file.pdf`:

```latex
\includepdf[pages=-]{file.pdf}
```

For more information, see the package's [documentation](https://ctan.org/pkg/pdfpages).
Use the [bookmark](https://ctan.org/pkg/bookmark) package if you want to manually create a bookmark entry linking to each inserted PDF file's first page.
More precisely, using `\includepdf[link]{<file>}` creates hyperlink destinations of the form `<file>.<page number>`, which is then used in the destination key for `\bookmark[dest={<file>.<page number>}]{<custom title>}` to link to the first page. Say, if you have two files `1.pdf` and `2.pdf` then what you can do are as folllows. (The original guide can be found [here](https://tex.stackexchange.com/a/284633).)

```latex
\documentclass{article}
\usepackage{bookmark,pdfpages}
\begin{document}

\includepdf[link]{1.pdf}

\includepdf[link]{2.pdf}

\bookmark[dest={1.pdf.1}]{file 1.pdf title}
\bookmark[dest={2.pdf.1}]{file 2.pdf title}

\end{document}
```

# Beamer: Handle overlays while printing handout

The original source is at [https://tex.stackexchange.com/a/129165](https://tex.stackexchange.com/a/129165).

In specifying overlay options, you can add the `handout:<number>` option. For example, `\only<1-3| handout:1>{content-1}` will print `content-1` that appears in frames 1 to 3 as the first page of the handout; `\only<4-5| handout:2>{content-2}` prints `content-2` which appears in frames 4 and 5 as the second page of the handout; and `\only<6-| handout:0>{content-3}` will instruct beamer not to print `content-3` that appears on frame 6 onwards. Notice that a space is needed between `|` and `handout`.

To not show an item/graphic in the handout, simply set `handout:0`.

# Some packages for reviewing and editing TeX documents

* `latexdiff`.

  `latexdiff` is a Perl script for visual mark up and revision of significant differences between two LaTeX files. 
  A short introduction on how to use `latexdiff` can be found [here](https://www.overleaf.com/learn/latex/Articles/Using_Latexdiff_For_Marking_Changes_To_Tex_Documents).

* `easyReview`.

  Another option for editing TeX documents is to use the [easyReview](https://ctan.org/pkg/easyreview) package. 
  See the package's [documentation](http://mirrors.ctan.org/macros/latex/contrib/easyreview/doc/easyReview.pdf) to know how to use this package.

* `todonotes`.

  The [todonotes](https://ctan.org/pkg/todonotes) package allows the user to mark things to do later, in a simple and visually appealing way. 
  See its [documentation](http://ftp.jaist.ac.jp/pub/CTAN/macros/latex/contrib/todonotes/todonotes.pdf) for more information.

* `minorrevision`.

  The [minorrevision](https://ctan.org/pkg/minorrevision) package supports those who publish articles in peer-reviewed journals. 
  In the final stages of the review process, the authors typically have to provide an additional document (such as a letter to the editors), in which they provide a list of modifications that they made to the manuscript. 
  The package automatically provides line numbers and quotations from the manuscript, for this letter.
  The package loads the package [lineno](https://ctan.org/pkg/lineno), so (in effect) shares `lineno`'s incompatibilities.
  
# Sync LaTeX papers between [GitHub](https://github.com/) and [Overleaf](https://www.overleaf.com/)

Suppose you have an Overleaf project <a href="https://www.overleaf.com/project/5ce5fb7abb7ad36e4a0f60bf">https://www.overleaf.com/project/<span style="color:red">5ce5fb7abb7ad36e4a0f60bf</span></a>. Overleaf will also provide you a link <a href="https://git.overleaf.com/5ce5fb7abb7ad36e4a0f60bf">https://git.overleaf.com/<span style="color:red">5ce5fb7abb7ad36e4a0f60bf</span></a> for using with `git`.

If you have no GitHub repository for managing your paper, you can create one, say `paper`, at the address, say `git@github.com/[your-github-username]/paper.git`. The workflow is simple: you first clone the Overleaf project, and then push it to GitHub.

* Clone Overleaf project

  ```bash
  git clone https://git.overleaf.com/5ce5fb7abb7ad36e4a0f60bf paper # everything now on the paper folder
  ```

  Overleaf may asks you to input your Overleaf's username and password. To enable credentials storage in `git`, use `git config --global credential.helper store`. For convenience, I want to rename the `origin` endpoint to `overleaf` using `git remote rename origin overleaf`. Then, when pushing and pulling Overleaf's project, I can simply use `git push -u overleaf master` and `git pull overleaf master`.

* Pushing to GitHub

  ```bash
  cd paper # the folder cloned from Overleaf
  git remote add github git@github.com/[your-github-username]/paper.git
  git add --all .
  git commit -S -m "initial commit"
  git push -u github master
  ```

## Other configuration

I also created a `Makefile` but do not want to put it in the repository. A simple way is to create `.gitignore` file and put the name `Makefile` in that file. An example of a `Makefile` I created may be as follows.

```bash
update:
	git pull overleaf master

push:
	@read -p "Commit message: " MESSAGE; git add --all .; git commit -S -m "$$MESSAGE"; git push -u overleaf master; git push -u github master

pdf:
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex

clean:
	rm -rf *.bbl *.pdf *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.eps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~
```

## A possibly better plan

A better plan is I get from [this blog post](https://saik.at/blog/github-and-overleaf-integration/) to maintain two branches on GitHub: `master` branch for your paper, and `overleaf` branch for updating changes from Overleaf, and then merge the two at a regular interval.
Basically, to create new `overleaf` branch:

```bash
git checkout --orphan overleaf
git rm -rf .
git remote add overleaf https://git.overleaf.com/5ce5fb7abb7ad36e4a0f60bf
git pull overleaf master --allow-unrelated-histories
```

The `.git/config` file needs manual editing to include the `pushurl` for Overleaf and separate tracking for `overleaf` branch of Github:

```bash
[remote "overleaf"]
	url = https://git.overleaf.com/5ce5fb7abb7ad36e4a0f60bf
	fetch = +refs/heads/*:refs/remotes/overleaf/*
	pushurl = https://git.overleaf.com/5ce5fb7abb7ad36e4a0f60bf
[branch "overleaf"]
	remote = overleaf
	merge = refs/heads/master
```

To push everything to Overleaf remote repository:

```bash
git add --all .
git commit -m "push changes to Overleaf"
git push -u overleaf overleaf:master
```

Now, to push everything from Overleaf to Github's `overleaf` branch:

```bash
git add --all .
git commit -m "push changes from Overleaf to GitHub"
git push -u origin overleaf
```

To merge `overleaf` branch onto `master` branch:

```bash
git checkout master
git merge --no-commit --no-ff overleaf
git commit -m "Merge overleaf onto master"
git push -u origin master
```

and for the opposite side:

```bash
git checkout overleaf
git merge --no-commit --no-ff master
git commit -m "Merge master onto overleaf"
git push -u origin overleaf
git push -u overleaf overleaf:master
```

# Insert a blank page

I use the command `\blankpage` as defined in [https://tex.stackexchange.com/a/374542](https://tex.stackexchange.com/a/374542). Simply insert it to where you want to have an empty page.

```latex
{% raw %}
\def\blankpage{%
      \clearpage%
      \thispagestyle{empty}%
      \addtocounter{page}{-1}%
      \null%
      \clearpage}
{% endraw %}
```

# Break long inline math formula

Insert `\allowbreak` where you want to break the formmula, for example, like `$x_1, x_2,...x_k,\allowbreak y_1,y_2,y_n$`. 
Note that this does not work if you have `\left...\right` delimiters that span the break in your equation.

# Table spacing example

From [here](https://www.overleaf.com/read/ndndjhrbbptf).

```latex
{% raw %}
%\title{LaTeX Table spacing example}  
% Example by John Hammersley

\documentclass{article}
\usepackage[usenames,dvipsnames]{xcolor}
\begin{document}

\section*{Table with default spacings}

% A table with the default row and column spacings
\begin{tabular}{ c c c }
First Row & -6 & -5 \\
Second Row & 4 & 10\\
Third Row & 20 & 30\\
Fourth Row & 100 & -30\\
\end{tabular}

\section*{Table with adjusted spacings}

% A table with adjusted row and column spacings
% \setlength sets the horizontal (column) spacing
% \arraystretch sets the vertical (row) spacing
\begingroup
\setlength{\tabcolsep}{10pt} % Default value: 6pt
\renewcommand{\arraystretch}{1.5} % Default value: 1
\begin{tabular}{ c c c }
First Row & -6 & -5 \\
Second Row & 4 & 10\\
Third Row & 20 & 30\\
Fourth Row & 100 & -30\\
\end{tabular}
\endgroup
% The \begingroup ... \endgroup pair ensures the separation
% parameters only affect this particular table, and not any
% sebsequent ones in the document.

\end{document}
{% endraw %}
```

# Change title of TOC

```latex
...
\renewcommand{\contentsname}{New TOC title} % default is "Contents"
....
\begin{document}
...
\tableofcontents
...
\end{document}
```
