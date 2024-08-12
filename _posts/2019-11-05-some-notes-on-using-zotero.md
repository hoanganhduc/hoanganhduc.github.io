---
layout: blog-post
title: "Some notes on using Zotero"
author: "Duc A. Hoang"
categories:
  - zotero
  - linux
  - windows
comment: true
last_modified_at: 2021-10-11
description: This post contains some notes on using Zotero
keywords: Zotero, WebDAV, usage, PaperShip, command-line
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This page contains some notes I want to remember when using [Zotero](https://www.zotero.org/).
</div>

# ZotFile Preferences

I use [ZotFile](http://zotfile.com/) for managing attachments. Here are some settings:

* In the **Tablet Settings** tab, I select *Use ZotFile to send and get files from tablet*. In the *Additional options* section, I selected "Save copy of annotated file with suffix" and set the value of the suffix as `_annotated`.
* In the **Renaming Rules** tab, I set *Format for all Item Types except Patents* as `{% raw %}{%a_}{%y_}{%t}{ [%T]}{% endraw %}`. I also set *Maximum length of title* as `150` and *Maximum number of authors* as `3` in the *Additional Settings* section of this tab. 
* In the **Advanced Settings** tab, I select *Only work with the following file types* option in the *Other Advanced Settings* section and set the following file types `pdf,doc,docx,txt,rtf,djvu,epub,mp4,ppt,pptx`.

# Better BibTeX Preferences

* In the **Citation keys** tab, I set *Citation key format* as `[auth:ascii][year][veryshorttitle:lower]`, which is somewhat similar to what Google Scholar would generate.

# WebDAV Sync

There is a [user-generated list of WebDAV services](https://www.zotero.org/support/kb/webdav_services) that users have reported success using with Zotero.
I personally use [TeraCLOUD](https://teracloud.jp/en/) (a free account provides 10GB storage space, and each successful referal gives you 2GB bonus space (probably more when having [campaign](https://teracloud.jp/en/campaign.html)) which you can use for one year). 
If you find the information about TeraCLOUD from this page and decide to use it with Zotero, I would be grateful if you could go to [your TeraCLOUD page](https://teracloud.jp/en/modules/mypage/usage/) and enter my introduce code **TEAYR** in the box *Enter friends Introduce code* of the *Get more capacity* section.
Please also note that *If you are using a free account and have not logged in for 90 days, the account and any data on TeraCLOUD will be deleted.*

# Dark Theme in Windows with `userchrome.css`

Create a folder `Chrome` in `%APPDATA%\Zotero\Zotero\Profiles\<some randome characters>.default\` and put the file {% include files.html name="userchrome.css" text="userchrome.css" %} (which is originally taken from [here](https://github.com/Rosmaninho/Zotero-Dark-Theme)) in that folder.

# PaperShip in iOS

I use the app [PaperShip](https://www.papershipapp.com/) to sync my Zotero library to my iPhone and iPad. Note that one needs to create a `lastsync.txt` file (which may be empty) in the `zotero` folder as instructed [here](https://forums.zotero.org/discussion/62579/papership-and-zotero-org-online-library-are-not-syncing) in order to make PaperShip correctly verifies the WebDAV server.

# Command-line interface

* [https://github.com/jbaiter/zotero-cli/](https://github.com/jbaiter/zotero-cli/)
* [https://zotero-cli.readthedocs.io/](https://zotero-cli.readthedocs.io/)

# Zotero for iOS beta (coming soon)

See [this page](https://www.zotero.org/iosbeta) for more information.

