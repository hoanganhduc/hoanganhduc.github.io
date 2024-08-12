---
layout: blog-post
title: Create Clonezilla Live from scratch
author: Duc A. Hoang
categories:
  - linux
<!--comment: true-->
last_modified_at: 2022-01-11
description: This post contains some notes of Duc A. Hoang on creating Clonezilla Live from scratch
keywords: clonezilla, live, build, debian, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains what I did to create a customized Clonezilla Live ISO image to use with my PC. Several steps here are based primarily on [this guide from Clonezilla's homepage](https://clonezilla.org/create_clonezilla_live_from_scratch.php).
</div>

* I created a virtual machine and run everything with the ISO image `clonezilla-live-2.8.1-12-amd64.iso` I downloaded from [here](https://clonezilla.org/downloads/download.php). I created a virtual hard disk with a single `ext4` partition `/dev/sda1` of size around 5-10 GB for storing the customized ISO image and some temp files.

* Open the virtual machine and boot it with the downloaded Clonezilla Live ISO. Choose `Start Clonezilla > device-image > enter_shell` to enter the command line prompt.

* Run `ocs-live-netcfg` to configure the network so that we can access Debian repository later. Run 
  ```bash
  rsync -aRv /etc/NetworkManager/system-connections ./
  rsync -aRv /var/lib/bluetooth ./
  tar czvf NetworkConnection.tar.gz etc var
  rm -rf etc var
  ```
  to backup the wired/wireless/bluetooth connections you have configured to `NetworkConnection.tar.gz`. This saves some time when you want to generate new images in the future.

* Modify `/etc/apt/sources.list` if you want to assign different apt repository. 

* `mkfs.ext4 /dev/sda1`, then `mount /dev/sda1 /home/partimag`, and finally `cd /home/partimag`.

* If the available space in dir `/tmp` is less than 500 MB (run `df -h` to see the size of `/tmp` and other mounted directories), tune it to be larger than 500 MB. You can make it by the commands like: `mount -t tmpfs -o "nosuid,size=60%,mode=1777" tmpfs /tmp` or `mount -t tmpfs -o "nosuid,size=524288000,mode=1777" tmpfs /tmp`.

* `apt-get -y purge drbl clonezilla`.

* `apt-get update`. **DO NOT** run `apt-get dist-upgrade` or `apt-get upgrade` to upgrade any packages, otherwise this will break the rest of procedure.

* `apt-get -y install drbl clonezilla`.

* If you want to add more packages in Clonezilla Live, and you are sure the packages are included in Debian repository, e.g. `ncpfs`, you can edit `/etc/drbl/drbl.conf`, append `ncpfs` in variable `PKG_FROM_DBN_WHICH_OCS_LIVE_NEED`. I added the following packages:
  ```
  live-boot live-boot-initramfs-tools live-config live-config-systemd live-tools \
  cryptsetup aria2 python3-cryptography squashfs-tools \
  ctorrent mktorrent transmission-cli python3-libtorrent \
  shim-signed grub-efi-amd64-signed syslinux extlinux syslinux-common \
  arch-install-scripts git crda ntp network-manager-openvpn
  ```
 
* `apt-get -y install live-build debootstrap xorriso`.

* `create-debian-live -f amd64 -c 'main contrib non-free' -b unstable -a 'firmware-linux-free firmware-linux ezio ocs-bttrack firmware-atheros firmware-realtek firmware-bnx2 firmware-bnx2x' -i 2.8.1-12-amd64_$(date +%Y%m%d)`. Run `create-debian-live --help` to see all possible options. To create an Ubuntu-based image, use `create-ubuntu-live`. You also need to `apt-get -y install ubuntu-keyring` before running `create-ubuntu-live`.

* Run:
  ```bash
  ocs-iso -s --extra-boot-param "quiet" -j debian-live-for-ocs-2.8.1-12-amd64_$(date +%Y%m%d).iso -i 2.8.1-12-amd64_$(date +%Y%m%d)
  ocs-live-dev -c -s --extra-boot-param "quiet" -j debian-live-for-ocs-2.8.1-12-amd64_$(date +%Y%m%d).iso -i 2.8.1-12-amd64_$(date +%Y%m%d)
  ```
  then 2 files, `clonezilla-live-2.8.1-12-amd64_$(date +%Y%m%d).iso` and `clonezilla-live-2.8.1-12-amd64_$(date +%Y%m%d).zip` will be created, respectively. Here `$(date +%Y%m%d)` will output the current date in the `YYYYMMDD` format.
 
* I created a shell script [genClonezillaLive.sh]({{ site.baseurl }}/clonezilla/genClonezillaLive.sh) to wrap up everything above and more. To use it, simply run `./genClonezillaLive.sh debian` for generating Debian-based images and `./genClonezillaLive.sh ubuntu` for Ubuntu-based images. You can also find the 
ISO and ZIP files I created with this script [here](https://drive.google.com/drive/folders/1VrNDWBveWVqnb1063_ABCMKUOXpkZSPW). To verify a downloaded file, download the file `MD5SUMS` from that page, put it in the same folder with the downloaded ZIP or ISO image, and run `cat MD5SUMS | md5sum -c --ignore-missing`. The size of the Ubuntu-based image is roughly twice the size of the Debian-based one because of the package `linux-firmware`.
