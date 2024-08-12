---
layout: blog-post
title: Arch Linux with UEFI boot and full disk encryption
author: Duc A. Hoang
lang: en
categories:
  - linux
<!--comment: true-->
last_modified_at: 2022-01-02
description: This post contains some notes when I install Arch Linux with UEFI boot and full disk encryption
keywords: arch linux, full disk encryption, uefi boot, installation, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes when I install Arch Linux with UEFI boot and full disk encryption. The following commands can be performed with a live Arch CD or USB booting UEFI.

* TOC
{:toc}
</div>

# Partitions

## Create and format

For UEFI boot, I use [GUID Partition Table (GPT)](https://en.wikipedia.org/wiki/GUID_Partition_Table) with the following partitions (which I created using `cfdisk`).

| Partition   | Mount point | Size | Type      | Format | Purpose |
|:-----------:|:-----------:|:----:|:---------:|:------:|:-------:|
| `/dev/sda1` |             | 2M   | BIOS boot |        | required if [using GRUB](https://wiki.archlinux.org/index.php/GRUB#GUID_Partition_Table_(GPT)_specific_instructions) |
| `/dev/sda2` | `/boot/efi` | 300M | EFI System | FAT32<br>`mkfs.fat -F32 /dev/sda2` |  [EFI system partition](https://en.wikipedia.org/wiki/EFI_system_partition) |
| `/dev/sda3` | `/boot`     | 500M | Linux filesystem | EXT4<br>`mkfs.ext4 /dev/sda3` | [boot partition](https://en.wikipedia.org/wiki/System_partition_and_boot_partition) |
| `/dev/sda4` | `/` | Remaining space | Linux filesystem | [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) encryption<br>`cryptsetup luksFormat -v -s 512 -h sha512 /dev/sda4`<br>`cryptsetup open /dev/sda4 luks_root`<br>`mkfs.ext4 /dev/mapper/luks_root` | encrypted<br>root partition |  

## Mount to `/mnt`

```bash
mount /dev/mapper/luks_root /mnt
mkdir -p /mnt/boot && mount /dev/sda3 /mnt/boot
mkdir -p /mnt/boot/efi && mount /dev/sda2 /mnt/boot/efi
```

## Create 1GB swap in `/mnt`

```bash
cd /mnt
dd if=/dev/zero of=swap bs=1M count=1024 # create `swap` block file
mkswap swap # format `swap`
swapon swap # enable swap
chmod 600 swap # change permission
```

# Installation

See [this post]({% link _posts/2018-05-26-some-notes-on-installing-and-using-arch-linux.md %}). 
In particular, you need to be careful about the followings.

## Generate `fstab`

```bash
genfstab -t PARTUUID /mnt > /mnt/etc/fstab
```

## Modify `/etc/default/grub`

Modify the line containing `GRUB_CMDLINE_LINUX=` as follows.

```bash
GRUB_CMDLINE_LINUX="cryptdevice=PARTUUID=<partuuid of root partition /dev/sda4>:luks_root root=/dev/mapper/luks_root rw"
```
where `<partuuid of root partition /dev/sda4>` can be found by running `blkid /dev/sda4`.

## Modify `/etc/mininitcpio.conf`

Chroot into the system with `arch-chroot /mnt`.
Then, modify the line containing `HOOK=` in `/etc/mkinitcpio.conf` as follows.

```bash
HOOKS=(base udev block keyboard keymap autodetect modconf encrypt filesystems fsck)
```
And remeber to run `mkinitcpio -p linux` after saving the modification.

## Boot with GRUB

```bash
arch-chroot /mnt # if not done already
grub-install --target=x86_64-efi --boot-directory=/boot/efi --efi-directory=/boot/efi --bootloader-id="Arch Linux" /dev/sda # Keep all files, including configurations, in `/boot/efi`
grub-mkconfig -o /boot/efi/grub/grub.cfg
```

If you use the option `--removable` then GRUB will be installed to `/boot/efi/EFI/BOOT/BOOTX64.EFI` (or `/boot/efi/EFI/BOOT/BOOTIA32.EFI` for the `i386-efi` target) and you will have the additional ability of being able to boot from the drive in case EFI variables are reset or you move the drive to another computer. 

I also use GRUB to boot in BIOS mode.

```bash
arch-chroot /mnt # if not done already
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

## Boot with systemd-boot

See [this page](https://wiki.archlinux.org/index.php/systemd-boot) for more details. To install the EFI boot manager, run

```bash
arch-chroot /mnt # if not done already
bootctl --esp-path=/boot/efi --boot-path=/boot/efi install
```

Create `/boot/efi/loader/entries/arch.conf` with the following contents

```bash
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options cryptdevice=PARTUUID=<partuuid of root partition /dev/sda4>:luks_root root=/dev/mapper/luks_root rw
```
and modify `/boot/efi/loader/loader.conf` by adding

```bash
timeout 3
default arch
editor 0
```
## Secure boot with systemd-boot and PreLoader

See [this page](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface/Secure_Boot#PreLoader) for more details.


* Install [preloader-signed](https://aur.archlinux.org/packages/preloader-signed/).

  ```bash
  yay -S preloader-signed 
  ```

* Copy `PreLoader.efi` and `HashTool.efi` to the boot loader directory.

  ```bash
  sudo cp -vp /usr/share/preloader-signed/{PreLoader,HashTool}.efi /boot/efi/EFI/systemd
  ```

* Copy over the boot loader binary and rename it to `loader.efi`.

  ```bash
  sudo cp -vp /boot/efi/EFI/systemd/systemd-bootx64.efi /boot/efi/EFI/systemd/loader.efi 
  ```

* Create a new NVRAM entry to boot `PreLoader.efi`, note that `/dev/sda2` is the EFI system partition.

  ```bash
  sudo efibootmgr --verbose --disk /dev/sda --part 2 --create --label "PreLoader" --loader /EFI/systemd/PreLoader.efi 
  ```

If there are problems booting the custom NVRAM entry, copy `HashTool.efi` and `loader.efi` to the default loader location booted automatically by UEFI systems:

```bash
sudo cp -vp /usr/share/preloader-signed/HashTool.efi /boot/efi/EFI/Boot
sudo cp -vp /boot/efi/EFI/systemd/systemd-bootx64.efi /boot/efi/EFI/Boot/loader.efi
```
then copy over `PreLoader.efi` and rename it:

```bash
sudo cp -vp /usr/share/preloader-signed/PreLoader.efi /boot/efi/EFI/Boot/bootx64.efi
```

# Extra tips and tricks

## Live Linux System with systemd-boot

### Clonezilla Live

I use [Clonezilla](https://clonezilla.org/) to clone/restore my system.
The following commands run on my Arch Linux system as root. 
For more details, see also [this guide](https://clonezilla.org/livehd.php) and [this guide](https://wiki.archlinux.org/title/systemd-boot#Grml_on_ESP).

* Shrink `/dev/sda4` to create a EFI partition `/dev/sda5` for booting Clonezilla. Then, `mkfs.fat -F32 /dev/sda5` and `mount /dev/sda5 /mnt`.
* Install systemd-boot by running `bootctl --path=/mnt install`. If the secure boot is enable, install Preloader as in the previous section.
* [Download](https://clonezilla.org/downloads.php) Clonezilla `zip` version. I downloaded `clonezilla-live-20211116-impish-amd64.zip` (`alternative` release branch [Ubuntu-based], version `20211116-impish`, CPU architecture `amd64`). After downloading, run `unzip clonezilla-live-20211116-impish-amd64.zip -d /mnt` and then `mv /mnt/live /mnt/live-hd`, as described [here](https://clonezilla.org/livehd.php).
* Create `/mnt/loader/entries/clonezilla.conf` with the following content. Replace `<sda5-part-uuid>` with the PARTUUID of `/dev/sda5`, which can be obtained by running `blkid /dev/sda5`.
  ```
  title Clonezilla
  linux /live-hd/vmlinuz
  initrd /live-hd/initrd.img
  options boot=live union=overlay username=user config components quiet noswap nolocales edd=on nomodeset ocs_live_run=\"ocs-live-general\" ocs_live_extra_param=\"\" keyboard-layouts= ocs_live_batch=\"no\" locales= vga=788 ip=frommedia nosplash live-media-path=/live-hd bootfrom=/dev/disk/by-partuuid/<sda5-part-uuid> toram=live-hd,syslinux,EFI
  ```

### Rescuezilla ISO image

[Rescuezilla](https://rescuezilla.com/) is a *Clonezilla GUI* and more.

* As in the previous section, `mount /dev/sda5 /mnt` and then `mkdir -p /mnt/rescuezilla` for Rescuezilla ISO.
* Download the latest Rescuezilla ISO image from [this page](https://rescuezilla.com/download/). I downloaded `rescuezilla-2.3-64bit.impish.iso` and placed it at `/mnt/rescuezilla`. 
* Mount the ISO image. Copy the two files `vmlinuz` and `initrd.lz` from the directory `casper` to `/mnt/rescuezilla`. Umount the ISO image after copying.
* Create `/mnt/loader/entries/rescuezilla.conf` with the following content.
  ```
  title Rescuezilla (Graphical fallback mode)
  linux /rescuezilla/vmlinuz
  initrd /rescuezilla/initrd.lz
  options boot=casper noeject noprompt nolocales iso-scan/filename=/rescuezilla/rescuezilla-2.3-64bit.impish.iso xforcevesa nomodeset vga=788 fsck.mode=skip edd=on toram 
  ```

### SystemRescueCD ISO image

[SystemRescueCD](https://www.system-rescue.org/) contains tools for reparing your system after a crash.

* As in the previous section, `mount /dev/sda5 /mnt` and then `mkdir -p /mnt/srcd` for SystemRescue ISO.
* Download the latest SystemRescue ISO image from [this page](https://www.system-rescue.org/Download/). I downloaded `systemrescue-8.07-amd64.iso` and placed it at `/mnt/srcd`. 
* Mount the ISO image. Copy the two files `vmlinuz` and `sysresccd.img` from the directory `sysresccd/boot/x86_64` to `/mnt/srcd`. Umount the ISO image after copying.
* Create `/mnt/loader/entries/sysresccd.conf` with the following content. Replace `<sda5-part-uuid>` with the PARTUUID of `/dev/sda5`, which can be obtained by running `blkid /dev/sda5`. Replace `RESCUE807` with the appropriate label of the downloaded ISO image, as explained [here](https://www.system-rescue.org/manual/Booting_SystemRescueCd/).
  ```
  title SystemRescue Live Linux
  linux /srcd/vmlinuz
  initrd /srcd/sysresccd.img
  options archisolabel=RESCUE807 archisobasedir=sysresccd setkmap=us dostartx nomodeset img_dev=/dev/disk/by-partuuid/<sda5-part-uuid> img_loop=/srcd/systemrescue-8.07-amd64.iso copytoram
  ```
  For more boot options, see [this page](https://www.system-rescue.org/manual/Booting_SystemRescueCd/). See [this documentation](https://gitlab.archlinux.org/mkinitcpio/mkinitcpio-archiso/blob/master/docs/README.bootparams) for more advanced boot options.
  
### RedoRescue ISO image

Another Live Ubuntu-based CD for backup and recovery is [RedoRescue](http://redorescue.com/).

* As in the previous section, `mount /dev/sda5 /mnt` and then `mkdir -p /mnt/redo` for RedoRescue ISO.
* Download the latest RedoRescue ISO image from [this page](http://redorescue.com/#download). I downloaded `redorescue-4.0.0.iso` and placed it at `/mnt/redo`. 
* Mount the ISO image. Copy the two files `vmlinuz` and `initrd` to `/mnt/redo`. Umount the ISO image after copying.
* Create `/mnt/loader/entries/redo.conf` with the following content.
  ```
  title Redo Rescue
  linux /redo/vmlinuz
  initrd /redo/initrd
  options boot=live quiet splash noprompt nocomponents setkmap=us toram findiso=/redo/redorescue-4.0.0.iso
  ```
  For more boot options, see [this page](https://manpages.debian.org/jessie/live-boot-doc/live-boot.7.en.html).

## Increase/Decrease the size of LUKS encrypted partitions (no LVM)

### Increase

Assume that there is space on the disc available which is *not yet used by the encrypted LUKS volume*. 
The steps to increase the volume size (which were originally described [here](https://blog.tinned-software.net/increase-the-size-of-a-luks-encrypted-partition/)) are:

1. Increase the partition's size used by the encrypted volume.

   In this case, I want to resize `/dev/sda4`. This can be done using `gparted`.

2. Increase the size of the encrypted LUKS volume.

   ```bash
   cryptsetup open /dev/sda4 luks_root
   cryptsetup resize luks_root -v # increase the LUKS volume to fit the resized partition `/dev/sda4`   
   ```

3. Resizing the file-system of the volume

   ```bash
   e2fsck -f /dev/mapper/luks_root # check file-system
   resize2fs /dev/mapper/luks_root # resize file-system
   ```

**Note:** This situation may happen when using [Clonezilla](https://clonezilla.org/) to clone one LUKS encrypted partition to another partition having much larger size than the original one. 

### Decrease

Let say I want to decrease the size of the encrypted LUKS volume on `/dev/sda4`. (See [this page](https://unix.stackexchange.com/questions/41091/how-can-i-shrink-a-luks-partition-what-does-cryptsetup-resize-do) for more details.)

1. Decrease the size of the encrypted LUKS volume.
   
   ```bash
   cryptsetup open /dev/sda4 luks_root
   ```
   
   The command `cryptsetup resize /dev/mapper/luks_root -b <size in sectors>` can be used to decreases the size of the encrypted LUKS volume. To compute the value of `<size in sectors>`, we first need to know the size of `luks_root`, which can be obtained by running `cryptsetup status luks_root`, and look at the value of `size:`. As an example, here is the result of this command running on my current system
  
   ```bash
   /dev/mapper/luks_root is active and is in use.
   type:    LUKS2
   cipher:  aes-xts-plain64
   keysize: 512 bits
   key location: keyring
   device:  /dev/sda4
   sector size:  512
   offset:  32768 sectors
   size:    121602048 sectors
   mode:    read/write
   ```
  
   and the size of `luks_root` is `121602048 sectors` (since the sector size is `512 bytes`, this is equivalent to `121602048 * 512 = 62260248576 bytes = 57.98 GiB`). Thus, to subtract `1 GiB`, the value of `<size in sectors>` should be `121602048 - 1 * 1024 * 1024 * 2 = 119504896`. 
   In short, run
  
   ```bash
   cryptsetup resize /dev/mapper/luks_root -b 119504896
   ```
  
   Then, we can 
  
   ```bash
   e2fsck -f /dev/mapper/luks_root # check file-system
   resize2fs /dev/mapper/luks_root # resize file-system
   ```
   
   and then `cryptsetup close luks_root`.
   
2. Resize `/dev/sda4` (be careful, do not make its size smaller than the size of the encrypted volume), which can be done using `cfdisk`.

## Automount encrypted partitions on system start

### LUKS encrypted non-root partitions

Assume that I have a LUKS encrypted partition `/dev/sda5` which I want to mount automatically on system start. The steps I will perform are as follows. (See the original guide [here](https://blog.tinned-software.net/automount-a-luks-encrypted-volume-on-system-start/).) All commands are run as `root`.

1. (Optional) Create a key to unlock the volume.
   
   LUKS encryption supports multiple keys. These keys can be passwords entered interactively or key files passed as an argument while unlocking the encrypted partition. The following command will generate a file with 4 KB of random data to be used as a key to unlock the encrypted volume.
   
   ```bash
   dd if=/dev/urandom of=/etc/luks-keys/disk_secret_key bs=512 count=8
   ```
   
   With the following commands the created key file is saved in `/etc/luks-keys` and added as a key to the LUKS encrypted volume. 
   
   ```bash
   mkdir -p /etc/luks-keys && cryptsetup -v luksAddKey /dev/sda5 /etc/luks-keys/disk_secret_key
   ```
   
   You can save your secret key in any place, instead of `/etc/luks-keys`.
   To verify that the key is working, the following command can be executed manually.
   
   ```bash
   cryptsetup -v open /dev/sda5 luks_part --key-file=/etc/luks-keys/disk_secret_key
   ```
2. Automatically open the encrypted volume. 

   This can be done by adding to `/etc/crypttab` the following line
   
   ```bash
   luks_part /dev/disk/by-partuuid/<partuuid of /dev/sda5> /etc/luks-keys/disk_secret_key luks 
   ```
   where `<partuuid of /dev/sda5>` can be found by running `blkid /dev/sda5`.
   In case you do not want to use keys, replace `/etc/luks-keys/disk_secret_key` by `none`, and you will then have to manually enter the passphrase to unlock the LUKS volume.
   
   Finally, to automatically mount the volume, say, to `/data`, on system start, add the following line to `/etc/fstab`. (Assuming that the volume is `ext4` formatted).
   
   ```bash
   /dev/mapper/luks_part /data ext4 nofail 0 2
   ```

### VeraCrypt encrypted files

Let say I have a [VeraCrypt](https://www.veracrypt.fr/code/VeraCrypt/) encrypted file `/secret.hc`, formatting as `ext4`, and unlocking it requires a passphrase and a key file `/key.file`. To unlock `/secret.hc`, run the following command as `root`.

```bash
cryptsetup -v open /secret.hc --type tcrypt --veracrypt --key-file /key.file veracrypt
```

The command will output `Command successful` after you enter the correct passphrase after the line `Enter passphrase for /secret.hc:`, and you will see that `/dev/mapper/veracrypt` is available.

As above, in order to automatically open `/secret.hc`, add the following line to `/etc/crypttab`

```bash
veracrypt /secret.hc <passphrase> tcrypt-veracrypt,tcrypt-keyfile=/key.file
```

When using an empty passphrase in combination with one or more key files, use `/dev/null` instead of `<passphrase>` as the password file in the third field. Otherwise, replace `<passphrase>` with your passphrase to unlock `/secret.hc`.

Finally, to automatically mount the volume on system start, add the following line to `/etc/fstab`.

```bash
/dev/mapper/veracrypt /mnt/veracrypt ext4 nofail 0 2
```

### Bitlocker encrypted partitions

To open a [Bitlocker](https://en.wikipedia.org/wiki/BitLocker) encrypted partition, you need to install [dislocker](https://github.com/Aorimn/dislocker), which can be done in Arch Linux by running `yay -S dislocker-git`. Let say I have a Bitlocker encrypted partition `/dev/sda6`, formatting as `ntfs`, and unlocking it requires a passphrase. To unlock `/dev/sda6`, run the following commands as `root`.

```bash
mkdir -p /media/bitlocker 
dislocker -v -V /dev/sda6 -u<passphrase> -- /media/bitlocker 
``` 

If the commands run successfully, you will see that `/media/bitlocker/dislocker-file` is available. You can replace `/media/bitlocker` with any directory you want, and replace `<passphrase>` with your own secret passphrase. If you want to use recovery password instead of passphrase, use `-p` instead of `-u`.
Next, you can mount `/media/bitlocker/dislocker-file` to any folder, say `/data`, as follows. To mount a NTFS partition, you need [ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G).

```bash
export your_uid=$(id -u)
export your_gid=$(id -g)
sudo mount -t ntfs-3g -o gid=$your_gid,uid=$your_uid,dmask=022,fmask=133 /media/bitlocker/dislocker-file /data
```

The options `gid=$your_gid,uid=$your_uid,dmask=022,fmask=133` is to keep the common permissions of files and folders in Linux (permissions on a Linux system are normally set to `755` for folders and `644` for files) in use for the NTFS partition as well.

Finally, to automatically mount the volume on system start, add the following lines to `/etc/fstab`. (Remember to replace the parts `<...>` with your own values.)

```bash
PARTUUID=<partuuid of /dev/sda6> /media/bitlocker fuse.dislocker user-password=<passphrase>,nofail 0 0
/media/bitlocker/dislocker-file /data ntfs-3g gid=<your_gid>,uid=<your_uid>,dmask=022,fmask=133 0 0
```

