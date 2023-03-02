---
layout: blog-post
title: Install LaTeX2HTML in Windows
author: Duc A. Hoang
categories:
  - windows
  - tex
<!--comment: true-->
last_modified_at: 2022-11-14
description: This post describes how Duc A. Hoang install LaTeX2HTML in Windows
keywords: latex2html, installation, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains a guide on how to install [LaTeX2HTML](http://www.latex2html.org/) in Windows 64-bit OS. 
</div>

# Perl 5.22.4.2205
Download from [https://www.activestate.com/activeperl/downloads](https://www.activestate.com/activeperl/downloads).

# Netpbm
Install from GNUWin32 [http://gnuwin32.sourceforge.net/packages/netpbm.htm](http://gnuwin32.sourceforge.net/packages/netpbm.htm) 

**Note:** Install to `C:\GNUWin32` directory (or any directory such that the name does not contain a blank space)

# Ghoscript AFPL 8.54
Download from [http://pages.cs.wisc.edu/~ghost/doc/AFPL/](http://pages.cs.wisc.edu/~ghost/doc/AFPL/).

**Note:** Install to `C:\gs` directory.

# GSView 5.0
Download from [http://pages.cs.wisc.edu/~ghost/gsview/get50.htm](http://pages.cs.wisc.edu/~ghost/gsview/get50.htm).

# LaTeX2HTML
Download from [https://github.com/latex2html/latex2html/](https://github.com/latex2html/latex2html/).

# Some notes after installing

* Add the following to `PATH` in Windows via `Control Panel > System and Security > System > Advanced System Settings > Advanced > Environment Variables ...`

```
C:\GnuWin32\bin;C:\gs\gs8.54\bin
```

* Fix error

```
Unmatched [ in regex; marked by <-- HERE in m/^[ <-- HERE .\]/ at C:\latex2html\bin/latex2html.bat line 432.
```
	
when compile with `.latex2html-init`. See [http://tug.org/pipermail/latex2html/2017-October/003977.html](http://tug.org/pipermail/latex2html/2017-October/003977.html).

* Use command: 

```
latex2html -tmp C:\Windows\TEMP somefile.tex 
```
	
for compilation to avoid the error 

```
'/tmp' not usable as temporary directory.
```

* Fix error when using latex2html with option `-html_version 3.2,latin2,unicode` in Windows

```
Extension: loading C:\latex2html\versions\latin1.pl
HTML version: loading C:\latex2html\versions\html3_2.pl

 *** processing declarations ***

Resetting image-cacheCannot read .\latin2.tex
```
	
See [http://tug.org/pipermail/latex2html/2017-October/003985.html](http://tug.org/pipermail/latex2html/2017-October/003985.html) or [http://tug.org/pipermail/latex2html/2017-October/003988.html](http://tug.org/pipermail/latex2html/2017-October/003988.html).

	
