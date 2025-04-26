---
layout: blog-post
title: Some Useful Scripts
author: Duc A. Hoang
categories:
  - "windows"
  - "linux"
<!--comment: true-->
last_modified_at: 2025-04-25
description: This post contains some useful scripts
keywords: scripts, windows, linux, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post lists some useful scripts I've created (with assistance from [GitHub Copilot](https://docs.github.com/en/copilot)) for various tasks. All scripts are provided as-is with no warranty of compatibility with your operating system. Feel free to download, modify, and adapt them to your needs. Questions or suggestions are always welcome. 

* TOC
{:toc}

</div>

# Download a shared folder from Google Drive with `rclone`

* You will need to config [rclone](https://rclone.org/docs/) first.
* Download {% include files.html name="gdrive-shared-folder/gdrive-shared-folder.bat" text="gdrive-shared-folder.bat" %} (for Windows) or {% include files.html name="gdrive-shared-folder/gdrive-shared-folder.sh" text="gdrive-shared-folder.sh" %} (for Linux).

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

# Remove workflow runs in a GitHub repository

* See [this page](https://stackoverflow.com/questions/57927115/delete-a-workflow-from-github-actions) for more details. This script requires [GitHub CLI](https://cli.github.com/).
* Download {% include files.html name="github/gh-remove-workflow-run.bat" text="gh-remove-workflow-run.bat" %} (for Windows) or {% include files.html name="github/gh-remove-workflow-run.sh" text="gh-remove-workflow-run.sh" %} (for Linux).

# Clone all branches of a GitHub repository

* Download {% include files.html name="github/gh-clone-all-branches.bat" text="gh-clone-all-branches.bat" %} (for Windows) or {% include files.html name="github/gh-clone-all-branches.sh" text="gh-clone-all-branches.sh" %} (for Linux).

# Re-run a workflow in a GitHub repository

* Download {% include files.html name="github/gh-rerun-workflow.bat" text="gh-rerun-workflow.bat" %} (for Windows) or {% include files.html name="github/gh-rerun-workflow.sh" text="gh-rerun-workflow.sh" %} (for Linux). This script requires [GitHub CLI](https://cli.github.com/).

# Remove releases and tags in a GitHub repository

* Download {% include files.html name="github/gh-remove-release.bat" text="gh-remove-release.bat" %} (for Windows) or {% include files.html name="github/gh-remove-release.sh" text="gh-remove-release.sh" %} (for Linux). This script requires [GitHub CLI](https://cli.github.com/).

# Download releases from a GitHub repository

* Download {% include files.html name="github/gh-download-release.bat" text="gh-download-release.bat" %} (for Windows) or {% include files.html name="github/gh-download-release.sh" text="gh-download-release.sh" %} (for Linux). This script requires [GitHub CLI](https://cli.github.com/).

# Add certain copyright and metadata information to PDF files

* Download {% include files.html name="pdfs/add_copyright.py" text="add_copyright.py" %}. This Python script requires `PyPDF2`, `reportlab`, and `tqdm` libraries.
* Download {% include files.html name="pdfs/add_metadata.py" text="add_metadata.py" %}. This Python script requires `PyPDF2`, `pikepdf`, `bibtexparser`, and `rispy` libraries.

# Sign files with GPG

* Download {% include files.html name="gpg/gpg_sign_pdf.py" text="gpg_sign_pdf.py" %}.