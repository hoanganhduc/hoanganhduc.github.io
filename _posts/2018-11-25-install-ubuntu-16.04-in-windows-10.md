---
layout: blog-post
title: Install Ubuntu 16.04 in Windows 10
author: Duc A. Hoang
categories:
  - "linux"
  - "windows"
<!--comment: true-->
last_modified_at: 2024-02-28
description: This post describes how to install Ubuntu 16.04 in Windows 10
keywords: ubuntu 16.04, windows 10, windows subsystem for linux, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
In this post, I record how to install Ubuntu 16.04 in Windows 10 using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about).
</div>

# Enable Windows Subsystem for Linux (WSL)

Open PowerShell as Administrator and use the following command.

```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Restart Windows if asked.

# Download Ubuntu 16.04 Distro

You can download the distro from [https://aka.ms/wsl-ubuntu-1604](https://aka.ms/wsl-ubuntu-1604). At the time of writing this post, the file I downloaded is `Ubuntu.1604.2017.711.0_v1.appx`.

It is also possible to download the file using PowerShell

```bash
Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1604 -OutFile Ubuntu.appx -UseBasicParsing
```

# Installing your distro

Once I have downloaded `Ubuntu.1604.2017.711.0_v1.appx`, in PowerShell, I use

```bash
Rename-Item .\Ubuntu.1604.2017.711.0_v1.appx .\Ubuntu.1604.2017.711.0_v1.zip
Expand-Archive .\Ubuntu.1604.2017.711.0_v1.zip C:\Users\[your-windows-username]\Ubuntu # or pick any folder you like
```

Replace `[your-windows-username]` with your Windows username.

Next, move to `C:\Users\[your-windows-username]\Ubuntu` and run `ubuntu.exe` to [initialize the new distro](https://docs.microsoft.com/en-us/windows/wsl/initialize-distro).

Finally, add `C:\Users\[your-windows-username]\Ubuntu` to the Windows environment `PATH` using PowerShell

```bash
$userenv = [System.Environment]::GetEnvironmentVariable("Path", "User")
[System.Environment]::SetEnvironmentVariable("PATH", $userenv + "C:\Users\[your-windows-username]\Ubuntu", "User")
```

# Add username to `/etc/sudoers`

Suppose that your Ubuntu's username is `username`, then add `username ALL=(ALL:ALL) ALL` to `/etc/sudoers`.

# Set default login user

In CMD, use

```bash
ubuntu.exe config --default-user username
```

# Change Ubuntu mirrors

One can replace the default Ubuntu mirror `http://archive.ubuntu.com/ubuntu/` in `/etc/apt/sources.list` with others. See [Official Archive Mirrors for Ubuntu](https://launchpad.net/ubuntu/+archivemirrors).

# Vanilla TexLive

Before installing Vanilla TexLive as instructed [here](https://www.tug.org/texlive/debian.html), use

```bash
sudo update-alternatives --set fakeroot /usr/bin/fakeroot-tcp
```

# Add Bash to the context menu

See [this instruction](https://www.howtogeek.com/270810/how-to-quickly-launch-a-bash-shell-from-windows-10s-file-explorer/), or simply download [this ZIP archive](https://www.howtogeek.com/wp-content/uploads/2016/09/Add-Bash-to-the-Context-Menu.zip), unzip, and double-click the `Add Bash to Your Context Menu.reg` file to get the context menu option. Double-click the `Remove Bash From Your Context Menu.reg` file to remove the option.

# Re-mount C: drive

See [this page](https://blogs.msdn.microsoft.com/commandline/2018/01/12/chmod-chown-wsl-improvements/) for more details.

```bash
sudo umount /mnt/c
sudo mount -t drvfs C: /mnt/c -o metadata,uid=1000,gid=1000,umask=22,fmask=111 # the default user that gets created when WSL is first installed has a uid=1000 and gid=1000
```
