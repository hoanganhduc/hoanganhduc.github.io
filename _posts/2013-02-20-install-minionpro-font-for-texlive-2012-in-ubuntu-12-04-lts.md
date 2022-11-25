---
layout: blog-post
title: Install MinionPro font for TeXLive 2012 in Ubuntu 12.04 LTS
author: Duc A. Hoang
categories:
  - "linux"
  - "tex"
<!--comment: true-->
last_modified_at: 2022-11-14
description: This post describes how to install MinionPro font for TeXLive 2012 in Ubuntu 12.04 LTS
keywords: Ubuntu 12.04, LaTeX, MinionPro, TexLive 2012
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post aims to record the process of installing the MinionPro font for TeXLive 2012 in Ubuntu 12.04 LTS. The post from [Carlo Hamalainen's blog](https://carlo-hamalainen.net/2007/12/11/installing-minion-pro-fonts/) was very helpful for me to work with the install process.
</div>

# Locate `$TEXMFLOCAL`
First, find the `$TEXMFLOCAL` folder using the following commands

```bash
kpsexpand '$TEXMFLOCAL'
```

The result in my terminal was `/usr/local/texlive/2012/../texmf-local`, which indicates that the `$TEXMFLOCAL` folder is `/usr/local/texlive/texmf-local/`. We shall install the fonts to that folder. Assume that all the required files are placed in `~/Downloads` folder.

# Install MnSymbol

Download the file {% include files.html name="MnSymbol-1.4.zip" text="MnSymbol-1.4.zip" %} and extract it to `~/Downloads`. In terminal, type

```bash
cd ~/Downloads/MnSymbol-1.4/tex
latex MnSymbol.ins
sudo mkdir -p /usr/local/texlive/texmf-local/tex/latex/MnSymbol/
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/source/public/MnSymbol/
sudo mkdir -p /usr/local/texlive/texmf-local/doc/latex/MnSymbol/
sudo cp MnSymbol.sty /usr/local/texlive/texmf-local/tex/latex/MnSymbol/
cd..
sudo cp source/* /usr/local/texlive/texmf-local/fonts/source/public/MnSymbol/
sudo cp MnSymbol.pdf README /usr/local/texlive/texmf-local/doc/latex/MnSymbol/
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/map/dvips/MnSymbol
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/enc/dvips/MnSymbol
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/type1/public/MnSymbol
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/tfm/public/MnSymbol
sudo cp enc/MnSymbol.map /usr/local/texlive/texmf-local/fonts/map/dvips/MnSymbol/
sudo cp enc/*.enc /usr/local/texlive/texmf-local/fonts/enc/dvips/MnSymbol/
sudo cp pfb/*.pfb /usr/local/texlive/texmf-local/fonts/type1/public/MnSymbol/
sudo cp tfm/* /usr/local/texlive/texmf-local/fonts/tfm/public/MnSymbol/
sudo mktexlsr
sudo updmap-sys --enable MixedMap MnSymbol.map
```

# Install MinionPro

Download the files 
* {% include files.html name="MinionProFonts.zip" text="MinionProFonts.zip" %}
* {% include files.html name="scripts.zip" text="scripts.zip" %}
* {% include files.html name="metrics-base.zip" text="metrics-base.zip" %}
* {% include files.html name="metrics-full.zip" text="metrics-full.zip" %}
* {% include files.html name="enc-1.001.zip" text="enc-1.001.zip" %}

Next, extract `scripts.zip` to get the `scripts` folder. Then, extract all the OTF fonts in `MinionProFonts.zip` to the `scripts/otf` folder. In terminal, type

```bash
cd ~/Downloads/scripts
./convert.sh
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/type1/adobe/MinionPro/
sudo cp pfb/*.pfb /usr/local/texlive/texmf-local/fonts/type1/adobe/MinionPro/
cd /usr/local/texlive/texmf-local
sudo unzip ~/Downloads/metrics-base.zip
sudo unzip ~/Downloads/metrics-full.zip
sudo unzip ~/Downloads/enc-1.001.zip
```

Edit the file `updmap.cfg`
```bash
sudo gedit /usr/local/texlive/2012/texmf-dist/web2c/updmap.cfg
```
by adding `Map MinionPro.map` to the end of the file.

Then, in terminal, type
```bash
sudo mktexlsr
sudo update-updmap
sudo updmap-sys
```
The process in finished.

**Note:** The required files can also be downloaded from [CTAN](https://ctan.org/tex-archive/fonts/minionpro/).





