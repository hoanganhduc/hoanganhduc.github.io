---
layout: blog-post
title: Setup Tor in Windows
author: Duc A. Hoang
categories:
  - "windows"
<!--comment: true-->
last_modified_at: 2024-10-30
description: This post describes how Duc A. Hoang setup Tor in Windows
keywords: tor, windows, installation, Duc A. Hoang
<!--published: false-->
---

**Note:** It is better to use [Tor Browser Bundle]()

* Download the latest [Tor Expert Bundle](https://www.torproject.org/download/tor/).
* Extract the downloaded files to `C:\Tor`.
* My configuration file `torrc` is in `C:\Tor\tor` and has the following content:
  ```
  ControlPort 9051
  CookieAuthentication 1
  DataDirectory C:\Tor\data
  SocksPort 9050
  ClientTransportPlugin meek_lite,obfs2,obfs3,obfs4,scramblesuit,webtunnel exec C:\Tor\tor\pluggable_transports\lyrebird.exe
  ClientTransportPlugin snowflake exec C:\Tor\tor\pluggable_transports\snowflake-client.exe
  ClientTransportPlugin conjure exec C:\Tor\tor\pluggable_transports\conjure-client.exe -registerURL https://registration.refraction.network/api
  GeoIPFile C:\Tor\data\geoip
  GeoIPv6File C:\Tor\data\geoip6
  ```
  Indeed, you can also use an empty `torrc` file.
* Configure Tor as a service (see [here](https://superuser.com/a/1631196)). Run the commands in `cmd` as admin.
  ```
  C:\Tor\tor\tor.exe --service install -options -f "C:\Tor\tor\torrc"
  ``` 
  Use the following commands to start and stop the service
  ```
  C:\Tor\tor\tor.exe --service start
  C:\Tor\tor\tor.exe --service stop
  ```
* Setup proxy by running in `cmd` (not as an admin) the following commands (Note that commands starting with `REM` are comments, and you can simply ignore them):
  ```
  REM Set the proxy server
  powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -Name 'ProxyServer' -Value 'socks=127.0.0.1:9050'"
  REM Enable the proxy
  powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -Name 'ProxyEnable' -Value 1"
  ```