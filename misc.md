---
layout: default
title: "Miscellaneous Stuff"
permalink: /misc/
last_modified_at: 2025-05-03
description: This page contains a collection of miscellaneous stuff that Duc A. Hoang is interested in
keywords: miscellaneous stuff, Duc A. Hoang
<!--sitemap: false-->
<!--published: false-->
buymeacoffee: true
---

<div class="row">
<div class="col-xs-12 col-sm-4 col md-4 col-lg-4" markdown="1">

* TOC
{:toc}

</div>

<div class="col-xs-12 col-sm-8 col-md-8 col-lg-8" markdown="1">
* Some of my [Zotero Collections]({{ site.baseurl }}/zotero/).
* I maintain [a webpage for collaboration](https://coauthor.hoanganhduc.org/) where I [deployed]({% link _posts/2024-10-25-some-notes-on-deploying-coauthor.md %}) a copy of the [coauthor](https://github.com/edemaine/coauthor) tool. See [this page](https://github.com/edemaine/cosuite) for more tools and information.
* I occasionally maintain a [non-exhaustive list of some resources]({% link reconf/index.md %}) related to [Combinatorial Reconfiguration](https://en.wikipedia.org/wiki/Reconfiguration).
* My [YouTube channel](https://www.youtube.com/@hoanganhduc).
  * See also a [Combinatorial Reconfiguration Playlist](https://youtube.com/playlist?list=PL7G0wYDBSwEb_YmR0ZGD7tD2lSh_mqlmG).
<!-- * See [this video (in Vietnamese)](https://www.youtube.com/watch?v=42jVt0YnAZc) which was made in 2021 by students who have been taught by Thầy giáo Nguyễn Hữu Mại (Đình Bảng, Từ Sơn, Bắc Ninh) from 2005 to 2008 (including me). The goal is to tribute Thầy Mại on the occasion of the Vietnamese Teacher Day. -->
* See [this page]({% link translation/index.md %}) for some documents I translated.
* See [this page]({% link tex/index.md %}) for all TeX resources I created/collected.
* Some [Chocolatey packages](https://chocolatey.org/profiles/hoanganhduc) (see also [this page](https://github.com/hoanganhduc/chocolatey)) and [AUR packages](https://aur.archlinux.org/packages/?K=hoanganhduc&SeB=m) I am maintaining.
* [Overleaf](https://www.overleaf.com?r=b42dc7aa&rm=d&rs=b) -- An online LaTeX editor which is quite useful for research collaborations.
* [InfiniCLOULD](https://infini-cloud.net/en/) -- A nice cloud storage service that supports WebDAV. I mainly use this service for storing data in my [Zotero](https://www.zotero.org/) library. Initially, you can have 20GB of storage space for free. If you find it useful, enter my referal code **TEAYR** in your InfiniCLOUD's [My Page](https://infini-cloud.net/en/modules/mypage/) to help me get extra 2GB bonus space for one year.
* [temp.sh](https://temp.sh) -- Upload and share files from command line.
* [This page]({% link misc/AFSA_News_Letter/index.md %}) contains a list of PDF copies of [AFSA](https://afsa.jp/) News Letter in Japanese.
* **Chế USB vừa cài Windows XP, vừa chạy Hiren's Boot**, Tạp chí Echip, số 438, ra ngày 30/06/2009 (thứ 3), trang 11. [[PDF]({{ site.baseurl }}/misc/e_chip_dxvl_438_3922.pdf)] (Một số công cụ kèm theo bài viết: [menu.lst]({{ site.baseurl }}/misc/menu.lst), [Hiren's Boot ISO](https://www.hirensbootcd.org/old-versions/).)

</div>
</div>

-----

# Miscellaneous Writings

Some of these originally appeared in an <a href="https://toihoctap.wordpress.com/">old (deleted) WordPress blog</a> of mine. 
{% for post in site.posts %}
* <a href="{{ post.url }}">{{ post.title }}</a> <time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">({% if post.lang == "vi" %}<b>Cập nhật:</b> {{ post.last_modified_at | date: "%d tháng %m, %Y" }}{% else %}<b>Updated:</b> {{ post.last_modified_at | date: "%B %d, %Y" }}{% endif %})</time>{% endfor %}

# Getting Scientific Papers/Books/etc.

* **(For Vietnamese)** [Online Portal](https://db0.vista.gov.vn) maintained by Vietnamese [National Agency for Science and Technology Information](https://vista.gov.vn).
* If you cannot get a paper, **get in touch with the (corresponding) author(s) to ask for a copy before trying the following resources.** 
  * [AbleSci](https://www.ablesci.com) – request published papers from the community (suggested to me by [Van-Giang Trinh](https://giang-trinh.github.io)).
  * [Mutual Aid-Science Community](http://www.wosonhj.com/) – request published papers from the community.
  * [Sci-Hub](https://sci-hub.se/) and [Sci-Net](https://sci-net.xyz/).
  * [Z-Library](https://singlelogin.se).
    * Desktop app: [Windows](https://go-to-zlibrary.se/soft/zlibrary-setup-latest.exe), [macOS](https://go-to-zlibrary.se/soft/zlibrary-setup-latest.dmg), [Linux (DEB)](https://go-to-zlibrary.se/soft/zlibrary-setup-latest.deb).
  * [Library Genesis](https://libgen.rs) (LibGen).
  * [Anna's Archive](https://annas-archive.org/).
  * [PDFDrive](https://www.pdfdrive.com).

# Advice and Inspiration

* Paul R. Halmos's advice on [How to write Mathematics](https://bookstore.ams.org/hwm). [[PDF](https://entropiesschool.sciencesconf.org/data/How_to_Write_Mathematics.pdf)] 
* [Writing Mathematical Papers---a Few Tips](https://web.archive.org/web/20231215125337/https://www.impan.pl/wydawnictwa/dla-autorow/writing.pdf), [Writing Mathematical Papers in English: a practical guide](https://doi.org/10.4171/014), and [Mathematical English Usage. A Dictionary](https://www.emis.de/monographs/Trzeciak/), by [Jerzy Trzeciak](https://www.impan.pl/~trzeciak/).
* Ian Parberry's advice on [giving a presentation](http://ianparberry.com/pubs/speaker.pdf) (also see [his paper with Bob Spillman](http://ianparberry.com/pubs/NAMSSpeakersGuide.pdf)) and [reviewing a paper](http://ianparberry.com/pubs/referee.pdf).
* [The Task of the Referee](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1989/CSD-89-511.pdf) (Alan J. Smith).
* [PC chair and general chair guidelines for TCS conferences](https://thmatters.wordpress.com/2023/08/22/1443/).
* [A Guide for New Program Committee Members at Theoretical Computer Science Conferences](https://arxiv.org/abs/2105.02773).
* [Ten Lessons I Wish I Had Been Taught](https://www.ams.org/notices/199701/comm-rota.pdf) (Gian-Carlo Rota).
* [Non-Technical Talks by David Patterson, U.C. Berkeley](https://people.eecs.berkeley.edu/~pattrsn/talks/nontech.html).
* [You and Your Research](https://youtu.be/a1zDuOPkMSw) (Richard Hamming, [Transcript](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html)).
* [Are you interested in theoretical computer science? (How not???) I have some advice for you](http://bulletin.eatcs.org/index.php/beatcs/article/view/415) (Michael Fellows).
* [EATCS Fellows' Advice to the Young Theoretical Computer Scientist.](http://bulletin.eatcs.org/index.php/beatcs/article/view/419) (Luca Aceto with contributions by: Mariangiola Dezani-Ciancaglini, Yuri Gurevich, David Harel, Monika Henzinger, Giuseppe F. Italiano, Scott Smolka, Paul G. Spirakis, Wolfgang Thomas).
* [A Few Lessons I've Learned](http://bulletin.eatcs.org/index.php/beatcs/article/view/129) (Erik D. Demaine).
* [The Ph.D Experience](https://cseweb.ucsd.edu/~mihir/phd.html) (Mihir Bellare).
* [Jukka Suomela](https://jukkasuomela.fi/)'s [career advice for TCS Postdocs](https://jukkasuomela.fi/career-advice/).
* [Math Study Tips](https://web.uvic.ca/~gmacgill/Pointers2.pdf) (Gary MacGillivray).
* [DOCUMENTA MATHEMATICA Extra Volume: Optimization Stories (2012)](https://www.emis.de/journals/DMJDMV/vol-ismp/60_liebling-thomas.html).
* [How the proof of the strong perfect graph conjecture was found](https://web.math.princeton.edu/~pds/papers/howtheperfect/howtheperfect.pdf), by [Paul Seymour](https://web.math.princeton.edu/~pds/).
* [Steven G. Krantz](https://www.math.wustl.edu/~sk/)'s books: 
  * [A Mathematician's Survival Guide: Graduate School and Early Career Development](https://bookstore.ams.org/gscm).
  * [The Survival of a Mathematician: From Tenure-Track to Emeritus](https://bookstore.ams.org/mbk-60) ([draft](https://www.math.wustl.edu/~sk/books/newsurv.pdf)). 
  * [A Primer of Mathematical Writing](https://bookstore.ams.org/mbk-112) ([arXiv:1612.04888](https://arxiv.org/abs/1612.04888)).
* [Scientific Paper Writing: A Survival Guide](https://www.chemistryworld.com/review/scientific-paper-writing-a-survival-guide/1010246.article), by [Bodil Holst](https://www.uib.no/en/persons/Bodil.Holst), illustrated by Jorge Cham of [PhD Comics](http://phdcomics.com/).
* Terence Tao's [career advice](https://terrytao.wordpress.com/career-advice/).
* Fan Chung Graham's [A few words on research for graduate students](https://www.math.ucsd.edu/~fan/teach/gradpol.html).
* [Simon Peyton Jones](https://simon.peytonjones.org)'s advice on [How to Write a Great Research Paper](https://www.youtube.com/watch?v=VK51E3gHENc) ([PDF slides](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/How-to-write-a-great-research-paper.pdf), [PPT Slides](https://www.microsoft.com/en-us/research/uploads/prod/2016/08/How-to-write-a-great-research-paper.pptx)), [How to Give a Great Research Talk](https://www.youtube.com/watch?v=sT_-owjKIbA) ([PDF slides](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/giving-a-talk.pdf), [PPT Slides](https://www.microsoft.com/en-us/research/uploads/prod/2016/08/How-to-give-a-great-research-talk.pptx)), and [How to write a great research proposal](https://www.microsoft.com/en-us/research/academic-program/how-to-write-a-great-research-proposal/) ([PDF Slides](https://www.microsoft.com/en-us/research/uploads/prod/2016/07/How-to-write-a-great-research-proposal.pdf), [PPT Slides](https://www.microsoft.com/en-us/research/uploads/prod/2016/06/How-to-write-a-great-research-proposal.pptx)).
* [Jason Eisner](https://www.cs.jhu.edu/~jason)'s [advice for research students](https://www.cs.jhu.edu/~jason/advice/).
* CMU's [How to survive as a graduate student](http://www.cs.cmu.edu/afs/cs/user/bnoble/mosaic/survival/survpage.html) and [Advice on research and writing](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/mleone/web/how-to.html).
* [Grad School Advice](http://www.cs.cmu.edu/~jasonh/advice.html), by [Jason I. Hong](http://www.cs.cmu.edu/~jasonh/advice.html).
* [Graduate study in the computer and mathematical sciences: A survival manual](http://www.cs.umd.edu/users/oleary/gradstudy/gradstudy.pdf), by [Dianne P. O'Leary](http://www.cs.umd.edu/~oleary/).
* [List of Proof Techniques you should **not** use](https://dl.acm.org/action/showFmPdf?doi=10.1145%2F1008908) (see page 16). [[PDF]({{ site.baseurl | append: "/misc/1008908.fm.pdf" }})]
  * A Vietnamese translation is [available]({{ site.baseurl | append: "/translation/Angluin_1983_Proof Techniques_vi.pdf" }}).
* Adrian Bondy's [Beautiful conjectures in graph theory](https://doi.org/10.1016/j.ejc.2013.07.006) in *Eur. J. Comb.* 37:4--23, 2014.
* [Richard Feynman: Fun to Imagine (BBC Series, July 1983)](https://www.bbc.co.uk/programmes/p0198zc1). [[YouTube](https://youtu.be/nYg6jzotiAc)].
* [How to be more impressive](https://www.overleaf.com/read/prjmtnwvtszh#0d1180). (A document circulated on the Internet about how to prove 1 + 1 = 2 in a ``fancy'' way. The author is unknown.)

# Useful Resources

* [MacTutor](https://mathshistory.st-andrews.ac.uk)
* [Theory of Computing Blog Aggregator](http://cstheory-feed.org/).
<!-- * [The Collection of Computer Science Bibliographies](http://liinwww.ira.uka.de/bibliography/Theory/index.html). (Discontinued since August 2023.) -->
<!-- * [Mathematics Archives](http://archives.math.utk.edu/index.html) (University of Tennessee). -->
* [Computational Geometry Pages](http://www.computational-geometry.org/).
* [The Parameterized Complexity Community Wiki](http://fpt.wikidot.com/).
* [Combinatorics Wiki](http://combinatoricswiki.org/wiki/Main_Page).
* [The Stony Brook Algorithm Repository](http://www3.cs.stonybrook.edu/~algorith/) (A comprehensive collection of algorithm implementations for over seventy of the most fundamental problems in combinatorial algorithms).
* [TheAlgorithms](https://github.com/thealgorithms) -- GitHub's largest open-source algorithm library.
* [VisuAlgo](http://visualgo.net/) (A comprehensive collection of algorithm animations from [Steve Halim](http://www.comp.nus.edu.sg/~stevenha/) at the National University of Singapore).
* Graphs.
  * [Encyclopedia of Graphs](http://atlas.gregas.eu/).
  * [Information System on Graph Classes and their Inclusions](http://www.graphclasses.org/).
  * [House of Graphs](https://houseofgraphs.org/).
* [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/).
* [Teach Yourself Computer Science](https://teachyourselfcs.com/).
* [A Self-Learning, Modern Computer Science Curriculum](https://functionalcs.github.io/curriculum/).
* [Quanta Magazine](https://www.quantamagazine.org/).
* [Bulletin of EATCS](http://eatcs.org/index.php/on-line-issues).
* [Notices of the AMS](https://www.ams.org/publications/notices/).
  * [Articles in "Early Career Section"](https://www.angelagibney.org/the-ec-by-topic/).
* [AMS eBook Collections](http://www.ams.org/publications/ebooks/ebooks).
* [US Northeast Combinatorics Network](https://sites.google.com/view/northeastcombinatoricsnetwork).
* [SIAM Activity Group on Discrete Mathematics](https://www.siam.org/membership/activity-groups/detail/discrete-mathematics).
* [European Mathematical Information Service](https://www.emis.de).
* [British Combinatorial Committee](https://britishcombinatorial.wordpress.com/).
* [Institute of Combinatorics and its Applications](http://www.the-ica.org/).
  * [Bulletin of the Institute of Combinatorics and its Applications](http://bica.the-ica.org).
* [Combinatorial Mathematics Society of Australasia](http://combinatorics-australasia.org).
* [The Erd&#337;s Project -- Collected Papers of Paul Erd&#337;s](https://www.renyi.hu/~p_erdos/).
* [Women in Combinatorics](https://www.womenincombinatorics.com).
* [CSAuthors](https://www.csauthors.net/).
* [Theoretical Computer Science Jobs](https://cstheory-jobs.org/).
* [MathJobs](https://www.mathjobs.org/jobs).
* Mailing Lists: [DMANET](http://www.zaik.uni-koeln.de/AFS/publications/dmanet/), [THEORYNT](https://listserv.nodak.edu/cgi-bin/wa.exe?A0=THEORYNT), [Reconf](https://lists.uwaterloo.ca/mailman/listinfo/reconf).
* [Blog](https://11011110.github.io/blog/) of [David Eppstein](https://www.ics.uci.edu/~eppstein/).
* [Blog on Computational Complexity and other stuff](https://blog.computationalcomplexity.org/) of [Lance Fortnow](https://lance.fortnow.com) and [Bill Gasarch](https://www.cs.umd.edu/~gasarch/).
* [Theory Matters](https://thmatters.wordpress.com).
* [FediScience](https://fediscience.org) -- a social network for publishing scientists (a part of the decentralized social network powered by [Mastodon](https://joinmastodon.org)).
* Technical Reports.
  * [CDAM: Computational, Discrete and Applicable Mathematics@LSE](http://www.cdam.lse.ac.uk/Reports/).
  * [IPSJ SIG Technical Reports on ALgorithms](https://ipsj.ixsq.nii.ac.jp/search?page=1&size=20&sort=custom_sort&search_type=2&q=2592). (The reports can be accessed freely after [two years or more of being online](https://support.nii.ac.jp/en/news/cinii/20080813).)
  * [IEICE Technical Report](https://www.ieice.org/ken/index/ieice-techrep-e.html). (You must [buy a license](https://www.ieice.org/ken/user/index.php?cmd=techreparchive&lang=eng) to download the reports in this series.)
  <!-- * [Technical Report Archive of the Department of Information and Computing Sciences, Utrecht University](http://www.cs.uu.nl/research/techreps/). -->
  * [CMU Computer Science Technical Report Collection](http://reports-archive.adm.cs.cmu.edu/cs.html).
* E-prints.
  * [arXiv](https://arxiv.org/).
    * [arXiv identifier scheme](https://info.arxiv.org/help/arxiv_identifier.html).
    * [Uploading a paper to arXiv.org](https://trevorcampbell.me/html/arxiv.html).
    * [Paper ownership](https://info.arxiv.org/help/authority.html).
  * [HAL](https://hal.archives-ouvertes.fr/).
  * [Preprints](https://preprints.org/).
* [Open Grants](https://www.ogrants.org/) -- a list of grant proposals openly shared by researchers "to open up science so that all stages of the process can benefit from better interaction and communication and to provide examples for early career scientists writing grants".
* [VideoArxiv](http://videoarxiv.org/) -- a searchable repository of links to math videos.
* [Anonymous GitHub](https://anonymous.4open.science/) -- a proxy server to support anonymous browsing of Github repositories for open-science code and data.
* [Teaching Discrete Mathematics via Primary Historical Sources](https://web.nmsu.edu/~davidp/hist_projects/) and [Learning Discrete Mathematics and Computer Science via Primary Historical Sources](https://www.cs.nmsu.edu/historical-projects/) -- based upon work supported in part by the US National Science Foundation under Grants No. 0715392 and 0717752.
* [LibreTexts Mathematics](https://math.libretexts.org/) -- A large collection of online open-access textbooks in Mathematics.
* [Open Textbook Library](https://open.umn.edu/opentextbooks/).
* [IFORS Developing Countries OR (Operations Research) Resources](https://ifors.org/developing_countries/index.php/Main_Page).
* [Graph Theory in LaTeX](https://graphtheoryinlatex.wordpress.com/).
* [Forage Job Simulations](https://www.theforage.com/simulations).

# Some Books

* [The Discrete Mathematical Charms of Paul Erd&#337;s](https://doi.org/10.1017/9781108912181), by [Vašek Chvátal](https://users.encs.concordia.ca/~chvatal/).
* [Martin Gardner's Mathematical Games: The Entire Collection of his *Scientific American* Columns](https://bookstore.ams.org/view?ProductCode=GARDNER-SET).
* [Algorithms](http://jeffe.cs.illinois.edu/teaching/algorithms/), by [Jeff Erickson](http://jeffe.cs.illinois.edu/).
* [Building Blocks for Theoretical Computer Science](https://mfleck.cs.illinois.edu/building-blocks/), by [Margaret M. Fleck](https://mfleck.cs.illinois.edu).
* [Connecting Discrete Mathematics and Computer Science](https://www.cambridge.org/highereducation/books/connecting-discrete-mathematics-and-computer-science/5BF486220B85F2EFAE7A1B05419F1203), by [David Liben-Nowell](http://www.cs.carleton.edu/faculty/dln/). A preprint version of the book is [available](https://cs.carleton.edu/faculty/dln/book/).
* [Introduction to Graph Theory](https://dwest.web.illinois.edu/igt/), by [Douglas B. West](https://dwest.web.illinois.edu/).
* [Graph Theory](https://diestel-graph-theory.com), by [Reinhard Diestel](https://www.math.uni-hamburg.de/home/diestel/index.html).
* [Fundamentals of Graph Theory](https://allanbickle.wordpress.com/2020/02/24/new-book-fundamentals-of-graph-theory/), by [Allan Bickle](https://allanbickle.wordpress.com).
* [Introduction to Theoretical Computer Science](https://introtcs.org/), by 
[Boaz Barak](http://www.boazbarak.org/). [[PDF](https://files.boazbarak.org/introtcs/lnotes_book.pdf)]
* [Concrete Mathematics: A Foundation for Computer Science](https://www.informit.com/store/concrete-mathematics-a-foundation-for-computer-science-9780201558029), by [Ronald Graham](https://en.wikipedia.org/wiki/Ronald_Graham), [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/), and [Oren Patashnik](https://en.wikipedia.org/wiki/Oren_Patashnik).
* [Introduction to the Theory of Computation](https://math.mit.edu/~sipser/book.html), by [Michael Sipser](https://math.mit.edu/~sipser/).
* [Computational Complexity: A Modern Approach](http://theory.cs.princeton.edu/complexity/), by [Sanjeev Arora](http://www.cs.princeton.edu/~arora/) and [Boaz Barak](http://www.boazbarak.org/). A draft of the book is [available](http://theory.cs.princeton.edu/complexity/book.pdf).
* [Computational Complexity: A Conceptual Perspective](https://www.wisdom.weizmann.ac.il/~oded/cc-book.html), by [Oded Goldreich](https://www.wisdom.weizmann.ac.il/~oded/). A draft of the book is [available](https://www.wisdom.weizmann.ac.il/~oded/cc-drafts.html).
* [Algorithms Illuminated](https://www.algorithmsilluminated.org), by [Tim Roughgarden](https://timroughgarden.org/).
* [Parameterized Algorithms](http://parameterized-algorithms.mimuw.edu.pl/) by Marek Cygan, Fedor V. Fomin, Łukasz Kowalik, Daniel Lokshtanov, Dániel Marx, Marcin Pilipczuk, Michał Pilipczuk, and Saket Saurabhs.
* [Proofs from THE BOOK](https://doi.org/10.1007/978-3-662-57265-8), by [Martin Aigner](https://en.wikipedia.org/wiki/Martin_Aigner) and [Günter M. Ziegler](https://en.wikipedia.org/wiki/G%C3%BCnter_M._Ziegler).
* [Book of Proof](https://www.people.vcu.edu/~rhammack/BookOfProof/), by [Richard Hammack](https://www.people.vcu.edu/~rhammack/).
* [Computers and Intractability: A Guide to the Theory of NP-Completeness](https://en.wikipedia.org/wiki/Computers_and_Intractability), by [Michael Garey](https://en.wikipedia.org/wiki/Michael_Garey) and [David S. Johnson](https://en.wikipedia.org/wiki/David_S._Johnson) -- One of the most influential books on the NP-complete theory, which is usually known as "the Garey&Johnson book".
* [Research Topics in Graph Theory and Its Applications](https://www.cambridgescholars.com/product/978-1-5275-3533-6) and [Modern Applications of Graph Theory](https://global.oup.com/academic/product/modern-applications-of-graph-theory-9780198856740), by [Vadim Zverovich](https://people.uwe.ac.uk/Person/VadimZverovich).
* [Toán rời rạc và ứng dụng](https://drive.google.com/file/d/1Nd7FPnn1y-h8WNio4ALidmHVpGZxbiPM/), Nguyễn Hữu Điển, NXB Đại học Quốc gia Hà Nội, 2019.
* [Thuật toán và lập trình](https://drive.google.com/file/d/1Pg8LsteNU8jtBJxNaXJfHcOeGCdN5wsj/), Nguyễn Hữu Điển, NXB Đại học Quốc gia Hà Nội, 2022.
* [Guide to Graph Colouring: Algorithms and Applications](https://doi.org/10.1007/978-3-030-81054-2), by [Rhyd Lewis](http://www.rhydlewis.eu/) (see aslo [these introductory videos](https://youtube.com/playlist?list=PL4P787kerPHpoaD4UGfHE1SJFhDH79IoO) of the book's author).
* [Graph Coloring Methods](https://graphcoloringmethods.com/), by [Daniel W. Cranston](https://www.people.vcu.edu/~dcranston/).
* [A Student's Guide to the Study, Practice, and Tools of Modern Mathematics](https://doi.org/10.1201/b10355), by Donald Bindner and Martin Erickson
* [Guide to Competitive Programming: Learning and Improving Algorithms Through Contests](https://link.springer.com/book/10.1007/978-3-319-72547-5), by [Antti Laaksonen](https://cs.helsinki.fi/u/ahslaaks/).
  * A primary version written by the same author: [Competitive Programmer's Handbook](https://cses.fi/book.pdf). [[GitHub](https://github.com/pllk/cphb/)] [[CSES Problem Set](https://cses.fi/problemset/)]
* [Learn AI-assisted Python programming: with GitHub Copilot and ChatGPT](https://www.manning.com/books/learn-ai-assisted-python-programming), by Leo Porter and Daniel Zingaro.

# Online Videos/Talks/Lectures/Seminars/etc.

* [Donald Knuth Lectures](https://www.youtube.com/playlist?list=PL94E35692EB9D36F3).
* [Discrete Mathematics Lectures](https://youtube.com/playlist?list=PL2-A74l7wSrNttmmx564N7cqGgFXlYcc_) by [Shai Simonson](https://web.stonehill.edu/compsci/shai.htm) at [ArsDigita University](https://web.archive.org/web/20221205172513/http://aduni.org/) in 2000. More lectures can be found [here](http://adunivids.neocities.org/).
* [CS50: Computer Science Courses and Programs from Harvard](https://www.edx.org/cs50).
* [MIT 18.404J, Fall 2020, Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/). See [this page](https://math.mit.edu/~sipser/18404/Lectures%20Fall%202020/index.html) for the PowerPoint slides.
* [Graph Theory Lectures](https://youtube.com/playlist?list=PL2BdWtDKMS6mplieDd_vls0TBX9Fq2jht) by [Luke Postle](https://www.math.uwaterloo.ca/~lpostle/) at University of Waterloo in Fall 2020.
* [MIT 6.890, Fall 2014, Algorithmic Lower Bounds: Fun with Hardness Proofs](https://courses.csail.mit.edu/6.890/fall14/).
* [MIT 18.217, Fall 2019, Graph Theory And Additive Combinatorics](https://ocw.mit.edu/courses/18-217-graph-theory-and-additive-combinatorics-fall-2019/).
* [School on Parameterized Algorithms and Complexity](http://fptschool.mimuw.edu.pl/) (17-22 August 2014, Będlewo, Poland). This summer school leads to the book [Parameterized Algorithms](http://parameterized-algorithms.mimuw.edu.pl/) by Marek Cygan, Fedor V. Fomin, Łukasz Kowalik, Daniel Lokshtanov, Dániel Marx, Marcin Pilipczuk, Michał Pilipczuk, and Saket Saurabhs.
* [Recent Advances in Parameterized Complexity](https://rapctelaviv.weebly.com/) (3-7 December 2017, Tel Aviv, Israel).
* [Parameterized Algorithms Lectures](https://youtube.com/playlist?list=PLzdZSKerwrXpr6hWq1s63a42YbkocAK1Q) by [Michał Pilipczuk](https://www.mimuw.edu.pl/~mp248287/) at University of Warsaw in Fall 2020.
* Some interesting [programs](https://simons.berkeley.edu/programs/) and [video lectures](https://simons.berkeley.edu/videos) from [Simons Institute for the Theory of Computing](https://simons.berkeley.edu/).
  * [Fine-Grained Complexity and Algorithm Design](https://simons.berkeley.edu/programs/complexity2015) (August 19, 2015 - December 18, 2015).
  * [Beyond Computation: The P versus NP question](https://simons.berkeley.edu/events/michael-sipser) (Speaker: Michael Sipser, Time: May 9, 2014, Place: Berkeley City College).
* [Beyond Computation: The P vs NP Problem.](https://www.youtube.com/watch?v=msp2y_Y5MLE) (Speaker: Michael Sipser, Time: October 3, 2006, Place: Harvard University Science Center).
* [P vs. NP: The Greatest Unsolved Problem in Computer Science](https://www.youtube.com/watch?v=pQsdygaYcE4).
* [Reconfiguration: How Martin Gardner Inspired an Area of Theoretical Computer Science](https://www.youtube.com/watch?v=4cWVjhBTDSY), by Robert A. Hearn, at G4G’s Celebration of Mind (2021-10-22).
* [Stony Brook Mathematics Video Archive](http://www.math.stonybrook.edu/videos/).
* [Vienna Gödel Lectures](https://informatics.tuwien.ac.at/vienna-goedel-lectures/). [[YouTube](https://youtube.com/playlist?list=PLQku6m__XAxGEb1-ZIWSYnLxINppXHbXF)]
* [Combinatorics Lectures Online](https://web.math.princeton.edu/~pds/onlinetalks/talks.html).
* [CS Theory Online Talks](https://cstheorytalks.wordpress.com/).
* [TCS+ Online Seminar](https://sites.google.com/site/plustcs/).
* [Parameterized Complexity Seminar](https://sites.google.com/view/pcseminar/home).
* [SFU Discrete Mathematics Seminar](https://www.sfu.ca/math/research/discrete-mathematics/discrete-math-seminars.html).
* [Atlantic Graph Theory Seminars](https://sites.google.com/view/atlanticgraphtheoryseminars).
* [CMSA Combinatorics Seminar](http://combinatorics-australasia.org/seminars.html).
* [ISU Discrete Math Seminar](https://seminar.mathematicaster.org/).
* [Georgia Tech Graph Theory/Combinatorics Seminars](https://abernshteyn3.math.gatech.edu/gt_gt/).
* [Korea-Taiwan-Vietnam joint seminar in Combinatorics and Analysis](https://sites.google.com/view/ktv-seminar/).

# Conferences and Journals

* [SHERPA RoMEO](http://sherpa.ac.uk/romeo/) -- a summary of publisher copyright policies and self-archiving.
* [Open Access Explained!](https://www.youtube.com/watch?v=L5rVH1KGBCY) from PhD Comics.
* Some open access journals (see also the [Free Journal Network](https://freejournals.org/current-member-journals/) and the [Directory of Open Access Journals](https://doaj.org/) for more information). See also [the Elsevier boyscott](http://thecostofknowledge.com/) and [No free view? No review!](https://nofreeviewnoreview.org).
  * [Discrete Mathematics & Theoretical Computer Science](https://dmtcs.episciences.org/).
  * [Electronic Journal of Combinatorics](https://www.combinatorics.org/).
  * [Advances in Combinatorics](https://www.advancesincombinatorics.com/).
  * [Combinatorial Theory](https://escholarship.org/uc/combinatorial_theory). (The [successor](http://fpsac.org/2020/09/13/CombinatorialTheoryJournal/) to Elsevier's [Journal of Combinatorial Theory, Series A](https://www.journals.elsevier.com/journal-of-combinatorial-theory-series-a/).)
  * [TheoretiCS](https://theoretics.episciences.org/).
  * [Theory of Computing](http://theoryofcomputing.org/).
  * [Innovations in Graph Theory](https://igt.centre-mersenne.org/).
  * [Ars Mathematica Contemporanea](https://amc-journal.eu/index.php/amc/).
  * [Journal of Graph Algorithms and Applications](http://jgaa.info/).
  * [Australasian Journal of Combinatorics](https://ajc.maths.uq.edu.au/).
  * [Discrete Mathematics Letters](https://www.dmlett.com).
  * [The Art of Discrete and Applied Mathematics](https://adam-journal.eu/index.php/ADAM).
  * [Contributions to Discrete Mathematics](http://cdm.ucalgary.ca/).
  * [Electronic Journal of Graph Theory and Applications](https://www.ejgta.org/index.php/ejgta).
  * [AKCE International Journal of Graphs and Combinatorics](https://www.tandfonline.com/journals/uakc20).
  * [Journal of Computational Geometry](https://journals.carleton.ca/jocg/).
  * [Ars Combinatoria](https://combinatorialpress.com/ars/).
  * [Theory and Applications of Graphs](https://digitalcommons.georgiasouthern.edu/tag/).
  * [Annales Mathematicae Silesianae](https://journals.us.edu.pl/index.php/AMSIL/).
* Some journals founded by Vietnamese institutes/universities.
  * [Vietnam Journal of Mathematics](https://www.springer.com/journal/10013).
  * [Acta Mathematica Vietnamica](https://www.springer.com/journal/40306).
* Some more journals.
  * [SIAM Journal on Discrete Mathematics](https://epubs.siam.org/journal/sjdmec).
  * [Journal of Graph Theory](https://onlinelibrary.wiley.com/journal/10970118).
  * [Algorithmica](https://www.springer.com/journal/453).
  * [Combinatorica](https://www.springer.com/journal/493).
  * [Discrete Mathematics](https://www.sciencedirect.com/journal/discrete-mathematics).
  * [European Journal of Combinatorics](https://www.sciencedirect.com/journal/european-journal-of-combinatorics).
  * [Journal of Computer and System Sciences](https://www.sciencedirect.com/journal/journal-of-computer-and-system-sciences).
  * [Graphs and Combinatorics](https://www.springer.com/journal/373).
  * [Theoretical Computer Science](https://www.sciencedirect.com/journal/theoretical-computer-science).
  * [Discrete Applied Mathematics](https://www.sciencedirect.com/journal/discrete-applied-mathematics).
  * [Journal of Combinatorial Optimization](https://www.springer.com/journal/10878).
  * [Information Processing Letters](https://www.sciencedirect.com/journal/information-processing-letters).
* Some conferences.
  * **(Top-tier)** [STOC](http://acm-stoc.org), [FOCS](http://ieee-focs.org), [SODA](https://archive.siam.org/meetings/archives.php)
  * [STACS](http://www.stacs-conf.org/), [SoCG](http://www.socg.org/), [ICALP](https://eatcs.org/index.php/international-colloquium), [WG](https://wg-conference.github.io/wg-conference/), [ISAAC](https://www.kurims.kyoto-u.ac.jp/isaac/ISAAC.html), [ESA](http://esa-symposium.org/), [MFCS](http://www.mfcs.sk), [COCOON](http://cocoon-conference.org), [FSTTCS](https://www.fsttcs.org.in), [FCT](https://www.uni-trier.de/en/universitaet/fachbereiche-faecher/fachbereich-iv/faecher/informatikwissenschaften/professuren/theoretische-informatik/research/conferences-and-workshops/fct-2023), [GD](http://www.graphdrawing.org), [CanaDAM](https://canadam.math.ca).
  * [SWAT](https://swat-symposium.org), [WADS](http://people.scs.carleton.ca/~wads/Home/), [IWOCA](https://nms.kcl.ac.uk/iwoca/), [IPEC](http://fpt.wikidot.com/ipec), [EUROCOMB](https://en.wikipedia.org/wiki/Eurocomb), [FUN](https://sites.google.com/unipi.it/fun2024), [CCCG](https://cccg.ca), [EuroCG](https://www.eurocg.org), [TAMC](https://tamc2024.comp.polyu.edu.hk/), [SOFSEM](https://www.sofsem.cz/), [WAOA](https://algo-conference.org/2024/waoa/), [COCOA](https://theory.utdallas.edu/COCOA2023/index.html), [LATIN](https://www.latintcs.org), [LAGOS](https://www.matem-juriquilla.unam.mx/XII-Symposium-LAGOS-2023), [ITCS](http://itcs-conf.org/).
  * [CIAC](https://easyconferences.eu/ciac2023/), [WALCOM](http://www.walcom-conference.org/), [CALDAM](https://events.iitbhilai.ac.in/caldam2024/), [ICTCS](https://ictcs2024.di.unito.it).
  * [JCDCG^3](http://www.alg.cei.uec.ac.jp/itohiro/JCDCGG/), [SEICCGTC](https://www.math.fau.edu/combinatorics/), [SOSA](https://www.siam.org/conferences/cm/conference/sosa23), [HALG](https://highlightsofalgorithms.org/), [BCC](http://staff.computing.dundee.ac.uk/kedwards/bcc/past.html), [MCCCC](https://mcccc.sites.unlv.edu), [ACC](https://46acc.github.io/), [AAAC](https://cs.kwansei.ac.jp/~tokuyama/AAAC2024.html), [WAAC](https://algo.postech.ac.kr/workshops/waac24/), [DMD](https://dmd2024.web.uah.es/).
* [WikiCFP - A Wiki for Calls for Papers](http://www.wikicfp.com/cfp/). (See [algorithms](http://www.wikicfp.com/cfp/call?conference=algorithms), [graph theory](http://www.wikicfp.com/cfp/call?conference=Graph%20Theory), [combinatorics](http://www.wikicfp.com/cfp/call?conference=combinatorics) and [theoretical computer science](http://www.wikicfp.com/cfp/call?conference=theoretical%20computer%20science) categories.)
* [Links to Combinatorial Conferences](https://dwest.web.illinois.edu/meetlist.html) (maintained by [Douglas B. West](https://dwest.web.illinois.edu)).
* [Conferences in Theoretical Computer Science](http://www.lix.polytechnique.fr/~hermann/conf.php) (maintained by [Miki (Nicolas) Hermann](http://www.lix.polytechnique.fr/~hermann/)).
* [Conferences and Meetings on Graph Theory and Combinatorics](https://www.conference-service.com/conferences/graph-theory.html).
* [International CORE Conference Rankings](https://www.core.edu.au/icore-portal).
* [Conference Ranks](http://www.conferenceranks.com/).
* [Scimago Journal & Country Rank](https://www.scimagojr.com).
* [Scopus Indexed Journals](https://www.scopus.com/sources).
* [WoS (Web of Science) Indexed Journals](https://mjl.clarivate.com/home/).
* [Acceptance ratio of some Theoretical Computer Science Conferences](https://www.lamsade.dauphine.fr/~sikora/ratio/confs.php) (maintained by [Florian Sikora](https://www.lamsade.dauphine.fr/~sikora/)).
* [Highlights of Algorithms](http://highlightsofalgorithms.org/).
* [List of TCS conferences and workshops](https://cstheory.stackexchange.com/questions/7900/list-of-tcs-conferences-and-workshops) @ StackExchange.
* [Graduate Research Workshop in Combinatorics (GRWC)](https://sites.google.com/view/grwc/).
* [SafeTOC](https://safetoc.org) -- a group of volunteers to help prevent and combat harassment in the Theory of Computing community.

# Free Ebooks/Audiobooks

* [Free eBooks - Project Gutenberg](http://www.gutenberg.org/).
* [Lit2Go - Free Online MP3 Audiobooks](https://etc.usf.edu/lit2go/).
* [Planet Ebook](https://www.planetebook.com/).
* [Việt Nam thư quán](http://vietnamthuquan.eu/) (free ebooks in Vietnamese).

# Travel

* [Google Maps](https://www.google.com/maps) (anywhere on earth), [Rome2rio](https://www.rome2rio.com/) (Europe), [GoThere.sg](https://gothere.sg/maps) (Singapore).
* Cheap Flights and Hotels: [Skyscanner](https://www.skyscanner.net), [Wego Travel](https://www.wegotravel.jp/en/flights), [Google Travel](https://www.google.com/travel/).
* [Prepaid Data SIM Card Wiki](https://prepaid-data-sim-card.fandom.com/wiki/Prepaid_SIM_with_data).
* [Visa requirements for Vietnamese citizens](https://en.wikipedia.org/wiki/Visa_requirements_for_Vietnamese_citizens).

# Vietnam

* [National Library of Vietnam](https://nlv.gov.vn).
* [National Agency for Science and Technology Information](https://www.vista.gov.vn/).
  * [Library](https://www.vista.gov.vn/thu-vien.html). ([Online access](https://db0.vista.gov.vn).)
* [Vietnam National University, Hanoi](https://vnu.edu.vn/).
  * [VNU University of Science (VNU-HUS)](https://hus.vnu.edu.vn/).
    * [Logo và mẫu PowerPoint](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/nhan-dien-thuong-hieu/tep-va-hinh-anh.html) 
    * Quy định, quy chế
      * [Cán bộ](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/can-bo.html)
      * [Học sinh, sinh viên](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/hoc-sinh-sinh-vien.html)
      * Đào tạo [đại học](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/dao-tao/dai-hoc.html), [sau đại học](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/dao-tao/sau-dai-hoc.html)
      * [Khoa học công nghệ](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/khoa-hoc-cong-nghe.html)
      * [Hợp tác quốc tế](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/quy-dinh-quy-che/hop-tac-quoc-te.html)
    * Biểu mẫu
      * [Cán bộ](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/can-bo.html)
      * [Học sinh, sinh viên](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/hoc-sinh-sinh-vien.html)
      * Đào tạo [đại học](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/dao-tao/dai-hoc.html), [sau đại học](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/dao-tao/sau-dai-hoc.html)
      * [Khoa học công nghệ](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/khoa-hoc-cong-nghe.html)
      * [Hợp tác quốc tế](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/hop-tac-quoc-te.html)
      * [Kế hoạch - Tài chính](https://hus.vnu.edu.vn/tai-lieu-bieu-mau/bieu-mau/ke-hoach-tai-chinh.html)
    * [Quản lý chế độ làm việc của giảng viên, nghiên cứu viên](http://qlgg.hus.edu.vn/).
* [National Foundation for Science & Technology Development (NAFOSTED)](https://nafosted.gov.vn/).
  * [List of prestigious journal in natural sciences and engineering 2021](https://nafosted.gov.vn/wp-content/uploads/2022/02/NAFOSTED-Danh-muc-tap-chi.rar).
* [Vingroup Innovation Foundation (VinIF)](https://vinif.org/).
* [Vietnam Institute for Advanced Study in Mathematics (VIASM)](http://www.viasm.edu.vn/).
  * [Visa Information for foreign visitors](https://docs.google.com/document/d/1B9JB8ifgrcgLkOu0l_drLyVt1XxKKjqoanHSw0cTBCY/).
* [Institute of Mathematics](http://math.ac.vn/), [Vietnam Academy of Science and Technology](http://www.vast.ac.vn/).
  * [International Center for Research and Postgraduate Training in Mathematics](http://icrtm.vast.vn/) (under the auspices of UNESCO).
* [Association for Vietnamese Language and Speech Processing](https://vlsp.org.vn/).
* [Vietnam Mathematical Society (VMS)](http://www.vms.org.vn/). 
* [The State Council for Professorship (SCP)](http://hdgsnn.gov.vn/).
  * [Quyết định số 37 /2018/QĐ-TTg](http://hdgsnn.gov.vn/files/anhbaiviet/files/2021/37%202018%20QD-TTG_signed.pdf) về việc ban hành quy định tiêu chuẩn, thủ tục xét công nhận đạt tiêu chuẩn và bổ nhiệm chức danh giáo sư, phó giáo sư; thủ tục xét hủy bỏ công nhận chức danh và miễn nhiệm chức danh giáo sư, phó giáo sư
  * [Quyết định số 25/2020/QĐ-TTg](http://hdgsnn.gov.vn/files/anhbaiviet/files/2021/25_signed.pdf) về việc sửa đổi bổ sung một số điều của Quyết định số 37/2018-TTg
  * [Quyết định số 25/QĐ-HĐGSNN](http://hdgsnn.gov.vn/tin-tuc/quyet-dinh-so-25-qd-hdgsnn-phe-duyet-danh-muc-tap-chi-khoa-hoc-duoc-tinh-diem-nam-2024_788/) phê duyệt Danh mục tạp chí khoa học được tính điểm năm 2024
* [Tạp chí Tia Sáng](http://tiasang.com.vn/).
* [Tạp chí Pi](https://pi.edu.vn/), [Tạp chí Epsilon](https://epsilonvn.github.io/).
* [Diễn đàn MathVN](https://www.mathvn.com/).
* [Unikey](https://www.unikey.org/) - The most well-known Vietnamese input keyboard.
* [Timo Bank](https://timo.vn/) (powered by [Viet Capital Bank](https://bvbank.net.vn)).
* [Thuế điện tử - eTax](https://thuedientu.gdt.gov.vn/).
* [Tra cứu thông tin người nộp thuế](http://tracuunnt.gdt.gov.vn/tcnnt/mstcn.jsp).
* Cổng Dịch vụ công trực tuyến.
  * [Cổng Dịch vụ công Quốc gia](https://dichvucong.gov.vn/p/home/dvc-trang-chu.html).
  * [Cổng Dịch vụ công - Bộ Công an](https://dichvucong.bocongan.gov.vn/).
  * [Cổng Dịch vụ công quản lý cư trú](https://dichvucong.dancuquocgia.gov.vn/portal/p/home/dvc-gioi-thieu.html). (Truy cập với địa chỉ IP từ Việt Nam.)
  * [Cổng thông tin điện tử - Bảo hiểm xã hội Việt Nam](https://dichvucong.baohiemxahoi.gov.vn).
* Mạng di động ảo - MVNO (Mobile Virtual Network Operator).
  * [WinTel](https://wintel.vn/), [iTel](https://itel.vn/) (sử dụng sóng mạng VinaPhone).
  * [Local](https://mylocal.vn/), [VNSKY](https://vnsky.vn/) (sử dụng sóng mạng MobiFone).
* [Tra cứu mã bưu chính (postal code) quốc gia Việt Nam](https://mabuuchinh.vn/).
* [Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến]({{ site.baseurl }}/misc/1504 CVBTGTU 2023-KEM.pdf).
* [Cẩm nang phòng chống tin giả, tin sai sự thật trên không gian mạng]({{ site.baseurl }}/misc/Cam nang phong chong tin gia.pdf).
* [The Official Tourism Website of Vietnam](https://vietnam.travel).
* [National Web Portal on Immigration](https://evisa.xuatnhapcanh.gov.vn/en_US/).
  * [E-visa issuance](https://evisa.xuatnhapcanh.gov.vn/web/guest/trang-chu-ttdt).
* [Exemption of Entry Visa to Vietnam](https://lanhsuvietnam.gov.vn/Lists/BaiViet/B%C3%A0i%20vi%E1%BA%BFt/DispForm.aspx?List=dc7c7d75-6a32-4215-afeb-47d4bee70eee&ID=306).
* [Foody](https://www.foody.vn/) -- Find good restaurants in Vietnam.
* [Tìm Buýt](http://timbus.vn/) -- Find bus routes in Hanoi, Vietnam.
* [BusMap](https://busmap.vn/). 
* [VinBus](https://vinbus.vn/).

# Japan

* [Embassy of the Socialist Republic of Vietnam in Japan](https://vnembassy-jp.org/).
* [Sổ tay ngôn ngữ du lịch Nhật Bản]({{ site.baseurl }}/misc/tourist_language_book_Viet_double_page_2016.pdf).
* [Sổ tay y tế](https://www.ia-ibaraki.or.jp/japan/wp-content/uploads/2022/02/all-vi.pdf) phát hành bởi [Hiệp hội giao lưu quốc tế tỉnh Ibaraki](https://www.ia-ibaraki.or.jp).
* Travel Agency: [GT center](http://www.gtcenter.co.jp/), [Art Tourist](http://art-tourist.co.jp/).
* Finding Rental Houses: [At Home](https://www.athome.co.jp/chintai/), [realestatejapan](https://realestate.co.jp/en/), [Best-Estate.jp](https://www.best-estate.jp/en/), [Oakhouse](https://www.oakhouse.jp/eng), [Sakura Rent](http://sakurarent.jp/en/) (Kyoto).
* Route Finding: [Yahoo!乗換案内](https://transit.yahoo.co.jp/), [Japan Transit Planner](https://world.jorudan.co.jp/mln/en/).
* Cheap Hotels: [Rakuten Travel](https://travel.rakuten.com/?scid=wi_trv_specialbanner).
* [Tabelog](https://tabelog.com/en) -- Find good restaurants in Japan.
* [Student Guide to Japan](https://www.jasso.go.jp/en/study_j/sgtj.html).
* [Facebook Vietnamese at JAIST](https://www.facebook.com/V.JAIST/).
* [Một số bài viết và slides](https://www.jaist.ac.jp/~bao/writingsinvietnamese.html) của thầy [Hồ Tú Bảo](https://www.jaist.ac.jp/~bao/).
* The [webpage](http://www.jaist.ac.jp/~uehara/jaist/lab/index.html.en) and [Facebook page](https://www.facebook.com/JAIST-%E4%B8%8A%E5%8E%9F%E7%A0%94%E7%A9%B6%E5%AE%A4-214989062217090/) of JAIST's Uehara Lab. (I was a graduate student there from April 2013 to June 2018 under the supervision of Professor [Ryuhei Uehara](http://www.jaist.ac.jp/~uehara/)). You can also see [my personal webpage at JAIST](http://www.jaist.ac.jp/~s1520016/) (which may have been deleted by the staffs in [JAIST RCACI](http://www.jaist.ac.jp/iscenter/en/)). There is also a page containing materials for [Seminars in Uehara Lab](http://www2.jaist.ac.jp/~uehara/lab/) (since April 2018), which is probably moved to [here](https://www.jaist.ac.jp/is/labs/uehara/) (since 2020?). <span style="color: red">[For lab members only; username and password are required]</span>
* [JAIST's LaTeX template](http://www2.jaist.ac.jp/is/private/stylefile/), [Documents related to Major Research Project](http://www.jaist.ac.jp/english/education/courses-private/major.html), [Useful Links](http://www.jaist.ac.jp/misc/circles/issc/16) <span style="color: red">[On-Campus Use Only]</span>, [Employment Opportunities](https://www.jaist.ac.jp/english/top/employment/index.html).
* [JAIST Research Center for Advanced Computing Infrastructure (RCACI)](http://www.jaist.ac.jp/iscenter/en/).
  * [How to publish your own personal website at JAIST](http://www.jaist.ac.jp/iscenter/en/web/).
* [Facebook JAIST Recycling and Exchange Group](https://www.facebook.com/groups/166361114034612/).
* [Nomi-city Bus Information System](http://nomibus.bus-go.com/english/). (See also [Nomi-city Public Transport Guide](https://www.city.nomi.ishikawa.jp/www/contents/1570440065817/index.html).)
* [Information for Foreign Residents at Iizuka-city (Fukuoka, Japan)](https://www.city.iizuka.lg.jp/kokusai/kokusai-gaikokujinsupport.html).
* [Nishitetsu Bus Timetable Search](http://jik.nishitetsu.jp/menu?lang=en) - Find bus routes in Fukuoka. (Nishitetsu (Nishi-Nippon Railroad) is a major bus company operating in Fukuoka Prefecture, Japan.)
* [Kyutech Algorithms Group](https://kyutech-algorithms-group.github.io/KAG-web/).
<!-- * [For Users of Kyutech Information Systems](http://jimu-www.jimu.kyutech.ac.jp/gakunai/network/top/index_en.htm).  -->
* [Group of Computer Algorithms (Minato Lab), Kyoto University](http://www.lab2.kuis.kyoto-u.ac.jp/en/index.html).
* [Kyoto University Research Administration (KURA) Office](https://www.kura.kyoto-u.ac.jp/).
* [Kyoto University International Service Office (KUISO)](https://kuiso.oc.kyoto-u.ac.jp/).
* [Kyoto University Handbook for foreign researchers](https://www.kyoto-u.ac.jp/ja/international/researcher/scholar-handbook).
* [Arukumachi KYOTO Route Planner](https://www.arukumachikyoto.jp/index.php?lang=en) - Find bus/train routes in Kyoto City.
* [Kyoto City International Foundation](https://www.kcif.or.jp/).
* [Airport Limousine Bus (Okinawa)](https://okinawabus.com/en/ls/ls_ridemethod/).
* [日本学術振興会(Japan Society for the Promotion of Science - JSPS)](https://www.jsps.go.jp/).
  * [LIFE in JAPAN For Foreign Researchers](https://www.jsps.go.jp/english/e-plaza/51_lifeInJapan.html).
  * [JSPS e-Learning Course on Research Ethics](https://elcore.jsps.go.jp/top.aspx).
  * [Email bulletin "JSPS Monthly"](https://www.jsps.go.jp/j-mailmagazine/index.html).
  * Information related to Grant/Fellowship application.
    * [Grants-in-Aid for Scientific Research (KAKENHI) Database](https://kaken.nii.ac.jp/en/index/).
    * [JSPS Electronic Application System](https://www-shinsei.jsps.go.jp/kaken/) (see also its [manual](https://www-shinsei.jsps.go.jp/kaken/docs/manual1ka-E.pdf)).
    * [UNOFFICIAL guidelines for JSPS DC fellowship application in English](http://www-hep.phys.s.u-tokyo.ac.jp/~hama/graduate_course/JSPS_English.html), by [Koichi Hamaguchi](http://www-hep.phys.s.u-tokyo.ac.jp/~hama/welcome-e.html).
    * Strategies for a Successful Grant Proposal, by Robert Cvitkovic and Max Praver, published in [The Language Teacher](https://jalt-publications.org/tlt), [Issues](https://jalt-publications.org/tlt/archive) 42.2 - 42.5, 2018. [[Part One](https://jalt-publications.org/node/4985/articles/24215-strategies-successful-grant-proposal-part-one)] [[Part Two](https://jalt-publications.org/articles/24328-strategies-successful-grant-proposal-part-two)] [[Part Three](https://jalt-publications.org/articles/24343-strategies-successful-grant-proposal-part-three)] [[Part Four](https://jalt-publications.org/articles/24847-strategies-successful-grant-proposal-part-four)]
    * [A Guide to Applying for JSPS Grants-in-Aid](https://jalt-publications.org/proceedings/articles/1706-guide-applying-jsps-grants-aid), by Gregory O’ Dowd and David Elmes, [Proceedings of JALT 2011](https://jalt-publications.org/proceedings/issues/2012-10_2011.1), pp. 12-23, August 2012. [[PDF](https://jalt-publications.org/sites/default/files/pdf-article/jalt2011-002.pdf)]
    * KAKENHI Writing Seminar (a part of KyotoU [ASHBi](https://ashbi.kyoto-u.ac.jp/) [Research Acceleration Programs](https://ashbi.kyoto-u.ac.jp/acceleration/research-acceleration-programs/)): [2022](https://ashbi.kyoto-u.ac.jp/archive/research-acceleration_220805/), [2021](https://ashbi.kyoto-u.ac.jp/archive/research-acceleration_210730/), [2020](https://ashbi.kyoto-u.ac.jp/archive/kakenhi-writing-seminar_2020/).
    * [科研費LaTeX](http://osksn2.hep.sci.osaka-u.ac.jp/~taku/kakenhiLaTeX/) - Templates for applying Japanese KAKENHI Grants (See also on [Overleaf](https://www.overleaf.com/gallery/tagged/japanese+grant-application)). (I modified some templates to create their [English versions](https://github.com/hoanganhduc/TeX-Templates#kakenhiLaTeX). See also some tips I collected when [Writing a KAKENHI grant proposal using LaTeX]({% link _posts/2021-08-23-writing-a-kakenhi-grant-proposal-using-latex.md %}).)
* [情報処理学会アルゴリズム研究会（IPSJ Special Interest Group on Algorithms - SIGAL, Japan)](http://sigal.sakura.ne.jp/).
* [コンピュテーション研究会（IEICE Computation Research Group - COMP, Japan)](https://www.ieice.org/~comp/).
* [EATCS Japan Chapter](http://www.ecei.tohoku.ac.jp/alg/EATCS-J/index.html).
* [Japan REsearch Career Information Network (JREC-IN)](https://jrecin.jst.go.jp/).
* [Japanese Center for Combinatorics and its Applications (JCCA)](https://infoshako.sk.tsukuba.ac.jp/jcca/).
* Banking/Money Transfer/Credit Card/Debit Card/etc.
  * [Japan Post Bank](https://www.jp-bank.japanpost.jp/). (See also [Yucho Direct](https://direct1.jp-bank.japanpost.jp/tp1web/pc/U010101SCK.do) and [Yucho Debit Card](https://www.jp-bank.japanpost.jp/kojin/cashless/yuchodebit/kj_cl_yd_index.html).)
  * [Seven Bank](https://www.sevenbank.co.jp/english/) (Vietnamese support, like [here](https://www.youtube.com/playlist?list=PL3DbFBC8CmDVybaqt-elFJLYqtOKzOkz9) or [here](https://www.sevenbank.co.jp/soukin/vi/kouza/)).
  * [Rakuten Credit Card](https://www.rakuten-card.co.jp/).
  * [DCOM Money Express](https://sendmoney.co.jp/) (Vietnamese support).
  * [Wise](https://wise.com/invite/dic/duch13) -- multi-currency account, cheap international money transfer, etc. (in some country, including Japan, you can also use a [Wise card](https://wise.com/help/topics/6Tme4V2z9ONNzQMeqJpcVi/wise-card)).
* SIM Cards.
  * [Prepaid Japan Travel SIM powered by IIJmio + Brastel Card](https://www.brastel.com/eng/japantravelsim).
  * [IIJmio eSIM](https://www.iijmio.jp/esim/) (Require a Credit Card for monthly payment).
  * [GTN Mobile](https://gtn-mobile.com/) - Buying a low-cost SIM card for data + voice + SMS.
* [What To Do Before Leaving Japan: Resident Tax, Pension, Bank Account, etc.](https://japanlifesupport.com/en/life/return.html).

# Useful Tutorials/Guides/Manuals

* [Windows 10 Tutorial](https://www.tenforums.com/tutorials/).
  * [Windows Subsystem for Linux - Add desktop experience to Ubuntu](https://www.tenforums.com/tutorials/144208-windows-subsystem-linux-add-desktop-experience-ubuntu.html).
  * [Create Windows 10 ISO image from Existing Installation](https://www.tenforums.com/tutorials/72031-create-windows-10-iso-image-existing-installation.html).
  * [How to create a custom bootable recovery partition to restore Windows](https://www.tenforums.com/tutorials/106215-factory-recovery-create-custom-recovery-partition.html).
* [ArchWiki](https://wiki.archlinux.org/).
* [The Linux Documentation Project](https://tldp.org/).
* [GNU Make Manual](https://www.gnu.org/software/make/manual/).
* [Bash tips: Colors and formatting (ANSI/VT100 Control sequences)](https://misc.flogisoft.com/bash/tip_colors_and_formatting).
* [Dell Latitude 7210 2-in-1 Repair Manuals](https://www.parts-people.com/blog/category/dell-latitude-repair-manuals/latitude-7210-2-in-1/), by [Parts-People.com - The experts with Dell laptops!](https://www.parts-people.com).
* [DevTut](https://devtut.github.io).

# Useful Tools/Softwares

* [GnuWin](https://gnuwin32.sourceforge.net) -- ports of tools with a [GNU](http://www.gnu.org/) or similar open source [license](https://gnuwin32.sourceforge.net/license.html) to modern MS-Windows.
* [Crontab Guru](https://crontab.guru).
* [OrgPad](https://orgpad.com/) -- A power tool for brainstorming, idea building and thought processing. See the [introduction video](https://youtu.be/Iv5am2q6m4A). [Pavel Klavík](https://pavel.klavik.cz/) introduced this tool to me when he visited JAIST, Japan (around 2016?) and I was a graduate student there. Back then, OrgPad had [limited functions](/misc/orgpad.html).
* [The Ipe extensible drawing editor](http://ipe.otfried.org/).
* [Ventoy - Boot Multiple ISOs in one USB](https://www.ventoy.net/en/index.html).
* Create temporary [email](https://temp-mail.org/) and [SMS](https://temp-sms.org/).
* [hack.chat](https://hack.chat/) - a minimal, distraction-free chat application with LaTeX support.
* [VPN Gate](https://www.vpngate.net/) -- an online service as an academic research at Graduate School of University of Tsukuba, Japan. The purpose of this research is to expand the knowledge of "Global Distributed Public VPN Relay Servers".
* [Convert text to title case](https://individed.com/code/to-title-case/).
* [Unminify](https://unminify.com/) -- a tool to unminify (unpack, deobfuscate) JavaScript, CSS, HTML, XML and JSON code, making it readable and pretty.
* Share large files with [WeTransfer](https://wetransfer.com/).
* [Dillinger - Online Markdown Editor](https://dillinger.io/).
* [Markdown to Wikidot Converter](https://kernelstack.net/md-to-wd/).
* [Adguard.net Techbench Windows ISO Download](https://files.rg-adguard.net). (You need to pay &euro;5 at [https://forum.rg-adguard.net/account/upgrades](https://forum.rg-adguard.net/account/upgrades) via PayPal to download files from this site for 30 days. Use at your own risk!)
* [';--have i been pwned? - Check if you have an account that has been compromised in a data breach](https://haveibeenpwned.com/).
* Secured OS: [Qubes OS](https://www.qubes-os.org/), [Tails](https://tails.net/), [Whonix](https://www.whonix.org/).

# Onion Sites

Below are links to various onion sites, accessible via the [Tor Browser](https://www.torproject.org/download/). Please be aware that some sites may host or link to illegal or potentially harmful content (scams, drugs, etc.). **Proceed with caution and use at your own risk.**

* [Torch](http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/) -- a search engine for the dark web. Some other search engines are [Ahmia](http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/), [Tornado](http://tornadox5n4g7apkcr23yqyi66eltomazrfgkljy22ccajywd2jsihid.onion/).
* [Trust Pilot](http://torpilohpusxkwjiou42gjiomvfjngiqgfs3xigimbqgdfvth4orrxyd.onion/) -- a review site for the dark web. Some other review sites are [TORLib](http://torlib7fmhyvfv2k7s77xigdds3rosio6k6bxnn256xmtzlbgyizduqd.onion/), [OnionList](http://onion4euorfs4g6qqv6uwxokda7p5hemzcwbfycbhkkjcq7bh64cqkyd.onion), [GoDark](http://gdark5np65mxg3v6lq4sdleiobntkyw3y3e6u26xe3vtgpkxm2efhkqd.onion/).
* [The Dark Web Pug's Ultimate Guide To The Dark Web](http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion/).
* [The Hidden Wiki](http://paavlaytlfsqyvkg3yqj7hflfg5jw2jdg2fgkza5ruf6lplwseeqtvyd.onion/).
* [Another Hidden Wiki](http://2jwcnprqbugvyi6ok2h2h7u26qc6j5wxm7feh3znlh2qu3h6hjld4kyd.onion/).
* [OnionLinks](http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/).
* [Shadow Wiki](http://zsxjtsgzborzdllyp64c6pwnjz5eic76bsksbxzqefzogwcydnkjy3yd.onion/).
* [Dig Deeper](http://edxlhvb3k4d2gn6omddulrfqrvkw7wcur5eexi3672jyoixxqblwlfyd.onion).
* [DefCon](http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/) and [InfoCon](http://w27irt6ldaydjoacyovepuzlethuoypazhhbot6tljuywy52emetn7qd.onion/).
* [Z-Library](http://bookszlibb74ugqojhzhg2a63w5i2atv5bqarulgczawnbmsb6s6qead.onion).
* [ProPublica](http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/).
* [cs.email](http://csmail3thcskmzvjicww3qdkvrhb6pb5s7zjqtb3gdst6guby2stsiqd.onion/) -- Disposable Temporary E-Mail Address.

# Other Stuff

* [Radio Garden](http://radio.garden/) -- listening to live radio stations across the globe.
* NASA's [Astronomy Picture of the Day](https://apod.nasa.gov/).
* [Mathematics Genealogy Project](https://genealogy.math.ndsu.nodak.edu/).
* [Internet Archive](https://archive.org/).
* Google Calendar Usage: Go to [https://www.google.com/calendar/syncselect](https://www.google.com/calendar/syncselect) to select which calendar(s) can be synced to iPhone/iPad/iCal/etc.
* Go to [https://drive.google.com/settings/storage](https://drive.google.com/settings/storage) to check the storage space available for your Google account.
* [Anywhere on Earth (AoE) Time Zone](https://www.timeanddate.com/time/zones/aoe) (UTC-12).
<!--* [Microsoft Activation Scripts (MAS)](https://massgrave.dev).-->
