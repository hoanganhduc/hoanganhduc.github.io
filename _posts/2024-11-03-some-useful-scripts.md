---
layout: blog-post
title: Some Useful Scripts
author: Duc A. Hoang
categories:
  - "windows"
  - "linux"
<!--comment: true-->
last_modified_at: 2025-02-18
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

* Download [make.bat]({{site.baseurl}}/tex/make.bat) (for Windows) or [Makefile]({{site.baseurl}}/tex/Makefile) (for Linux).

# Crawling Articles Information with Specific Keywords

* This is a Python script.
* Download {% include files.html name="crawl_articles/crawl_articles.tar.gz" text="crawl_articles.tar.gz" %}, extract it, go to the `crawl_articles` folder, and run `pip install -r requirements.txt` to install some required libraries, then go back and run `python crawl.py --help` to see how to use it.

# A Workflow with GitHub and Overleaf

* See [A Workflow with GitHub and Overleaf]({% post_url 2024-12-20-a-workflow-with-github-and-overleaf %})

# Add a folder to Windows Explorer Navigation Pane

* See [this page](https://stackoverflow.com/a/34595293) or [this page](https://www.tenforums.com/customization/157121-add-specific-folders-navigation-pane.html) for more details.
* Download {% include files.html name="navigation_pane.bat" text="navigation_pane.bat" %}.

# Remove all workflow runs in a GitHub repository

* See [this page](https://stackoverflow.com/questions/57927115/delete-a-workflow-from-github-actions) for more details. This script requires [GitHub CLI](https://cli.github.com/).
* Download {% include files.html name="github/gh-remove-workflow-run.bat" text="gh-remove-workflow-run.bat" %} (for Windows) or {% include files.html name="github/gh-remove-workflow-run.sh" text="gh-remove-workflow-run.sh" %} (for Linux).

# Clone all branches of a GitHub repository

* Download {% include files.html name="github/gh-clone-all-branches.bat" text="gh-clone-all-branches.bat" %} (for Windows) or {% include files.html name="github/gh-clone-all-branches.sh" text="gh-clone-all-branches.sh" %} (for Linux).