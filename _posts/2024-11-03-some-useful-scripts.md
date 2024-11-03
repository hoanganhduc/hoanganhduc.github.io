---
layout: blog-post
title: Some Useful Scripts
author: Duc A. Hoang
categories:
  - "windows"
  - "linux"
<!--comment: true-->
last_modified_at: 2024-11-03
description: This post contains some useful scripts
keywords: scripts, windows, linux, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some useful scripts that I have written with the help of [GitHub Copilot](https://docs.github.com/en/copilot). You can download and modify them as you see fit.

* TOC
{:toc}

</div>

# Download a shared folder from Google Drive with `rclone`

* You will need to config [rclone](https://rclone.org/docs/) first.
* Download {% include files.html name="gdrive-shared-folder/run.bat" text="run.bat" %} (for Windows) or {% include files.html name="gdrive-shared-folder/run.sh" text="run.sh" %} (for Linux).

# Create a file `.timestamps` to back up/restore the updated time of all files/folders in a folder

* This is a bash script used in Linux.
* Download {% include files.html name="linux-timestamps/timestamp.sh" text="timestamp.sh" %}.

# Quickly handling TeX files

* Download {% include files.html name="latex/make.bat" text="make.bat" %} (for Windows) or {% include files.html name="latex/Makefile" text="Makefile" %} (for Linux).