---
layout: default
title: "Homepage of Duc A. Hoang (Hoàng Anh Đức)"
permalink: "/"
last_modified_at: 2024-04-20
mathjax: true
---

{% include author-info.html %}

-----

# Introduction

{% assign myCV-en = site.static_files | where_exp: "file", "file.path contains 'CV.pdf'" %}
{% assign myCV-vi = site.static_files | where_exp: "file", "file.path contains 'CV-vi.pdf'" %}
{% assign student-info = site.static_files | where_exp: "file", "file.path contains 'Information_for_Students.pdf'" %}

* As of February 01, 2023, I am a *Lecturer* at [VNU-HUS](http://hus.vnu.edu.vn/) (Hanoi, Vietnam). In 2024, I also visit [VIASM](https://viasm.edu.vn) (supported by [VIAMS's one-year postdoctoral fellowship](https://viasm.edu.vn/en/information-for-applicants/call-for-applicants/detail/announcement-call-for-proposals-2024)).
* From September 05, 2018 to December 31, 2018, I was a *Lecturer* at [VNU-HUS](http://hus.vnu.edu.vn/) (Hanoi, Vietnam). From April 01, 2019 to June 15, 2021, I was a *Postdoc* (partially supported by KAKENHI Grant Number [19K24349](https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-19K24349/)) and then a *Research Assistant* (from April 01, 2021) at [Kyutech](https://www.kyutech.ac.jp) (Fukuoka, Japan) under the direction of [Toshiki SAITOH](http://algorithm.ces.kyutech.ac.jp/wp/members/saitoh/). From June 16, 2021 to January 31, 2023, I was a *Postdoc* at [Kyoto University](https://www.kyoto-u.ac.jp/) (Kyoto, Japan) under the direction of [Shin-ichi MINATO](http://www.lab2.kuis.kyoto-u.ac.jp/minato), in the [B01 Group](https://afsa.jp/en/member/#b01) of the [AFSA Project](https://www.afsa.jp/en/) (supported by KAKENHI Grant Number [20H05964](https://kaken.nii.ac.jp/en/grant/KAKENHI-PLANNED-20H05964/)). (See also [my (deleted) profile in KyotoU's database](https://web.archive.org/web/20220702024653/https://kdb.iimc.kyoto-u.ac.jp/profile/en.5844068fa96cdf8c.html) and [my brief introduction in AFSA News Letter No. 4 (Oct. 2022)]({{ site.baseurl }}/misc/AFSA_News_Letter/AFSA_no4_web.pdf).)
* I received the B.Math degree ([Advanced Undergraduate Program in Mathematics](http://mim.hus.vnu.edu.vn/sites/default/files/KCT_TTToan_Final.pdf)) from [VNU-HUS](http://hus.vnu.edu.vn/) (Hanoi, Vietnam) in 2013, and the M.S. and Ph.D. degrees ([Information Science](https://www.jaist.ac.jp/english/areas/information-science.html)) respectively in 2015 and 2018 from [JAIST](https://www.jaist.ac.jp/) (Ishikawa, Japan) under the advice of [Ryuhei UEHARA](https://www.jaist.ac.jp/~uehara/).
* My [list of publications]({% link publications.md %}) (see also [DBLP]({{ site.dblp_url }}), [Google Scholar]({{ site.googlescholar_url }}), [Researchmap]({{ site.researchmap_url }}), and some eprints on [arXiv]({{ site.arxiv_url }})). 
* Some [events]({% link events.md %}) where my co-author(s) or I gave a (oral/poster) presentation of our research.
* Some [open problems]({% link problems/index.md %}) I am interested in.
* Some other [activities]({% link activities.md %}).
* Some [courses]({% link teaching.md %}) which I participated in as a *TA* or *Lecturer*. (Some related materials may be available.)
* Some of [my visitors]({% link visitors.md %}).
* Some [students]({% link students.md %}) whom I have worked with. See also [some information for potential students]({{ student-info[0].path }}) who want to work with me on a research problem.
* More details can be found in [my CV]({{ myCV-en[0].path }}).
* Some [miscellaneous stuff]({% link misc.md %}).

-----

<div class="alert alert-announce" markdown="1">
<!-- <h1 class="alert-heading">Announcement</h1> -->

* The [call for presentations](https://dmatheorynet.blogspot.com/2024/04/dmanet-5th-combinatorial.html) of [the 5th **Co**mbinatorial **Re**configuration Workshop (CoRe 2024)](https://joint.imi.kyushu-u.ac.jp/post-15540/) has been announced. The conference's venue is in Fukuoka, Japan. The submission deadline is July 7, 2024, 23:59 (AoE).
* Some events for math and CS students.
  * [VIASM REU](https://viasm.edu.vn/hdkh/VIASM-REU-2024). Deadline: May 15, 2024.
  * [Application Driven Mathematics](https://institute.vinbigdata.org/programs/application-driven-mathematics/). Application: From April 07 to May 15, 2024.
  * [Thực tập nghiên cứu khoa học tại Viện Toán học năm 2024](http://math.ac.vn/vi/news/1374-thuctapnckh2024.html). Deadline: April 29, 2024. 

</div>

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
