---
layout: blog-post
title: YouTube Subscriptions to RSS Feeds
author: Duc A. Hoang
categories:
  - linux
  - windows
<!--comment: true-->
last_modified_at: 2021-12-14
description: This post describes how to export YouTube subscriptions to RSS feeds
keywords: youtube, subscriptions, rss, export
<!--published: false-->
---

An old way of exporting YouTube subscriptions to RSS feeds is to go to the [Subscription Manager](https://www.youtube.com/subscription_manager) page of YouTube and simply click the `Export subscriptions` button to download the exported `.opml` file.
Currently, I cannot do it.
So, here is a workaround I found from the Internet.

* Go to [https://www.youtube.com/feed/channels](https://www.youtube.com/feed/channels).
* Open Google Chrome (you may use another browser), press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd> to open the console prompt.
* Paste `$$("#main-link.channel-link").reduce((str, el)=>str+'\n'+el.href)` to receive a list of YouTube channels and users you subscribed to.
* RSS for YouTube channels and users are of the following formats:
  * For channels: `https://www.youtube.com/feeds/videos.xml?channel_id=[channel id]`.
  * For users: `https://www.youtube.com/feeds/videos.xml?user=[username]`.
* From the list you received, replace all `https://www.youtube.com/user/` by `https://www.youtube.com/feeds/videos.xml?user=`, and `https://www.youtube.com/channel/` by `https://www.youtube.com/feeds/videos.xml?channel_id=`. You now have a list of RSS feeds of your YouTube subscriptions.
* Go to [https://opml-gen.ovh/](https://opml-gen.ovh/), paste the RSS feeds list to add them into a single file `subscriptions.xml`.
* You can now import it to your favourite RSS reader; for example, I like [Feedly](https://feedly.com/) and [QuiteRSS](https://quiterss.org/). Note that if you use Feedly, you can import/export `.opml` from [https://feedly.com/i/organize/me](https://feedly.com/i/organize/me). 

**Note (2021-07-25):** The script `$$("#main-link.channel-link").reduce((str, el)=>str+'\n'+el.href)` no longer works. You may probably try [this Python script](https://stackoverflow.com/a/38825902) to get a list of the channels you subscribed to. A simpler option is to export your YouTube data via [Google Takeout](https://takeout.google.com/). After extracting the generated ZIP file from Takeout, you can go to the folder `Takeout/YouTube and YouTube Music/subscriptions` and there is a `subscriptions.csv` file containing the list of your YouTube subscriptions. 

**Note (2021-12-14):** Arkadij Orlov created a [script](https://gist.github.com/arkov/e8c0d463c9817d4b0b90462992589198) to extract a list of RSS feeds of your YouTube subscriptions.