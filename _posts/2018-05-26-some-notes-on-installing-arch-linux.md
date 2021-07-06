---
layout: blog-post
title: Some notes on installing Arch Linux
author: Duc A. Hoang
categories:
  - linux
<!--comment: true-->
description: This post contains some notes of Duc A. Hoang on installing Arch Linux
keywords: arch linux, installation, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes I want to remember when installing Arch Linux. I will keep updating its contents as time goes by. 

**Note (2020-09-30):** For a more secure system, I am now using [Arch Linux with UEFI boot and full disk encryption]({% link _posts/2020-09-30-arch-linux-with-uefi-boot-and-full-disk-encryption.md %}).

* TOC
{:toc}
</div>

# Install Arch Linux

The official Arch Linux can be downloaded from [https://www.archlinux.org/download/](https://www.archlinux.org/download/). 
If you are new to Arch Linux, it is better to install [Manjaro Linux](https://manjaro.org/) or [Anarchy-Linux](https://anarchy-linux.org/).
The installation guide can be found at [https://wiki.archlinux.org/index.php/installation_guide](https://wiki.archlinux.org/index.php/installation_guide).
Here, I describe how I install Arch Linux to my [ASUS X44H laptop](https://www.asus.com/me-en/Laptops/X44H/).

## Create live USB of Arch Linux

I download the latest ISO from [https://www.archlinux.org/download/](https://www.archlinux.org/download/) and create a live USB with that iso file.
In a Linux system, you can use the `dd` command

```bash
dd bs=4M if=/path/to/archlinux.iso of=/dev/sdx status=progress && sync
```

In a Windows system, my recommendation is [Rufus](https://rufus.akeo.ie/) or [Ventoy](https://www.ventoy.net/).
You can also [remaster the install ISO](https://wiki.archlinux.org/index.php/Remastering_the_Install_ISO).

**Update (2020-09-23):** I also created [some custom Arch Live ISOs for my personal use]({{ site.baseurl }}/archlinux/).

## Keyboard

I have the default console keymap (i.e., US), so I do not need to re-configure the keyboard layout. 
To list all available layouts, use

```bash
ls /usr/share/kbd/keymaps/**/*.map.gz
```

To set a layout, use `loadkeys` command.

## Boot mode

To verify if your computer supports [UEFI](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface), use `ls /sys/firmware/efi/efivars`.
If the directory does not exist, your computer does not support UEFI.
In fact, my computer supports both [UEFI](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface) and [BIOS](https://en.wikipedia.org/wiki/BIOS) boot modes.

## Internet connection

If you connect to the internet using wired network devices (as I do) then you can verify the connection (which is enabled on boot by the installation image) using `ping` command. 
See [this page](https://wiki.archlinux.org/index.php/Network_configuration) for more details on how to configure a network connection.

## Time settings

Use the command

```bash
timedatectl set-ntp true
```

to ensure the system clock is accurate.

<!--
**Update (2019-12-31):** I use the package `tz-data 2016j-1` (downloaded from [here](https://archive.org/download/archlinux_pkg_tzdata/tzdata-2016j-1-any.pkg.tar.xz)) in order to get an old representation of time zones (e.g., `date +%Z` will output `ICT` for the `Asia/Ho_Chi_Minh` timezone, and the latter version of `tz-data` will output `+07`). 
-->

## Disk partitions

The command `fdisk -l` lists all available storage devices and its partitions.
Suppose that I install the system in `/dev/sda`.
To create/delete/re-size a partition in a storage device, I use [cfdisk](https://jlk.fjfi.cvut.cz/arch/manpages/man/cfdisk.8) (DOS partition tables). 

I created three partitions `/dev/sda1`, `/dev/sda2`, and `/dev/sda3` for `/`, `/home`, and swap, respectively. 
It is recommended that if you have less than 1GB RAM then you should spend 1GB for swap, if you have 2-4GB RAM then you should spend half of the size of RAM for swap, and otherwise you should spend 2GB for swap.

To format a partition, use the command `mkfs.filsystem_type /dev/sdax`, here `filesystem_type` can be `ext2`, `ext4`, `jfs`, etc., and `/dev/sdax` is the partiton number.
You should also format and enable the swap partition with the `mkswap` and `swapon` commands.

```bash
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda2
mkswap /dev/sda3
swapon /dev/sda3
```

## Mount the system

For example,
* Mount the root partition (mount point `/`) at `/mnt`.
  
  ```bash
  mount /dev/sda1 /mnt
  ```
  
* Create `/mnt/home` for mounting the home partition (mount point `/home`). 

  ```bash
  mkdir -p /mnt/home
  mount /dev/sda2 /mnt/home
  ```
  
* I have Windows OS installed in `/dev/sda4`, so I create `/mnt/windows` directory for mounting the partition.

  ```bash
  mkdir -p /mnt/windows
  mount /dev/sda4 /mnt/windows
  ```

## Basic packages

```bash
pacstrap /mnt base base-devel linux-lts linux-lts-headers linux-firmware
```

It might be safer to use the [Linux LTS kernel](https://www.archlinux.org/packages/core/x86_64/linux-lts/) instead of the latest one.
<!--
**Update (2020-03-13):** When using LTS kernel versions `>= 5.4.17-1`, the webcam of my [ASUS X44H laptop](https://www.asus.com/me-en/Laptops/X44H/) only shows a black screen. Downgrading to version `4.19.101-2` resovles this issue.
-->

I also want to use `wifi-menu` (a part of the [netctl](https://wiki.archlinux.org/index.php/Netctl) package) in my newly installed system:

```bash
pacstrap /mnt netctl iw dialog wpa_supplicant
```

## Generate a `fstab` file

A `fstab` file defines how disk partitions, block devices or remote file systems are mounted into the filesystem.

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

The option `-U` indicates defining by [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier).
To define by labels, use option `-L`.

## Configure new system

### Change root into the new system with

```bash
arch-chroot /mnt
```

### Set timezone

```bash
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
hwclock --systohc # generate /etc/adjtime
```

For Vietnamese, the Region is `Asia`, and the City is `Ho_Chi_Minh`.

### Locale

Uncomment `en_US.UTF-8 UTF-8` and other needed localizations in `/etc/locale.gen`, and generate them with:

```bash
locale-gen
```

Set the `LANG` variable in `/etc/locale.conf` accordingly, for example `LANG=en_US.UTF-8`.

### Hostname

Create `/etc/hostname` 

```bash
echo my_hostname > /etc/hostname
```

and matching entries to `/etc/hosts`

```bash
127.0.0.1 localhost
::1 localhost
127.0.1.1 my_hostname.localdomain my_hostname
```

### Users

To change root password, use `passwd` command. 
To create a new user, use `useradd` command.
For example, 

```bash
useradd -m -g users -G audio,lp,optical,storage,video,wheel,games,power,scanner -k /etc/skel/ -s /bin/bash user
```

Use `/usr/bin/zsh` instead of `/bin/bash` if you want to use [Z Shell](https://en.wikipedia.org/wiki/Z_shell) instead of [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) as your default shell. 
Now, edit `/etc/sudoers` by uncommenting the line `%wheel ALL=(ALL) ALL` to allow all members of the group `wheel` sudo access.
To add an user to a group, use `usermod -aG <group name> <username>`.
To remove an user, use `userdel <username>`.
To remove a group, use `groupdel <groupname>`.
To change a user default shell, use `chsh -s <shell>`, where `<shell>` can be obtained from a list resulted by running `chsh -l`.

See [this page](https://wiki.archlinux.org/index.php/users_and_groups) for more details.
For making your `bash` or `zsh` shells look more beautiful, see also [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) and [oh-my-bash](https://github.com/ohmybash/oh-my-bash).

### Boot loader

My [ASUS laptop](https://www.asus.com/me-en/Laptops/X44H/) has *Intel(R) Pentium(R) CPU B950 @ 2.10GHz* (use `cat /proc/cpuinfo` to show CPU info), so I need to first install `intel-ucode` package using

```bash
pacman -S intel-ucode
```

I also have Windows partition, so I need `os-prober` package.

```bash
pacman -S os-prober
```

I also edit `/etc/default/grub` by changing

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet"
```
into

```bash
GRUB_CMDLINE_LINUX_DEFAULT=""
```

Now, I can run the grub installation using

```bash
grub-install /dev/sda
```

and finally generate the grub configuration file

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

### Initramfs

I modify `/etc/mkinitcpio.conf` by changing 

```bash
HOOKS=(base udev autodetect modconf block filesystems keyboard fsck)
```

into

```bash
HOOKS=(base udev autodetect modconf block filesystems keyboard fsck shutdown)
```

and recreate the initramfs image with

```bash
mkinitcpio -p linux-lts
```

## Reboot

Exit the chroot environment by typing `exit` or press <kbd>Ctrl</kbd> + <kbd>D</kbd>.
Unmount all the partitions with `umount -R /mnt`.
Type `reboot` to restart the system.
Remove the installation media and then login into the new system with the root account.

# Packages and Configuration

## Rank Mirrors

```bash
sudo pacman -S --needed --noconfirm python
sed -ie'' 's/^#S/S/g' /etc/pacman.d/mirrorlist
rankmirrors -v /etc/pacman.d/mirrorlist | tee /etc/pacman.d/mirrorlist.new && mv /etc/pacman.d/mirrorlist.new /etc/pacman.d/mirrorlist
sudo pacman -Syy
```

## Desktop Environments

```bash
sudo pacman -S --needed --noconfirm gnome gnome-extra gnome-flashback
sudo pacman -S --needed --noconfirm xorg xorg-server
```

## Enable Networking

```bash
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```

## Enable Printing Service

You must install `cups` before doing this.

```bash
sudo systemctl start org.cups.cupsd.service
sudo systemctl enable org.cups.cupsd.service
```

## Time Setting

To avoid time display error between Arch Linux and Windows, use

```bash
sudo timedatectl set-local-rtc 1 --adjust-system-clock
```

**Note:** If you log in as a normal user, run `timedatectl set-local-rtc 1 --adjust-system-clock` (without `sudo`).

## Archive Formats

```bash
yay -S --needed --noconfirm rsync unace unrar unzip zip lrzip p7zip sharutils uudeview mpack arj cabextract file-roller
```

## Packer/Yaourt/Pamac

In Arch Linux, users can add and install their favorite packages from [AUR](https://aur.archlinux.org/), aka **A**rch **U**ser **R**epository via the [pacman package manager](https://www.archlinux.org/pacman/). 
Since AUR contains about 44,000 packages, for most of them, one need to manually download, check, and install. 
This is where [packer](https://aur.archlinux.org/packages/packer/) or [yaourt](https://aur.archlinux.org/packages/yaourt/) come in handy. 
Here is how I install `yaourt`. 
(The original guide is [here](https://www.ostechnix.com/install-yaourt-arch-linux/)).

```bash
sudo pacman -S --needed --noconfirm base-devel git wget yajl
git clone https://aur.archlinux.org/package-query.git
cd package-query
makepkg -si
cd ..
git clone https://aur.archlinux.org/yaourt.git
cd yaourt
makepkg -si
cd ..
sudo rm -dR yaourt/ package-query/
```

If you need a GUI, install [pamac-aur](https://aur.archlinux.org/packages/pamac-aur/).

**Update (2018-11-14)**: Both `packer` and `yaourt` are outdated and discontinued. Use [yay](https://aur.archlinux.org/packages/yay/) (**y**et **a**nother **y**ogurt) instead.

## Theme

```bash
yay -S --needed --noconfirm arc-gtk-theme paper-icon-theme papirus-icon-theme
```

## Media Codecs

```bash
yay -S --needed --noconfirm exfat-utils fuse-exfat a52dec faac faad2 flac jasper lame libdca libdv \
gst-libav libmad libmpeg2 libtheora libvorbis libxv wavpack x264 xvidcore gstreamer0.10-plugins \
flashplugin libdvdcss libdvdread libdvdnav dvd+rw-tools dvdauthor dvgrab
```

## Fonts and Keyboards

```bash
yay -S --needed --noconfirm ibus ibus-unikey ibus-anthy 
yay -S --needed --noconfirm ttf-vietnamese-tcvn3 ttf-vietnamese-vni ttf-hannom 
yay -S --needed --noconfirm ttf-google-fonts-git ttf-mac-fonts ttf-monaco
```

## Enable GDM

To enable GDM (**G**NOME **D**isplay **M**anager), use

```bash
sudo systemctl start gdm
sudo systemctl enable gdm
```

##  Oracle Java & Eclipse

```bash
sudo pacman -S --needed --noconfirm jdk-openjdk jre-openjdk # latest java
sudo pacman -S --needed --noconfirm jdk11-openjdk jre11-openjdk jdk8-openjdk jre8-openjdk # version 8 and 11
sudo archlinux-java set java-11-openjdk # set default Java environment, use `sudo archlinux-java status` to see available versions
yay -S --needed --noconfirm eclipse-java
```

As `eclipse-java` and `eclipse-cpp` are in conflict, to use C/C++ Development Tools, I install [CDT 9.5.5 for Eclipse Photon and 2018-09](https://www.eclipse.org/cdt/downloads.php) in `eclipse-java` by choosing `Help > Install New Software...`, add the CDT repository [http://download.eclipse.org/tools/cdt/releases/9.5](http://download.eclipse.org/tools/cdt/releases/9.5), and install the `CDT Main Features` and `CDT Optional Features`.

<!--
## SoftMaker FreeOffice 2018

Download from [http://www.freeoffice.com/en/download](http://www.freeoffice.com/en/download).
You need to *register* to get a product key (free of charge).
Let say you download `softmaker-freeoffice-2018-931-amd64.tgz`, then the installation steps are

```bash
tar -xvzf softmaker-freeoffice-2018-931-amd64.tgz
sudo ./installfreeoffice
```

If you want to uninstall FreeOffice 2018, you can just simply run `/usr/bin/uninstall_smfreeoffice2018`.
For more information, see [this page](https://www.freeoffice.com/en/tips-and-tricks-linux).

**Update (2020-09-30):** A simple `yay -S freeoffice` is enough.
-->

## Missing Firmware

When running `mkinitcpio -p linux-lts`, if you get the warning

```bash
==> WARNING: Possibly missing firmware for module: wd719x
==> WARNING: Possibly missing firmware for module: aic94xx
```

then simply install the `wd719x-firmware` and `aic94xx-firmware` packages using `yay` and run `mkinitcpio -p linux-lts` again.

## Downgrade

Install the [downgrade](https://aur.archlinux.org/packages/downgrade/) package using `yay`. 
This package helps you install some previous version of a current package, which is very useful in case of conflicted dependencies. 
If you want a specific version of a package, say `netpbm-10.73-1-x86_64.pkg.tar.xz` (a dependency for `latex2html`), you can go to [https://archive.archlinux.org/packages/](https://archive.archlinux.org/packages/) to look for the package at [https://archive.archlinux.org/packages/n/netpbm](https://archive.archlinux.org/packages/n/netpbm) and install using

```bash
sudo pacman -U https://archive.archlinux.org/packages/n/netpbm/netpbm-10.73-1-x86_64.pkg.tar.xz
```

**Update (2019-12-31):** Another place to look for old Arch Linux packages is [Internet Archive](https://archive.org/search.php?query=subject%3A%22archlinux+package%22). 
A trick is to go to the page `https://archive.org/download/archlinux_pkg_<package-name>` if you want to find old versions of `<package-name>`, e.g., to find old versions of `netpbm`, go to [https://archive.org/download/archlinux_pkg_netpbm](https://archive.org/download/archlinux_pkg_netpbm).
For more information, see [Arch Linux Archive](https://wiki.archlinux.org/index.php/Arch_Linux_Archive).

## (Vanilla) TeXLive 2017

There is no trouble installing Vanilla TeXLive, but I want to add some note: Install [texlive-dummy](https://aur.archlinux.org/packages/texlive-dummy/) via `yaourt` in order to tell `pacman` that you've already installed TeXLive. 
You can also install TeXLive with 

```bash
sudo pacman -S --needed --noconfirm texlive-most texlive-lang texmaker biber
```
<!--
## LaTeX2HTML

If you use `perl >= 5.26.0`, you need a workaround: add `PERL5LIB=$PERL5LIB:.; export PERL5LIB` to `/etc/bash.bashrc`. 
The reason is that LaTeX2HTML uses module `cfgcache.pm` from the installation directory, but since version `5.26.0`, `perl` no longer includes the current directory in `@INC` path (see [this page](http://search.cpan.org/dist/perl-5.26.0/pod/perldelta.pod\#Removal_of_the_current_directory_(\%22.\%22)_from_@INC)).
-->

## pdf2htmlEX

To compile and install pdf2htmlEX (in Arch Linux 64-bit version), I use `poppler` and `poppler-glib` version `0.59.0-1`, `fontforge` version `20141126-3`, together with the [pdf2htmlex-git](https://aur.archlinux.org/packages/pdf2htmlex-git/) package. 

First, install some necessary packages

```bash
sudo pacman -S --needed --noconfirm poppler-data
wget https://archive.org/download/archlinux_pkg_poppler/poppler-0.59.0-1-x86_64.pkg.tar.xz && sudo pacman -U --noconfirm poppler-0.59.0-1-x86_64.pkg.tar.xz 
wget https://archive.org/download/archlinux_pkg_poppler-glib/poppler-glib-0.59.0-1-x86_64.pkg.tar.xz && sudo pacman -U --noconfirm poppler-glib-0.59.0-1-x86_64.pkg.tar.xz
wget https://archive.org/download/archlinux_pkg_automake/automake-1.15-1-any.pkg.tar.xz && sudo pacman -U automake-1.15-1-any.pkg.tar.xz
sudo pacman -S --needed --noconfirm libxi pango giflib libtool desktop-file-utils gtk-update-icon-cache libunicodenames gc python shared-mime-info openjpeg2 qt5-base poppler popper-glib poppler-qt5
```

Next, install `fontforge 20141126-3` along with its dependencies

```bash
yay -S readline6 # for `libreadline.so.6`
wget https://archive.org/download/archlinux_pkg_libsodium/libsodium-0.7.1-1-x86_64.pkg.tar.xz && sudo pacman -U --noconfirm libsodium-0.7.1-1-x86_64.pkg.tar.xz
wget https://archive.org/download/archlinux_pkg_zeromq/zeromq-4.0.6-1-x86_64.pkg.tar.xz && sudo pacman -U zeromq-4.0.6-1-x86_64.pkg.tar.xz
wget https://archive.org/download/archlinux_pkg_libxkbui/libxkbui-1.0.2-6-x86_64.pkg.tar.xz && sudo pacman -U libxkbui-1.0.2-6-x86_64.pkg.tar.xz
wget https://archive.org/download/archlinux_pkg_libspiro/libspiro-1%3A0.5.20150702-2-x86_64.pkg.tar.xz && sudo pacman -U libspiro-1:0.5.20150702-2-x86_64.pkg.tar.xz
wget https://archive.org/download/archlinux_pkg_fontforge/fontforge-20141126-3-x86_64.pkg.tar.xz && sudo pacman -U fontforge-20141126-3-x86_64.pkg.tar.xz
```

Now, install `pdf2htmlex-git` with the command `yay -S pdf2htmlex-git`. To see how it was actually installed, I put here the content of the corresponding `PKGBUID`.

```bash
# Maintainer: Miguel Revilla <yo at miguelrevilla dot com>
# Contributor: Arthur Țițeică arthur.titeica/gmail/com

pkgname=pdf2htmlex-git
pkgver=1742.f12fc15
pkgrel=3
epoch=1
pkgdesc="Convert PDF to HTML without losing format. Text is preserved as much as possible."
arch=('i686' 'x86_64')
url="https://github.com/coolwanglu/pdf2htmlEX"
license=('GPL3' 'custom')
depends=('poppler' 'fontforge')
makedepends=('cmake' 'git')
optdepends=('ttfautohint: Provides automated hinting process for web fonts')
provides=('pdf2htmlex')
conflicts=('pdf2htmlex')
replaces=('pdf2htmlex')
source=('git://github.com/coolwanglu/pdf2htmlEX.git'
        '735.patch'
        'override.patch')
md5sums=('SKIP'
         '61100dcfa593c90ef9ee2ac3f6206a77'
         'ae6ab1c7b5d5f2a4d4edf67ff4746143')

_gitname=pdf2htmlEX
_pkgname=pdf2htmlEX

pkgver() {
  cd "${_gitname}"
  # git describe --always | sed 's|-|.|g'
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

prepare() {
  cd "${_gitname}"
  patch -p1 < "${srcdir}/735.patch"
  patch < "${srcdir}/override.patch"

  cd 3rdparty/poppler/git
  sed -i 's|globalParams->getStrokeAdjust()|gTrue|' CairoOutputDev.cc
}

build() {
  cd "${_gitname}"

  cmake . \
  -DCMAKE_INSTALL_PREFIX=/usr
  make CXXFLAGS=-Doverride=
}

package() {
  cd "${_gitname}"
  make DESTDIR="${pkgdir}/" install
  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

}

# vim:set ts=2 sw=2 et:
```

Finally, upgrading `poppler`, `poppler-glib`, and reinstalling their old versions to `/usr/local`:

* `sudo pacman -S --noconfirm --needed poppler poppler-glib libsodium`.

* Install `poppler 0.59.0` from source

  ```bash
  wget https://poppler.freedesktop.org/poppler-0.59.0.tar.xz
  tar -xvf poppler-0.59.0.tar.xz
  cd poppler-0.59.0/
  ./configure --prefix=/usr/local --enable-xpdf-headers
  make
  sudo make install
  sudo ln -s /usr/local/lib/libpoppler.so.70 /usr/lib/libpoppler.so.70 # so that pdf2htmlEX can find it later
  ```

* Install `libsodium 0.7.1` from source

  ```bash
  curl -O https://download.libsodium.org/libsodium/releases/old/unsupported/libsodium-0.7.1.tar.gz
  tar xvf libsodium-0.7.1.tar.gz
  cd libsodium-0.7.1/
  ./configure --prefix=/usr/local
  make
  sudo make install
  sudo ln -sf /usr/local/lib/libsodium.so.13 /usr/lib/libsodium.so.13
  ```

<!--
## Foxit Reader

```bash
git clone https://aur.archlinux.org/gstreamer0.10.git
cd gstreamer0.10
makepkg -si
cd ..
git clone https://aur.archlinux.org/gstreamer0.10-base.git
cd gstreamer0.10-base
makepkg -si
cd ..
git clone https://aur.archlinux.org/foxitreader.git
cd foxitreader
makepkg -si
cd ..
rm -r gstreamer0.10 gstreamer0.10-base foxitreader
```

**Update (2020-02-14):** Some errors occurred when I compiled `gstreamer0.10-base` in my recent updated Arch Linux, and I cannot figure out the reason. This installation may also not work for you.

**Update (2020-09-30):** A simple `yay -S foxitreader` is enough.

## VMWare Horizon Client

```bash
yay -S --needed --noconfirm openssl098 gstreamer0.10-base vmware-horizon-client
```

**Update (2020-02-14):** `gstreamer0.10-base` may not be compiled, as mentioned above.

## IPE extensible drawing editor

I often use [IPE](http://ipe.otfried.org/) for drawing graphs in my papers. To install IPE in Arch Linux, you can just simply use `yay -S --needed --noconfirm ipe` (assuming you've already installed `yay`). Several useful tools (`pdftoipe`, `figtoipe`, `ipe5toxml`, `svgtoipe`) for IPE can be found in the `ipe-tools-git` package. I also use the ipelet [ipe2tikz](https://github.com/QBobWatson/ipe2tikz) to export IPE pictures to [TikZ](https://sourceforge.net/projects/pgf/) code. One thing you may want to remember when using the generated TikZ pictures is [how to scale your TikZ picture to fit the paper size](https://tex.stackexchange.com/a/11536). Several other useful ipelets are also [available](https://github.com/otfried/ipe-wiki/wiki/Ipelets). Finally, for convenience, I also create the file `/usr/share/applications/ipe.desktop` and make it executable.

```bash
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=IPE
Comment=IPE extensible drawing editor
Exec=/usr/bin/ipe
Icon=/usr/share/ipe/7.2.7/icons/ipe.png
Terminal=false
Categories=Graphics
```

**Update (2020-02-14):** I failed to build and install `ipe-tools-git` in my recent updated Arch Linux.
-->

## ClamAV

```bash
sudo pacman -S --needed --noconfirm clamav clamtk # installation
sudo systemctl enable clamav-daemon # enable clamav-daemon
sudo systemctl start clamav-daemon # start clamav-daemon
sudo freshclam # update virus database
```

## Docker

```bash
sudo pacman -S --needed --noconfirm docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER # if the group `docker` does not exist then create it using `sudo groupadd docker`
```

## `pass` password manager

```bash
yay -S --noconfirm tree pass pass-import dmenu
```

If you get the error

```bash
pass-import-2.3.tar.gz ... FAILED (unknown public key C5469996F0DF68EC)
```

then run 

```bash
gpg --keyserver pool.sks-keyservers.net --recv-keys C5469996F0DF68EC
```

One can also install the latest `pass-import` from its GitHub repository as follows

```bash
git clone https://github.com/roddhjav/pass-import/
cd pass-import 
sudo make install
```

See [this page](https://github.com/docker/docker-credential-helpers) for a guide on how to use `pass` with `docker`.

## Some other packages

A non-exhaustive list of some packages I installed (using `yay`) are: 

```bash
guake firefox thunderbird google-chrome torbrowser-launcher gedit-plugins mailnag
tlp lsb-release smartmontools ethtool
gparted gksu testdisk partimage xfsprogs reiserfsprogs jfsutils ntfs-3g dosfstools mtools grub-customizer hwinfo dislocker-git
openssh subversion git git-lfs github-cli mercurial gufw filezilla openvpn 
mlocate cups cups-pdf system-config-printer 
gnupg1 veracrypt secure-delete tree authenticator-git
goldendict pdfarranger calibre djview shutter shotwell foxitreader freeoffice ms-office-online zotero
vlc mplayer alsa-utils pulseaudio ytmdesktop-git vidcutter 4kvideodownloader
dropbox-cli nautilus-dropbox megasync grive-git onedrive-abraunegg-git
skypeforlinux-stable-bin telegram-desktop irssi caprine zoom
pidgin finch libpurple pidgin-gnome-shell-extension-git pidgin-gnome-keyring pidgin-indicator purple-facebook-git slack-libpurple-git
visual-studio-code-bin atom asymptote
sagemath sagemath-doc sagemath-jupyter sagetex octave python-networkx python-matplotlib python-graphillion
vnware-horizon-client
woeusb-git multisystem multibootusb
julia eclipse-java
ipe tikzit
gnome-shell-extension-appindicator libappindicator-gtk3 gnome-shell-extension-topicons-plus mailnag-gnome-shell
latex2html perl-latexml
```

For a recommendation, see [this page](https://wiki.archlinux.org/index.php/general_recommendations) or [this page](https://novelist.xyz/tech/things-to-do-after-installing-arch-linux/). 
See [this page](https://wiki.archlinux.org/index.php/List_of_applications) for a list of available applications.

## List of installed packages

Keeping a list of installed packages is useful when you want to speed up installation on a new system or backup a working system. The command

```bash
pacman -Qqe > pkglist.txt
```

generates a list of installed packages (including packages from [AUR](https://wiki.archlinux.org/index.php/AUR)). 
The command

```bash
yay -S --needed - < pkglist.txt
```

One can also use the [reflector](https://www.archlinux.org/packages/community/any/reflector/) package for retrieving and filtering the latest Pacman mirror list.
See [pacman/Tips and tricks](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks) for more information.

# Extra configurations and resolving issues

## Error ``Pacman is currently in use, please wait''

```bash
sudo rm /var/lib/pacman/db.lck
```

## Accessing `JAIST` or `eduroam` wifi in JAIST

[JAIST](https://www.jaist.ac.jp/) provides [two wireless network services](https://www.jaist.ac.jp/iscenter/en/network/wireless/) with SSIDs `JAIST` and `eduroam`. 
The instruction is for Windows, MacOS X, and Android. 
I figure that it can also be used for Arch Linux (and maybe some other Linux distributions). 
Basically, the wifi security information for accessing these wifi SSIDs (I use [NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager) for managing network connection) is as follows.

* Security type : WPA & WPA2 Enterprise
* Authentication : TLS
* Identity : [Your JAIST account]@jaist.ac.jp (for students, sXXXXXXX@jaist.ac.jp)
* Domain : [Leave it empty]
* CA certificate : Use the file `/etc/ssl/ca-certificates.crt` (make sure that the package [ca-certificates-utils](https://www.archlinux.org/packages/core/any/ca-certificates-utils/) is installed)
* User certificate : Use the [digital certificate](https://www.jaist.ac.jp/iscenter/en/digital-certificate/) provided from JAIST
* User private key : Use the [digital certificate](https://www.jaist.ac.jp/iscenter/en/digital-certificate/) provided from JAIST
* User key password : [Your password for reading the provided digital certificate]

**Note:** Put your [digital certificate](https://www.jaist.ac.jp/iscenter/en/digital-certificate/) in some place where the path to it contains no file/folder whose name containing blank space.

## Using JAIST's SSL-VPN service

[JAIST](https://www.jaist.ac.jp/) also provides [an SSL-VPN gateway system](https://www.jaist.ac.jp/iscenter/en/remote-access/ssl-vpn/).
In Arch Linux, I download {% include files.html name="linuxsslvpn.gz" text="F5 Linux CLI (command line interface) Edge Client Installer" %} (file `linuxsslvpn.gz`) and install as follows.

```bash
tar -xvf linuxsslvpn.tgz 
sudo ./Install.sh # Answer `yes` for both questions
```

To use JAIST SSL-VPN, from the Terminal, you can use the command

```bash
f5fpc --start --host vpn.jaist.ac.jp --cert /path/to/your/jaist/digital/certificate
```

You will have to input your password for reading your digital certificate (provided from JAIST), your username (for student, sXXXXXXX), and the password of your JAIST's account.
After you successfully start the connection, you can use `f5fpc --info` to check the connection status.
At the time of writing this post, JAIST provides two VPN networks `/Common/jaist-vpn1-na` and `/Common/jaist-vpn2-na` (as shown when using `f5fpc --info`).
The `vpn1` only passes accesses to JAIST through VPN, while `vpn2` passes all accesses through VPN.

{% include image.html name="fp_jaistvpn1and2.png" caption="The difference between JAIST <code>vpn1</code> and <code>vpn2</code> (&copy; JAIST RCACI)" width="40%" %}

To use, say `vpn2`, you can use the command

```bash
f5fpc --start --host vpn.jaist.ac.jp --cert /path/to/your/jaist/digital/certificate --fname "/Common/jaist-vpn2-na"
```

To stop using JAIST SSL-VPN, use the command

```bash
f5fpc --stop
```

**Update (2020-09-30):** A simpler way to install `f5fpc` in Arch Linux is to run `yay -S f5fpc`.

## Using Kyutech VPN

To use [Kyutech VPN](https://onlineguide.isc.kyutech.ac.jp/guide2017/index.php/home/2017-02-24-00-51-59/vpn.html) <span style="color:red;">[Username and Password Required]</span>, I installed `networkmanager-l2tp`, `xl2tpd`, `strongswan` and `networkmanager-strongswan` as follows (assuming that `yay` was installed).

```bash
yay -S networkmanager-l2tp xl2tpd strongswan networkmanager-strongswan
```
<!--
Then, enable and start `strongswan` and `xl2tpd`

```bash
sudo systemctl enable strongswan
sudo systemctl start strongswan
sudo systemctl enable xl2tpd
sudo systemctl start xl2tpd
```
-->

The information for setting up VPN are as follows

* Name: Any name you want, for instance, `KIT VPN`.
* Gateway: Enter the server name as instructed by Kyutech [here](https://onlineguide.isc.kyutech.ac.jp/guide2017/index.php/home/2017-02-24-00-51-59/vpn.html).
* Username: Your username provided by Kyutech.
* Password: The password of your Kyutech account.
* IPsec Settings: Choose `Enable IPsec Tunnel to L2TP host` and enter the pre-shared key as instructed by Kyutech [here](https://onlineguide.isc.kyutech.ac.jp/guide2017/index.php/home/2017-02-24-00-51-59/vpn.html). In the `Advanced` section, click `Legacy Proposals`. 

**Update (2020-02-14):** In my recent system, clicking `Legacy Proposals` is not required.

## Using KyotoU VPN

You will need to get a [client certificate](https://www.iimc.kyoto-u.ac.jp/en/services/cert/client_cert/) <span style="color:red;">[KyotoU Credentials Required]</span>. Use `NetworkManager` to import the following [OpenVPN configuration file](http://www.iimc.kyoto-u.ac.jp/services/kuins/vpn/kuins.ovpn) and adjust the path to the above certificate.

## Anjuta opens my folders

To fix this, use the command

```bash
xdg-mime default org.gnome.Nautilus.desktop inode/directory
```

## Visual Studio Code (VS Code) opens my folders

After installing VS Code (`visual-studio-code-bin`), anything opened using the "Places" extension in GNOME opens VS Code instead of the default folder/path (as described [here](https://github.com/Microsoft/vscode/issues/41037)). To resolve this issue, I simply add the lines

```bash
[Default Applications]
inode/directory=org.gnome.Nautilus.desktop
```

to `~/.config/mimeapps.list` (or just the second line if `[Default Applications]` already exists).

## Auto reconnect Bluetooth devices at boot

The original instruction is available [here](https://bbs.archlinux.org/viewtopic.php?id=223949).

* Enable `bluetooth` service: `sudo systemctl enable bluetooth.service`.
* Set bluetooth adapter to automatically power on: edit `/etc/bluetooth/main.conf` and set `AutoEnable=true`.
* Set paired devices as trusted: Type `bluetoothctl`, it will open a new console. In that console, type `trust XX:XX:XX:XX:XX:XX` for each paired device (replace `XX...` with mac address).

## Pairing bluetooth devices on dual boot of Windows and Linux

Recently, I've bought a [HP X4000b Bluetooth Mouse](https://support.hp.com/vn-en/product/hp-x4000b-bluetooth-mouse/5286917) and having trouble when I have to re-pair the device again and again every time I switch between Arch Linux and Windows 10. Luckily, I found [this instruction](https://unix.stackexchange.com/a/255510). I describe the steps here.

* Pair all Bluetooth devices with Arch Linux.
* Pair all Bluetooth devices with Windows 10.
* Copy the Windows pairing keys
  * Install `chntpw` using `sudo pacman -S --needed --noconfirm chntpw`.
  * Mount Windows system drive.
  * `cd /[windowsSystemDrive]/Windows/System32/config`.
  * `chntpw -e SYSTEM` opens up a console. Run the following commands in that console.
	```bash
	cd ControlSet001\Services\BTHPORT\Parameters\Keys
	ls 
	# shows your bluetooth port's mac address, 
	# for example, the output is as follows
	# Node has 1 subkeys and 0 values
	#   key name
	#   <aa1122334455>
	cd aa1122334455  # CD into the folder
	ls # lists of existing devices' MAC addresses
	# for example, the output is as follows
	# Node has 0 subkeys and 1 values
	# size     type            value name             [value if type DWORD]
	#   16  REG_BINARY        <001f20eb4c9a>
	hex 001f20eb4c9a
	# the output is of the form
	# :00000 XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX ...ignore..chars..
	# the XXs are the pairing key
	```
  * Make a note of which Bluetooth device MAC address matches which paring key. In Arch Linux, we won't need the spaces in-between. Ignore the `:00000`.
  * Add the windows key to Linux config entries.
    * Switch to root `sudo -s`.
    * `cd` to your bluetooth config location `/var/lib/bluetooth/[bth port  mac addresses)]`.
    * Here you'll find folders for each device you've paired with. The folder names being the Bluetooth devices mac address and contain a single file `info`. In these files, you'll see the link key you need to replace with your windows ones like so.
	  ```bash
	  [LinkKey]
	  Key=B99999999FFFFFFFFF999999999FFFFF
	  ```
  * Once updated, restart the bluetooth service `sudo systemctl restart bluetooth`.
  
**Note:** If you Pair all Bluetooth devices with Windows 10 first, and then with Arch Linux, then the key for all systems should be the key of the last system the devices were paired, which is Arch Linux in this case.

## GnuPG

### Missing PGP keys when installing `gnupg1`

If you get the error

```bash
==> PGP keys need importing:
 -> D8692123C4065DEA5E0F3AB5249B39D24F25E3B6, required by: gnupg1
 -> 46CC730865BB5C78EBABADCF04376F3EE0856959, required by: gnupg1
 -> 031EC2536E580D8EA286A9F22071B08A33BD3F06, required by: gnupg1
 -> D238EA65D64C67ED4C3073F28A861B1C7EFD60D9, required by: gnupg1
```

when installing `gnupg1` then you can import the missing keys with the command

```bash
gpg --keyserver pgp.mit.edu --recv-keys D8692123C4065DEA5E0F3AB5249B39D24F25E3B6 \ 
	46CC730865BB5C78EBABADCF04376F3EE0856959 \
	031EC2536E580D8EA286A9F22071B08A33BD3F06 \
	D238EA65D64C67ED4C3073F28A861B1C7EFD60D9 
```

### Remove passphrase of a secret key

Let say you want to remove the passphrase of a secret key named `PGP-key.asc`.

```bash
gpg1 --import PGP-key.asc
gpg1 --edit-key <imported PGP key fingerprint>
```

Then, type `passwd` in the `gpg>` command prompt, enter the old passhrase of the imported PGP key, and press <kbd>Enter</kbd> for the new passhrase. Answer `y` when you were asked `You don't want a passphrase - this is probably a *bad* idea! Do you really want to do this? (y/N)`. Finally, type `save` to save the result and exit the command prompt.

## Backup `$HOME` folder with `rsync`

```bash
cd /path/to/backup/directory
rsync -arvz -H --progress --numeric-ids $HOME/ .
```

## Full backup with `rsync`

See also the [ArchWiki](https://wiki.archlinux.org/index.php/Rsync#Full_system_backup).

```bash
rsync -aAXHv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /path/to/backup
```

## Error "Failed to start User Manager for UID 120. See `systemctl status user@120.service` for details"

To resolve this error, simply press <kbd>Alt</kbd> + <kbd>F2</kbd>, login to the TTY shell as `root`, and run `systemctl restart gdm`. See [this page](https://bbs.archlinux.org/viewtopic.php?id=225817) for more information.

## [Laptop] Cannot enable "Tap to click" function of a touchpad

One way is to try to remove `xf86-input-synaptics` and install `xf86-input-libinput`. Also, in GNOME, enable "Tap to click" using `gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true` and `gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll false`. To ensure the touchpad events are being sent to the GNOME desktop, use `gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled`.

## Change the directory where `cups-pdf` outputs printed files

Edit `/etc/cups/cups-pdf.conf` by adding `Out ${HOME}/Documents/cups-pdf`. The output will be in your `$HOME/Documents/cups-pdf` directory.

## Some tips when using `sudo`

See [this ArchWiki page](https://wiki.archlinux.org/index.php/Sudo) for more details.

* Editting files as `root` while still using `gedit` as your user.

  ```bash
  SUDO_EDITOR=gedit sudo -e file.txt
  ```
  `sudo -e` will check that you’re allowed to do this, make a copy of the file that you can edit without changing ids manually, start your editor, and then, when the editor exits, copy the file back if it has been changed.

* Reduce the number of times you have to type a password by adding the following line to `/etc/sudoers`:

  ```bash
  Defaults timestamp_timeout=10 # in minutes
  ```
  
## Backup/restore/reset GNOME settings with `dconf`

* Install [dconf](https://www.archlinux.org/packages/extra/x86_64/dconf/) with `sudo pacman -S dconf`.
* Backup all settings with `dconf dump / > gnome-settings`.
* Restore the settings with `dconf load / < gnome-settings`.
* Reset to default setting with `dconf reset -f /`.

## Backup and restore wired/wireless/vpn/hotspot connections with NetworkManager

By default, [NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager) stores all connection files at `/etc/NetworkManager/system-connections/`, and I just simply backup all of them with

```bash
sudo tar czvf /NetworkConnections.tar.gz /etc/NetworkManager/system-connections
```

To restore the connection files, simply run `sudo tar xvf /NetworkConnections.tar.gz -C /`, and restart NetworkManager with `systemctl restart NetworkManager`. Note that if you want to restore these files in *a different computer*, you also need to change the corresponding MAC addresses of the devices using the commands `cd /etc/NetworkManager/system-connections && sed -i -e 's/<old mac>/<new mac>/ *`, as described [here](https://unix.stackexchange.com/a/442633). To list all network connnections, use `nmcli connection show`.

## Rollback/Restore a `pacman -Su` sytem update/upgrade with `aura`

Install the `aura` or `aura-bin` or `aura-git` package using `yay`. 
(I would suggest `aura-bin`.)
To save the list of installed packages and versions, run `sudo aura -B`.
To select a previous restore point from date-stamped list, run `sudo aura -Br`.
To remove all but the last 3 restore points, run `sudo aura -Bc 3`.
For more details, see [The Aura User Guide](https://fosskers.github.io/aura/).

## Apache, MariaDB, PHP (LAMP stack), and so on

### Apache

Install `apache`

```bash
pacman -S apache
```

and edit `/etc/httpd/conf/httpd.conf` by commenting out (adding `#` at the beginning of) the line

```bash
LoadModule unique_id_module modules/mod_unique_id.so
```

Then,

```bash
sudo systemctl enable httpd
sudo systemctl start httpd
```

### Use TLS with `localhost` in Apache server

Note that this aims to be used only in `localhost`. 
If you plan to deploy TLS in your server, you may need to be [more careful](https://weakdh.org/sysadmin.html) in order to prevent vulnerabilities.
The first step is to generate self-signed certificates.
[This page](https://stackoverflow.com/a/60516812) contains a very nice step-by-step instruction on how to do it.
I put them all together in a bash script {% include files.html name="gen_certs.sh" text="gen_certs.sh" %} with a slight modification.
You can download script and simply run `bash gen_certs.sh localhost`.

```bash
#!/bin/bash

if [ "$#" != 1 ]; then
	echo "Usage: ./gen_certs.sh NAME"
	exit 1
fi 

######################
# Become a Certificate Authority
######################

if [ ! -f "myCA.key" ]; then  
	# Generate private key
	openssl genrsa -out myCA.key 4096

	# Create configuration file for generating root certificates
	>config_ssl_ca.cnf cat <<-EOF
	[ req ]
	default_bits = 4096

	prompt = no
	distinguished_name=req_distinguished_name
	req_extensions = v3_req

	[ req_distinguished_name ]
	countryName=UA
	stateOrProvinceName=root region
	localityName=root city
	organizationName=root organisation
	organizationalUnitName=roote department
	commonName=root
	emailAddress=root_email@root.localhost

	[ alternate_names ]
	DNS.1        = localhost
	DNS.2        = www.localhost
	DNS.3        = mail.localhost
	DNS.4        = ftp.localhost

	[ v3_req ]
	keyUsage=digitalSignature
	basicConstraints=CA:true
	subjectKeyIdentifier = hash
	subjectAltName = @alternate_names
	EOF

	# Generate root certificate
	openssl req -new -x509 -nodes -key myCA.key -sha256 -days 36500 -out myCA.pem -config config_ssl_ca.cnf
fi

######################
# Create CA-signed certs
######################

NAME="$1"
# Generate a private key
openssl genrsa -out $NAME.key 4096

# Create a configuration file for generating a certificate-signing request
>$NAME-config_ssl.cnf cat <<-EOF
[ req ]
default_bits = 4096

prompt = no
distinguished_name=req_distinguished_name
req_extensions = v3_req

[ req_distinguished_name ]
countryName=UA
stateOrProvinceName=root region
localityName=root city
organizationName=root organisation
organizationalUnitName=roote department
commonName=root
emailAddress=root_email@root.localhost

[ alternate_names ]
DNS.1        = $NAME
DNS.2        = www.$NAME
DNS.3        = mail.$NAME
DNS.4        = ftp.$NAME

[ v3_req ]
keyUsage=digitalSignature
basicConstraints=CA:false
subjectKeyIdentifier = hash
subjectAltName = @alternate_names
EOF

# Create a certificate-signing request
openssl req -new -sha256 -key $NAME.key -config $NAME-config_ssl.cnf -out $NAME.csr

# Create a config file for the extensions
>$NAME.ext cat <<-EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = $NAME # Be sure to include the domain name here
DNS.2 = www.$NAME
DNS.3 = mail.$NAME
DNS.4 = ftp.$NAME
EOF

# Create the signed certificate
openssl x509 -req -in $NAME.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial \
-out $NAME.crt -days 825 -sha256 -extfile $NAME.ext

# Cleaning up
rm -rf $NAME.ext 
```

Next, move `localhost.key` and `localhost.crt` to `/etc/httpd/conf`, and in `/etc/httpd/conf/httpd.conf`, uncomment the following three lines:

```bash
LoadModule ssl_module modules/mod_ssl.so
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
Include conf/extra/httpd-ssl.conf
```

Finally, edit `/etc/httpd/conf/extra/httpd-ssl.conf`

```bash
SSLCertificateFile "/etc/httpd/conf/localhost.crt"
SSLCertificateKeyFile "/etc/httpd/conf/localhost.key"
```

and `sudo systemctl restart httpd`.
Remeber to import the CA certificate `myCA.pem` to your browser (Google Chrome, Firefox, etc.) in order to avoid the error `NET::ERR_CERT_AUTHORITY_INVALID`.

### Both SSL and non-SSL protocols on the same `localhost` server

This can be done by creating new `VirtualHost`. 
I simply add the following to `/etc/httpd/conf/httpd.conf`

```bash
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot "/srv/http"
    ServerName localhost
    ServerAlias localhost
    ErrorLog "/var/log/httpd/localhost-error_log"
    CustomLog "/var/log/httpd/localhost-access_log" common

    <Directory "/srv/http">
        Require all granted
    </Directory>
</VirtualHost>

<VirtualHost *:443>
    ServerAdmin webmaster@localhost
    DocumentRoot "/srv/http"
    ServerName localhost:443
    ServerAlias localhost:443
    SSLEngine on
    SSLCertificateFile "/etc/httpd/conf/localhost.crt"
    SSLCertificateKeyFile "/etc/httpd/conf/localhost.key"
    ErrorLog "/var/log/httpd/localhost-error_log"
    CustomLog "/var/log/httpd/localhost-access_log" common

    <Directory "/srv/http">
        Require all granted
    </Directory>
</VirtualHost>
```

### MariaDB

To install, run

```bash
sudo pacman -S mysql
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
sudo systemctl enable mysqld
sudo systemctl start mysqld
```

Run the following command to setup MariaDB `root` user password

```bash
sudo mysql_secure_installation
```

To create a new user, start MariaDB as `root` (with the created password in the previous step)

```bash
mysql -u root -p
```

Then, run

```bash
CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';
```

To grant all privileges to `<username>`:

```bash
GRANT ALL PRIVILEGES ON *.* TO '<username>'@'localhost' IDENTIFIED BY '<password>';
```

then refresh the privileges with

```bash
FLUSH PRIVILEGES;
```

To quit, type `\q`.

You can also combine these commands (see [this page](https://stackoverflow.com/a/13144274) for more details):

```bash
mysql -u root -p<mysql-root-password> -Bse "CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';GRANT ALL PRIVILEGES ON *.* TO '<username>'@'localhost' IDENTIFIED BY '<password>';FLUSH PRIVILEGES;"
```

### PHP 7.4 (2020-10)

<!--
To install, run

```bash
sudo pacman -S php php-apache # or maybe `yay -S php74 php74-apache` if newer versions of `php` are available
```

and then edit `/etc/httpd/conf/httpd.conf` by commenting out

```bash
LoadModule mpm_event_module modules/mod_mpm_event.so
```

and add the following lines at the bottom

```bash
LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
LoadModule php7_module modules/libphp7.so
AddHandler php7-script php
Include conf/extra/php7_module.conf
```

Finally, run `sudo systemctl restart httpd`.
-->

<!--
To install, run

```bash
sudo pacman -S php mod_fcgid php-cgi
```

Then, reate the needed directory and symlink it for the PHP wrapper:

```bash
sudo mkdir -p /srv/http/fcgid-bin
sudo ln -s /usr/bin/php-cgi /srv/http/fcgid-bin/php-fcgid-wrapper
```

Next, create `/etc/httpd/conf/extra/php-fcgid.conf` with the following content:

```bash
# Required modules: fcgid_module

<IfModule fcgid_module>
    AddHandler php-fcgid .php
    AddType application/x-httpd-php .php
    Action php-fcgid /fcgid-bin/php-fcgid-wrapper
    ScriptAlias /fcgid-bin/ /srv/http/fcgid-bin/
    SocketPath /var/run/httpd/fcgidsock
    SharememPath /var/run/httpd/fcgid_shm
        # If you don't allow bigger requests many applications may fail (such as WordPress login)
        FcgidMaxRequestLen 536870912
        # Path to php.ini – defaults to /etc/phpX/cgi
        DefaultInitEnv PHPRC=/etc/php/
        # Number of PHP childs that will be launched. Leave undefined to let PHP decide.
        #DefaultInitEnv PHP_FCGI_CHILDREN 3
        # Maximum requests before a process is stopped and a new one is launched
        #DefaultInitEnv PHP_FCGI_MAX_REQUESTS 5000
    <Location /fcgid-bin/>
        SetHandler fcgid-script
        Options +ExecCGI
    </Location>
</IfModule>
```

Edit `/etc/httpd/conf/httpd.conf`:

* Uncomment `LoadModule actions_module modules/mod_actions.so`.
* Add `LoadModule fcgid_module modules/mod_fcgid.so` after `<IfModule unixd_module>`.
* Uncomment `Include conf/extra/httpd-mpm.conf`
* Add `Include conf/extra/php-fcgid.conf`.
-->

To [install](https://wiki.archlinux.org/index.php/Apache_HTTP_Server#Using_php-fpm_and_mod_proxy_fcgi), run

```bash
sudo pacman -S php php-fpm
```

Next, create `/etc/httpd/conf/extra/php-fpm.conf` with the following content:

```bash
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so

DirectoryIndex index.php index.html
<FilesMatch \.php$>
    SetHandler "proxy:unix:/run/php-fpm/php-fpm.sock|fcgi://localhost/"
</FilesMatch>
```
and then add `Include conf/extra/php-fpm.conf` to the end of `/etc/httpd/conf/httpd.conf`, and finally 

```bash
sudo systemctl start php-fpm
sudo systemctl enable php-fpm
sudo systemctl restart httpd
```
 
For other methods, see [this ArchWiki page](https://wiki.archlinux.org/index.php/Apache_HTTP_Server#PHP).

### phpMyAdmin

To install, run

```bash
yay -S phpmyadmin php74-mcrypt
```

and edit `/etc/php/php.ini` by uncommenting (removing the semicolon `;` at the beginning of) the lines (if a line does not exist, add it)

```bash
extension=bz2
extension=mcrypt
extension=mysqli
```

Next, create `/etc/httpd/conf/extra/phpmyadmin.conf` with the contents

```bash
Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
 <Directory "/usr/share/webapps/phpMyAdmin">
  DirectoryIndex index.php
  AllowOverride All
  Options FollowSymlinks
  Require all granted
 </Directory>
```

and finally add `Include conf/extra/phpmyadmin.conf` to `/etc/httpd/conf/httpd.conf`. Go to [http://localhost/phpmyadmin/](http://localhost/phpmyadmin/) to test if your settings work correctly.

### WebDAV

I wanted to setup a simple WebDAV configuration with my pre-installed [Apache HTTP Server](https://wiki.archlinux.org/index.php/Apache_HTTP_Server), following [this instruction](https://wiki.archlinux.org/index.php/WebDAV). 

As in the instruction, with `root` permission, run 

```bash
mkdir -p /home/httpd/DAV
chown -R http:http /home/httpd/DAV
mkdir -p /home/httpd/html/dav
chown -R http:http /home/httpd/html/dav
```

Now, to setup authentication, run `sudo htpasswd -c /etc/httpd/conf/passwd username`.

Then, I created `/etc/httpd/conf/httpd-dav.conf` with the following contents.

```bash
LoadModule dav_module modules/mod_dav.so
LoadModule dav_fs_module modules/mod_dav_fs.so
LoadModule dav_lock_module modules/mod_dav_lock.so

DAVLockDB /home/httpd/DAV/DAVLock

Alias /dav "/home/httpd/html/dav"

<Directory "/home/httpd/html/dav">
  DAV On
  AllowOverride None
  Options Indexes FollowSymLinks
  AuthType Basic
  AuthName "WebDAV"
  AuthBasicProvider file
  AuthUserFile /etc/httpd/conf/passwd
  Require valid-user
</Directory>
```

then added `Include conf/httpd-dav.conf` to `/etc/httpd/conf/httpd.conf` and finally `sudo systemctl restart httpd`. To test if these settings work, go to [http://localhost/dav](http://localhost/dav).

### A simple email system at `localhost` with Postfix, Dovecot, and Roundcube

We will install 

* [Postfix](https://wiki.archlinux.org/index.php/Postfix): A [mail transfer agent](https://en.wikipedia.org/wiki/Message_transfer_agent) (MTA) that receives and sends emails via [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol). Those emails are then stored using a [mail delivery agent](https://en.wikipedia.org/wiki/Mail_delivery_agent) (MDA).
  
* [PostfixAdmin](https://wiki.archlinux.org/index.php/PostfixAdmin): Postfix's Web Interface.
  
* [Dovecot](https://wiki.archlinux.org/index.php/dovecot): Allow users to remote access the emails stored by MDA via [IMAP](https://en.wikipedia.org/wiki/IMAP) or [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol).

* [Roundcube](https://wiki.archlinux.org/index.php/Roundcube): A web-based email client.

#### Postfix

To install, run

```bash
sudo pacman -S postfix
```

Next, I did some configurations as follows.

* Uncomment the following line in `/etc/postfix/aliases`, and change `you` to a real account.

  ```bash
  root: you
  ```
  
  Then, `sudo postalias /etc/postfix/aliases` and `sudo newaliases`. 
  
* Edit `/etc/postfix/main.cf` to reflect the following configuration. Uncomment, change, or add the following lines

  ```bash
  myhostname = localhost
  inet_interfaces = all
  inet_protocols = all
  mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
  mynetworks_style = host
  home_mailbox = Maildir/
  smtp_host_lookup = native # To look up a host's IP address, Postfix SMTP uses the native service
  ```

All other settings may remain unchanged.
Then, we can `sudo systemctl start postfix && sudo systemctl enable postfix`.

To check if everything works as expected, type from console the following commands to *send an email*:

```bash
telnet localhost smtp
Trying ::1...
Connection failed: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
220 localhost ESMTP Postfix

mail from: hoanganhduc@localhost
250 2.1.0 Ok

rcpt to: hoanganhduc@localhost 
250 2.1.0 Ok

data
354 End data with <CR><LF>.<CR><LF>

A test email using Postfix
.
250 2.0.0 Ok: queued as A91FDC05E0

quit
221 2.0.0 Bye
Connection closed by foreign host.
```

To check if the email has been received, look at the `~/Maildir/new` directory.

To enable TLS with Postfix, first, edit `/etc/postfix/main.conf` by adding the following lines:

```bash
# Secure SMTP sending
smtp_tls_security_level = may # Use TLS if available. To enforce TLS, change `may` to `encrypt`
# Secure SMTP receiving
smtpd_tls_security_level = may
smtpd_use_tls = yes
smtpd_tls_cert_file = /etc/httpd/conf/localhost.crt # See the section regarding using TLS with Apache server
smtpd_tls_key_file = /etc/httpd/conf/localhost.key
```
Now, to enable STARTTLS (port 587), modify the following lines in `/etc/postfix/master.cf` as follows:

```bash
submission inet n       -       n       -       -       smtpd
  -o syslog_name=postfix/submission
  -o smtpd_tls_security_level=encrypt
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_tls_auth_only=yes
  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
  -o smtpd_recipient_restrictions=
  -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
  -o milter_macro_daemon_name=ORIGINATING
```

To enable SMTPS (port 465), modify the following lines in `/etc/postfix/master.cf` as follows:

```bash
smtps     inet  n       -       n       -       -       smtpd
  -o syslog_name=postfix/smtps
  -o smtpd_tls_wrappermode=yes
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
  -o smtpd_recipient_restrictions=
  -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
  -o milter_macro_daemon_name=ORIGINATING
```

and in the first line, replace `smtps` with `submissions`. 

#### PostfixAdmin

PostfixAdmin is a web interface for Postfix used to manage mailboxes, virtual domains and aliases. 
To install, run

```bash
sudo pacman -S postfixadmin
```

Next. we need to configure it to work with Apache and MySQL.
To do this, we first create an empty database `postfix_db` and the corresponding user `postfix_user` who will have read/write access to `postfix_db` using the password `hunter2`.

```bash
mysql -u root -p
CREATE DATABASE postfix_db;
GRANT ALL ON postfix_db.* TO 'postfix_user'@'localhost' IDENTIFIED BY 'hunter2';
FLUSH PRIVILEGES;
\q
```

Next, we can edit the PostfixAdmin configuration file `/etc/webapps/postfixadmin/config.inc.php`.

```bash
<?php
$CONF['configured'] = true;
// correspond to dovecot maildir path /home/vmail/%d/%u 
$CONF['domain_path'] = 'YES';
$CONF['domain_in_mailbox'] = 'NO';
$CONF['database_type'] = 'mysqli';
$CONF['database_host'] = 'localhost';
$CONF['database_user'] = 'postfix_user';
$CONF['database_password'] = 'hunter2';
$CONF['database_name'] = 'postfix_db';

// globally change all instances of ''change-this-to-your.domain.tld'' 
// to an appropriate value
$CONF['default_aliases'] = array (
    'abuse' => 'abuse@localhost',
    'hostmaster' => 'hostmaster@localhost',
    'postmaster' => 'postmaster@localhost',
    'webmaster' => 'webmaster@localhost'
);

$CONF['vacation_domain'] = 'autoreply.localhost';

$CONF['footer_text'] = 'Return to localhost';
$CONF['footer_link'] = 'http://localhost';
```

The next step is to configure `postfixadmin` with my pre-installed Apache server with `php-fpm` above.
Create `/etc/httpd/conf/postfixadmin.conf` with the following contents

```bash
Alias /postfixadmin "/usr/share/webapps/postfixadmin/public"
<Directory "/usr/share/webapps/postfixadmin/public">
    DirectoryIndex index.html index.php
    <FilesMatch \.php$>
        SetHandler "proxy:unix:/run/postfixadmin/postfixadmin.sock|fcgi://localhost/"
    </FilesMatch>
    AllowOverride All
    Options FollowSymlinks
    Require all granted
    SetEnv PHP_ADMIN_VALUE "open_basedir = /tmp/:/usr/share/webapps/postfixadmin:/etc/webapps/postfixadmin/:/var/cache/postfixadmin/templates_c"
    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1
</Directory>
```

and add `Include conf/postfixadmin.conf` to `/etc/httpd/conf/httpd.conf` and then `sudo systemctl restart httpd`.

Next, create `/etc/php/php-fpm.d/postfixadmin.conf` with the following contents

```bash
[postfixadmin]
user = postfixadmin
group = postfixadmin
listen = /run/postfixadmin/postfixadmin.sock
listen.owner = root
listen.group = http
listen.mode = 0660
pm = ondemand
pm.max_children = 4
php_admin_value['date.timezone'] = UTC
php_admin_value['session.save_path'] = /tmp
php_admin_value['open_basedir'] = /tmp/:/usr/share/webapps/postfixadmin/:/etc/webapps/postfixadmin/:/usr/bin/doveadm:/var/cache/postfixadmin
```

and `sudo systemctl restart php-fpm`.

Finally, go to [http://127.0.0.1/postfixadmin/setup.php](http://127.0.0.1/postfixadmin/setup.php) to finish the setup.
Generate your setup password hash at the bottom of the page once it is done. Write the hash to the config file `/etc/webapps/postfixadmin/config.local.php`:

```bash
$CONF['setup_password'] = 'yourhashhere';
```

and now you can create a superadmin account at [http://127.0.0.1/postfixadmin/setup.php](http://127.0.0.1/postfixadmin/setup.php).

#### Dovecot

To install, run

```bash
sudo pacman -S dovecot
```

Now, we need to configure `dovecot`. 
First, we copy the configuration files to `/etc/dovecot`.

```bash
sudo mkdir -p /etc/dovecot
sudo rsync -arv /usr/share/doc/dovecot/example-config/* /etc/dovecot
```

Next, edit `/etc/dovecot/dovecot.conf`

```bash
protocols = imap pop3 lmtp
```

Then, edit `/etc/dovecot/conf.d/10-mail.conf`


```bash
mail_location = maildir:~/Maildir
```

Next, edit `/etc/doveconf/conf.d/10-auth.conf`

```bash
disable_plaintext_auth = no
auth_username_format = %n
auth_mechanisms = plain login
```
Finally, edit `/etc/dovecot/conf.d/10-master.conf`

```bash
unix_listener auth-userdb { 
    #mode = 0600 
    user = postfix 
    group = postfix 
}
```

Then, we can now `sudo systemctl start dovecot && sudo systemctl enable dovecot`.
In case you get the error

```bash
doveconf: Fatal: Error in configuration file /etc/dovecot/conf.d/10-ssl.conf line 12: ssl_cert: Can't open file /etc/ssl/certs/dovecot.pem: No such file or directory
```

then just simply comment out the lines containing `/etc/ssl/certs/dovecot.pem`. 

To enable SSL/TLS with Dovecot, edit `/etc/dovecot/conf.d/10-ssl.conf`:

```bash
ssl = yes
ssl_cert = </etc/httpd/conf/localhost.crt
ssl_key = </etc/httpd/conf/localhost.key
```

To test if your Dovecot's configuration works: [IMAP](https://wiki.dovecot.org/TestInstallation) and [POP3](https://wiki.dovecot.org/TestPop3Installation).

#### Postfix with SASL

I follow the instruction [here](https://wiki.archlinux.org/index.php/Postfix_with_SASL) to setup SASL authentication for Postfix with Dovecot. 
The steps are as follows:

* Edit `/etc/postfix/main.cf` by adding

  ```bash
  # Enable SASL
  smtpd_sasl_auth_enable=yes
  broken_sasl_auth_clients = yes
  smtpd_sasl_type=dovecot
  smtpd_sasl_path=private/auth
  smtpd_sasl_security_options=noanonymous
  smtpd_sasl_local_domain=$myhostname
  smtpd_client_restrictions=permit_sasl_authenticated,reject
  smtpd_recipient_restrictions=reject_non_fqdn_recipient,reject_unknown_recipient_domain,permit_sasl_authenticated,reject
  ```
  
* Edit `/etc/dovecot/conf.d/10-master.conf`:

  ```bash
  service auth {
  #unix_listener auth-userdb {
  #  mode = 0666
  #  user = postfix 
  #  group = postfix
  #}

  # Postfix smtp-auth
  unix_listener /var/spool/postfix/private/auth {
    mode = 0660
    user = postfix
    group = postfix
  }

  # Auth process is run as this user.
  user = root
  }
  ```

* Finally, restart both `postfix` and `dovecot`. To test if your configuration works, follow [this instruction](http://www.postfix.org/SASL_README.html#server_test).

#### Roundcube

To install, run

```bash
sudo pacman -S roundcubemail
```

I already have [MariaDB](https://wiki.archlinux.org/index.php/MariaDB) for managing databases, and an [Apache server with PHP support](https://wiki.archlinux.org/index.php/Apache_HTTP_Server).

Next, we create a database `roundcubemail` for the user `roundcube` identified by paswword `password`:

```bash
mysql -u root -p
CREATE DATABASE `roundcubemail` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
CREATE USER `roundcube`@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `roundcubemail`.* TO `roundcube`@`localhost`;
FLUSH PRIVILEGES;
\q
```

and then initialize the `roundcubemail` database tables by `mysql -u root -p roundcubemail < /usr/share/webapps/roundcubemail/SQL/mysql.initial.sql`.

Now, we copy the example configuration file

```bash
cd /etc/webapps/roundcubemail/config
sudo cp -vp config.inc.php.sample config.inc.php
sudo chown http:http config.inc.php
```

and then edit `/etc/webapps/roundcubemail/config/config.inc.php`: (Remeber to replace `password` with your `roundcube` user password you set before when creating database.)

```bash
$config['db_dsnw'] = 'mysql://roundcube:password@localhost/roundcubemail';
$config['default_host'] = 'tls://localhost'; // IMAP host
$config['smtp_server'] = 'tls://localhost';
$config['smtp_port'] = 587;
$config['des_key'] = 'some_awesome_long_semi_random_string';
$config['enable_installer'] = true; // enable the setup wizard
```

For roundcube to be able to detect mime-types from filename extensions you need to point it to a mime.types file. Apache usually comes with one, thus we can just copy it over.

```bash
sudo cp /etc/httpd/conf/mime.types /etc/webapps/roundcubemail/config/mime.types
sudo chown http:http /etc/webapps/roundcubemail/config/mime.types
```

and then edit `/etc/webapps/roundcubemail/config/config.inc.php` by adding

```bash
$config['mime_types'] = '/etc/webapps/roundcubemail/config/mime.types'; // detect mime-types from filename extensions
```

Next, edit `/etc/php/php.ini`

```bash
date.timezone = "UTC"
```

and uncomment `extension=iconv` and `extension=pdo_mysql`.

If you have configured `open_basedir` in `php.ini`, make sure it includes `/etc/webapps` and `/usr/share/webapps`, so PHP can open the required Roundcube files. If `open_basedir` is disabled/commented out (the default setting), you don't have to do anything.

Now, copy the configuration file for Apache to `/etc/httpd/conf/extra`:

```bash
sudo cp -vp /etc/webapps/roundcubemail/apache.conf /etc/httpd/conf/extra/roundcube.conf
```

then, edit `/etc/httpd/conf/extra/roundcube.conf` by replacing the line `php_admin_value open_basedir "/tmp/:/var/cache/roundcubemail:/usr/share/webapps/roundcubemail:/etc/webapps/roundcubemail:/usr/share/pear/:/var/log/roundcubemail"` with `SetEnv PHP_ADMIN_VALUE "open_basedir=/tmp/:/var/cache/roundcubemail:/usr/share/webapps/roundcubemail:/etc/webapps/roundcubemail:/usr/share/pear/:/var/log/roundcubemail"` (if you do not use `php-fpm`, ignore this setting),
and add `Include conf/extra/roundcube.conf` to `/etc/httpd/conf/httpd.conf`, and `sudo systemctl restart httpd`.

Finally you can visit the Roundcube installation wizard in your browser: [http://localhost/roundcube/installer](http://localhost/roundcube/installer).
When testing SMTP config with Roundcube, I get the following error

```bash
postfix/submission/smtpd[25422]: warning: TLS library problem: error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca:ssl/record/rec_layer_s3.c:1543:SSL alert number 48:
```

Typically, this error indicated that [PHP fails to verify peer certificate because unknown CA](https://serverfault.com/questions/655995/roundcube-postfix-smtp-ssl-routinesssl3-read-bytestlsv1-alert-unknown-cas3). 
A simple solution is to disable `verify_peer` and/or `verify_peer_name` in Roundcube's `smtp_conn_options` and `imap_conn_options` by adding the follwoing lines to `/etc/webapps/roundcubemail/config/config.inc.php`:

```bash
$config['smtp_conn_options'] = array(
  'ssl'         => array(
     'verify_peer'      => false,
     'verify_peer_name' => false,
  ),
);
$config['imap_conn_options'] = array(
  'ssl'         => array(
     'verify_peer'      => false,
     'verify_peer_name' => false,
  ),
);
```

Another solution according to [ArchWiki](https://wiki.archlinux.org/index.php/Roundcube) is to copy `myCA.pem` to `/etc/ssl/certs/` and add the following lines to `/etc/webapps/roundcubemail/config/config.inc.php`

```bash
// For STARTTLS IMAP
$config['imap_conn_options'] = array(
 'ssl' => array(
   'verify_peer'       => true,
   // certificate is not self-signed if cafile provided
   'allow_self_signed' => false,
   'cafile'  => '/etc/ssl/certs/myCA.pem',
   // For Letsencrypt use the following two lines and remove the 'cafile' option above.
   //'ssl_cert' => '/etc/letsencrypt/live/mail.my_domain.org/fullchain.pem',
   //'ssl_key'  => '/etc/letsencrypt/live/mail.my_domain.org/privkey.pem',
   // probably optional parameters
   'ciphers' => 'TLSv1+HIGH:!aNull:@STRENGTH',
   'peer_name'         => 'localhost',
 ),
);
// For STARTTLS SMTP
$config['smtp_conn_options'] = array(
 'ssl' => array(
   'verify_peer'       => true,
   // certificate is not self-signed if cafile provided
   'allow_self_signed' => false,
   'cafile'  => '/etc/ssl/certs/myCA.pem',
   // For Letsencrypt use the following two lines and remove the 'cafile' option above.
   //'ssl_cert' => '/etc/letsencrypt/live/mail.my_domain.org/fullchain.pem',
   //'ssl_key'  => '/etc/letsencrypt/live/mail.my_domain.org/privkey.pem',
   // probably optional parameters
   'ciphers' => 'TLSv1+HIGH:!aNull:@STRENGTH',
   'peer_name'         => 'localhost',
 ),
);
```

Finally, after finishing configuration, add `$config['enable_installer'] = false;` to `/etc/webapps/roundcubemail/config/config.inc.php`, and add these lines to `/etc/httpd/conf/extra/roundcube.conf`.

```bash
<Directory /usr/share/webapps/roundcubemail/config>
	Options -FollowSymLinks
	AllowOverride None
	Require all denied
</Directory>
```

### Gitweb

[Gitweb](https://wiki.archlinux.org/index.php/gitweb) is the default [web-based visualizer](https://git-scm.com/book/en/v2/Git-on-the-Server-GitWeb) that comes with [Git](https://wiki.archlinux.org/index.php/Git).
To have a quick look, you can `sudo pacman -S lighttpd` and run `git instaweb --httpd=lighttpd` in your project directory and refer to [http://127.0.0.1:1234](http://127.0.0.1:1234). 
(The command will directly open Firefox with that address.)
To stop, run `git instaweb --stop`.
To use [Google Chrome](https://aur.archlinux.org/packages/google-chrome/) as the default browser for `git`, run:

```bash
git config --global web.browser chrome
git config --global browser."chrome".path "/usr/bin/google-chrome-stable"
```

To make Gitweb work with Apache, I use the following [configurations](https://wiki.archlinux.org/index.php/gitweb). 
First, run

```bash
sudo pacman -S --noconfirm --needed git perl-cgi
```

Then, create `/etc/httpd/conf/extra/gitweb.conf` with the following contents

```bash
LoadModule cgi_module modules/mod_cgi.so

Alias /gitweb "/usr/share/gitweb"
<Directory "/usr/share/gitweb">
    DirectoryIndex gitweb.cgi
    Options ExecCGI
    Require all granted
    <Files gitweb.cgi>
    SetHandler cgi-script
    </Files>
    SetEnv  GITWEB_CONFIG  /etc/gitweb.conf
</Directory>
```

and then add `Include conf/extra/gitweb.conf` to `/etc/httpd/conf/httpd.conf`.

I want to have all my projects in one directory `/srv/git`, which can be done by editting/creating `/etc/gitweb.conf` with

```bash
# The directories where your projects are. Must not end with a slash.
our $projectroot = "/srv/git"; 
```

Now, I can simple create symbolic links to my projects saved at `$HOME` directory, for example

```bash
sudo ln -s $HOME/hoanganhduc.github.io /srv/git/hoanganhduc.github.io
```

Some other configurations with `/etc/gitweb.conf` are:
* To enable "blame" view (showing the author of each line in a source file), add `$feature{'blame'}{'default'} = [1];`.
* To enable syntax highlighting with Gitweb, install the [highlight](https://www.archlinux.org/packages/?name=highlight) package and add `$feature{'highlight'}{'default'} = [1];`.
* To enable display remote heads, add `$feature{'remote_heads'}{'default'} = [1];`.

Finally, go to [http://localhost/gitweb](http://localhost/gitweb) to see your projects.

{% include image.html name="Screenshot from 2020-11-07 19-32-33.png" caption="The repository of my personal webpage displayed locally by Gitweb" width="60%" %}

## FTP with `vsftpd`

I follow the instruction from [ArchWiki](https://wiki.archlinux.org/index.php/Very_Secure_FTP_Daemon). 
Another good resource is [this guide](https://www.netarky.com/programming/arch_linux/Arch_Linux_SFTP_setup.html).
To install, run

```bash
sudo pacman -S vsftpd
sudo systemctl enable vsftpd
```

Next, add the following lines to `/etc/hosts.allow`

```bash
# Allow all connections
vsftpd: ALL
# IP address range
vsftpd: 10.0.0.0/255.255.255.0
```

Then, edit `/etc/vsftpd.conf` to enable/disable certain options.
My `vsftpd.conf` looks like this

```bash
# Allow anonymous FTP? (Beware - allowed by default if you comment this out).
anonymous_enable=NO
# Uncomment this to allow local users to log in.
local_enable=YES
#
# Uncomment this to enable any form of FTP write command.
write_enable=YES
#
# Default umask for local users is 077. You may wish to change this to 022,
# if your users expect that (022 is used by most other ftpd's)
local_umask=022
#
# Uncomment this if you want the anonymous FTP user to be able to create
# new directories.
anon_mkdir_write_enable=YES
# Directory to be used for an anonymous login  
anon_root=public
#
# Activate directory messages - messages given to remote users when they
# go into a certain directory.
dirmessage_enable=YES
#
# Activate logging of uploads/downloads.
xferlog_enable=YES
#
# Make sure PORT transfer connections originate from port 20 (ftp-data).
connect_from_port_20=YES
#
# When "listen" directive is enabled, vsftpd runs in standalone mode and
# listens on IPv4 sockets. This directive cannot be used in conjunction
# with the listen_ipv6 directive.
listen=YES
listen_port=21
passv_min_port=5000
passv_max_port=5003


# Set own PAM service name to detect authentication settings specified
# for vsftpd by the system package.
pam_service_name=vsftpd

ssl_enable=YES

# if you accept anonymous connections, you may want to enable this setting
allow_anon_ssl=NO

# by default all non anonymous logins and forced to use SSL to send and receive password and data, set to NO to allow non secure connections
force_local_logins_ssl=NO
force_local_data_ssl=NO

# provide the path of your certificate and of your private key
# note that both can be contained in the same file or in different files
rsa_cert_file=/etc/httpd/conf/localhost.crt
rsa_private_key_file=/etc/httpd/conf/localhost.key

# this setting is set to YES by default and requires all data connections exhibit session reuse which proves they know the secret of the control channel.
# this is more secure but is not supported by many FTP clients, set to NO for better compatibility
require_ssl_reuse=NO

seccomp_sandbox=NO
```

The last line `seccomp_sandbox=NO` is to avoid the following error message when using FileZilla.

```bash
Error:	GnuTLS error -15 in gnutls_record_recv: An unexpected TLS packet was received.
Error:	Could not read from socket: ECONNABORTED - Connection aborted
Error:	Disconnected from server
```
<!--
Since I allow anonymous FTP (login with username `anonymous` and empty password) and set the value of `anon_root=public`, I also need to `sudo mkdir -p /srv/ftp/public` and `sudo chown -R root:ftp /srv/ftp/public`. 
-->

Note that `localhost.crt` and `localhost.key` come from the instruction in a previous section of this post regarding using TLS in Apache server. 
And since I allow local user login, I also need `sudo usermod -aG ftp $USER` to allow myself to use FTP service.

In order to have both FTP and FTPS simultaneously, I create an extra configuration file `/etc/vsftpd_ssl.conf` with the above contents, and the file `/etc/vsftpd.conf` with almost the same content, except the part starting from `ssl_enable=YES`, and the `listen_port=990`. 
(Port 21 is considered the default control connection port for FTP connections. 
Port 990 is the accepted default control connection port for FTPS (implicit port). 
Actually, you can change them to whatever ports you like.
See [this page](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) for more details on other wel-known ports and their corresponding system processes.)
Next, create `/usr/lib/systemd/system/vsftpd_ssl.service` with the following content

```bash
[Unit]
Description=vsftpd daemon with SSL/TLS
After=network.target

[Service]
ExecStart=/usr/bin/vsftpd /etc/vsftpd_ssl.conf
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process

[Install]
WantedBy=multi-user.target
```

and `sudo systemctl enable vsftpd_ssl && sudo systemctl start vsftpd_ssl`.

## oh-my-zsh does not apply themes

You may try to remove the `grml-zsh-config` package, as described [here](https://stackoverflow.com/a/58831804).

## Automount NTFS USB drive with default Linux file permissions

I want to mount my NTFS USB drive with default Linux file permissions (i.e., `644` for files, and `755` for folders) every time I plug it in. A simple way to do it is to add the following lines to `/etc/udisks2/mount_options.conf` and then `sudo systemctl restart udisks2`.

```bash
[defaults]
ntfs_defaults=uid=$UID,gid=$GID,umask=0022,fmask=0133,windows_names
```

## Copy contents of a file to clipboard

Install [xclip](https://www.archlinux.org/packages/extra/x86_64/xclip/) and run

```bash
xclip -sel clip < file.txt
```

to copy the contents of `file.txt` to clipboard. See [this page](https://github.com/astrand/xclip) for some other things you can do with `xclip`. 

## IRC server

I created a simple [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) server with [biltbee](https://wiki.archlinux.org/index.php/bitlbee). 
Basically, I have to `yay -S bitlbee`, then edit `/etc/bitlbee/bitlbee.conf` as instructed in the wiki, and finally `sudo systemctl start bitlbee` and maybe also `sudo systemctl enable bitlbee`. My `bitlbee.conf` file may look pretty much like

```bash
[settings]
RunMode = ForkDaemon
User = bitlbee

DaemonInterface = 0.0.0.0
DaemonPort = 6667
```

You can replace `<your-password>` by any password you like.
For an IRC client software, I use [irssi](https://wiki.archlinux.org/index.php/irssi) (another option might be [hexchat](https://wiki.archlinux.org/index.php/HexChat)). 
If you are not familiar with IRC, some [basic IRC commands](https://www.mirc.com/help/html/index.html?basic_irc_commands.html) will probably be helpful. 
It is also possible to setup [bitlbee with Facebook](https://wiki.bitlbee.org/HowtoFacebookMQTT) using the [bitlbee-facebook](https://aur.archlinux.org/packages/bitlbee-facebook/) package (maybe [this blog post](https://blog.wyrihaximus.net/2012/04/starting-with-bitlbee/) has some useful information), and the ["self_messages" setting](https://wiki.bitlbee.org/SelfMessages) seems to be interesting. 
It is also useful to look at some [bitlbee commands](https://wiki.bitlbee.org/Commands). 
What I did for setting `bitlbee-facebook` may look something like 
(Please ignore the part starting from the hashtag `#` sign, they are just my comments. 
Additionally, after the first line, the command prompt starts after `[...]`.)

```bash
irssi # start `irssi`
[(status)] /connect localhost
[(status)] /join &facebook # `creating &facebook channel`
[&facebook] account add facebook <your-fb-email> <your-fb-password> # a suggestion is to use 
[&facebook] account facebook on
[&facebook] account facebook set nick_source full_name
[&facebook] account facebook set nick_format %-@full_name
[&facebook] channel facebook set fill_by account
[&facebook] channel facebook set account facebook
[&facebook] register <your-password> # your secret password used to save and load account settings
[&facebook] save # next time, to load account settings, run `identify <your-password>` 
```

## Some tips with file timestamps

* Comparing timestamps of two files. (Originally from [this page](https://unix.stackexchange.com/a/372904).)

  A simple way (comparing up to seconds) is

  ```bash
  [ file1 -nt file2 ] && echo "file1 is newer than file2"
  ```
  
  To be more precise (comparing up to nanoseconds),
  
  ```bash
  file1time=$(ls --time-style=+%s%N -l file1 | awk "{print(\$6)}")
  file2time=$(ls --time-style=+%s%N -l file2 | awk "{print(\$6)}")
  [ $file1time -gt $file2time ] && echo "file1 is newer than file2"
  ```
  
* Copy the timestamp of `src.file` to `dst.file`. (Originally from [this page](https://stackoverflow.com/a/15181135).)

  You will need [coreutils](https://www.archlinux.org/packages/core/x86_64/coreutils/).

  ```bash
  touch -d @$(stat -c "%Y" "src_file") "dst.file"
  ```
  
* Save and restore files' created/modified timestamps. (Originally from [this page](https://superuser.com/a/513854).)

  You will need [perl](https://www.archlinux.org/packages/core/x86_64/perl/).
  
  ```bash
  # Save
  find / -mount -print0 | perl -ne 'INIT{ $/ = "\0"; use File::stat;} chomp; my $s = stat($_); next unless $s; print $s->ctime . "/" . $s->mtime . "/" . $s->atime ."/$_\0"; ' > dates.dat

  # Restore
  cat dates.dat |  perl -ne 'INIT{ $/ = "\0";} chomp; m!^([0-9]+)/([0-9]+)/([0-9]+)/(.*)!s or next; my ($ct, $mt, $at, $f) = ($1, $2, $3, $4); utime $at, $mt, $f;'
  ```
  
## Cleaning

See [this guide](https://averagelinuxuser.com/clean-arch-linux/) for more details.

* Clean package cache.

  The script `paccache` is useful for cleaning cached packages saved at `/var/cache/pacman/pkg/`. 
  To install, run
  
  ```bash
  sudo pacman -S pacman-contrib
  ```
  
  and use `paccache -h` to see available options.
  To clean all cached packages that are not currently installed, run `sudo pacman -Sc`.
  To clean all cached packages, run `sudo pacman -Scc`.
  The command `yay -Scc` also does that along with removing all cached AUR packages installed using `yay`.

* Remove orphan packages that are not used by any program.

  To list all unused packages, run `sudo pacman -Qtdq`. To remove all of them, run `sudo pacman -Rns $(pacman -Qtdq)`.
  
* Clean `$HOME/.cache`.

  To check the size of the folder, run `du -sh $HOME/.cache/`. To delete the folder, simply run `rm -rf $HOME/.cache`.
  
* Clean duplicates, empty files/folders, broken links. 

  Use [rmlint](https://www.archlinux.org/packages/community/x86_64/rmlint/). Run `rmlint $HOME` will check your home directory for duplicated files and creates a shell script `rmlint.sh` to remove them.
  
* Clean systemd journal stored at `/var/log/journal`.

  You can keep only the latest logs by size limit (e.g. keep only 50MB of the latest logs):
  
  ```bash
  sudo journalctl --vacuum-size=50M
  ```
  
  Or by time limit (e.g. last 4 weeks):
  
  ```bash
  sudo journalctl --vacuum-time=4weeks
  ```
  
## Quick Clonezilla commands

* Save partitions `/dev/sdc1`, `/dev/sdc2`, `/dev/sdc3`, and `/dev/sdc4` to image `2020-10-25-03-img`.

  ```bash
  /usr/bin/ocs-sr -q2 -c -j2 -z1p -i 4096 -sfsck -senc -p choose saveparts 2020-10-25-03-img sdc1 sdc2 sdc3 sdc4
  ```
* Restore `sdb4` from image `2020-10-25-03-img` to partition `/dev/sda4` on disk

  ```bash
  /usr/bin/ocs-sr -e1 auto -e2 -t -r -j2 -c -k -p choose -f sdb4 restoreparts 2020-10-25-03-img sda4
  ```
  
  Remeber to mount the directory containing `2020-10-25-03-img` as `/home/partimag` before running this command.

* Clone `/dev/sdb4` to `/dev/sda4`.

  ```bash
  /usr/bin/ocs-onthefly -e1 auto -e2 -r -j2 -sfsck -k -pa choose  -f sdb4 -t sda4
  ```
  
## [Live Arch] Adjust The Size of The Root Partition on Live Arch Linux

This is a quite useful tip when booting from Live Arch system to test your installation.
Let say you want to use 1GB *from your RAM* as space for the root partition: 

```bash
mount -o remount,size=1G /run/archiso/cowspace
```

Using `df -h` to confirm that the size of `airootfs` mounted on `/` is now `1.0G`.

## Mondo Rescue

Back in 2014, I used [Mondo Rescue](http://www.mondorescue.org/) as an option for [backing up and restoring my Ubuntu system]({% link _posts/2014-01-08-clonebackup-ubuntu-systems-using-mondo-rescue.md %}). 
Even though I am now using [Clonezilla](https://clonezilla.org/), I still want to have Mondo Rescue on my Arch Linux system. 
So I went ahead and installed [mondo](https://aur.archlinux.org/packages/mondo/) with `yay -S --noconfirm --needed mondo`.
Unfortunately, as I am using `gcc 10.2.0`, the compilation failed:

```bash
/usr/bin/ld: ../../src/common/libmondo.a(libmondo-tools.o):(.bss+0x210): multiple definition of `g_mondo_home'; mondorestore.o:(.bss+0x0): first defined here
collect2: error: ld returned 1 exit status
make[3]: *** [Makefile:422: mondorestore] Error 1
```

I found a similar [bug report](https://bugs.square-r00t.net/index.php?do=details&task_id=77) but cannot understand what the solution is.
I decided to use an older version of `gcc` and try to compile again. 
Downgrading `gcc` is not an option, as it would break the dependencies of some other packages I need.
I follow [this instruction](https://unix.stackexchange.com/a/486059) to temporarily change the default version of `gcc` and then I can install `mondo` successfully.  

```bash
yay -S --needed --noconfirm gcc9 gcc9-libs
sudo ln -s $(which gcc-9) /usr/local/bin/gcc
hash -r
yay -S --needed --noconfirm mondo
sudo rm -rf /usr/local/bin/gcc
```

## Error 12 when using `zip -u` in `Makefile`

When using [zip](https://www.archlinux.org/packages/extra/x86_64/zip/) with `-u` option in a `Makefile`, e.g., `zip -u archive.zip *.pdf`, it may happen that nothing changes and therefore `archive.zip` will not be updated.
In this case, `zip` returns exit code `12`, meaning "`zip` has nothing to do".
`make` may produce something like `make: *** [Makefile:8: all] Error 12`.
To avoid such error, you can possibly do:

```bash
zip -u archive.zip *.pdf || if [[ $$? -eq 12 ]]; then echo "Nothing changes!"; exit 0; fi
```

In a Linux terminal, you can use `echo $?` to get the exit code of a command. 
The output `0` means the command is executed successfully.
In a `Makefile`, to get the exit code, we need an extra `$`.

## Which package holds my program?

Let say I want to know which package holds `latexmk`, what I did is to run `pacman -Qo latexmk`, and the result was something like `/usr/bin/latexmk is owned by texlive-core 2020.55416-1`. Another way would be using the [pkgfike](https://wiki.archlinux.org/index.php/pkgfile) package, which can be installed by `sudo pacman -S --noconfirm --needed pkgfile && sudo pkgfile --update`. 

## Some tips for using `git`

* Create empty branch (see [here](https://stackoverflow.com/a/34100189)).

  ```bash
  git checkout --orphan empty-branch
  git rm -rf .
  git commit --allow-empty -m "root commit"
  git push origin empty-branch
  ```

* Save login credentials

  ```bash
  git config --global credential.helper store
  ```
  
  Remove `--global` option if you only want to enable saving credentials for your repository.
  You only need to enter the credentials the first time you push/pull from the remote repository, and then they with be stored in `~/.git-credentials`.

## Convert BibTeX to RIS

I need [RIS format](https://en.wikipedia.org/wiki/RIS_(file_format)) to import references to Zotero. 
(Importing with BibTeX always convert math symbols between `$...$` into HTML markups, which is not very nice.)
I use [bibutils](http://bibutils.refbase.org/) (installed by `yay -S bibutils`) as follows:

```bash
bib2xml file.bib > file.xml
xml2ris file.xnl > file.ris
```

## Some useful packages involving LaTeX

* There are some AUR packages that install LaTeX Templates: [latex-template-springer](https://aur.archlinux.org/packages/latex-template-springer/), [latex-template-lipics](https://aur.archlinux.org/packages/latex-template-lipics/).
* The [arxiv-collector](https://aur.archlinux.org/packages/arxiv-collector/) package provides a small Python script to collect LaTeX sources for upload to the [arXiv](https://arxiv.org/).

## Static HTML file index generator for Github Pages

Install the [apindex](https://aur.archlinux.org/packages/apindex/) package with `yay`. See [this page](https://github.com/smclt30p/apindex) for more details on how to use this program.

## HiDPI Display Settings

Several settings can be found [here](https://wiki.archlinux.org/index.php/HiDPI). Here are some of my settings.

* **GNOME text scaling:** `gsettings set org.gnome.desktop.interface text-scaling-factor 1.2`.
* **Q5t apps:** For Zoom, edit `/usr/share/applications/Zoom.desktop` by replacing `Exec=/usr/bin/zoom %U` by `Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=1 /usr/bin/zoom %U`. Similar tricks can be done with other Qt5 apps (such as Insync).
* **GRUB Bootloader:** Add `GRUB_GFXMODE=1024x768x32,auto` to `/etc/default/grub`.
* **GNOME scaling:** I first scale GNOME with scale factor 2 via `gsettings set org.gnome.desktop.interface scaling-factor 2` (which is too big). Then, I use `xrandr` to scaling down: first, use `xrandr --listmonitors` to identify my monitor, which is `eDP-1`, then use `xrandr --output eDP-1 --scale 1.25x1.25` to zoom out 1.25 times. If the UI is too big, increase the scale factor; otherwise, decrease it. To do this automatically every time you login, put `/usr/bin/xrandr --output eDP-1 --scale 1.25x1.25` to the `~/.xprofile` file and `chmod +x .xprofile`. 

## Mobile Broadband

* Install `modemmanager`, `mobile-broadband-provider-info`, `usbutils`, `usb_modeswitch`, as instructed [here](https://wiki.archlinux.org/index.php/USB_3G_Modem). You can also install `modem-manager-gui` using `yay`.
* Enable and start `ModemManager` service

  ```bash
  sudo systemctl enable ModemManager
  sudo systemctl start ModemManager
  ```
  
* A system restart might be necessary for `ModemManager` to detect the USB modem.
* Enable `wwan` with `nmcli radio wwan on`.
* The `vnstat` package can be installed to monitor network traffic.

## Drivers for HP Printer/Scanner/Fax Devices

You will need [HP Linux Imaging and Printing](https://developers.hp.com/hp-linux-imaging-and-printing). 

```bash
yay -S hplip hplip-plugin
```

## Drivers for Kyocera TASKalpha Printer

You will need to install [kyocera-cups](https://aur.archlinux.org/packages/kyocera-cups). The file `Kyocera_Linux_PPD_Ver_8.1601.tar.gz` does not seem to be available from the URL provided in the [PKGBUILD](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=kyocera-cups) file. I keep a copy [here](https://kon8n2liffm1llqwuzlnjg-on.drv.tw/Public/Linux/Kyocera_Linux_PPD_Ver_8.1601.tar.gz). If you want to install it, just download the file, put it in `$HOME/.cache/yay/kyocera-cups/`, and run `yay -S kyocera-cups`.

A better option may be to install [kyocera_universal](https://aur.archlinux.org/packages/kyocera_universal/).
