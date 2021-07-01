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
  
## Copy contents of a file to clipboard

```bash
clip.exe < file.txt # do not miss the .exe part
```
## SSH

I use `keychain` to avoid typing SSH passphrases multiple times. After installing `keychain` in my Arch WSL, I simply put the following to `.bashrc`

```bash
/usr/bin/keychain --nogui $HOME/.ssh/id_rsa
source $HOME/.keychain/$HOST-sh
```

In this way, I have to type in the passphrase for the first time I open a Arch WSL terminal. As long as the distribution is running (which can be veerified by typing `wsl -l --running` in a `cmd` windows), I don't have to type it again when using `ssh`.

Another way is to use [wsl-ssh-agent](https://github.com/rupor-github/wsl-ssh-agent).