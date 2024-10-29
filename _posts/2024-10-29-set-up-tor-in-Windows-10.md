---
layout: blog-post
title: Setup Tor in Windows
author: Duc A. Hoang
categories:
  - "windows"
<!--comment: true-->
last_modified_at: 2024-10-29
description: This post describes how Duc A. Hoang setup Tor in Windows
keywords: tor, windows, installation, Duc A. Hoang
<!--published: false-->
---

**Note:** It is better to use [Tor Browser Bundle]()

* Download the latest [Tor Expert Bundle](https://www.torproject.org/download/tor/).
* Extract the downloaded files to `C:\Tor`.
* Configure Tor as a service (see [here](https://superuser.com/a/1631196)). Run the commands in `cmd` as admin.
  ```
  echo( > C:\Tor\tor\torrc
  C:\Tor\tor\tor.exe --service install -options -f "C:\Tor\torrc"
  ``` 
  Use the following commands to start and stop the service
  ```
  C:\Tor\tor\tor.exe --service start
  C:\Tor\tor\tor.exe --service stop
  ```
* Setup proxy by running in `cmd` (not as an admin):
  ```
  REM Set the proxy server to
  powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -Name 'ProxyServer' -Value 'socks=127.0.0.1:9050'"
  REM Enable the proxy
  powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -Name 'ProxyEnable' -Value 1"
  ```