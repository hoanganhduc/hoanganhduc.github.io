---
layout: blog-post
title: Tor Browser Bundle
author: Duc A. Hoang
categories:
  - "linux"
comment: true
last_modified_at: 2024-03-12
description: This post describes how to install Tor Browser Bundle in Ubuntu
keywords: Ubuntu, Tor Browser Bundle
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
The [Tor software](https://www.torproject.org/) protects you by bouncing your communications around a distributed network of relays run by volunteers all around the world: it prevents somebody watching your Internet connection from learning what sites you visit, it prevents the sites you visit from learning your physical location, and it lets you access sites which are blocked. This post describes how to install Tor Browser Bundle in Ubuntu.
</div>

The [Tor Browser Bundle](https://www.torproject.org/download/) lets you use Tor on Windows, Mac OS X, or Linux without needing to install any software. It can run off a USB flash drive, comes with a pre-configured web browser to protect your anonymity, and is self-contained.

For downloading, go to [https://www.torproject.org/download/](https://www.torproject.org/download/).

**Update (February 26, 2014):** There is a PPA for Tor Browser Bundle made by [WebUpd8](http://www.webupd8.org/2013/12/tor-browser-bundle-ubuntu-ppa.html).

```bash
sudo add-apt-repository ppa:webupd8team/tor-browser
sudo apt-get update
sudo apt-get install tor-browser
```