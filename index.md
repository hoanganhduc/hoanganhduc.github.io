---
layout: default
title: "Homepage of Duc A. Hoang (Hoàng Anh Đức)"
permalink: "/"
last_modified_at: 2023-08-01
mathjax: true
---

{% include author-info.html %}

-----

# Introduction

{% assign myCV-en = site.static_files | where_exp: "file", "file.path contains 'CV.pdf'" %}
{% assign myCV-vi = site.static_files | where_exp: "file", "file.path contains 'CV-vi.pdf'" %}

* As of February 01, 2023, I am a *Lecturer* at [VNU-HUS](http://www.hus.vnu.edu.vn/) (Hanoi, Vietnam).
* From September 05, 2018 to December 31, 2018, I was a *Lecturer* at [VNU-HUS](http://www.hus.vnu.edu.vn/) (Hanoi, Vietnam). From April 01, 2019 to June 15, 2021, I was a *Postdoc* (partially supported by KAKENHI Grant Number [19K24349](https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-19K24349/)) and then a *Research Assistant* (from April 01, 2021) at [Kyutech](https://www.kyutech.ac.jp) (Fukuoka, Japan) under the direction of [Toshiki SAITOH](http://algorithm.ces.kyutech.ac.jp/wp/members/saitoh/). From June 16, 2021 to January 31, 2023, I was a *Postdoc* at [Kyoto University](https://www.kyoto-u.ac.jp/) (Kyoto, Japan) under the direction of [Shin-ichi MINATO](http://www.lab2.kuis.kyoto-u.ac.jp/minato), in the [B01 Group](https://afsa.jp/en/member/#b01) of the [AFSA Project](https://www.afsa.jp/en/) (supported by KAKENHI Grant Number [20H05964](https://kaken.nii.ac.jp/en/grant/KAKENHI-PLANNED-20H05964/)). (See also [my (deleted) profile in KyotoU's database](https://web.archive.org/web/20220702024653/https://kdb.iimc.kyoto-u.ac.jp/profile/en.5844068fa96cdf8c.html) and [my brief introduction in AFSA News Letter No. 4 (Oct. 2022)]({{ site.baseurl }}/misc/AFSA_News_Letter/AFSA_no4_web.pdf).)
* I received the B.Math degree ([Advanced Undergraduate Program in Mathematics](http://mim.hus.vnu.edu.vn/sites/default/files/KCT_TTToan_Final.pdf)) from [VNU-HUS](http://www.hus.vnu.edu.vn/) (Hanoi, Vietnam) in 2013, and the M.S. and Ph.D. degrees ([Information Science](https://www.jaist.ac.jp/english/areas/information-science.html)) respectively in 2015 and 2018 from [JAIST](https://www.jaist.ac.jp/) (Ishikawa, Japan) under the advice of [Ryuhei UEHARA](https://www.jaist.ac.jp/~uehara/).
* My [list of publications]({% link publications.md %}) (see also [DBLP]({{ site.dblp_url }}), [Google Scholar]({{ site.googlescholar_url }}), [Researchmap]({{ site.researchmap_url }}), and some eprints on [arXiv]({{ site.arxiv_url }})). 
* Some [events]({% link events.md %}) where my co-author(s) or I gave a (oral/poster) presentation of our research.
* Some [open problems]({% link problems/index.md %}) I am interested in.
* Some [courses]({% link teaching.md %}) which I participated in as a *TA* or *Lecturer*. (Some related materials may be available.)
* More details can be found in [my CV]({{ myCV-en[0].path }}).
* Some [miscellaneous tips]({% link tips.md %}) I collected on doing research in TCS.
* Some [miscellaneous stuff]({% link misc.md %}).

-----

# News

<div class="table-noborder" style="height: 200px; overflow-y: scroll;">
<table>
{% for item in site.data.news %}    
<tr style="padding: 10px;">
    <td style="width: 20%;" {% unless item.present %}class="text-muted"{% endunless %}><strong>{{ item.time }}</strong></td> 
    <td style="width: 80%;" {% unless item.present %}class="text-muted"{% endunless %}>{% if item.important %}<span style="color:red; font-weight: bold;">[NEW] </span>{% endif %}{% if item.future %}<span style="color: #228B22; font-weight: bold;">[COMING SOON] </span>{% endif %}{{ item.text }}</td>
</tr>
{% endfor %}
</table>
</div>
