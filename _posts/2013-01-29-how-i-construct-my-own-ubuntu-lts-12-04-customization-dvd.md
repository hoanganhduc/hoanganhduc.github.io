---
layout: blog-post
title: How I construct my own Ubuntu LTS 12.04 Customization DVD
author: Duc A. Hoang
categories:
  - "linux"
<!--comment: true-->
last_modified_at: 2020-10-05
description: This post describes how Duc A. Hoang constructs his own Ubuntu LTS 12.04 Customization DVD
keywords: ubuntu, customization dvd
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post aims to record what I did to construct my own Ubuntu LTS 12.04 Customization DVD. You can still find the old configuration files at [Google Code Archive](https://code.google.com/archive/p/ubuntu-precise-customization/), and the whole repository can be downloaded [here](https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/ubuntu-precise-customization/source-archive.zip). 
Even though the [original instruction](http://toihoctap.wordpress.com/2013/01/29/how-i-construct-my-own-ubuntu-lts-12-04-customization-dvd/) was deleted, you can still access [a saved copy at the Internet Archive](https://web.archive.org/web/20130804073659/http://toihoctap.wordpress.com/2013/01/29/how-i-construct-my-own-ubuntu-lts-12-04-customization-dvd/).
</div>

# Prepare for configuring system

The system configurations were processed in Ubuntu Linux. For convenience, you should execute sudo without typing password. In order to do that, in terminal, type

```bash
sudo visudo
```
and add the following line to the end of the file

```bash
[username] ALL=(ALL) NOPASSWD: ALL
```
where `[username]` is your username. The configuration required at least 15 - 20 GB of free disk space. The following packages are also needed

```bash
sudo apt-get install grub2 xorriso squashfs-tools debootstrap qemu subversion rar unrar zip unzip p7zip-full p7zip-rar
```
A good internet connection is highly recommended.

# Create working directory

```bash
export WORK=~/work CD=~/cd FORMAT=squashfs FS_DIR=casper
sudo mkdir -p ${CD}/{${FS_DIR},boot/grub} ${WORK}/rootfs
sudo debootstrap precise ${WORK}/rootfs
```

# Download required files to `${WORK}/rootfs/`

* {% include files.html name="apt.zip" text="apt.zip" %}: Contents of `/etc/apt`
* {% include files.html name="wink15_b1060.tar.gz" text="wink15_b1060.tar.gz" %}: Wink
* {% include files.html name="deb_links" text="deb_links" %}: List of links
* {% include files.html name="default.zip" text="default.zip" %}: Mplayer Default Theme
* {% include files.html name="installed-software" text="installed-software" %}: Install packages 
* {% include files.html name="DMZ-icons.zip" text="DMZ-icons.zip" %}: DMZ-icons
* {% include files.html name="backgrounds.zip" text="backgrounds.zip" %}: Background Pictures
* {% include files.html name="add.firefox.extension.sh" text="add.firefox.extension.sh" %}: Add firefox extension
* {% include files.html name="59794-Original.tar.gz" text="59794-Original.tar.gz" %}: Pidgin Yahoo Emoticon

# Build my own custom system

## Prepare the new system before chrooting it

```bash
sudo unzip ${WORK}/rootfs/apt.zip -d ${WORK}/rootfs/etc
```

Answer `A` (which means overwrite all) for the question. Next, in terminal, type

```bash
for i in /etc/resolv.conf /etc/hosts /etc/hostname; do sudo cp -pv $i ${WORK}/rootfs/etc/; done
sudo mount --bind /dev ${WORK}/rootfs/dev
sudo mount -t proc proc ${WORK}/rootfs/proc
sudo mount -t sysfs sysfs ${WORK}/rootfs/sys
sudo chroot ${WORK}/rootfs /bin/bash
apt-get update --allow-unauthenticated
```

## Modify the new system

### Install some basic packages.

* Generic Linux Kernel

  ```bash
  apt-get install --yes wget linux-generic
  ```
If you were asked for installing `grub-pc`, continue without installing it.

* Other packages

  ```bash
  dpkg --get-selections < installed-software
  apt-get -y update
  apt-get dselect-upgrade
  ```

### GNOME desktop

```bash
apt-get install aptitude dselect xorg lightdm faenza-icon-theme ambiance-blue-theme \
indicator-applet-complete gnome-tweak-tool compiz-gnome dconf-tools gconf-defaults-service gconf-editor
```

To set GNOME as the default desktop, use the command

```bash
/usr/lib/lightdm/lightdm-set-defaults -s gnome
```

### Install packages for various archive formats

```bash
apt-get install unace unrar zip unzip p7zip-full p7zip-rar \
sharutils rar uudeview mpack lha arj cabextract file-roller
```

### Complie and install Mplayer

* Prepare...

  ```bash
  apt-get install build-essential subversion checkinstall yasm git-core docbook-xml \
  docbook-xsl xsltproc libxml2-utils libaa1-dev libasound2-dev libcaca-dev \
  libcdparanoia-dev libdca-dev \
  libdirectfb-dev libggi-target-fbdev libenca-dev libesd0-dev libfontconfig1-dev libfreetype6-dev \
  libfribidi-dev libgif-dev libreadline-gplv2-dev libgl1-mesa-dev libjack-jackd2-dev libopenal1 libpulse-dev \
  libsdl1.2-dev libsvga1-dev libvdpau-dev libxinerama-dev libxv-dev libxvmc-dev libxxf86dga-dev \
  libxxf86vm-dev librtmp-dev libsctp-dev libass-dev libfaac-dev libsmbclient-dev libtheora-dev \
  libogg-dev libxvidcore-dev libspeex-dev libvpx-dev libschroedinger-dev libdirac-dev libdv4-dev \
  libopencore-amrnb-dev libopencore-amrwb-dev libmp3lame-dev liblivemedia-dev libtwolame-dev \
  libmad0-dev libgsm1-dev libbs2b-dev liblzo2-dev ladspa-sdk libopenjpeg-dev libfaad-dev 
  ```
  
  ```bash
  apt-get build-dep mplayer
  ```

* Codecs

  ```bash
  mkdir mplayer_build && cd /mplayer_build && \
  mkdir -pv /usr/local/lib/codecs && \
  if [ "$(uname -m)" = "x86_64" ]; then
   wget http://www.mplayerhq.hu/MPlayer/releases/codecs/essential-amd64-20071007.tar.bz2
   tar xjvf essential-amd64-20071007.tar.bz2
   cp -v essential-amd64-20071007/* /usr/local/lib/codecs
  else
   wget http://www.mplayerhq.hu/MPlayer/releases/codecs/all-20110131.tar.bz2
   tar xjvf all-20110131.tar.bz2
   cp -v all-20110131/* /usr/local/lib/codecs
  fi
  ```

* x264...

  ```bash
  if [ "$(uname -m)" = "x86_64" ]; then
    ARCHOPTS="--enable-pic"
   else
    ARCHOPTS=""
  fi && \
  cd /mplayer_build && \
  git clone git://git.videolan.org/x264.git --depth 1 && \
  cd x264 && \
  ./configure --prefix=/mplayer_build/mplayer_deps/usr \
              --enable-static --disable-cli $ARCHOPTS && \
  make && make install
  ```

* Bluray Playback...

  For libbluray 
  ```bash  
  cd /mplayer_build && \
  wget ftp://ftp.videolan.org/pub/videolan/libbluray/0.2.2/libbluray-0.2.2.tar.bz2 && \
  tar xjvf libbluray-0.2.2.tar.bz2 && cd libbluray-0.2.2 && \
  ./configure && make && \
  checkinstall --pakdir "/mplayer_build" --backup=no --deldoc=yes \
		            --pkgname libbluray --pkgversion "2:0.2.2" --fstrans=no \
		            --deldesc=yes --delspec=yes --default && \
  make distclean
  ```

  For libaacs
  ```bash
  cd /mplayer_build && \
  apt-get -y install libgcrypt11-dev bison flex && \
  wget ftp://ftp.videolan.org/pub/videolan/libaacs/0.4.0/libaacs-0.4.0.tar.bz2 && \
  tar xjvf libaacs-0.4.0.tar.bz2 && cd libaacs-0.4.0 && \
  ./configure && make && \
  checkinstall --pakdir "/mplayer_build" --backup=no --deldoc=yes \
	                --pkgname libaacs --pkgversion "2:0.4.0" --fstrans=no \
	                --deldesc=yes --delspec=yes --default && \
  make distclean
  ```

* Installing mpg123...

  ```bash
  apt-get -y remove mpg123 libmpg123-dev && \
  cd /mplayer_build && mkdir mpg123 && \
  cd mpg123 && \
  wget http://www.mpg123.de/download/mpg123-1.14.4.tar.bz2 && \
  tar xjvf mpg123-1.14.4.tar.bz2 && cd mpg123-1.14.4 && \
  ./configure && make && \
  checkinstall --pakdir "/mplayer_build" --backup=no --deldoc=yes \
                    --pkgname mpg123 --pkgversion "1.14.4" --fstrans=no \
                    --deldesc=yes --delspec=yes --default && \
  make distclean
  ```

* Installing libopus...

  ```bash
  cd /mplayer_build && \
  wget http://downloads.xiph.org/releases/opus/opus-1.0.1-rc.tar.gz && \
  tar xvf opus-1.0.1-rc.tar.gz && cd opus-1.0.1-rc && \
  ./configure && make && \
  mkdir -vp doc-pak && \
  cp -v AUTHORS README doc-pak && \
   checkinstall -D --install=yes --fstrans=no --pakdir "/mplayer_build" \
     --pkgname libopus --backup=no --deldoc=yes --deldesc=yes --delspec=yes \
     --default --pkgversion "1.0.1"  && \
  make distclean && ldconfig
  ```

* Compiling MPlayer

  ```bash
  cd /mplayer_build && \
  svn checkout svn://svn.mplayerhq.hu/mplayer/trunk mplayer && \
  cd mplayer && \
  PKG_CONFIG_PATH="/mplayer_build/mplayer_deps/usr/lib/pkgconfig" \
  ./configure \
             --extra-cflags="-I/mplayer_build/mplayer_deps/usr/include" \
             --extra-ldflags="-L/mplayer_build/mplayer_deps/usr/lib" \
             --confdir=/etc/mplayer --enable-gui \
             --codecsdir=/usr/local/lib/codecs && \
  make -j 2 && make html-chunked && \
  mkdir -vp doc-pak && \
  cp -v DOCS/HTML/*/* AUTHORS Changelog LICENSE README doc-pak && \
  checkinstall -D --install=yes --fstrans=no --pakdir "/mplayer_build" \
     --pkgname mplayer --backup=no --deldoc=yes --deldesc=yes --delspec=yes --default \
     --pkgversion "2:1.0~svn$(LC_ALL=C svn info 2> /dev/null | \
       grep Revision | cut -d' ' -f2)" --provides "mplayer,mencoder" && \
  make distclean && ldconfig
  ```

* Extract MPlayer theme

  ```bash
  unzip default.zip -d /usr/local/share/mplayer/skins
  ```

### Install office and media packages

```bash
apt-get install gedit gedit-plugins gedit-developer-plugins \
libreoffice-gnome libreoffice-pdfimport mozilla-libreoffice \
ubuntu-restricted-extras app-install-data-medibuntu apport-hooks-medibuntu evince \
non-free-codecs gxine mencoder flac faac faad sox libmpeg3-1 mpeg3-utils \
mpegdemux mpeg2dec mpg321 totem-mozilla tagtool easytag \
id3tool nautilus-script-audio-convert libjpeg-progs libdvdcss2 \
ibus-unikey scim-unikey ttf-abc-fonts ttf-bkunicode-fonts ttf-vni-fonts \
vlc mozilla-plugin-vlc audacity gimp \
pidgin pidgin-data \
skype bleachbit nuvolaplayer avidemux lives gtkpod sopcast-player \
gtk-recordmydesktop cheese
```

### Install language packages

```bash
apt-get install language-pack-vi-base language-pack-en-base
```

### Install some extra useful packages

```bash
apt-get install firefox nautilus-dropbox dropbox-share ubuntuone-client-gnome \
indicator-ubuntuone rhythmbox-ubuntuone goldendict artha fbreader \
galculator djview4 shotwell shutter wine1.4 tasksel
```

### Install packages for utilities and configurations

```bash
apt-get install synaptic y-ppa-manager gdebi \
ubuntu-tweak super-boot-manager preload \
network-manager network-manager-gnome network-manager-openvpn openvpn \
unetbootin grub2 xorriso isomaster squashfs-tools debootstrap dkms virtualbox-4.1 \
samba smbfs system-config-samba ssh subversion git git-core mercurial mercurial-common \
filezilla transmission-gtk transmission-common nitroshare openjdk-7-jre gnome-terminal \
nautilus-open-terminal xfig gnome-power-manager hibernate remastersys \
python-dev python-mysqldb python-setuptools python-pip python-matplotlib libnetpbm10 libnetpbm10-dev
```

### Install games

```bash
apt-get install gnugo uligo qgo gmchess 
```

### Install Fonts

* Ubuntu Fonts Family

  ```bash
  wget http://launchpadlibrarian.net/98992843/ttf-ubuntu-font-family_0.80-0ubuntu2_all.deb
  dpkg -i ttf-ubuntu-font-family_0.80-0ubuntu2_all.deb
  rm ttf-ubuntu-font-family_0.80-0ubuntu2_all.deb
  ```

* Other Fonts

  ```bash
  apt-get install fonts-cantarell lmodern ttf-aenigma ttf-georgewilliams \
  ttf-bitstream-vera ttf-sjfonts ttf-tuffy tv-fonts \
  ttf-dustin ttf-larabie-deco ttf-larabie-straight ttf-larabie-uncommon \
  ttf-droid ttf-inconsolata xfonts-terminus console-terminus gsfonts-x11
  ```

### Install packages for using in emergency situations

```bash
apt-get install boot-repair os-uninstaller gparted testdisk wipe \
partimage xfsprogs reiserfsprogs jfsutils ntfs-3g ntfsprogs dosfstools mtools winusb
```

### Install some deb packages: Google Video and Voice Chat Plugin for Ubuntu, Foxit Reader, Google Chrome, Teamviewer, mail.ru agent for pidgin, Foobnix, Livestation, XvidCap

```bash
wget -i deb_links
dpkg -i google-talkplugin_current_i386.deb FoxitReader_1.1.0_i386.deb google-chrome-stable_current_i386.deb \
teamviewer_linux.deb mrim-prpl_0.1.28-2_i386.deb foobnix_2.5.36p_i386.deb xvidcap_1.1.7-0.2ubuntu12_i386.deb
rm google-talkplugin_current_i386.deb FoxitReader_1.1.0_i386.deb google-chrome-stable_current_i386.deb \
teamviewer_linux.deb mrim-prpl_0.1.28-2_i386.deb foobnix_2.5.36p_i386.deb xvidcap_1.1.7-0.2ubuntu12_i386.deb
```

### Install Winetricks

```bash
wget http://winetricks.org/winetricks
chmod +x winetricks
mv winetricks /usr/local/bin
```

### Install TeX Live 2012

* Download the ISO file `texlive2012-20120701.iso` from [http://ftp.ctex.org/mirrors/CTAN/systems/texlive/Images/](http://ftp.ctex.org/mirrors/CTAN/systems/texlive/Images/) and put it in your host system `$HOME` folder.

* Open a new terminal, and type

  ```bash
  export WORK=~/work
  sudo mount -o loop $HOME/texlive2012-20120701.iso ${WORK}/rootfs/mnt
  ```

* In the chroot terminal, i.e. the first terminal window that we opened from beginning

  ```bash
  cd mnt
  ./install-tl
  ```
Respectively type `O` and `L`. After configuring the symbolic links, type respectively `R` and `I`.

* After the install process finished, some informations will appear in the chroot terminal

  ```bash
  Add /usr/local/texlive/2012/texmf/doc/man to MANPATH, if not dynamically determined.
   Add /usr/local/texlive/2012/texmf/doc/info to INFOPATH.
  
   Most importantly, add /usr/local/texlive/2012/bin/i386-linux
   to your PATH for current and future sessions.

   Welcome to TeX Live!
  Logfile: /usr/local/texlive/2012/install-tl.log
  ```

* Now, open the file `bash.bashrc`

  ```bash
  nano /etc/bash.bashrc
  ```

  Then add following in the end

  ```bash
  PATH=/usr/local/texlive/2012/bin/i386-linux:$PATH; export PATH
  MANPATH=/usr/local/texlive/2012/texmf/doc/man:$MANPATH; export MANPATH
  INFOPATH=/usr/local/texlive/2012/texmf/doc/info:$INFOPATH; export INFOPATH
  ```

* Open the file `manpath.config`

  ```bash
  nano /etc/manpath.config
  ```

  Under `# set up PATH to MANPATH mapping`, add the line

  ```bash
  MANPATH_MAP /usr/local/texlive/2012/bin/i386-linux /usr/local/texlive/2012/texmf/doc/man
  ```

* Install and use getnonfreefonts script

  ```bash
  wget http://tug.org/fonts/getnonfreefonts/install-getnonfreefonts
  texlua install-getnonfreefonts
  cd /usr/local/bin
  ln -s /usr/local/texlive/2012/bin/i386-linux/getnonfreefonts
  ln -s /usr/local/texlive/2012/bin/i386-linux/getnonfreefonts-sys
  getnonfreefonts-sys -a
  cd /
  ```

* Finally, in the new opened terminal, type

  ```bash
  sudo umount ${WORK}/rootfs/mnt
  exit
  ```

### Install Texmaker

```bash
wget http://www.xm1math.net/texmaker/texmaker_ubuntu_12.04_3.5_i386.deb
apt-get install libpoppler-qt4-3
dpkg -i texmaker_ubuntu_12.04_3.5_i386.deb
rm texmaker_ubuntu_12.04_3.5_i386.deb
```

### Install Customizer

```bash
wget https://github.com/downloads/fluxer/Customizer/install.sh
chmod a+x install.sh
./install.sh -i
rm install.sh
```

### Install Sphinx

```bash
easy_install -U Sphinx
```

### Install Oxford Advanced Learner’s Dictionary 8th edition

* Put file `OALD8.iso` (ISO image of the CD dictionary) in `$HOME` folder, just like the `texlive2012-20120701.iso` before.

* Open a new terminal, type

  ```bash
  export WORK=~/work
  sudo mount -o loop $HOME/OALD8.iso ${WORK}/rootfs/mnt
  ```

* In the chroot terminal, type

  ```bash
  apt-get install flashplugin-installer
  mkdir /usr/local/OALD8
  export HOME=/usr/local/OALD8
  cd /mnt/linux
  ./setup.sh
  ```
and setup OALD8 to the folder `/usr/local/OALD8`. Next, open `oald8.desktop`

  ```bash
  nano $HOME/Desktop/oald8.desktop
  ```

  and replace the content of the file with

  ```bash
  [Desktop Entry]
  Comment=oald8
  Encoding=UTF-8
  Exec=padsp '/usr/local/OALD8//oald8'
  GenericName=
  GenericName[en]=
  Icon=/usr/local/OALD8//splash.xpm
  Name=OALD8
  Terminal=false
  Type=Application
  Categories=Office;Dictionary;Education
  ```

  then save the file and exit. Next, in the chroot terminal, type

  ```bash
  chmod +x $HOME/Desktop/oald8.desktop
  mv $HOME/Desktop/oald8.desktop /usr/share/applications
  rm -R $HOME/Desktop
  cd /
  ```

  Finally, in the new opened terminal, type
  ```bash
  sudo umount ${WORK}/rootfs/mnt
  exit
  ```

### Install Wink

* Install files

  ```bash
  mkdir /usr/local/wink
  mv wink15_b1060.tar.gz /usr/local/wink
  cd /usr/local/wink
  tar -zxvf wink15_b1060.tar.gz
  ln -s  /lib/i386-linux-gnu/libexpat.so.1  /lib/i386-linux-gnu/libexpat.so.0
  ./installer.sh
  tar -zxvf installdata.tar.gz
  ldd wink
  chmod +x wink
  cp wink /usr/bin
  wget http://www.debugmode.com/wink/winklogo.gif
  ```

* Create `wink.desktop` file

  ```bash
  nano /usr/share/applications/wink.desktop
  ```

  with the contents

  ```bash
  [Desktop Entry]
  Comment=wink
  Encoding=UTF-8
  Exec='/usr/local/wink/wink'
  GenericName=
  GenericName[en]=
  Icon=/usr/local/wink/winklogo.gif
  Name=Wink
  Terminal=false
  Type=Application
  Categories=AudioVideo;Player;Recorder
  ```

* Remove unnecessary files

  ```bash
  rm installer.sh installdata.tar.gz wink15_b1060.tar.gz 
  cd /
  ```

### Install Packages Essential for live CD

```bash
apt-get install casper lupin-casper ubiquity ubiquity-frontend-gtk
```

### Some Extra Configurations

* Yahoo Emoticon for Pidgin

  ```bash
  tar -xvvzf  59794-Original.tar.gz -C /usr/share/pixmaps/pidgin/emotes
  ```

* Metacity theme

  ```bash
  gconftool-2 -s --type string /apps/metacity/general/theme "Ambiance Blue"
  ```

* Desktop background and theme

  Unzip `backgrounds.zip`

  ```bash
  unzip backgrounds.zip -d /usr/share/backgrounds
  ```

  Edit `10_gsettings-desktop-schemas.gschema.override`

  ```bash
  nano /usr/share/glib-2.0/schemas/10_gsettings-desktop-schemas.gschema.override
  ```

  by replacing the contents of the file with

  ```bash
  [org.gnome.desktop.background]
  show-desktop-icons=true
  picture-uri='file:///usr/share/backgrounds/Lightning/Lightning.xml'

  [org.gnome.desktop.interface]
  menus-have-icons=true
  buttons-have-icons=true
  icon-theme='Faenza-Ambiance'
  gtk-theme='Ambiance Blue'
  cursor-theme='DMZ-White'
  font-name='Ubuntu 11'
  monospace-font-name='Ubuntu Mono 13'

  [org.gnome.desktop.wm.preferences]
  theme='Ambiance Blue'

  [org.gnome.desktop.GDesktopClockFormat]
  clock-show-seconds=true
  clock-show-date=true

  [org.gnome.desktop.wm.keybindings]
  minimize = ['<Primary><Alt>KP_0']
  move-to-corner-ne = ['<Primary><Alt>KP_Prior']
  move-to-corner-nw = ['<Primary><Alt>KP_Home']
  move-to-corner-se = ['<Primary><Alt>KP_Next']
  move-to-corner-sw = ['<Primary><Alt>KP_End']
  move-to-side-e = ['<Primary><Alt>KP_Right']
  move-to-side-n = ['<Primary><Alt>KP_Up']
  move-to-side-s = ['<Primary><Alt>KP_Down']
  move-to-side-w = ['<Primary><Alt>KP_Left']
  toggle-maximized = ['<Super>Up','<Primary><Super>Up','<Primary><Alt>KP_5']
  toggle-shaded = ['<Primary><Alt>s']
  unmaximize = ['<Super>Down','<Alt>F5','<Primary><Super>Down']
  show-desktop = ['<Primary><Alt>d','<Primary><Super>d','<Super>d']
  ```

  Change gnome-shell favourite by replacing the content of `10_gnome-shell.gschema.override`

  ```bash
  nano /usr/share/glib-2.0/schemas/10_gnome-shell.gschema.override
  ```

  with the following

  ```bash
  [org.gnome.shell]
  favorite-apps=[ 'firefox.desktop', 'pidgin.desktop', 'gnome-terminal.desktop', 'texmaker.desktop', 'teamviewer.desktop', 'filezilla.desktop', 'nautilus.desktop', 'yelp.desktop', 'gparted.desktop', 'boot-repair.desktop', 'os-uninstaller.desktop' ]

  [org.gnome.shell.clock]
  show-seconds=true
  show-date=true

  [org.gnome.shell.overrides]
  button-layout="menu:minimize,maximize,close"
  ```

  Finally, type

  ```bash
  glib-compile-schemas /usr/share/glib-2.0/schemas
  ```

* Install firefox addons

  ```bash
  chmod +x add.firefox.extension.sh
  ./add.firefox.extension.sh [name_of_extension].xpi
  ```

* Lightdm

  Edit the file `lightdm.conf`

  ```bash
  nano /etc/lightdm/lightdm.conf
  ```
  by replacing its contents with

  ```bash
  [SeatDefaults]
  user-session=gnome
  greeter-session=unity-greeter
  greeter-show-manual-login=true
  ```

### Finish configuring system
In chroot terminal

```bash
export kversion=`cd /boot && ls -1 vmlinuz-* | tail -1 | sed 's@vmlinuz-@@'`
depmod -a $kversion
update-initramfs -u -k $kversion
apt-get clean
apt-get --purge autoremove
aptitude purge ?config-files
rm wink15_b1060.tar.gz deb_links default.zip installed-software \
DMZ-icons.zip backgrounds.zip add.firefox.extension.sh 59794-Original.tar.gz
rm /etc/resolv.conf /etc/hostname
exit
```

## Prepare The CD directory tree

* Copy the kernel, the updated initrd and memtest prepared in the chroot

  ```bash
  export kversion=`cd ${WORK}/rootfs/boot && ls -1 vmlinuz-* | tail -1 | sed 's@vmlinuz-@@'`
  sudo cp -vp ${WORK}/rootfs/boot/vmlinuz-${kversion} ${CD}/${FS_DIR}/vmlinuz
  sudo cp -vp ${WORK}/rootfs/boot/initrd.img-${kversion} ${CD}/${FS_DIR}/initrd.img
  sudo cp -vp ${WORK}/rootfs/boot/memtest86+.bin ${CD}/boot
  ```

* Generate manifest

  ```bash
  sudo chroot ${WORK}/rootfs dpkg-query -W --showformat='${Package} ${Version}\n' | sudo tee ${CD}/${FS_DIR}/filesystem.manifest
  sudo cp -v ${CD}/${FS_DIR}/filesystem.manifest{,-desktop}
  REMOVE='ubiquity casper user-setup os-prober libdebian-installer4'
  for i in $REMOVE 
  do
          sudo sed -i "/${i}/d" ${CD}/${FS_DIR}/filesystem.manifest-desktop
  done
  ```

* Unmount bind mounted dirs

  ```bash
  sudo umount ${WORK}/rootfs/proc
  sudo umount ${WORK}/rootfs/sys
  sudo umount ${WORK}/rootfs/dev
  ```

* Convert the directory tree into a squashfs

  ```bash
  sudo mksquashfs ${WORK}/rootfs ${CD}/${FS_DIR}/filesystem.${FORMAT} -noappend
  ```

* Make `filesystem.size`

  ```bash
  echo -n $(sudo du -s --block-size=1 ${WORK}/rootfs | tail -1 | awk '{print $1}') | sudo tee ${CD}/${FS_DIR}/filesystem.size
  ```

* Calculate MD5

  ```bash
  find ${CD} -type f -print0 | xargs -0 md5sum | sed "s@${CD}@.@" | grep -v md5sum.txt | sudo tee -a ${CD}/md5sum.txt
  ```

* Make Grub the bootloader of the CD

  Make the `grub.cfg`

  ```bash
  nano ${CD}/boot/grub/grub.cfg
  ```

  with the following contents

  ```bash
  set default="0"
  set timeout=10

  menuentry "Ubuntu GUI" {
  linux /casper/vmlinuz boot=casper quiet splash
  initrd /casper/initrd.img
  }


  menuentry "Ubuntu in safe mode" {
  linux /casper/vmlinuz boot=casper xforcevesa quiet splash
  initrd /casper/initrd.img
  }


  menuentry "Ubuntu CLI" {
  linux /casper/vmlinuz boot=casper textonly quiet splash
  initrd /casper/initrd.img
  }


  menuentry "Ubuntu GUI persistent mode" {
  linux /casper/vmlinuz boot=casper persistent quiet splash
  initrd /casper/initrd.img
  }


  menuentry "Ubuntu GUI from RAM" {
  linux /casper/vmlinuz boot=casper toram quiet splash
  initrd /casper/initrd.img
  }

  menuentry "Check Disk for Defects" {
  linux /casper/vmlinuz boot=casper integrity-check quiet splash
  initrd /casper/initrd.img
  }


  menuentry "Memory Test" {
  linux16 /boot/memtest86+.bin  
  }


  menuentry "Boot from the first hard disk" {
  set root=(hd0)
  chainloader +1  
  }

  ```

## Build the CD/DVD

```bash
sudo grub-mkrescue -o ~/live-cd.iso ${CD}
```

## Clean the workspace

```bash
[ -d "$WORK" ] && sudo rm -r $WORK $CD
```

# References

* [Make a live CD/DVD/Bootable flash from your harddisk installation](https://ubuntuforums.org/showthread.php?t=688872).
* [LiveCDCustomizationFromScratch](https://help.ubuntu.com/community/LiveCDCustomizationFromScratch).
* [AskUbuntu – How to customize live Ubuntu CD?](https://askubuntu.com/questions/48535/how-to-customize-the-ubuntu-live-cd).
* [Things to do after installing Ubuntu 12.04 Precise Pangolin](https://howtoubuntu.org/things-to-do-after-installing-ubuntu-12-04-precise-pangolin/).
* [To Do List After installing Ubuntu 12.04.1 LTS aka Precise Pangolin](https://debianhelp.wordpress.com/2012/03/09/to-do-list-after-installing-ubuntu-12-04-lts-aka-precise-pangolin/).
* [Things to do after Installing Ubuntu 12.04 for perfect desktop](https://smashingweb.info/things-to-do-after-installing-ubuntu-12-04-for-perfect-desktop/).
* [Ubuntu:Precise](http://ubuntuguide.org/wiki/Ubuntu:Precise).
* [How to install firefox extensions for all users](https://ubuntuforums.org/showthread.php?t=1485995&page=2&p=10372816#post10372816).
* [LiveCDCustomization](https://help.ubuntu.com/community/LiveCDCustomization).
* [Howto: Build the svn MPlayer under the latest release version of Ubuntu](http://www.andrews-corner.org/mplayer.html).
* [Ubuntu: Sửa lỗi không phát âm được trên Oxford Advanced Learner’s Dictionary 8th](http://blog.sangnd.info/2012/08/ubuntu-sua-loi-khong-phat-am-duoc-tren-oxford-advanced-learners-dictionary-8th.html).
