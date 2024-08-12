---
layout: blog-post
title: Install and Configure Ubuntu 16.04 LTS
author: Duc A. Hoang
categories:
  - "linux"
<!--comment: true-->
last_modified_at: 2022-11-29
description: This post describes how Duc A. Hoang install and configure Ubuntu 16.04LTS
keywords: ubuntu 16.04 lts, install, configure, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains a collection of tips and tricks for installing and configuring Ubuntu 16.04 LTS. The system was pre-installed with the [official release](http://releases.ubuntu.com/16.04/) of Ubuntu 16.04 LTS. All commands are executed in a Ubuntu Terminal--the default commandline interface of Ubuntu. For a brief introduction on Ubuntu commands, see, e.g., [this tutorial](https://fullcirclemagazine.org/2017/10/17/command-conquer-special-editions-1-3/). Several useful tips and tricks for using Ubuntu and other Linux distribution can be found at [this page](https://sites.google.com/site/easylinuxtipsproject/Home). 
</div>

# Enable Ubuntu `partner` repository

Edit the file `/etc/apt/sources.list` by adding the following lines.

```bash
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
```

# Desktop environment

## GNOME (Shell, Flashback) desktop

```bash
sudo apt update
sudo apt install gnome gnome-shell gnome-panel gnome-flashback gnome-session-flashback gnome-tweak-tool
sudo apt upgrade
```

Several Gnome-Shell extensions can be installed from [here](https://extensions.gnome.org).

# Some configuration tools

```bash
sudo apt install unetbootin grub2 xorriso isomaster squashfs-tools debootstrap checkinstall libcdio-utils
sudo apt install gparted testdisk partimage xfsprogs reiserfsprogs jfsutils ntfs-3g dosfstools mtools
sudo apt install secure-delete wipe
sudo apt install samba cifs-utils system-config-samba 
sudo apt install lnav # Logfile navigator
sudo apt install ssh subversion git git-core mercurial mercurial-common ufw
sudo apt install python python-dev python-mysqldb python-setuptools python-pip python-matplotlib python-pywapi
sudo apt install openjdk-8-jdk openjdk-8-jre icedtea-8-plugin
sudo apt install libnetpbm10 libnetpbm10-dev
```

# Extract and compress files

```bash
sudo apt install unace unrar unzip zip lrzip p7zip-full p7zip-rar sharutils rar uudeview mpack arj cabextract file-roller
```

# Some common applications

```bash
sudo apt install pidgin pidgin-otr nautilus-dropbox encfs
sudo apt install goldendict pdfshuffler artha calibre fbreader djview4 shutter tasksel cups cups-pdf 
sudo apt install network-manager-openvpn openvpn 
sudo apt install filezilla gnugo uligo qgo gmchess
```

# Language packages and input keyboards

```bash
sudo apt install language-selector-gnome 
sudo apt install language-pack-gnome-en language-pack-gnome-vi language-pack-gnome-ja 
sudo apt install ibus ibus-unikey ibus-anthy ibus-m17n ibus-gtk scim scim-unikey
```

# Themes

## Arc theme

```bash
sudo apt install autoconf automake pkg-config libgtk-3-dev git
cd $HOME
git clone https://github.com/horst3180/arc-theme --depth 1
cd arc-theme
./autogen.sh --prefix=/usr
sudo make install
cd ..
git clone https://github.com/horst3180/arc-firefox-theme
cd arc-firefox-theme
./autogen.sh --prefix=/usr
sudo make install
cd ..
sudo rm -rf arc-theme arc-firefox-theme
```

## Numix theme

```bash
sudo add-apt-repository ppa:numix/ppa 
sudo apt update
sudo apt install numix-gtk-theme numix-icon-theme
```

## Vivacious colors icon theme

```bash
sudo add-apt-repository ppa:ravefinity-project/ppa
sudo apt-get update
sudo apt-get install vivacious-colors
```

## Faenza icon theme

```bash
sudo apt install faenza-icon-theme
```

## Papirus icon theme

```bash
sudo add-apt-repository ppa:varlesh-l/papirus-pack
sudo apt update
sudo apt install papirus-gtk-icon-theme
```

# Extra configurations

## Disable Guest account

Edit the file `/etc/lightdm/lightdm.conf` by adding the following lines.

```bash
[SeatDefaults]
greeter-session=unity-greeter
allow-guest=false
```

Next, restart the service

```bash
sudo /etc/init.d/lightdm restart
```

## Reconfigure keyboard

In case your <kbd>Fn</kbd> button in your laptop keyboard does not work, you might need to reconfigure the keyboard.

```bash
sudo dpkg-reconfigure keyboard-configuration
```

## Enable firewall

```bash
sudo apt install gufw # for graphical interface
sudo ufw enable
```

## Move window buttons to the right

```bash
gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'
```

## Show user name in Unity panel

```bash
gsettings set com.canonical.indicator.session show-real-name-on-panel true
```

## Change background, theme and icon theme of the login screen

```bash
sudo gsettings set com.canonical.unity-greeter background "/usr/share/backgrounds/milkyway.jpg" 
# the default background is warty-final-ubuntu.png
sudo gsettings set com.canonical.unity-greeter icon-theme-name "Vivacious-Dark-Blue" 
# the default theme is ubuntu-mono-dark
sudo gsettings set com.canonical.unity-greeter theme-name "Arc-Dark" 
# the default theme is Ambiance
```

## Change window border in GNOME Flashback
 
I use Arc-Dark theme instead of the default Ambiance theme.

```bash
gsettings set org.gnome.metacity theme 'Arc-Dark' # the default theme is Ambiance
```

## Dual monitor

I use a [FlexScan EV2116W-A](http://www.eizo.co.jp/products/lcd/ev2116wa/index.html) monitor as a second monitor (beside the built-in monitor in my laptop). A note is that you need to configure the monitor to make it recieve [D-SUB input](https://en.wikipedia.org/wiki/D-subminiature) or [DVI input](https://en.wikipedia.org/wiki/Digital_Visual_Interface) signals (using the `SIGNAL` button at the bottom of the monitor), depending on the connector you use.

## Fix error: Network Manager wired Ethernet stuck in ``getting IP config'' after resume from suspend

Create a file named `ethernet_fix` in `/usr/bin` with the following contents

```bash
#!/bin/sh

/sbin/modprobe -v -r r8169
/sbin/modprobe -v r8169
```

and make it executable using

```bash
sudo chmod a+x /usr/bin/ethernet_fix
```

Then, create a file `ethernet_fix` in `/lib/systemd/system-sleep` with the following contents

```bash
#!/bin/sh

case "${1}" in
 hibernate|suspend) ;;
 resume|thaw) ethernet_fix;;
esac
```

and make it executable using

```bash
sudo chmod a+x /lib/systemd/system-sleep/ethernet_fix
```

Finally, create a file `ethernet_fix.service` in `/etc/systemd/system` with the following contents

```bash
[Unit]
Description=Restart ethernet after resume
After=suspend.target
#After=hibernate.target
#After=hybrid-sleep.target

[Service]
ExecStart=/usr/bin/ethernet_fix

[Install]
WantedBy=suspend.target
#WantedBy=hibernate.target
#WantedBy=hybrid-sleep.target
```

and install that service file with

```bash
sudo systemctl enable ethernet_fix.service
```

## Change SSH default port

The SSH default port is `22`. To avoid anonymous security theft, you may want to change it by editing the file `/etc/ssh/sshd_config`. The port option are at the lines.

```bash
# What ports, IPs and protocols we listen for
Port 22
# Use these options to restrict which interfaces/protocols sshd will bind to 
```

After changing the port, say from `22` to `220`, restart the SSH service

```bash
sudo service ssh restart
```

and try to login

```bash
sudo ssh -X -p 220 username@192.51.245.250
```

# Skype (x64 OS only)

Download [https://www.skype.com/en/download-skype/skype-for-linux/](https://www.skype.com/en/download-skype/skype-for-linux/).

# TexLive 2017

## Download TexLive ISO Image

Visit [this page](http://www.tug.org/texlive/acquire-iso.html). JAIST also maintains a CTAN mirror, so you can download the ISO image at [http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/Images/](http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/Images/). 

For TexLive 2017, I downloaded the file `texlive2017-20170524.iso` and put it at my `$HOME` folder.

## How to Install

```bash
cd $HOME
mkdir mnt 
sudo mount -t iso9660 -o ro,loop,noauto texlive2017-20170524.iso mnt
cd mnt
sudo ./install-tl -gui text 
# use a plain text interfact
# see http://www.tug.org/texlive/quickinstall.html for other options of the installer's interface
# Install as instructed in the installer
cd $HOME 
sudo umount mnt
```

## Setting `PATH`, `MANPATH`, `INFOPATH`

For 64-bit OS, add the followings to `/etc/bash.bashrc`.

```bash
MANPATH=/usr/local/texlive/2017/texmf-dist/doc/man:$MANPATH; export MANPATH
INFOPATH=/usr/local/texlive/2017/texmf-dist/doc/info:$INFOPATH; export INFOPATH
PATH=/usr/local/texlive/2017/bin/x86_64-linux:$PATH; export PATH
```

Next, add the following after the line `# set up PATH to MANPATH mapping` in `/etc/manpath.config`.

```bash
MANPATH_MAP /usr/local/texlive/2017/bin/x86_64-linux /usr/local/texlive/2017/texmf-dist/doc/man
```

For 32-bit OS, replace `x86_64-linux` by `i386-linux`.

## Tell `APT` about your TexLive installation using a dummy package

The original instruction is at [https://www.tug.org/texlive/debian.html](https://www.tug.org/texlive/debian.html).

```bash
sudo apt-get install equivs
mkdir /tmp/tl-equivs && cd /tmp/tl-equivs
equivs-control texlive-local
# edit texlive-local (see below)
equivs-build texlive-local
sudo dpkg -i texlive-local_2017-1_all.deb
sudo apt-get install tex-common texinfo lmodern
```

At the step `edit texlive-local`, edit the Maintainer field and the list of the packages provided by your local TeX Live installation as appropriate. If you installed scheme-full except collection-texinfo as recommended, the file should look like the following example file for TexLive 2017.

```bash
Section: misc
Priority: optional
Standards-Version: 3.9.8

Package: texlive-local
Version: 2017-1
Maintainer: you <you@yourdomain.example.org>
Provides: chktex, biblatex, biblatex-dw, cm-super, cm-super-minimal, context, 
 dvidvi, dvipng, feynmf, fragmaster, jadetex, lacheck, latex-beamer, 
 latex-cjk-all, latex-cjk-chinese, latex-cjk-chinese-arphic-bkai00mp, 
 latex-cjk-chinese-arphic-bsmi00lp, latex-cjk-chinese-arphic-gbsn00lp, 
 latex-cjk-chinese-arphic-gkai00mp, latex-cjk-common, latex-cjk-japanese, 
 latex-cjk-japanese-wadalab, latex-cjk-korean, latex-cjk-thai, latexdiff, 
 latexmk, latex-sanskrit, latex-xcolor, lcdf-typetools, lmodern, luatex, 
 musixtex, passivetex, pgf, preview-latex-style, prosper, ps2eps, psutils, 
 purifyeps, t1utils, tex4ht, tex4ht-common, tex-gyre, texlive, texlive-base, 
 texlive-bibtex-extra, texlive-binaries, texlive-common, texlive-extra-utils,
 texlive-fonts-extra, texlive-fonts-extra-doc, texlive-fonts-recommended,
 texlive-fonts-recommended-doc, texlive-font-utils, texlive-formats-extra,
 texlive-games, texlive-generic-extra, texlive-generic-recommended,
 texlive-humanities, texlive-humanities-doc, texlive-lang-african,
 texlive-lang-all, texlive-lang-arabic, texlive-lang-cjk, texlive-lang-cyrillic,
 texlive-lang-czechslovak, texlive-lang-english, texlive-lang-european,
 texlive-lang-japanese, texlive-lang-chinese, texlive-lang-korean,
 texlive-lang-french, texlive-lang-german, texlive-lang-greek, 
 texlive-lang-indic, texlive-lang-italian, texlive-lang-other, 
 texlive-lang-polish, texlive-lang-portuguese, texlive-lang-spanish,
 texlive-latex-base, texlive-latex-base-doc, texlive-latex-extra, 
 texlive-latex-extra-doc, texlive-latex-recommended, 
 texlive-latex-recommended-doc, texlive-luatex, texlive-math-extra, 
 texlive-metapost, texlive-metapost-doc, texlive-music,
 texlive-omega, texlive-pictures, texlive-pictures-doc, texlive-plain-extra,
 texlive-plain-generic,
 texlive-pstricks, texlive-pstricks-doc, texlive-publishers,
 texlive-publishers-doc, texlive-science, texlive-science-doc, texlive-xetex,
 thailatex, tipa, tipa-doc, xindy, xindy-rules, xmltex, asymptote, texinfo
Depends: freeglut3
Architecture: all
Description: My local installation of TeX Live 2017.
 A full "vanilla" TeX Live 2017
 http://tug.org/texlive/debian#vanilla
```

## Install `getnonfreefonts`

For 64-bit OS.

```bash
wget http://tug.org/fonts/getnonfreefonts/install-getnonfreefonts
sudo -s
texlua install-getnonfreefonts
ln -s /usr/local/texlive/2017/bin/x86_64-linux/getnonfreefonts /usr/local/bin
ln -s /usr/local/texlive/2017/bin/x86_64-linux/getnonfreefonts-sys /usr/local/bin
getnonfreefonts --sys -a
exit
rm install-getnonfreefonts
```

For 32-bit OS, replace `x86_64-linux` by `i386-linux`.

# Texmaker

## Install via `APT`

```bash
sudo apt install texmaker
```

In Ubuntu 16.04, it may happen that the English spell check does not work. To fix this, re-set the spelling dictionary as `/usr/share/hunspell/en_US.dic`.

## Solarized theme

The original instruction is at [https://tex.stackexchange.com/a/196020](https://tex.stackexchange.com/a/196020).
Edit `$HOME/.config/xm1/texmaker.ini`

```bash
Color\Background=@Variant(\0\0\0\x43\x1\xff\xff\0\0++66\0\0)
Color\Command=@Variant(\0\0\0\x43\x1\xff\xff&&\x8b\x8b\xd2\xd2\0\0)
Color\Comment=@Variant(\0\0\0\x43\x1\xff\xffllqq\xc4\xc4\0\0)
Color\Highlight=@Variant(\0\0\0\x43\x1\xff\xff\a\a66BB\0\0)
Color\Keyword=@Variant(\0\0\0\x43\x1\xff\xff\xdc\xdc\x32\x32//\0\0)
Color\KeywordGraphic=@Variant(\0\0\0\x43\x1\xff\xff\x85\x85\x99\x99\0\0\0\0)
Color\Line=@Variant(\0\0\0\x43\x1\xff\xff\a\a66BB\0\0)
Color\Math=@Variant(\0\0\0\x43\x1\xff\xff**\xa1\xa1\x98\x98\0\0)
Color\NumberGraphic=@Variant(\0\0\0\x43\x1\xff\xff\xcb\xcbKK\x16\x16\0\0)
Color\Standard=@Variant(\0\0\0\x43\x1\xff\xff\x83\x83\x94\x94\x96\x96\0\0)
Color\Todo=@Variant(\0\0\0\x43\x1\xff\xff\xd3\xd3\x36\x36\x82\x82\0\0)
Color\Verbatim=@Variant(\0\0\0\x43\x1\xff\xff\xb5\xb5\x89\x89\0\0\0\0)
```

# LaTeX2HTML

```bash
git clone https://github.com/latex2html/latex2html.git
cd latex2html
./configure
make # Run `make test` for compiling a small test document at the `tests` subdirectory
sudo make install
```

I also made a quick note on [installing LaTeX2HTML in Windows]({% post_url 2018-05-26-install-latex2html-in-windows %}).

# IPE Extensible Drawing Editor 7.2.7

For more information on IPE, see [its homepage](http://ipe.otfried.org/). The original instruction can be found [here](https://github.com/otfried/ipe-wiki/wiki/Downloading,%20Compiling,%20and%20Installing%20Ipe).

```bash
sudo apt install checkinstall zlib1g-dev qtbase5-dev qtbase5-dev-tools
sudo apt install libfreetype6-dev libcairo2-dev libjpeg8-dev
sudo apt install libpng12-dev liblua5.3-dev
wget https://dl.bintray.com/otfried/generic/ipe/7.2/ipe-7.2.7-src.tar.gz
tar -xvf ipe-7.2.7-src.tar.gz
cd ipe-7.2.7/src
export QT_SELECT=5
make IPEPREFIX=/usr/local
sudo checkinstall --pkgname=ipe --pkgversion=7.2.7 --backup=no --fstrans=no --default make install IPEPREFIX=/usr/local
sudo ldconfig
```

Finally, create `/usr/share/applications/ipe.desktop` with the following contents

```bash
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=IPE
Comment=IPE extensible drawing editor
Exec=/usr/local/bin/ipe
Icon=/usr/local/share/ipe/7.2.7/icons/ipe.png
Terminal=false
Categories=Graphics
```

and make it executable.

```bash
sudo chmod a+x /usr/share/applications/ipe.desktop
```

# Secured login with Google Authenticator

## Install `libpam-google-authenticator` package

```bash
sudo apt install libpam-google-authenticator
```

## Create an Authentication Key

```bash
google-authenticator
```

Allow the command to update your Google Authenticator file by typing `y`. Google Authenticator will present you with a secret key and several ``emergency scratch codes.'', which will be used in case you lose your phone. Enter the secret key in the Google Authenticator app on your phone (official apps are available for Android, iOS, and Blackberry). You'll now have a constantly changing verification code on your phone.


## Activate authentication for SSH login

Edit the file `/etc/pam.d/sshd` by adding the following line.

```bash
auth required pam_google_authenticator.so
```

Next, open the `/etc/ssh/sshd_config` file, locate the `ChallengeResponseAuthentication` line, and change it to `ChallengeResponseAuthentication yes`.

Finally, restart the SSH service

```bash
sudo service ssh restart
```

## Activate authentication for graphical logins

Here's how to do this with LightDM login manager. Similar to the case of SSH login, edit the file `/etc/pam.d/lightdm` by adding the following line.

```bash
auth required pam_google_authenticator.so nullok
```

In this case, the `nullok` option allows the system to let a user log in even if they haven't run the google-authenticator command to set up two-factor authentication. If they have set it up, they'll have to enter a time-baesd code --- otherwise they won't. Remove the `nullok` and user accounts who haven't set up a Google Authenticator code just won't be able to log in graphically.

You could also force Google Authenticator to be required for other types of logins - potentially even all system logins - by adding the line `auth required pam_google_authenticator.so` to other PAM configuration files. Be careful if you do this. And remember, you may want to add `nullok` so users who haven't gone through the setup process can still log in.

# ClamAV

```bash
sudo apt install clamav clamtk
```

# purple-facebook plugin for Pidgin

```bash
sudo apt install autoconf automake libtool mercurial build-essential
sudo apt install libglib2.0-dev libjson-glib-dev libpurple-dev
git clone https://github.com/jgeboski/purple-facebook.git
cd purple-facebook
./autogen.sh
make
sudo make install
```

# TLP power manager

```bash
sudo add-apt-repository ppa:linrunner/tlp
sudo apt update
sudo apt install tlp tlp-rdw smartmontools ethtool
tlp start
```

# Systemback - Backup and Restore

```bash
echo "Installing Systemback - A backup and restore tool for Linux"
sudo add-apt-repository ppa:nemh/systemback 
sudo apt update
sudo apt install systemback
```

# Tor

```bash
echo "deb http://deb.torproject.org/torproject.org xenial main" | sudo tee -a /etc/apt/sources.list
gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
sudo apt update
sudo apt install deb.torproject.org-keyring tor
```

# Zotero Standalone

If you want to use the latest binary version, download it from the [Zotero's download page](https://www.zotero.org/download/). An alternative way is installing Zotero Standalone via PPA.

```bash
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt update
sudo apt install zotero-standalone
```

# Jekyll

## Installing Ruby 

### With Ruby Version Manager

First of all, install `curl`.

```bash
sudo apt-get install curl
```

Then install RVM

```bash
curl -sSL https://get.rvm.io | bash -s stable
```

You will get some output report like the followings. Here `username` is my username and `YOUR-PC` is my computer name.

```bash
username@YOUR-PC: $ curl -sSL https://get.rvm.io | bash -s stable
Downloading https://github.com/wayneeseguin/rvm/archive/stable.tar.gz

Installing RVM to /home/username/.rvm/
    Adding rvm PATH line to /home/username/.profile /home/username/.bashrc /home/username/.zshrc.
    Adding rvm loading line to /home/username/.bash_profile /home/username/.zlogin.
Installation of RVM in /home/username/.rvm/ is almost complete:

  * To start using RVM you need to run `source /home/username/.rvm/scripts/rvm`
    in all your open shell windows, in rare cases you need to reopen all shell windows.

# username,
#
#   Thank you for using RVM!
#   We sincerely hope that RVM helps to make your life easier and more enjoyable!!!
#
#  Wayne, Michal & team.

In case of problems: http://rvm.io/help and https://twitter.com/rvm_io 
```

To run RVM, you neend to use the command `source /home/username/.rvm/scripts/rvm`.

See [this page](https://www.ruby-lang.org/en/downloads/) for information about the latest Ruby version. At the time I wrote this guide, the latest version is `2.5.3`.

```bash
rvm requirements
rvm install 2.5.3
rvm use 2.5.3 --default
```

### With Rbenv

An alternative option is to install Ruby with `rbenv`. Note that `rbenv` and `rvm` may be conflicted, so it is recommended to install just one of them.

```bash
sudo apt install git zsh libssl-dev zlib1g-dev libreadline-dev libyaml-dev
cd
git clone https://github.com/rbenv/rbenv.git $HOME/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> $HOME/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL

git clone https://github.com/rbenv/ruby-build.git $HOME/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> $HOME/.bashrc
exec $SHELL

rbenv install 2.5.3
rbenv global 2.5.3
rbenv rehash
```

## Install nodejs

```bash
sudo apt-get install nodejs
```

## Install Jekyll

Since I've already got my own `Gemfile` and `Gemfile.lock` files, I install Jekyll and all other dependencies using `bundler`.

```bash
gem install bundler
# Move to the folder that contains `Gemfile` and `Gemfile.lock`
bundle install
```

The content of my file `Gemfile`

```bash
source 'https://rubygems.org'

gem 'jekyll'
gem 'rouge'
gem 'kramdown'
gem 'rake'
gem 'jekyll-scholar'
gem 'pygments.rb'
gem 'jekyll-sitemap'
gem 'jekyll-feed'
gem 'jekyll-email-protect'
```

The content of my file `Gemfile.lock`

```bash
GEM
  remote: https://rubygems.org/
  specs:
    addressable (2.5.1)
      public_suffix ( > 2.0, >= 2.0.2)
    bibtex-ruby (4.4.3)
      latex-decode ( > 0.0)
    citeproc (1.0.5)
      namae ( > 0.8)
    citeproc-ruby (1.1.6)
      citeproc (>= 1.0.4, < 2.0)
      csl ( > 1.4)
    colorator (1.1.0)
    csl (1.4.5)
      namae ( > 0.7)
    csl-styles (1.0.1.7)
      csl ( > 1.0)
    ffi (1.9.18)
    ffi (1.9.18-x64-mingw32)
    ffi (1.9.18-x86-mingw32)
    forwardable-extended (2.6.0)
    jekyll (3.4.3)
      addressable ( > 2.4)
      colorator ( > 1.0)
      jekyll-sass-converter ( > 1.0)
      jekyll-watch ( > 1.1)
      kramdown ( > 1.3)
      liquid ( > 3.0)
      mercenary ( > 0.3.3)
      pathutil ( > 0.9)
      rouge ( > 1.7)
      safe_yaml ( > 1.0)
    jekyll-email-protect (1.0.3)
    jekyll-feed (0.9.2)
      jekyll ( > 3.3)
    jekyll-sass-converter (1.5.0)
      sass ( > 3.4)
    jekyll-scholar (5.9.1)
      bibtex-ruby ( > 4.0, >= 4.0.13)
      citeproc-ruby ( > 1.0)
      csl-styles ( > 1.0)
      jekyll ( > 3.0)
    jekyll-sitemap (1.1.1)
      jekyll ( > 3.3)
    jekyll-watch (1.5.0)
      listen ( > 3.0, < 3.1)
    kramdown (1.13.2)
    latex-decode (0.2.2)
      unicode ( > 0.4)
    liquid (3.0.6)
    listen (3.0.8)
      rb-fsevent ( > 0.9, >= 0.9.4)
      rb-inotify ( > 0.9, >= 0.9.7)
    mercenary (0.3.6)
    multi_json (1.12.1)
    namae (0.11.3)
    pathutil (0.14.0)
      forwardable-extended ( > 2.6)
    public_suffix (2.0.5)
    pygments.rb (1.1.2)
      multi_json (>= 1.0.0)
    rake (12.0.0)
    rb-fsevent (0.9.8)
    rb-inotify (0.9.8)
      ffi (>= 0.5.0)
    rouge (1.11.1)
    safe_yaml (1.0.4)
    sass (3.4.23)
    unicode (0.4.4.4)
    unicode (0.4.4.4-x86-mingw32)

PLATFORMS
  ruby
  x64-mingw32
  x86-mingw32

DEPENDENCIES
  jekyll
  jekyll-email-protect
  jekyll-feed
  jekyll-scholar
  jekyll-sitemap
  kramdown
  pygments.rb
  rake
  rouge

BUNDLED WITH
   1.14.6
```

# Ubuntu Tweak

Ubuntu Tweak - a tool for Ubuntu that makes it easy to configure your system and desktop settings - can be installed from the [GetDeb repository](http://www.getdeb.net) as follows.

```bash
wget http://archive.getdeb.net/install_deb/getdeb-repository_0.1-1 getdeb1_all.deb
sudo dpkg -i getdeb-repository_0.1-1 getdeb1_all.deb
sudo apt update
sudo apt install ubuntu-tweak
```

# VMWare Horizon Client in Ubuntu 16.04 LTS x64

To access [JAIST Cloud Desktop](https://www.jaist.ac.jp/iscenter/en/jaist-cloud/desktop/windows/) (Windows environment), one needs to install [VMware Horizon Clients](https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_horizon_clients/4_0). The following tutorial describes how to install VMware Horizon Clients in Ubuntu 16.04 64-bit.

## Download VMWare Horizon Client and Install

One can download VMware Horizon Clients for 64-bit Linux from [here](https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_horizon_clients/4_0). At the time of writing this tutorial, the downloaded file is `VMware-Horizon-Client-4.6.0-6617224.x64.bundle`.

```bash
chmod +x VMware-Horizon-Client-4.6.0-6617224.x64.bundle
sudo ./VMware-Horizon-Client-4.6.0-6617224.x64.bundle
```

## Some errors after install VMWare Horizon Client

### Missing `libffi.so.5`

```bash
sudo ln -s /usr/lib/x86_64-linux-gnu/libffi.so.6 /usr/lib/x86_64-linux-gnu/libffi.so.5
```

### Cannot share folder
 
The original solution is available [here](https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/4.5/com.vmware.horizon-client.linux-45.doc/GUID-CFB7E9B1-63E0-418A-8814-572296507783.html). The reason of this error is that, on Ubuntu 16.04 x64 distributions, the `libglibmm-2.4.so.1.3.0` library included in the distribution is incompatible with the current Client Drive Redirection (CDR) implementation. To work around this limitation, copy the `libglibmm-2.4.so.1.3.0` library file from an Ubuntu 14.04 x64 distribution (which can be downloaded from [here](https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/4.5/com.vmware.horizon-client.linux-45.doc/GUID-CFB7E9B1-63E0-418A-8814-572296507783.html)) to your Ubuntu 16.04 x64 distribution.

# pdf2htmlEX

## Poppler 0.43.0

```bash
sudo apt-get install -qq -y cmake gcc libgetopt++-dev git pkg-config libopenjpeg-dev libfontconfig1-dev libfontforge-dev poppler-data poppler-utils poppler-dbg
wget https://poppler.freedesktop.org/poppler-0.43.0.tar.xz
tar -xvf poppler-0.43.0.tar.xz
cd poppler-0.43.0/
./configure --enable-xpdf-headers
make
sudo make install
```

## Fonforge

```bash
sudo apt-get install -qq -y packaging-dev pkg-config python-dev libpango1.0-dev libglib2.0-dev libxml2-dev giflib-dbg libjpeg-dev libtiff-dev uthash-dev libspiro-dev
git clone --depth 1 https://github.com/coolwanglu/fontforge.git
cd fontforge/
./bootstrap
./configure
make
sudo make install
```

## pdf2htmlEX

```bash
git clone --depth 1 https://github.com/coolwanglu/pdf2htmlEX.git
cd pdf2htmlEX/
cmake .
make
sudo make install
```
