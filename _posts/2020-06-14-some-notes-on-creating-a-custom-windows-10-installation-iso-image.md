---
layout: blog-post
title: Some notes on creating a custom Windows 10 installation ISO image
author: Duc A. Hoang
lang: en
categories:
  - windows
<!--comment: true-->
last_modified_at: 2021-11-27
description: This post contains some notes when creating a custom Windows 10 installation ISO image
keywords: windows, installation, custom, ISO image, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes which I want to remember when creating a custom Windows 10 installation ISO image.
</div>

[This post](https://www.tenforums.com/tutorials/72031-create-windows-10-iso-image-existing-installation.html) is a very clear guide on how to create a custom Windows 10 installation ISO image. It is also possible to create an ISO with [multiple Windows 10 images](https://www.tenforums.com/tutorials/133098-dism-create-bootable-iso-multiple-windows-10-images.html) and [multilingual support](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-multilingual-support-to-windows-setup). [This page](https://tb.rg-adguard.net/public.php) contains several links to original Windows 10 installation ISO images, and you can verify the downloaded images by seeking their SHA1SUMs [here](https://msdn.rg-adguard.net/). I use the ISO image of `Windows 10 Version 2004 - 20H1 (build 19041.264)` as the original one.

To install Microsoft Office, you can use [Office Deployment Tool
](https://www.microsoft.com/en-us/download/details.aspx?id=49117). The detailed instruction is [here](https://docs.microsoft.com/en-us/deployoffice/office-deployment-tool-configuration-options). I recommend you to download all necessary files before installation by running `setup.exe /download <path-to-configuration-file>` as Administrator. Here is an example of my configuration file `configuration.xml` for installing Microsoft Office 2021 Professional Plus Retail with only Word, Excel, and PowerPoint. To perform the installation, simply run `setup.exe /configure configuration.xml` as Administrator. See also [a list of Product IDs](https://docs.microsoft.com/en-us/office365/troubleshoot/installation/product-ids-supported-office-deployment-click-to-run). Remember to replace `<your-25-characters-product-key>` with the product key you purchased.

```bash
<Configuration>

  <Add OfficeClientEdition="64" Channel="Current">
    <Product ID="ProPlus2021Retail" PIDKEY="<your-25-characters-product-key>">
      <Language ID="en-us" />
      <ExcludeApp ID="Access" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="OneNote" />
      <ExcludeApp ID="Outlook" />
      <ExcludeApp ID="Publisher" />
      <ExcludeApp ID="Teams" />
    </Product>
  </Add>

  <Property Name="AUTOACTIVATE" Value="1" />
</Configuration>

```

It took me some time to figure out how to install apps in Windows 10 for all users. (For installing softwares, I use [chocolatey](https://chocolatey.org/). Another option might be the [Windows Package Manager Client (aka winget)](https://github.com/microsoft/winget-cli).) Basically, say, if I want to install [Facebook Messenger](https://www.microsoft.com/en-us/p/messenger/9wzdncrf0083), I go to [this page](https://store.rg-adguard.net/), paste the link from the Microsoft Store to get avaiable links for downloading the app for offline installation. Usually, you will have to download the `.Appx` (or `.AppxBundle`, and so on) file along with a `.BlockMap` file. For example, in my case, I downloaded `FACEBOOK.317180B0BB486_550.7.119.0_x64__8xx8rvfyw5nnt.appx` and `FACEBOOK.317180B0BB486_550.7.119.0_x64__8xx8rvfyw5nnt.BlockMap` files. Then, to install the app, open PowerShell as admin, move to the folder containing the downloaded files, and run `Add-AppxProvisionedPackage -Online -SkipLicense -PackagePath .\FACEBOOK.317180B0BB486_550.7.119.0_x64__8xx8rvfyw5nnt.appx`. Some package like [Microsoft Whiteboard](https://www.microsoft.com/en-us/p/microsoft-whiteboard/9mspc6mp8fm4) appears with its dependent packages when seeking download links, and you should also download and install them also. More information on the `Add-AppxProvisionedPackage` command can be found [here](https://docs.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=win10-ps). ~~Unfortunately, I have no idea why the Facebook Messenger app is not available for all users, while other apps, like Microsoft Whiteboard, are.~~ A better way is to add apps to `install.wim` as described [here](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism).
Here is the command I used to install Microsoft Whiteboard.

```bash
dism /Online /Add-ProvisionedAppxPackage /PackagePath:".\Microsoft.Whiteboard_20.10518.5186.0_x64__8wekyb3d8bbwe.Appx" /DependencyPackagePath:".\Microsoft.NET.Native.Framework.2.2_2.2.27912.0_x64__8wekyb3d8bbwe.Appx" /DependencyPackagePath:".\Microsoft.NET.Native.Runtime.2.2_2.2.28604.0_x64__8wekyb3d8bbwe.Appx" /DependencyPackagePath:".\Microsoft.VCLibs.140.00_14.0.27810.0_x64__8wekyb3d8bbwe.Appx" /SkipLicense
```

Another problem is to install language packs and their additional features. [This post](https://www.ntlite.com/community/index.php?threads/how-to-add-integrate-language-pack-language-feature-pack-into-a-iso-via-ntlite.978/post-10097) was quite useful for me. Basically, you will have to download a language interface package in `.Appx` format and several `.cab` files, as described in details [here](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-language-packs-to-windows). You may search for avaialble packages (note that I will need the build number to be at least newer than `19041.264`, since I use this build as my original installation) at [uupdump.ml](https://uupdump.ml/) (for instance, like [this](https://uupdump.ml/findfiles.php?id=cf03d086-4c37-43ba-8e18-e379fa99b140&q=language+pack)). At this page, the language pack may have extension `.esd`, and you can convert it to `.cab` with [this small commandline tool](https://github.com/abbodi1406/WHD/blob/master/scripts/ESD2CAB-CAB2ESD.zip). Finally, to install `.cab` files, use the command `dism /Online /Add-Package /PackagePath:\path\to\your\cab`. Here is an example of how I install Japanese and Vietnamese language packs and their features. (All packages are placed at the `.\lang\ja-jp` and `.\lang\vi-vn` folders.)

```bash
dism /Online /Add-Package /PackagePath:".\lang\ja-jp\microsoft-windows-client-languagepack-package_ja-jp-amd64-ja-jp.cab"
dism /Online /Add-ProvisionedAppxPackage /PackagePath:".\lang\ja-jp\LanguageExperiencePack.ja-JP.Neutral.appx" /LicensePath:".\lang\ja-jp\License.xml"
dism /Online /Add-Capability /CapabilityName:"Language.Basic~~~ja-JP~0.0.1.0" /CapabilityName:"Language.Handwriting~~~ja-JP~0.0.1.0" /CapabilityName:"Language.OCR~~~ja-JP~0.0.1.0" /CapabilityName:"Language.Speech~~~ja-JP~0.0.1.0" /CapabilityName:"Language.TextToSpeech~~~ja-JP~0.0.1.0" /Source:".\lang\ja-jp\"
dism /Online /Add-Package /PackagePath:".\lang\vi-vn\microsoft-windows-client-languagepack-package_vi-vn-amd64-vi-vn.cab"
dism /Online /Add-ProvisionedAppxPackage /PackagePath:".\lang\vi-vn\LanguageExperiencePack.vi-VN.Neutral.appx" /LicensePath:".\lang\vi-vn\License.xml"
dism /Online /Add-Capability /CapabilityName:"Language.Basic~~~vi-VN~0.0.1.0" /CapabilityName:"Language.TextToSpeech~~~vi-VN~0.0.1.0" /Source:".\lang\vi-vn\"
```

It is required to enable the [block clean-up of unused language packs](https://www.exitcodezero.ch/2018/08/16/gpo-block-clean-upofunusedlp/) setting; otherwise, Windows 10 will uninstall unused language packs which are not added to any user. Also, I added the line `PowerShell -Command "$A = Get-WinUserLanguageList; $A.Add('ja-jp'); $A.Add('vi-vn'); Set-WinUserLanguageList $A -force"` to the `RunOnce.bat` file (created as in [this tutorial](https://www.tenforums.com/tutorials/72031-create-windows-10-iso-image-existing-installation.html)) to initiate language packages at the first time a user login (see [this page](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/language-packs-known-issue) for more details).

You can also perform [many other settings](https://www.tenforums.com/tutorials/1977-windows-10-tutorial-index.html), like 
* [Add, Delete, Enable, or Disable Startup Items in Windows 10](https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html), 
* add [Open command windows here](https://www.tenforums.com/tutorials/72024-open-command-window-here-add-windows-10-a.html), [Open command windows here as administrator](https://www.tenforums.com/tutorials/59686-open-command-window-here-administrator-add-windows-10-a.html), [Open PowerShell windows here](https://www.tenforums.com/tutorials/60175-open-powershell-window-here-context-menu-add-windows-10-a.html), and [Open PowerShell windows here as administrator](https://www.tenforums.com/tutorials/60177-add-open-powershell-window-here-administrator-windows-10-a.html) to the context menu,
* add [secure delete](https://www.tenforums.com/tutorials/124286-add-secure-delete-context-menu-windows-10-a.html) to the context menu.

An useful toolkit for customizing your Windows installation is [Win Toolkit](https://www.wincert.net/forum/forum/179-win-toolkit/).
You may also need [DiskInternals' Linux Reader](https://www.diskinternals.com/linux-reader/) to read Linux file systems such as `ext4`.
