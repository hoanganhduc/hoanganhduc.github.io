---
layout: blog-post
title: "Convert DJVU to PDF with text kept in Arch Linux"
author: "Duc A. Hoang"
categories:
  - linux
comment: true
last_modified_at: 2022-11-14
description: This post contains information on how to convert DJVU to PDF with text kept in Arch Linux
keywords: arch, djvu to pdf, text kept, convert
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
In this post, I described how to convert files in [DJVU format](http://djvu.org/) to PDF with text kept in Arch Linux. This post was orginally based on [this instruction for Ubuntu Linux](http://shawnleezx.github.io/blog/2015/03/27/how-to-convert-djvu-file-to-pdf-with-text-kept/) and my experience when installing the necessary packages in Arch.
</div>

# Required Installation

```bash
yay -S ruby-iconv ruby-mini_portile2 ruby-nokogiri ruby-rmagick ruby-hpricot
```

**Update (2022-11-14):** The installation does not seem to work well with `ruby 2.7.0-1`. As a result, use `ruby 2.6.5-1` along with `rubygems 3.1.2-1`, and install the above gems with

```bash
sudo pacman -S imagemagick libmagick6
gem install iconv mini_portile2 nokogiri rmagick hpricot
```

```bash
yay -S ocrodjvu leptonica jbig2enc-git pdfbeads
```

# Converting Script

Download the shell script [djvu_2_pdf.sh](https://raw.githubusercontent.com/shawnLeeZX/daily_tools/master/djvu_2_pdf.sh). (I also keep a copy {% include files.html name="djvu_2_pdf.sh" text="here" %}.) To use this script, in terminal, type

```bash
bash djvu_2_pdf.sh INPUT_FILE
```
