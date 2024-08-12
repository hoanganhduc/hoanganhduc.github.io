---
layout: blog-post
title: Clone/Backup Ubuntu Systems Using Mondo Rescue
author: Duc A. Hoang
categories:
  - "linux"
comment: true
last_modified_at: 2022-11-25
description: This post describes how to clone/backup Ubuntu system using Mondo Rescue
keywords: ubuntu, backup, clone, mondo rescue
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
[Mondo Rescue](http://mondorescue.org/) is an open source, free disaster recovery and backup utility that allows you to easily create complete system (Linux or Windows) Clone/Backup ISO Images to CD, DVD, Tape, USB devices, Hard Disk, and NFS. And can be used to quickly restore or redeploy working image into other systems, in the event of data loss, you will be able to restore as much as entire system data from backup media. Mondo program is available freely for download and released under GPL (GNU Public License) and has been tested on a large number of Linux distributions. This post describes how to clone/backup Ubuntu system using Mondo Rescue. 
</div>

# Installation
To install Mondo Rescue in Ubuntu 12.10, 12.04, 11.10, 11.04, 10.10 and 10.04 or Linux Mint 13, open the terminal and add the MondoRescue repository in `/etc/apt/sources.list` file. Run these following commands to install Mondo Resuce packages.

```bash
wget ftp://ftp.mondorescue.org/ubuntu/`lsb_release -r|awk '{print $2}'`/mondorescue.sources.list
sudo sh -c "cat mondorescue.sources.list >> /etc/apt/sources.list"
sudo apt-get update
sudo apt-get install mondo
```

# Clone/Backup Ubuntu
After installing Mondo, run the following command as `root` user to backup the system. Replace `[username]` with your username and `[machine]` with any prefix name you want to use for generating ISO files.

```bash
mondoarchive -OV -0 -G -E "/home/[username]/Download|/home/[username]/Documents|/home/[username]/Music|/home/[username]/Videos|/home/[username]/Pictures|/home/[username]/Desktop" -i -s 4480m -p "[machine]" -d /
```

The meaning of the options:

* `-OV` 
<br />backup your PC and verify your backup

* `-[0-9]` 
<br />Specify the compression level. Default is 3. No compression is 0.

* `-G` 
<br />Use gzip, the standard and quicker Linux compression engine, instead of bzip2.

* `-E "dir|..."` 
<br />Exclude dir(s) from backup. The dirs should be separated with a pipe and surrounded by quotes. This is the prefered and recommended option when doing partial archiving. Note that mondo automatically excludes removable media (`/mnt/floppy`, `/mnt/cdrom`, `/proc`, `/sys`, `/run`, `/tmp`). For example, if you are backing up to an NFS mount but you do not want to include the contents of the mount in a backup, exclude your local mount-point with this switch.

* `-i` 
<br />Use ISO files (CD images) as backup media. This is good for backing up your system to a spare hard drive.

* `-p "prefix-name"` 
<br />Use prefix to generate the name of your ISO images. By default, mondoarchive names images `mondorescue-1.iso`, `mondorescue-2.iso`,... Using `-p "machine"` will name your images `machine-1.iso`, `machine-2.iso`,...

* `-s size` 
<br />How much can each of your backup media hold? You may use `m` and `g` on the end of the number, e.g. `700m` for an extra-large CD-R, or `4480m` for a normal DVD-R.

* `-I "dir|..."` 
<br />Include dirs(s) in backup. The dirs should be separated with a pipe and surrounded by quotes. This option is mainly used to perform tests in order to reduce the time taken by the archiving operation. The default backup dir is / but you may specify alternatives.

* `-d dev|dir` 
<br />Specify the backup device (CD/tape/USB) or directory (NFS/ISO). For CD-R[W] drives, this is the SCSI node where the drive may be found, e.g. `0,1,0`. For tape users, this is the tape streamers `/dev` entry, e.g. `/dev/st0`. For USB users, this is the device name of your key or external disk. For ISO users, this is the directory where the ISO images are stored. For NFS users, this is the subdirectory under the NFS mount where the backups are stored. The default for ISO and NFS is `/var/cache/mondo`.

# References
For more information, there is a detail explanation at [http://www.tecmint.com/how-to-clone-linux-systems/](http://www.tecmint.com/how-to-clone-linux-systems/) and [http://www.mondorescue.org/docs/mondoarchive.8.html](http://www.mondorescue.org/docs/mondoarchive.8.html).
