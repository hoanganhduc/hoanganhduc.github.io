---
layout: default
title: "TeX Resources"
last_modified_at: 2024-12-20
description: TeX Resources collected by Duc A. Hoang
keywords: resource, tex, setting, template, Duc A. Hoang
directory-listing: true
buymeacoffee: true
---

# Personal TeX Settings and Templates

<div class="directory-listing" markdown="1">
{% include_relative dircontent.html %}
</div>

-----

# Some Tips and Tricks

<ul>

{% for post in site.categories.tex %}
<li><a href="{{ post.url }}">{{ post.title }}</a> <time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">({% if post.lang == "vi" %}<b>Cập nhật:</b> {{ post.last_modified_at | date: "%d tháng %m, %Y" }}{% else %}<b>Updated:</b> {{ post.last_modified_at | date: "%B %d, %Y" }}{% endif %})</time></li>
{% endfor %}

</ul>

# More Resources

* Some [TeX templates](https://github.com/hoanganhduc/TeX-Templates) I collected. Some of them are available on [Overleaf](https://www.overleaf.com/latex/templates?q=Duc+A.+Hoang).
* [Historic archive of TeX material](https://www.tug.org/historic/).
* [TeX Resources on the Web](https://www.tug.org/interest.html).
* [The LaTeX Project](https://www.latex-project.org/).
* More Templates
  * [Mẫu soạn LaTeX](https://vietex.blog.fc2.com/blog-entry-182.html), sưu tập bởi thầy Nguyễn Hữu Điển.
  * [Japan IEICE LaTeX Style](https://www.ieice.org/ftp/index-e.html). (See also [Cloud LaTeX](https://cloudlatex.io/), an online TeX editor with several Japanese templates.)
  * Jesper Kjær Nielsen's collection of [Aalborg University LaTeX-templates](https://github.com/jkjaer/aauLatexTemplates).
  * [Amurmaple Beamer Theme](https://gitlab.gutenberg-asso.fr/mchupin/amurmaple).
  * [LATEX macros for TUGboat articles](https://ctan.org/pkg/tugboat).
* TeX Editors and Softwares
  * [Overleaf](https://www.overleaf.com/) -- one of the most popular online TeX editors.
  * [VieTeX](https://nhdien.wordpress.com/) -- Chương trình soạn thảo TeX với nhiều mẫu tiếng Việt có sẵn chạy trên nền Windows. (Xem [Cài đặt VieTeX trong Windows 10 với Chocolatey](https://hoanganhduc.github.io/blog/2020/12/21/c%C3%A0i-%C4%91%E1%BA%B7t-vietex-trong-windows-10-v%E1%BB%9Bi-chocolatey/).)
  * [TeXstudio](https://www.texstudio.org/) -- a cross-platform open-source LaTeX editor.
  * [TeX Live](https://www.tug.org/texlive/), availble for Linux, MacOS, and Windows.
  * [LaTeX Cloud Compiler](https://latexonline.cc/), build a PDF from GIT repository with TeX files.
  * [Tools for Publishing LaTeX Documents on the Web](https://ccrma.stanford.edu/~jos/webpub/webpub.html) (Julius Orion Smith III) -- A really nice tutorial about how to generate HTML pages with [LaTeX2HTML](https://www.latex2html.org/).
  * [LaTeXML](https://dlmf.nist.gov/LaTeXML/) -- A LaTeX to XML/HTML/MathML Converter.
  * [bibtex2html](https://www.lri.fr/~filliatr/bibtex2html/) -- BibTeX to HTML Converter.
  * [BibTeX Tidy](https://github.com/FlamingTempura/bibtex-tidy) -- This tool tidies BibTeX files by fixing inconsistent whitespace, removing duplicates, removing unwanted fields, and sorting entries. You can [use it online](https://flamingtempura.github.io/bibtex-tidy/).
  * [arxiv-collector](https://github.com/djsutherland/arxiv-collector) -- A little Python script to collect LaTeX sources for upload to the arXiv.
  * [pympress](https://github.com/Cimbali/pympress) -- A simple yet powerful PDF reader designed for dual-screen presentations.
* [Detexify](http://detexify.kirelabs.org/classify.html) (Draw a symbol to get its corresponding LaTeX command).
* [LaTeX Color](http://latexcolor.com/).
* [Online tutorials on LaTeX (Indian TUG)](https://www.tug.org/tutorials/tugindia/).
* [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX/).
* [LaTeX and Friends](https://www.springer.com/gp/book/9783642238154), by [Marc van Dongen](http://csweb.ucc.ie/~dongen), and its [supplementary webpage](http://csweb.ucc.ie/~dongen/LAF/LAF.html).
* [Beamer](https://github.com/josephwright/beamer).
  * [Beamer User Guide](http://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf).
  * [Charles Batts Beamer Tutorial](https://www.uncg.edu/cmp/reu/presentations/Charles\%20Batts\%20-\%20Beamer\%20Tutorial.pdf).
  * [Beamer Theme Gallery](http://www.deic.uab.es/~iblanes/beamer_gallery/).
* [VisualTikZ](https://ctan.org/pkg/visualtikz).
* [TikZ and PGF Resources](http://www.texample.net/tikz/resources/).
* [PGF/TikZ Manual](https://tikz.dev/).
* [Blog](https://vietex.blog.fc2.com/) và [nhóm Facebook](https://www.facebook.com/groups/vietex/) về *LaTeX và Ứng Dụng* của thầy Nguyễn Hữu Điển, tác giả [VieTeX](https://nhdien.wordpress.com/).
* [LaTeX Notes for Professionals](https://goalkicker.com/LaTeXBook/).
* [LaTeX Documents for École Doctorale Physique en Île-de-France (ED PIF, The Doctoral School)](https://www.edpif.org/documents/?f=latex). [[7Z](edpif_latex.7z)]