---
layout: blog-post
title: `latex-pax` in Windows and Linux
author: Duc A. Hoang
categories:
  - "windows"
  - "linux"
<!--comment: true-->
last_modified_at: 2024-11-12
description: This post contains information about using latex-pax in Windows and Linux
keywords: latex-pax, windows, linux, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains information about using [latex-pax](https://ctan.org/pkg/pax) (see also [this page](https://github.com/bastien-roucaries/latex-pax)) in Windows and Arch Linux.

</div>

# In Windows

* I installed a full version of TeXLive 2024 from [an ISO image](https://www.tug.org/texlive/acquire-iso.html). This already contains `latex-pax`.
* Download [PDFBox 0.7.3](https://sourceforge.net/projects/pdfbox/files/) and extract the downloaded ZIP file to `C:\`.
* Create a `pax.bat` file with the following content.
  ```
  @echo off
  SETLOCAL
  
  set CLASSPATH=C:\PDFBox-0.7.3\lib\PDFBox-0.7.3.jar;%CLASSPATH%
  perl "C:\texlive\2024\texmf-dist\scripts\pax\pdfannotextractor.pl" %*
  ```
* Run `pax.bat <filename>.pdf` to generate a `<filename>.pax` file that contains the PDF informations of `<filename>.pdf`.

# In Arch Linux

* Again, `latex-pax` is already installed.
* Install `pdfbox` by running `yay -S pdfbox`. You can also download [PDFBox 0.7.3](https://sourceforge.net/projects/pdfbox/files/) and extract the downloaded ZIP file to `/usr/share/java`
* Create a `/usr/bin/pax` file with the following content.
  ```
  #!/bin/sh
  
  PAX_JAR=/usr/share/texmf-dist/scripts/pax/pax.jar
  # PDFBOX_JAR=/usr/share/java/PDFBox-0.7.3/lib/PDFBox-0.7.3.jar
  PDFBOX_JAR=/usr/share/pdfbox/pdfbox.jar
  
  java -cp $PAX_JAR:$PDFBOX_JAR pax.PDFAnnotExtractor "$@"
  ```
  Also run `chmod a+x /usr/bin/pax` as root user to allow everyone to run the command `pax`.
* Run `pax <filename>.pdf` to generate a `<filename>.pax` file that contains the PDF annotations of `<filename>.pdf`.