---
layout: blog-post
title: Install package <code>pgfornament</code> for TeXLive 2012 in Ubuntu 12.04 LTS
author: Duc A. Hoang
categories:
  - "linux"
  - "tex"
<!--comment: true-->
last_modified_at: 2024-03-19
description: This post describes how to install package pgfornament for TeXLive 2012 in Ubuntu 12.04 LTS
keywords: Ubuntu 12.04, LaTeX, pgfornament, TexLive 2012
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
The [pgfornament](https://ctan.org/pkg/pgfornament) package allows the drawing of Vectorian ornaments (196) with [PGF/TikZ](https://ctan.org/pkg/pgf). This post describes how to install `pgfornament` for TeXLive 2012 in Ubuntu 12.04 LTS.
</div>

The package can be downloaded from [CTAN](http://mirrors.ctan.org/macros/latex/contrib/tkz/pgfornament.zip).

We will install the package on the `$TEXMFLOCAL` folder, which in my case is `/usr/local/texlive/texmf-local/`. First, extract the downloaded ZIP file to the `~/Downloads` folder, then in terminal, type

```bash
cd ~/Downloads/pgfornament
sudo cp pgfornament.sty /usr/local/texlive/texmf-local/tex/latex
sudo cp tikzrput.sty /usr/local/texlive/texmf-local/tex/latex
sudo cp pgflibraryam.code.tex /usr/local/texlive/texmf-local/tex/latex
sudo cp pgflibraryvectorian.code.tex /usr/local/texlive/texmf-local/tex/latex
sudo mkdir /usr/local/texlive/texmf-local/tex/generic
sudo cp vectorian/* /usr/local/texlive/texmf-local/tex/generic
sudo cp am/* /usr/local/texlive/texmf-local/tex/generic
sudo mktexlsr
```
