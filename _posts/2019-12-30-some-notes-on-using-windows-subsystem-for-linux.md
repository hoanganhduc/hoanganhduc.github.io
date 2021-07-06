---
layout: blog-post
title: "Some notes on using Windows Subsystem for Linux"
author: "Duc A. Hoang"
categories:
  - windows
comment: true
description: This post describes some notes on using Windows Subsystem for Linux
keywords: file permission, wsl, import, export
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes on using Windows Subsystem for Linux.

* TOC
{:toc}
</div>

# File permissions in WSL

Here, we describe how to handle file permission in Windows Subsystem for Linux. 
It was originally from [here](https://www.turek.dev/post/fix-wsl-file-permissions/).

Windows Subsystem for Linux (WSL) usually mounts Windows drives under `/mnt`.
However, the Linux file permission seems to be awful.
To fix this issue, simply add to `/etc/wsl.conf` (if the file does not exist, simply create it):

```bash
[automount]
enabled = true
options = "metadata,umask=22,fmask=11"
```

In short, every files now have permission `0644` and every directories have permission `0755`.

Also, add the following to `~/.profile` to fix the permission of newly created files and directories.

```bash
if [[ "$(umask)" = "0000" ]]; then
	umask 0022
fi
```

# Export and import WSL Distros

* **Export:** Let say I want to export my `Arch` WSL Distro which I downloaded from [this page](https://github.com/yuk7/ArchWSL) and customized for my personal use (it was pretty much like [what I did in my real Arch system]({% link _posts/2018-05-26-some-notes-on-installing-arch-linux.md %})). The following command, executed in `cmd`, will compress the distro into a single file `%userprofile%\Desktop\ArchWSL.tar`. (The `%userprofile%` directory is `C:\Users\[your-username]`.)

  ```bash
  wsl --export Arch %userprofile%\Desktop\ArchWSL.tar
  ```
  
  Additionally, as the size of my `ArchWSL.tar` is too big (around 8GB), I decided to compress it with [7-Zip](https://www.7-zip.org/) using the following command
  
  ```bash
  "C:\Program Files\7-Zip\7z.exe" a -tzip %userprofile%\Desktop\ArchWSL.tar.zip -m0=LZMA -mx=9 %userprofile%\Desktop\ArchWSL.tar
  ```
  
  Basically, the above command will create an archive `ArchWSL.tar.zip` in the folder `%userprofile%\Desktop` with "ultra" compression (option `-mx=9`, the highest compression level used by `7-Zip`) using the [LZMA compression method](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) (option `-m0=LZMA`), which is the default and general compression method of `7z` format. Use the `-sdel` option if you want to delete `%userprofile%\Desktop\ArchWSL.tar` after compression (Be careful!). If you want to protect the archive with a password, use the option `-p[your-password]` (there is no space between `-p` and your password).

* **Import:** To import back the exported distro, in case we compressed `ArchWSL.tar` with `7-Zip` before, we first need to extract `ArchWSL.tar.zip`, say, to the `%userprofile%\Desktop` folder. 
  
  ```bash
  "C:\Program Files\7-Zip\7z.exe" x ArchWSL.tar.zip -o%userprofile%\Desktop
  ```
  
  If the archive is password-protected, the program will ask you to enter the password you used at the time it was created.
  Now, we can import back the distro by running in `cmd` the following command:
  
  ```bash
  wsl --import Arch %localappdata%\Packages\yuk7.archwsl_35zwpb4sx6e50\LocalState %userprofile%\Desktop\ArchWSL.tar
  ```
  
# Copy contents of a file to clipboard

```bash
clip.exe < file.txt # do not miss the .exe part
```
# SSH

I use `keychain` to avoid typing SSH passphrases multiple times. After installing `keychain` in my Arch WSL, I simply put the following to `.bashrc`

```bash
/usr/bin/keychain --nogui $HOME/.ssh/id_rsa
source $HOME/.keychain/$HOST-sh
```

In this way, I have to type in the passphrase for the first time I open a Arch WSL terminal. As long as the distribution is running (which can be veerified by typing `wsl -l --running` in a `cmd` windows), I don't have to type it again when using `ssh`.

Another way is to use [wsl-ssh-agent](https://github.com/rupor-github/wsl-ssh-agent).

# Install SageMath 9.3 on Ubuntu WSL

## Enable WSL2

Follow [this official instruction](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Install Ubuntu (version 18.04 or newer) as a WSL

Follow [this official instruction](https://ubuntu.com/wsl).
After finishing installation, run the following in a `cmd` or `powershell` (if you run `wsl --set-default-version 2`, you don't need to do this):

```bash
wsl --set-version Ubuntu 2
```

Adjust file permissions in Ubuntu if necessary, following the [above instruction](#file-permissions-in-wsl).

## Installation

Follow [this instruction](https://doc.sagemath.org/html/en/installation/source.html).
I recorded the steps here.
Open a Ubuntu terminal and run:

```bash
sudo apt update
sudo apt upgrade
```

```bash
sudo apt-get install  bc binutils bzip2 ca-certificates cliquer curl eclib-tools fflas-ffpack flintqs g++ g++ gcc gcc gfan gfortran glpk-utils gmp-ecm lcalc libatomic-ops-dev libboost-dev libbraiding-dev libbrial-dev libbrial-groebner-dev libbz2-dev libcdd-dev libcdd-tools libcliquer-dev libcurl4-openssl-dev libec-dev libecm-dev libffi-dev libflint-arb-dev libflint-dev libfreetype6-dev libgc-dev libgd-dev libgf2x-dev libgiac-dev libgivaro-dev libglpk-dev libgmp-dev libgsl-dev libhomfly-dev libiml-dev liblfunction-dev liblrcalc-dev liblzma-dev libm4rie-dev libmpc-dev libmpfi-dev libmpfr-dev libncurses5-dev libntl-dev libopenblas-dev libpari-dev libpcre3-dev libplanarity-dev libppl-dev libpython3-dev libreadline-dev librw-dev libsqlite3-dev libssl-dev libsuitesparse-dev libsymmetrica2-dev libz-dev libzmq3-dev libzn-poly-dev m4 make nauty openssl palp pari-doc pari-elldata pari-galdata pari-galpol pari-gp2c pari-seadata patch perl pkg-config planarity ppl-dev python3 python3 python3-distutils r-base-dev r-cran-lattice sqlite3 sympow tachyon tar xcas xz-utils yasm
```

```bash
sudo apt-get install  cmake coinor-cbc coinor-libcbc-dev git graphviz libboost-dev libfile-slurp-perl libigraph-dev libisl-dev libjson-perl libmongodb-perl libnauty-dev libperl-dev libsvg-perl libterm-readkey-perl libterm-readline-gnu-perl libterm-readline-gnu-perl libxml-libxslt-perl libxml-writer-perl libxml2-dev libxml2-dev lrslib ninja-build pari-gp2c tox
```

```bash
wget http://www.mirrorservice.org/sites/www.sagemath.org/src/sage-9.3.tar.gz
echo "e826c848c6bb972a188d5ddd4dc48308 sage-9.3.tar.gz" | md5sum -c
tar -xvf sage-9.3.tar.gz -C $HOME
cd $HOME/sage-9.3
./configure
make
```

**Note:** The compilation may take very long time (around 3 hours in my computer).

## To open SageMath Jupyter Notebook in Google Chrome

In Ubuntu Terminal. run:

```bash
cd $HOME/sage-9.3
sage jupyter notebook –generate-config
```

Edit `$HOME/.sage/jupyter-4.1/jupyter_notebook_config.py` by adding the following content to the end:

```
#——————————————————————————
# NotebookApp(JupyterApp) configuration
#——————————————————————————
c.NotebookApp.use_redirect_file = False
```

Finally, add the following to `$HOME/.bashrc`:

```bash
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
```

Note that `C:\Program Files\Google\Chrome\Application\chrome.exe` is the location of Google Chrome installed in my computer.