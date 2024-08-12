---
layout: blog-post
title: Install Plymouth Stargate Theme in Ubuntu
author: Duc A. Hoang
categories:
  - "linux"
<!--comment: true-->
last_modified_at: 2024-03-16
description: This post describes how to install Plymouth Stargate Theme in Ubuntu
keywords: ubuntu, plymouth stargate, install
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post describes how to install a plymouth theme named [Stargate](https://www.deviantart.com/love2spooge/art/Plymouth-Stargate-Theme-193977103) in Ubuntu.
</div>

[Stargate Theme](https://www.deviantart.com/love2spooge/art/Plymouth-Stargate-Theme-193977103) is an awesome plymouth theme which I am now using for my Ubuntu Desktop. To install this theme, download {% include files.html name="plymouth_stargate_theme_by_love2spooge-d37hlov.zip" text="plymouth_stargate_theme_by_love2spooge-d37hlov.zip" %} and move the extracted folder to `/lib/plymouth/themes`.

Next, in terminal, type
```bash
sudo update-alternatives --install /lib/plymouth/themes/default.plymouth default.plymouth /lib/plymouth/themes/Stargate/Stargate.plymouth 100
```
To list all currently installed themes and input the number of the theme that you want to use, type
```bash
sudo update-alternatives --config default.plymouth
```
Finally, run the following command to apply the change
```bash
sudo update-initramfs -u
```
To fix the delayed loading of the splash, we can use
```bash
sudo -s
echo FRAMEBUFFER=y > /etc/initramfs-tools/conf.d/splash
update-initramfs -u
```
