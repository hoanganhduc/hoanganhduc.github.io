---
layout: blog-post
title: Arch Linux
author: Duc A. Hoang
date: 2020-03-15
<!--comment: true-->
description: This page contains some personal Arch Linux settings of Duc A. Hoang
keywords: arch linux, repository, installation, live ISO
<!--published: false-->
---

## User Repository Information

* **Maintainer:** Duc A. Hoang.
* **Description:** A repo containing [some packages I often use]({% post_url 2018-05-26-some-notes-on-installing-arch-linux %}), following [this ArchWiki tutorial](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Custom_local_repository). (Packages of size larger than 100MB are not available due to [GitHub's file size limit](https://help.github.com/en/github/managing-large-files/what-is-my-disk-quota#file-and-repository-size-limitations).)
* **PGP Key ID:** `FBEAAAD6C193858F7D9BCFD73D544026D4E51506`.
* **Upstream page:** [https://hoanganhduc.github.io/archlinux](https://hoanganhduc.github.io/archlinux).
* **Usage:**
  * Run the following as `root`.
  
    ```bash
    pacman-key --keyserver pool.sks-keyservers.net --recv-keys FBEAAAD6C193858F7D9BCFD73D544026D4E51506
    pacman-key --lsign-key FBEAAAD6C193858F7D9BCFD73D544026D4E51506
    ```
  * Add the following to `/etc/pacman.conf`.
  
    ```bash
    [hoanganhduc]
    Server = https://hoanganhduc.github.io/archlinux/$arch
    ```

## Live Arch ISO

Using this repository, [archiso](https://wiki.archlinux.org/index.php/Archiso) and some additional configurations, one can build a live Arch ISO image. Here are some images I created for my own personal use. 

### archlinux-2020.11.04-x86_64.iso [unofficial]

To recreate what I have built, download [livearch.tar.gz]({{ site.baseurl }}/archlinux/iso/livearch.tar.gz) (or [livearch-20201104-x86_64.tar.gz]({{ site.baseurl }}/archlinux/iso/livearch-20201104-x86_64.tar.gz)), and with `root` permission: extract it with `tar xvf livearch.tar.gz` to obtain the `livearch` folder, edit `livearch/profiledef.sh` by commenting out (adding `#` at the beginning of) the line `gpg_key="FBEAAAD6C193858F7D9BCFD73D544026D4E51506"`, and run `./build.sh -v` inside the `livearch` folder. (You may need around 25 - 30 GiB of free disk space, and the package [archiso-47.1-1](https://archive.archlinux.org/packages/a/archiso/archiso-47.1-1-any.pkg.tar.zst).)

* **Dowload:** [Google Drive](https://drive.google.com/file/d/1RKzdxJDcYOj6OChZ7IE9wLeOScjv1L3O) (5.5 GiB - 5,887,365,120 bytes)
* **Created:**  2020-11-04 19:15:15.202939463 +0900
* **Included Kernel:** linux 5.7.12-arch1-1
* **PGP Signature:** [archlinux-2020.11.04-x86_64.iso.sig]({{ site.baseurl }}/archlinux/iso/archlinux-2020.11.04-x86_64.iso.sig)
* **MD5:** 047c4aa98bfbfa5a80949c98346595e3
* **SHA1SUM:** 16729b3ec9be4097a45f6640e4f075b493b3eb5f

### archlinux-2020.03.14-x86_64.iso [unofficial]

To recreate what I have built, use [livearch-20200314-x86_64.tar.gz]({{ site.baseurl }}/archlinux/iso/livearch-20200314-x86_64.tar.gz) and [archiso-43-1](https://archive.archlinux.org/packages/a/archiso/archiso-43-1-any.pkg.tar.xz).

* **Dowload:** [Google Drive](https://drive.google.com/open?id=1AlQm9OnWJ24AY5R69Q7vGyxFGzUVBNN4) (4.0 GiB - 4,261,412,864 bytes)
* **Created:** 2020-03-15 00:46:18.699853700 +0900
* **Included Kernel:** linux-lts 4.19.101-2
* **PGP Signature:** [archlinux-2020.03.14-x86_64.iso.sig]({{ site.baseurl }}/archlinux/iso/archlinux-2020.03.14-x86_64.iso.sig)
* **MD5:** a6de7d31ddabad70a9cc693d3bf022af
* **SHA1SUM:** 40458b4d2fd6ce0a8aba6b3b328c54f2d670847d

### How to verify?

Let say you want to verify `archlinux-2020.03.14-x86_64.iso`.

* Verify **PGP Signature**
  ```bash
  gpg --verify archlinux-2020.03.14-x86_64.iso.sig archlinux-2020.03.14-x86_64.iso
  ```

* Verify **MD5** and **SHA1SUM**
  ```bash
  echo a6de7d31ddabad70a9cc693d3bf022af archlinux-2020.03.14-x86_64.iso | md5sum -c
  echo 40458b4d2fd6ce0a8aba6b3b328c54f2d670847d archlinux-2020.03.14-x86_64.iso | sha1sum -c
  ```










