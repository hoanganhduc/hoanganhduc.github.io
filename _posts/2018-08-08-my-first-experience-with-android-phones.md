---
layout: blog-post
title: My first experience with Android phones
author: Duc A. Hoang
categories:
  - "linux"
<!--comment: true-->
description: This post describes Duc A. Hoang's first experience with Android phones
keywords: phone, SonyXperia SP, experience, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
Recently, my iPhone 5 has been broken. 
I got a chance to play with an old phone of my sister--a [Sony Xperia SP C5303](https://en.wikipedia.org/wiki/Sony_Xperia_SP).
In this post, I described my experience with installing Android and other apps in this phone.
</div>

# Unlocking Bootloader

Originally, the phone was installed with a Sony's version of Android JellyBean 4.3.
The system works OK.
However, I want to install some Android 8 custom ROMs in this phone.
To do that, I need to unlock the phone's bootloader, as instructed [here](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/). 
Unfortunately, the process somehow does not work with my Windows 10 64-bit, and I have to switch to a computer with Windows 7 32-bit.
The steps are as follows.

1. Check if the phone's bootloader can be unlocked: Type `*#*#7378423#*#*#`, then choose `Service info --> Configuration --> Rooting status`.
  * `Bootloader unlocked : Yes` (The phone's bootloader has been unlocked).
  * `Bootloader unlock allowed : Yes` (The phone's bootloader has not been unlocked).
  * `Bootloader unlock allowed : No` (The phone's bootloader cannot be unlocked).
2. Install the device drivers and platform tools.
  * For Windows: Download and install the latest [USB drivers](https://developer.android.com/studio/run/win-usb.html). Follow the instructions on the site.
3. Download and extract the [Platform tools](https://developer.android.com/studio/releases/platform-tools.html) zip file.
4. On your device, turn on `USB debugging` by going to `Settings --> Developer options` and click to enable USB debugging.
For Android 4.2+, the `Developer options` are hidden by default.
To enable, tap on `Settings --> About Phone --> Build Version` multiple times (around 7 times).
5. Connect to Fastboot
  * Turn off your device.
  * Connect a USB-cable to your computer.
  * On your device, press the Volume up key at the same time as you connect the other end of the USB-cable.
  * When your device is connected, open a command window on your computer and go to the platform-tools folder within the Android SDK folder. Enter `fastboot devices` and verify that you get an answer back without any error.
6. Enter the [unlock key](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/) taken from Sony, using the command `fastboot -i 0x0fce oem unlock 0x[insert your unlock code]`

For steps 2 and 3, I recommend download and install [KingoRoot](https://www.kingoapp.com/). 
It automatically installs the USB drivers of your phone, and contains a collection of SDK platform tools which we can use.


# TWRP Recovery

To flash a customed ROM to the phone, I need [TWRP Recovery](https://twrp.me/).
Basically, what I did are:
* Connect to Fastboot.
* Download [twrp-3.2.2-20180708-boot-huashan.img](https://basketbuild.com/filedl/devs?dev=AdrianDC&dl=AdrianDC/Huashan/TWRP-Recovery/twrp-3.2.2-20180708-boot-huashan.img) and flash the image with `fastboot flash boot twrp-3.2.2-20180708-boot-huashan.img`.
* Reboot the system. The phone will boot into TWRP Recovery 3.2.2.
* Copy the custom ROM (ZIP file) to the phone, and flash it with TWRP. Some custom ROMs for Sony Xperia SP are:
  * [AOSP 8.1.0 Oreo](https://forum.xda-developers.com/xperia-sp/orig-development/rom-aosp-oreo-xperia-sp-t3666304).
  * [AOSP Extended 5.4](https://downloads.aospextended.com/huashan/).
  * [LinegaOS](https://download.lineageos.org/huashan).
* Flash [OpenGapps](http://opengapps.org/), I used the ARM 8.1 pico version.

# Rooting the device

The instruction is [here](https://forum.xda-developers.com/crossdevice-dev/sony/mod-boot-bridge-sony-elf-t3506883).

# Some apps I installed

* `SuperSU`: For managing root access.
* `K-9 Mail` and `OpenKeychain`: For sending email with [my PGP signature](https://keybase.io/hoanganhduc#show-public). 
Other interesting features of `K-9 Mail` are exporting/importing app settings, and using dark theme.
* `Orbot`: For browsing Internet with [Tor](https://www.torproject.org/).
* `Termux` and `BusyBox`: For playing with Linux commands in Android. You may also need `Hacker's Keyboard`. At the first time using `Termux`, you should use the command `termux-setup-storage` to allow `Termux` access to your storage devices.
* `SHAREit`: For sharing files among different devices.
* `VLC`: For playing audio and video files. An interesting feature is that it allows the option for playing music in the background.

# Screenshot

Here are some screenshots from the phone after I completed the configuration and settings.

{% include image.html name="screen1.png" %}
{% include image.html name="screen2.png" %}
{% include image.html name="screen3.png" %}
{% include image.html name="screen4.png" %}
