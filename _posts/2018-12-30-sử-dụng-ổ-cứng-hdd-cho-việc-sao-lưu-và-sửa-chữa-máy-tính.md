---
layout: blog-post
title: Sử dụng ổ cứng HDD cho việc sao lưu và sửa chữa máy tính
author: Duc A. Hoang
lang: vi
categories:
  - linux
  - windows
<!--comment: true-->
last_modified_at: 2020-11-07
description: Bài viết ghi lại cách tạo và sử dụng ổ HDD gắn ngoài như là một công cụ để thực hiện việc sao lưu và sửa chữa máy tính
keywords: manjaro architect, windows, installation, rescue, backup, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Tóm tắt</h1>
Tôi có một ổ cứng HDD SATA 320GB còn dư và muốn cài đặt và sử dụng ổ cứng này như một công cụ để thực hiện việc sửa chữa và sao lưu từ máy tính của tôi. Bài viết này ghi lại quá trình tôi cài đặt ổ cứng này với các công cụ cần thiết. Quá trình này được thực hiện chủ yếu trên Windows 10.

* TOC
{:toc}
</div>

# Mục tiêu

* Cài đặt HDD với chức năng Multi-boot phục vụ việc cài đặt, sao lưu và sửa chữa máy tính.
* Cài đặt hệ điều hành [Manjaro](https://manjaro.org/) trên HDD với các công cụ cần thiết để phục vụ quá trình làm việc của tôi. (Do đó, tôi có thể boot vào bất cứ máy tính nào thông qua ổ HDD này mà vẫn có thể tiếp tục công việc).

# Các công cụ cần thiết

* [Easy2Boot](http://www.easy2boot.com/): Công cụ hỗ trợ tạo USB hoặc ổ cứng có chức năng multi-boot. Tải [Easy2Boot v1.A7](http://www.easy2boot.com/download/) (tệp `Easy2Boot_v1.A7.zip`), [MPI Toolkit](http://www.easy2boot.com/download/mpi-pack/) (tệp `MPI_Tool_Pack_Plus_CloverLite_089.zip`), và [RMPrepUSB](http://files.easy2boot.com/200003276-bb22cbc1de/Install_RMPrepUSB_Full_v2.1.741a.exe.zip) (tệp `Install_RMPrepUSB_Full_v2.1.741a.exe.zip`). Xem thêm các hướng dẫn khác liên quan đến Easy2Boot tại [đây](http://rmprepusb.blogspot.com/p/easy2boot-useful-blogs.html). 
  * {% include files.html name="Easy2Boot_v1.A7.zip" text="Easy2Boot_v1.A7.zip" %}: Easy2Boot_v1.A7.zip (21.2 MB)
  * {% include files.html name="MPI_Tool_Pack_Plus_CloverLite_089.zip" text="MPI_Tool_Pack_Plus_CloverLite_089.zip" %}: MPI_Tool_Pack_Plus_CloverLite_089.zip (26.4 MB)
  * {% include files.html name="Install_RMPrepUSB_Full_v2.1.741a.exe.zip" text="Install_RMPrepUSB_Full_v2.1.741a.exe.zip" %}: Install_RMPrepUSB_Full_v2.1.741a.exe.zip (10 MB)
* [EaseUS Partition Master Free](https://www.easeus.com/partition-manager/epm-free.html): Hỗ trợ quản lý phân vùng (partition).
* ISO Boot Images:
  * [Hiren's BootCD PE x64](https://www.hirensbootcd.org/download/) và [Hiren's BootCD 15.2](https://www.hirensbootcd.org/old-versions/).
  * [Acronis True Image 2019 BootCD ISO](https://dl.acronis.com/u/AcronisTrueImage2019_14110.iso) (and version [2020](https://dl.acronis.com/u/AcronisTrueImage2020.iso)).
  * Windows Installtion ISO
    * [Adguard.net Techbench](https://tb.rg-adguard.net/public.php).
    * Tải trực tiếp từ [Microsoft](https://www.microsoft.com/en-us/software-download/).
      * Windows 10: truy cập [https://www.microsoft.com/en-us/software-download/windows10ISO/](https://www.microsoft.com/en-us/software-download/windows10ISO/).
      * Windows 8: truy cập [https://www.microsoft.com/en-us/software-download/windows8ISO/](https://www.microsoft.com/en-us/software-download/windows8ISO/).
      * Windows 7: truy cập [https://www.microsoft.com/en-gb/software-download/windows7](https://www.microsoft.com/en-gb/software-download/windows7). Cần có một *retail product key* để có thể tải ISO image.
  * Linux Installation ISO: [Arch Linux](https://www.archlinux.org/), [Manjaro](https://manjaro.org/), [Ubuntu](https://www.ubuntu.com/), [Linux Mint](https://www.linuxmint.com), [Fedora](https://getfedora.org/).

# Cài đặt Easy2Boot lên HDD bằng RMPrepUSB

Trước tiên, giải nén tệp `Easy2Boot_v1.A7.zip` để thu được thư mục `Easy2Boot_v1.A7` với nội dung như sau:

```bash
C:\USERS\[USERNAME]\DOWNLOADS\EASY2BOOT_V1.A7
└───_ISO
    ├───ANTIVIRUS
    ├───AUTO
    ├───BACKUP
    ├───docs
    │   ├───BOOT_ME_USING_QEMU
    │   │   └───QEMU
    │   ├───ChocBox
    │   ├───Download URLs
    │   │   └───GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}
    │   ├───E2B Utilities
    │   │   ├───Convert Unicode file to UTF8
    │   │   ├───DelSysFiles
    │   │   ├───Disable_System_Volume_Information_Folder_Creation
    │   │   ├───Force_Windows_Safe_Mode
    │   │   ├───Fribidi
    │   │   ├───GIFtoIMA
    │   │   ├───LZMA
    │   │   ├───Make_CONTIG.ISO
    │   │   ├───MD5
    │   │   ├───MOVE_IMGPTN
    │   │   ├───Protect
    │   │   └───WinNTSetup
    │   │       └───Tools
    │   │           └───diskpart
    │   ├───FASTLOAD
    │   ├───Fonts
    │   ├───GFXBoot
    │   │   ├───cpio
    │   │   └───files
    │   │       └───penguin
    │   ├───linux_utils
    │   ├───Make_E2B_USB_Drive
    │   │   └───ChangeDriveLetter
    │   ├───Make_Ext
    │   ├───MyThemes
    │   ├───PassPass
    │   ├───Sample mnu files
    │   │   ├───DOS
    │   │   ├───E2B Menus
    │   │   │   └───GRUB2
    │   │   ├───Falcon4.6
    │   │   ├───Hirens
    │   │   ├───Linux
    │   │   ├───OpenElec
    │   │   ├───Others
    │   │   ├───WinBuilder_PE_Multiple_ISOs
    │   │   │   └───_ISO
    │   │   │       └───MAINMENU
    │   │   │           └───WB1
    │   │   ├───Windows
    │   │   └───Windows Password
    │   │       ├───PassPass_chenall
    │   │       └───PassPass_E2B
    │   ├───SysInfo
    │   ├───Templates
    │   │   ├───Aliums
    │   │   ├───Animate
    │   │   ├───BeepShowBackgroundDemo
    │   │   ├───Blue
    │   │   ├───BoxDemo
    │   │   ├───CenteredMenu
    │   │   ├───GFXMenu
    │   │   ├───Jolene
    │   │   ├───LargeFont
    │   │   ├───LargeFontCentred
    │   │   ├───LargeFontCentredOffset
    │   │   ├───Mac
    │   │   ├───MainMenu Only
    │   │   ├───N0F1F7F8F10
    │   │   ├───PET
    │   │   ├───Quick800
    │   │   ├───StripedFlat_pwd_is_fred
    │   │   ├───TextMinimal
    │   │   └───WinInstInMain
    │   │       └───MAINMENU
    │   ├───Tunes
    │   ├───USB FLASH DRIVE HELPER FILES
    │   ├───UtilMan
    │   └───WINCONTIG
    │       └───lang
    ├───DOS
    │   └───MNU
    ├───e2b
    │   ├───firadisk
    │   │   ├───awealloc
    │   │   │   ├───amd64
    │   │   │   └───i386
    │   │   ├───cli
    │   │   │   ├───amd64
    │   │   │   └───i386
    │   │   ├───cpl
    │   │   │   ├───amd64
    │   │   │   └───i386
    │   │   ├───svc
    │   │   │   ├───amd64
    │   │   │   └───i386
    │   │   └───sys
    │   │       ├───amd64
    │   │       └───i386
    │   └───grub
    │       ├───ARABIC
    │       ├───CZECH
    │       ├───DPMS
    │       │   ├───D
    │       │   ├───FIRA
    │       │   ├───NTBOOT.MOD
    │       │   └───WINV
    │       ├───DUTCH
    │       ├───ENG
    │       ├───FRENCH
    │       ├───GERMAN
    │       ├───GERMAN_ALT
    │       ├───GREEK
    │       ├───ITALIAN
    │       ├───POLISH
    │       ├───PORTU_BRAZIL
    │       ├───ROMANIAN
    │       ├───RUSSIAN
    │       ├───SIMP_CHINESE
    │       ├───SPANISH
    │       ├───SWEDISH
    │       ├───TRAD_CHINESE
    │       ├───UKRAINIAN
    │       └───VIETNAMESE
    ├───LINUX
    ├───MAINMENU
    │   ├───$$$$CONFIG
    │   └───MNU
    ├───UTILITIES
    │   └───MNU
    ├───UTILITIES_MEMTEST
    │   └───MNU
    ├───WIN
    ├───WINDOWS
    │   ├───installs
    │   │   ├───APPS
    │   │   │   ├───CHOCBOX
    │   │   │   └───CHROME
    │   │   │       ├───AMD64
    │   │   │       ├───BOTH
    │   │   │       └───X86
    │   │   ├───CONFIGS
    │   │   │   └───SDI_CHOCO
    │   │   ├───DRIVERS
    │   │   ├───INSTALLCHOCO
    │   │   ├───SNAPPY
    │   │   │   ├───drivers
    │   │   │   ├───indexes
    │   │   │   │   └───SDI
    │   │   │   │       └───txt
    │   │   │   ├───logs
    │   │   │   ├───scripts
    │   │   │   └───tools
    │   │   │       └───SDI
    │   │   │           ├───langs
    │   │   │           └───themes
    │   │   │               ├───dark
    │   │   │               ├───green_blue
    │   │   │               ├───metallic
    │   │   │               ├───metro
    │   │   │               ├───sky_clouds
    │   │   │               └───winter
    │   │   └───wsusoffline
    │   ├───SVR2012
    │   │   └───SAMPLE XML FILES
    │   ├───SVR2016
    │   ├───SVR2019
    │   ├───SVR2K8R2
    │   ├───VISTA
    │   ├───WIN10
    │   │   └───SAMPLE XML FILES
    │   │       └───Disk1 for VMs
    │   ├───WIN7
    │   │   └───SAMPLE XML FILES
    │   │       └───Disk1 for VMs
    │   ├───WIN8
    │   │   └───SAMPLE XML FILES
    │   │       └───Disk1 for VMs
    │   ├───WINAIO
    │   └───XP
    └───WINPE
```

Cài đặt `RMPrepUSB` và chạy với quyền Administrator.

{% include image.html name="RMPrepUSB-0.png" caption="Cửa sổ <code>RMPrepUSB</code>" width="50%" %}

Các bước lựa chọn (xem thêm ở [trang này](http://www.easy2boot.com/make-an-easy2boot-usb-drive/make-and-e2b-usb-drive-using-rmprepusb/)) như sau:

* Chọn menu `Settings > List Large Drives > 128GiB`, hoặc bấm <kbd>Ctrl</kbd> + <kbd>Z</kbd>, để làm việc với ổ HDD.
* Tick `No User Prompts` check box.
* Mục `1. Partition Size (MiB)`: Tôi muốn sử dụng khoảng 30GB để lưu và boot các ISO images, do đó tôi chọn kích thước phân vùng là khoảng 30720 MiB. Kích thước tối đa mà `Easy2Boot` đề nghị là 131072 MiB (xem [trang này](http://www.easy2boot.com/faq-/a137gb-bios-bug/)).
* Mục `2. Volume Name`: `EASY2BOOT` (hoặc bất kỳ tên nào bạn thích).
* Mục `3. Bootloader Options`: Chọn `WinPEv2/WinPEv3/Vista/Win 7 bootable [BOOTMGR] (CC4)` (thực ra bất kỳ lựa chọn nào ngoài `SYSLINUX` đều được).
* Mục `4. Filesystem and Overrides`: Chọn `NTFS`.
* Mục `5. Copy OS Files`: Bấm `Choose Source`, trả lời `Copy Files='YES'`, và chọn đường dẫn tới thư mục `Easy2Boot_v1.A7` (trong trường hợp của tôi là `C:\Users\[username]\Downloads\Easy2Boot_v1.A7`, với `[username]` là username sử dụng trong Windows).
* Bấm `6. Prepare drive`. Bước này sẽ định dạng ổ HDD, tạo phân vùng mới với nhãn bạn đã chọn (`EASY2BOOT`), và sao chép các tệp cần thiết từ thư mục `Easy2Boot_v1.A7` vào phân vùng này.
* Sau khi hoàn thành bước trên, bấm `Install grub4dos`, chọn `Yes` để cài `Grub4dos` vào MBR (**M**aster **B**oot **R**ecord) của HDD. Chọn `Cancel` khi được hỏi `Overwrite existing grldr file on E:` (với `E:` là tên Windows gán cho phân vùng `EASY2BOOT`) để **tránh việc ghi đè tệp `grldr` của Easy2Boot**.
* Bấm `Install grub4dos`, chọn `No` để cài `Grub4dos` vào PBR (**P**artition **B**oot **R**ecord) của phân vùng `EASY2BOOT`. Chọn `Cancel` khi được hỏi `Overwrite existing grldr file on E:` (với `E:` là tên Windows gán cho phân vùng `EASY2BOOT`) để **tránh việc ghi đè tệp `grldr` của Easy2Boot**.

# Tạo các phân vùng khác trên HDD

Như đã nói ở trên, tôi muốn cài đặt [Manjaro](https://manjaro.org/) trên HDD để phục vụ quá trình làm việc của mình. Tôi sử dụng `EaseUS Partition Master Free` để tạo các **phân vùng Logical** trên HDD như sau:

* Phân vùng có nhãn `E2B_PTN2`, định dạng FAT32 để cài đặt và sử dụng GRUB2 với Easy2Boot (phiên bản Beta, xem ở [đây](http://www.easy2boot.com/uefi-grub2-ptn2/)).
* Phân vùng có nhãn `DATA`, định dạng NTFS, để chứa các dữ liệu và bản sao cần thiết.
* Phân vùng có nhãn `EFI_BOOT`, kích thước khoảng 300MiB, định dạng FAT32 để chứa các thông tin liên quan đến việc boot với UEFI mode. (Tôi muốn cài đặt cả UEFI và (Legacy) BIOS boot mode). 
* Phân vùng có nhãn `LINUX_SWAP`, kích thước khoảng 2GB, định dạng EXT3.
* Phân vùng có nhãn `MANJARO_ROOT`, định dạng EXT3, để cài hệ điều hành Manjaro.

Chú ý rằng việc khởi tạo các phân vùng logical như trên chỉ nhằm mục đích tạo ra cấu trúc có sẵn để cài hệ điều hành. Khi cài Manjaro, tất cả các phân vùng trên (trừ `E2B_PTN2` và `DATA`) sẽ được định dạng lại.

# Cài đặt Easy2Boot

Cách đơn giản nhất là bạn chỉ cần sao chép ISO image vào một trong các thư mục con của thư mục `_ISO` trong phân vùng `EASY2BOOT`. Bạn cũng có thể chuyển đổi tệp có đuôi `.iso` sang tệp có đuôi `.imgPTN` để boot từ `Easy2Boot` menu (xem [trang này](http://www.easy2boot.com/add-payload-files/makepartimage)). [Trang chủ của Easy2Boot](http://www.easy2boot.com/) có chứa các hướng dẫn chi tiết về việc cài đặt và sử dụng Easy2Boot. Chú ý rằng bạn có thể đổi đuôi `.imgPTN` sang `.imgPTN23` nếu muốn hiện các phân vùng còn lại của ổ HDD khi bạn boot với tệp đuôi `.imgPTN`. Để cài đặt GRUB2 với Easy2Boot, xem hướng dẫn ở [đây](http://www.easy2boot.com/uefi-grub2-ptn2/).

# Cài đặt Manjaro

Tôi cài đặt Manjaro với [Manjaro Architect](https://manjaro.org/download/architect/). Xem hướng dẫn cài đặt tại [đây](https://wiki.manjaro.org/index.php?title=Installation_with_Manjaro_Architect). Cấu trúc menu của Manjaro Architect ở thời điểm tôi viết bài này có dạng như sau:

```bash
|
├── Prepare Installation
│    ├── Set Virtual Console
│    ├── List Devices
│    ├── Partition Disk
│    ├── LUKS Encryption
│    ├── Logical Volume Management
│    ├── Mount Partitions
│    ├── Configure Installer Mirrorlist
│    └── Refresh Pacman Keys
│
├── Install Desktop System
│   ├── Install Manjaro Desktop
│   ├── Install Bootloader
│   ├── Configure Base
│   │   ├── Generate FSTAB
│   │   ├── Set Hostname
│   │   ├── Set System Locale
│   │   ├── Set Desktop Keyboard Layout
│   │   ├── Set Timezone and Clock
│   │   ├── Set Root Password
│   │   └── Add New User(s)
│   │
│   ├── Security and systemd Tweaks
│   │   ├── Amend journald Logging
│   │   ├── Disable coredump Logging
│   │   └── Restrict Access to Kernel Logs
│   │
│   ├── Review Configuration Files
│   └── Chroot into Installation
│
├── Install CLI System
│   ├── Install Base Packages
│   ├── Install Bootloader
│   ├── Configure Base
│   │   ├── Generate FSTAB
│   │   ├── Set Hostname
│   │   ├── Set System Locale
│   │   ├── Set Desktop Keyboard Layout
│   │   ├── Set Timezone and Clock
│   │   ├── Set Root Password
│   │   └── Add New User(s)
│   │
│   ├── Install Custom Packages
│   ├── Security and systemd Tweaks
│   │   ├── Amend journald Logging
│   │   ├── Disable coredump Logging
│   │   └── Restrict Access to Kernel Logs
│   │
│   ├── Review Configuration Files
│   └── Chroot into Installation
│
├── Install Custom System
│   ├── Install Base Packages
│   ├── Install Unconfigured Desktop Environments
│   │   ├── Install Display Server
│   │   ├── Install Desktop Environment
│   │   ├── Install Display Manager
│   │   ├── Install Networking Capabilities
│   │   ├── Install Multimedia Support
│   │   └── Install Custom Packages
│   ├── Install Bootloader
│   ├── Configure Base
│   │   ├── Generate FSTAB
│   │   ├── Set Hostname
│   │   ├── Set System Locale
│   │   ├── Set Desktop Keyboard Layout
│   │   ├── Set Timezone and Clock
│   │   ├── Set Root Password
│   │   └── Add New User(s)
│   │
│   ├── Install Custom Packages
│   ├── Security and systemd Tweaks
│   │   ├── Amend journald Logging
│   │   ├── Disable coredump Logging
│   │   └── Restrict Access to Kernel Logs
│   │
│   ├── Review Configuration Files
│   └── Chroot into Installation
│
└── System Rescue
    ├── Install Hardware Drivers
    │   ├── Install Display Drivers
    │   └── Install Network Drivers
    │
    ├── Install Bootloader
    ├── Configure Base
    │   ├── Generate FSTAB
    │   ├── Set Hostname
    │   ├── Set System Locale
    │   ├── Set Desktop Keyboard Layout
    │   ├── Set Timezone and Clock
    │   ├── Set Root Password
    │   └── Add New User(s)
    │
    ├── Install Custom Packages
    ├── Remove Packages
    ├── Review Configuration Files
    └── Chroot into Installation
```

Cấu trúc HDD của tôi nhìn từ  Manjaro sau khi hoàn tất cài đặt có dạng như sau (kết quả từ `sudo fdisk -l`):

```bash
Disk /dev/sdb: 298.1 GiB, 320072933376 bytes, 625142448 sectors
Disk model: 5AS             
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 33553920 bytes
Disklabel type: dos
Disk identifier: 0x6b85a911

Device     Boot     Start       End   Sectors   Size Id Type
/dev/sdb1            2048  56623103  56621056    27G  7 HPFS/NTFS/exFAT
/dev/sdb2        56623104  83886079  27262976    13G  c W95 FAT32 (LBA)
/dev/sdb3        83886080 625141759 541255680 258.1G  f W95 Ext'd (LBA)
/dev/sdb5        83886143 398458879 314572737   150G  7 HPFS/NTFS/exFAT
/dev/sdb6  *    398458943 399507455   1048513   512M ef EFI (FAT-12/16/32)
/dev/sdb7       399509504 403703807   4194304     2G 82 Linux swap / Solaris
/dev/sdb8       403705856 625141759 221435904 105.6G 83 Linux
```

Quan hệ giữa các phân vùng là

| Nhãn trên Windows ban đầu | Định dạng trên Windows ban đầu | Phân vùng trên Linux sau khi cài | Định dạng trên Linux sau khi cài | Loại (Primary/Logical) | Chức năng |
|:-----------------:|:----------------------:|:--------------------:|:-------------------:|:---------:|
| `EASY2BOOT` | NTFS | `/dev/sdb1` | HPFS/NTFS/exFAT <br> **[Không thay đổi]** | Primary | Phân vùng Multi-boot sử dụng bởi Easy2Boot |
| `E2B_PTN2` | FAT32 | `/dev/sdb2` | W95 FAT32 (LBA) <br> **[Không thay đổi]** | Primary | Phân vùng 2 sử dụng bởi Easy2Boot với GRUB2 |
| `DATA` | NTFS | `/dev/sdb5` | HPFS/NTFS/exFAT <br> **[Không thay đổi]** | Logical | Lưu trữ dữ liệu |
| `EFI_BOOT` | FAT32 | `/dev/sdb6` | EFI (FAT-12/16/32) <br> **[Định dạng lại]** | Logical | Phân vùng cài đặt EFI boot |
| `LINUX_SWAP` | EXT3 | `/dev/sdb7` | Linux swap / Solaris <br> **[Định dạng lại]**  | Logical | Phân vùng swap cho Manjaro |
| `MANJARO_ROOT` | EXT 3 | `/dev/sdb8` | Linux (EXT4) <br> **[Định dạng lại]** | Logical | Phân vùng cài đặt Manjaro |

Một số chú ý khi cài đặt:

* Ở bước `Mount Partitions`, chọn `/dev/sdb6` khi được hỏi về "EFI boot partition". Chọn mount phân vùng này vào thư mục `/boot/efi`, và chọn `grub` ở mục `Install Bootloader` sau này.
* Ở bước `Chroot into Installation`, cài đặt lại GRUB2 bootloader để boot với UEFI mode như sau (xem thêm ở [đây](https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks)):

```bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Manjaro --boot-directory=/boot/efi --debug
grub-mkconfig -o /boot/efi/grub/grub.cfg
```

Tiếp đó, cài đặt GRUB Bootloader để boot với BIOS mode như sau (xem thêm ở [đây](https://github.com/alberthdev/alberthdev-misc/wiki/Installing-GRUB2-to-a-Partition)):

```bash
grub-install --target=i386-pc /dev/sdb # Install GRUB2 to MBR, which overwrites Grub4dos installed before
chattr -i /boot/grub/i386-pc/core.img
grub-install --target=i386-pc --debug --force /dev/sdb8 # Install GRUB2 to partition /dev/sdb8
chattr +i /boot/grub/i386-pc/core.img
grub-mkconfig -o /boot/grub/grub.cfg
```

# Cài đặt Windows 

## Windows To Go

Thay vì Manjaro, có thể sử dụng [WinToUSB](https://www.easyuefi.com/wintousb/) để cài đặt [Windows To Go](https://docs.microsoft.com/en-us/windows/deployment/planning/windows-to-go-overview).
Có thể thực hiện điều này bằng cách tạo phân vùng `EASY2BOOT` định dạng NTFS để cài Windows lên ổ HDD thông qua `WinToUSB`, và phân vùng `WIN_BOOT` định dạng FAT32 tầm 300MiB để chứa thông tin liên quan đến việc boot vào Windows với cả BIOS và UEFI mode. Tôi sử dụng ISO image của phiên bản Windows 10 Enterprise LTSC 2019 tải trực tiếp từ [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise) với WinToUSB.
Khi sử dụng `WinToUSB`, chọn `WIN_BOOT` là `system partition` và `EASY2BOOT` là `boot partition`. Chú ý rằng `EASY2BOOT` phải là phân vùng thứ nhất. Điều này nhằm thuận lợi cho việc cài đặt Easy2Boot lên phân vùng này với `RMPrepUSB` (chỉ sao chép các tệp của Easy2Boot vào phân vùng `EASY2BOOT` và thực hiện cài `Grub4dos`, **không định dạng lại phân vùng `EASY2BOOT`**) sau khi hoàn thành các bước cài đặt với `WinToUSB`. Nếu gặp lỗi `PROBLEM: Sector at LBA30 appears to contain code - please reformat using RMPrepUSB` khi boot với tệp đuôi `.imgPTN` thì xử lý như sau: Chọn ổ HDD với phân vùng `EASY2BOOT` từ `RMPrepUSB`. Sau đó bấm nút `Drive->File`, lưu tệp với tên `MBR.bin` và điền các tham số như sau: **Start** = 0, **Length**=1SEC, **FileStart**=0. Tiếp theo, bấm nút `File->Drive`, chọn tệp `MBR.bin` vừa lưu và điền các tham số như sau: **Start**=0, **USBStart**=30, **Length**=0. (Xem thêm ở [đây](http://www.easy2boot.com/faq-/) để biết thêm chi tiết.) Để cài đặt phần mềm trên Windows, có thể sử dụng [Chocolatey](https://chocolatey.org) với lệnh `choco install packages.config -y`, với tệp `packages.config` có dạng như sau (cho Windows 64-bit). Chú ý là một số phần mềm như `texmaker` phiên bản `5.0.3` hay `jdk11` chỉ chạy trên nền hệ điều hành 64-bit.

```bash
<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="7zip" version="18.6"/>
  <package id="7zip.install" version="18.6"/>
  <package id="7zip.portable" version="18.6"/>
  <package id="adobereader" version="2019.010.20064.01"/>
  <package id="autohotkey.portable" version="1.1.30.01"/>
  <package id="chocolatey" version="0.10.11"/>
  <package id="chocolatey-core.extension" version="1.3.3"/>
  <package id="chocolatey-misc-helpers.extension" version="0.0.3.1"/>
  <package id="chocolatey-windowsupdate.extension" version="1.0.3"/>
  <package id="chocolateygui" version="0.16.0"/>
  <package id="defraggler" version="2.22.995.20181017"/>
  <package id="DotNet3.5" version="3.5.20160716"/>
  <package id="DotNet4.5.2" version="4.5.2.20140902"/>
  <package id="dropbox" version="64.4.141"/>
  <package id="filezilla" version="3.39.0"/>
  <package id="Firefox" version="64.0.2"/>
  <package id="git" version="2.20.1"/>
  <package id="git.install" version="2.20.1"/>
  <package id="GoogleChrome" version="71.0.3578.98"/>
  <package id="gpg4win" version="3.1.5"/>
  <package id="imdisk" version="2.0.10.20181231"/>
  <package id="jdk11" version="11.0.1"/>
  <package id="k-litecodecpackmega" version="14.6.0"/>
  <package id="KB2919355" version="1.0.20160915"/>
  <package id="KB2919442" version="1.0.20160915"/>
  <package id="KB2999226" version="1.0.20181019"/>
  <package id="KB3033929" version="1.0.4"/>
  <package id="KB3035131" version="1.0.2"/>
  <package id="notepadplusplus" version="7.6.2"/>
  <package id="notepadplusplus.install" version="7.6.2"/>
  <package id="Opera" version="57.0.3098.116"/>
  <package id="ruby" version="2.5.3.101"/>
  <package id="texmaker" version="5.0.3"/>
  <package id="thunderbird" version="60.4.0"/>
  <package id="unikey" version="4.3.180714"/>
  <package id="vcredist140" version="14.16.27024.1"/>
  <package id="vcredist2015" version="14.0.24215.20170201"/>
  <package id="veracrypt" version="1.23.2"/>
  <package id="vlc" version="3.0.6"/>
  <package id="vmware-horizon-client" version="4.10.0"/>
  <package id="vscode" version="1.30.2"/>
  <package id="Wget" version="1.20"/>
  <package id="windjview" version="2.1"/>
  <package id="zotero" version="5.0.60"/>
</packages>
```

Phiên bản Windows 10 Enterprise LTSC 2019 cho phép sử dụng thử trong 90 ngày, và có thể sử dụng lệnh `slmgr /rearm` 3 lần để gia hạn. Một cách thường dùng với các phiên bản Windows Enterprise và Windows Server cũ để gia hạn thời gian sử dụng mỗi khi hết 90 ngày là như sau: tìm đến `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform` trong Windows Registry và thay giá trị của `SkipRearm` từ `0` thành `1`, sau đó dùng lệnh `slmgr /rearm` để gia hạn thời gian sử dụng thử. Có thể đọc thêm về `SkipRearm` ở [đây](https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-security-spp-skiprearm).

## Tạo bộ cài đặt Windows 10 với các phần mềm cài sẵn

Các bước thực hiện có thể được tóm tắt như sau (xem bài hướng dẫn gốc ở [đây](https://www.tenforums.com/tutorials/72031-create-windows-10-iso-image-existing-installation.html)).

* Cài đặt Windows 10.
* Khi đến màn hình đầu tiên sau khi Windows 10 khởi động lại máy tính và bắt đầu hỏi các thông tin về Region, Keyboard, v.v..., thay vì trả lời các thông tin này, bấm <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F3</kbd> để khởi động lại vào Audit Mode.
* Sau khi khởi động vào Audit Mode, bạn sẽ thấy một cửa sổ `System Preparation Tool` đang mở. Để cửa sổ đó và tiến hành cài đặt các phần mềm bạn muốn (chú ý luôn cài phần mềm cho **all users**).
* Sau khi cài xong, gõ lệnh `cmd.exe /c Cleanmgr /sageset:65535 & Cleamngr /sagerun:65535` trong cửa sổ CMD với quyền Administrator để dọn dẹp hệ thống. Nếu bạn dùng [Chocolatey](https://chocolatey.org) để cài phần mềm như tôi đã nói ở trên thì có thể cài thêm `choco-cleaner` và chạy tệp `C:\ProgramData\chocolatey\lib\choco-cleaner\tools\Choco-Cleaner-manual.bat` để dọn dẹp các tệp không cần thiết sinh ra trong quá trình cài đặt với `Chocolatey`.
* Tạo tệp `C:\Windows\System32\Sysprep\unattend.xml` với nội dung sau:

Cho Windows 64-bit

```bash
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="specialize">
        <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <CopyProfile>true</CopyProfile>
        </component>
    </settings>
</unattend> 
```

Cho Windows 32-bit

```bash
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="specialize">
        <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="x86" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <CopyProfile>true</CopyProfile>
        </component>
    </settings>
</unattend>
```

Khi chạy `Sysprep`, tệp này sẽ sao chép tất cả các cài đặt trong profile bạn đang dùng cho tất cả các user khác.

* Tạo tệp `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\RunOnce.bat` với nội dung sau.

```bash
echo Y|del %appdata%\microsoft\windows\recent\automaticdestinations\*
del %0
```

Tệp này sẽ reset `Quick Access` về cài đặt mặc định, và tự xóa chính nó (bằng lệnh `del %0`) sau khi hoàn thành việc này.

* Quay lại cửa sổ `System Preparation Tool`, chọn `Enter System Out-of-Box Experience (OOBE)` trong menu `System Cleanup Action`, tích chọn hộp vuông bên cạnh `Generalize`, và chọn `Shutdown` trong menu `Shutdown Options`.

* Tiếp theo, ta tạo ảnh `install.wim` của phân vùng chứa Windows đã được dọn dẹp bởi `Sysprep`. Tệp `install.wim` là một phần của tệp ISO phục vụ cho việc cài Windows sau này. Sau khi quá trình trên kết thúc, khởi động máy tính với bộ cài Windows (mới nhất có thể) từ DVD hoặc USB. Ở màn hình đầu tiên, bấm <kbd>Shift</kbd>+<kbd>F10</kbd> để khởi động cửa sổ dòng lệnh của Windows. Sử dụng `diskpart` để liệt kê tất cả các phân vùng hiện có trên máy tính bằng lệnh `list vol`. Giả sử phân vùng cài Windows của bạn là ở ổ `D:\` và bạn muốn lưu `install.wim` ở ổ `E:\` (hoặc bất kỳ ổ đĩa hoặc phân vùng nào khác trừ `D:\`). Tạo thư mục `E:\Scratch` là thư mục tạm thời phục vụ cho quá trình tạo tệp ảnh `install.wim`.

```bash
dism /capture-image /imagefile:E:\install.wim /capturedir:D:\ /ScratchDir:E:\Scratch /name:"AnyName" /compress:maximum /checkintegrity /verify /bootable
```

Quá trình này có thể mất rất nhiều thời gian, tùy thuộc vào cấu hình máy tính của bạn.

* Sau khi hoàn thành quá trình trên, khởi động lại máy tính vào Windows. Lấy tệp ISO dùng để cài đặt Windows mới nhât từ Microsoft, giải nén tệp này (dùng `WinRAR` hoặc `7-zip`) vào một thư mục, ví dụ như `D:\isofiles`. Xóa tệp `install.wim` ở `D:\isofiles\sources\install.wim` và thay bằng tệp `install.wim` đã được tạo từ quá trình trên.

* Tải phiên bản mới nhất của [Windows Assessment and Deployment Kit (ADK) for Windows 10](https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit). Cài đặt toàn bộ gói này cần tải về khoảng 7.5GB, tuy nhiên ta chỉ cần `Deployment Tools`. Khi cài Windows ADK, ta bỏ hết tất cả các thành phần còn lại để giảm dung lượng tải về.

* Sau khi cài Windows ADK, mở cửa sổ dòng lệnh `Deployment and Imaging Tools` với quyền Administrator. Trong cửa sổ dòng lệnh mới mở ra, gõ lệnh sau để tạo tệp ISO cài đặt Windows với một số phần mềm cài sẵn.

```bash
oscdimg.exe -m -lCCCOMA_X64FRE_EN-US_DV9_CUSTOM -o -u2 -udfver102 -bootdata:2#p0,e,bd:\isofiles\boot\etfsboot.com#pEF,e,bd:\isofiles\efi\microsoft\boot\efisys.bin d:\isofiles d:\Win10Prox64Custom.iso
```

<!--
oscdimg.exe -m -lCCCOMA_X64FRE_EN-US_DV9_RECOVERY -o -u2 -udfver102 -bootdata:2#p0,e,be:\isofiles\boot\etfsboot.com#pEF,e,be:\isofiles\efi\microsoft\boot\efisys.bin e:\isofiles c:\Win10_Pro_x64_Backup_20190129.iso
-->

Bạn có thể thay `CCCOMA_X64FRE_EN-US_DV9_CUSTOM` bằng bất kỳ nhãn nào bạn thích. Sau khi hoàn tất, tệp ISO mới sẽ được lưu ở ổ `D:\` với tên `Win10Prox64Custom.iso`. Tham khảo thêm từ [trang nguồn của hướng dẫn này](https://www.tenforums.com/tutorials/72031-create-windows-10-iso-image-existing-installation.html) với hình ảnh minh họa đầy đủ và hướng dẫn cách làm với máy ảo.

## Sao lưu và khôi phục hệ thống

Hoàn toàn có thể sử dụng các công cụ ở phần trước để sao lưu và khôi phục hệ thống Windows. 
Để sao lưu hệ thống Windows, tạo tệp ảnh `install.wim` như sau. 
Khởi động máy tính và boot vào bộ cài đặt Windows (mới nhất có thể), bấm <kbd>Shift</kbd>+<kbd>F10</kbd> để khởi động cửa sổ dòng lệnh của Windows. Sử dụng `diskpart` để liệt kê tất cả các phân vùng hiện có trên máy tính bằng lệnh `list vol`. Giả sử phân vùng cài Windows của bạn là ở ổ `C:\` và bạn muốn lưu `install.wim` ở ổ `D:\` (hoặc bất kỳ ổ đĩa hoặc phân vùng nào khác trừ `C:\`). 

```bash
dism /capture-image /imagefile:D:\install.wim /capturedir:C:\ /name:"Recovery" /compress:maximum
```

Sau khi quá trình này hoàn tất, bạn có thể tạo tệp ISO như hướng dẫn ở trên. Để khôi phục hệ thống, tiến hành tạo USB boot với nội dung của tệp ISO đã tạo như trên (hoặc bạn cũng có thể tiến hành tách `install.wim` thành nhiều tệp đuôi `.swm` và tiến hành ghi ra DVD để cài đặt, như hướng dẫn ở [đây](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/split-a-windows-image--wim--file-to-span-across-multiple-dvds)) và cài đặt bình thường như khi bạn cài Windows. 
Tôi ghi lại ở đây câu lệnh sử dụng để tách `install.wim` thành các tệp đuôi `.swm` có kích thước nhỏ hơn (để ghi ra nhiều đĩa DVD).

```bash
dism /split-image /imagefile:install.wim /swmfile:install.swm /filesize:3800
```

# GRUB2 và Grub4dos menu

Từ  Windows 10, sử dụng `RMPrepUSB` để cài đặt lại Grub4dos như đã thực hiện ở trên. Sau đó, tạo một tệp `_ISO/MAINMENU/MNU/Manjaro.mnu` với nội dung sau

```bash
# --- Manjaro Linux Boot Menu -----
title Pre-Installed Manjaro Linux
kernel (hd0,7)/boot/grub/i386-pc/core.img
```

để boot Manjaro từ Grub4dos menu của Easy2Boot.

Ở đây, `(hd0, 7)` ứng với phân vùng `/dev/sdb8` trên ổ HDD.

Từ Manjaro, để boot vào Easy2Boot, thêm dòng sau vào `/etc/grub.d/40_custom`

```bash
if [ "${grub_platform}" == "pc" ]; then
	menuentry "EASY2BOOT"{
		set root='(hd1,1)'
		search --no-floppy --fs-uuid --set 48B001F4B001E970
		drivemap -s (hd0) ${root}
		chainloader +1
	}
fi
```

trong đó `48B001F4B001E970` là UUID của phân vùng `/dev/sdb1` chứa Easy4Boot. Để lấy UUID của `/dev/sdb1`, dùng lệnh `sudo blkid /dev/sdb1`. Cập nhật lại GRUB2 bootloader menu như sau:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Để load từ GRUB2 menu của Easy2Boot, tôi tạo tệp `_ISO/MAINMENU/MNU/grub2/Manjaro.grub2` và `_ISO/MAINMENU/grub2/Manjaro.grub2` với nội dung như sau:

```bash
if $EFI; then
if $BIT64; then
menuentry 'Pre-Installed Manjaro Linux (x64 UEFI)' --class manjaro --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-simple-e76694c2-cd39-443c-b487-be95c5bac27e' {
	if [ -z "${boot_once}" ]; then
		saved_entry="${chosen}"
		save_env saved_entry
  	fi
	if [ x$feature_all_video_module = xy ]; then
    	insmod all_video
  	else
		insmod efi_gop
		insmod efi_uga
		insmod ieee1275_fb
		insmod vbe
		insmod vga
		insmod video_bochs
		insmod video_cirrus
  	fi
	set gfxpayload=keep
	insmod gzio
	insmod part_msdos
	insmod ext2
	set root='hd0,msdos6'
	if [ x$feature_platform_search_hint = xy ]; then
	  search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos6 --hint-efi=hd0,msdos6 --hint-baremetal=ahci0,msdos6  350E-515A
	else
	  search --no-floppy --fs-uuid --set=root 350E-515A
	fi
	chainloader /efi/boot/bootx64.efi
}
fi
fi
```

Chú ý rằng phân vùng `/dev/sdb6` là phân vùng lưu giữ các thông tin phục vụ việc boot với UEFI boot mode. Ở đây, khi bạn load GRUB2 menu từ Grub4dos của Easy2Boot bằng cách load tệp `UEFI_GRUB2_PTN2_xxxx.imgPTNLBAa23`, đuôi `.imgPTNLBAa23` cho thấy sau khi load tệp này thì ổ HDD (chứa Easy2Boot) của bạn sẽ được coi là ổ `hd0` khi boot, và các phân vùng khác trên ổ HDD này đều sẽ được nhận dạng (nếu bỏ đuôi `23` thì bạn sẽ không tìm thấy các phân vùng này khi chạy bất kỳ chương trình nào, ví dụ như Acronis True Image CD). Do đó, tôi đặt `set root='hd0,msdos6'`, với `msdos6` ở đây chỉ phân vùng `/dev/sdb6` chứa các thông tin để boot Manjaro Linux với UEFI mode. Để chắc chắn hơn, tôi đặt lệnh tìm kiếm UUID của phân vùng này (ở đây là `350E-515A`, thông tin này có thể được lấy bằng lệnh `sudo blkid /dev/sdb6` trong Manjaro Linux) và đặt lại root nếu phân vùng không phải `'hd0,msdos6'`. Chú ý rằng tôi có thể boot thành công là do **tôi đã sao chép tất cả các tệp cần thiết cho việc boot với UEFI mode vào phân vùng `/dev/sdb6` khi cài đặt với `grub-install` và `grub-mkconfig`**.

# GRUB2 menu entry cho một số tệp ISO để sử dụng với Easy2Boot

Các entry sau được thêm vào các tệp đuôi `.grub2` tương ứng. Chú ý rằng **tên tệp ISO cần phải trùng với tên tệp trong entry, và tốt nhất là không chứa khoảng cách**.

## manjaro-architect-18.0-stable-x86_64.iso

```bash
if $BIT64; then
if [ -e "$isofpath/manjaro-architect-18.0-stable-x86_64.iso" ]; then
menuentry 'Manjaro Architect (x86-64 UEFI)' --unrestricted --class manjaro{
    set isoname=manjaro-architect-18.0-stable-x86_64.iso ; CHECK_MNU_FOLDER
	set root=$root2
	loopback loop $isofile
# probe params: -p = partmap, -f = filesystem, -u = uuid, -l = label
	probe -l (loop) --set=isolabel
	linux  (loop)//boot/vmlinuz-x86_64  img_dev=/dev/disk/by-uuid/$root2uuid img_loop=$isofile 
	initrd (loop)/boot/intel_ucode.img (loop)/boot/initramfs-x86_64.img
	boot
}
fi
fi
```

## clonezilla-live-20180812-bionic-amd64.iso

```bash
if $BIT64; then
if [ -e "$isofpath/clonezilla-live-20180812-bionic-amd64.iso" ]; then
menuentry "Clonezilla Live Bionic (64-bit)" --unrestricted --class clonezilla {
	set isoname=clonezilla-live-20180812-bionic-amd64.iso ; CHECK_MNU_FOLDER
	gfxpayload=keep
	set root=$root2
	loopback loop $isofile
	linux (loop)/live/vmlinuz boot=live union=overlay username=user config components quiet noswap nolocales edd=on nomodeset nodmraid ocs_live_run=\"ocs-live-general\" ocs_live_extra_param=\"\" keyboard-layouts= ocs_live_batch=\"no\" locales= vga=788 ip=frommedia nosplash toram=filesystem.squashfs findiso=$isofile
	initrd (loop)/live/initrd.img
} 
fi
fi
```

## AcronisTrueImage2019_14110.iso

```bash
if $BIT64; then
if [ -e "$isofpath/AcronisTrueImage2019_14110.iso" ]; then
menuentry "Acronis True Image Home 2019 (ISO)" --unrestricted --class icon-ati {
    set isoname=AcronisTrueImage2019_14110.iso ; CHECK_MNU_FOLDER
	set quiet=1
	set pager=0
	set gfxpayload=1024x768x32,1024x768
	set mbrcrcs=on
	set root=$root2
	loopback loop $isofile
	linux (loop,msdos1)/dat10.dat quiet force_modules=usbhid lang=1
	initrd (loop,msdos1)/dat11.dat (loop,msdos1)/dat12.dat
	boot
}
fi
fi
```

Chú ý rằng bạn cũng có thể đặt tệp ISO trên vào thư mục bất kỳ trên ổ cứng, ví dụ như `/iso`, và thêm một entry tương tự vào `/etc/grub.d/40_custom` để boot tệp ISO này từ ổ cứng của máy tính bạn đang sử dụng. Xem thêm ở [đây](http://reboot.pro/topic/20004-boot-a-acronis-true-image-2014-iso-image-with-grub2-at-uefi/page-3#entry195438) để tìm hiểu về một số cách khác để boot Acronis True Image CD.

```bash
menuentry "Acronis True Image Home 2019 (ISO)" {
    set quiet=1
	set gfxpayload=1024x768x32,1024x768
	set mbrcrcs=on
	set isofile="/iso/AcronisTrueImage2019_14110.iso"
	search --set -f $isofile
	loopback loop $isofile
	linux (loop,msdos1)/dat10.dat lang=1 quiet force_modules=usbhid
	initrd (loop,msdos1)/dat11.dat (loop,msdos1)/dat12.dat
	boot
}
```

