---
layout: default
title: "Publications"
permalink: /publications/
mathjax: true
last_modified_at: 2026-06-11
description: This page contains a list of Duc A. Hoang's publications
keywords: publication, journal, conference, preprint, research, Duc A. Hoang
#bibbase: "https://bibbase.org/show?bib=https://hoanganhduc.github.io/pubs.bib&theme=default&groupby=pubtype&authorFirst=1&jsonp=1"
---

* I have been collaborated with the following coauthors (in alphabetical order by last name): {% for author in site.data.coauthors %}{% if author.homepage != "" %}{% if author == site.data.coauthors.last %}<a href="{{ author.homepage }}">{{ author.name}}</a>. {% else %}<a href="{{ author.homepage }}">{{ author.name}}</a>, {% endif %}{% else %}{% if author == site.data.coauthors.last %}{{ author.name | append: ". " }}{% else %}{{ author.name | append: ", " }}{% endif %}{% endif %}{% endfor %}
* Traditionally, in most areas of mathematics and theoretical computer science, [authors are listed in alphabetical order by last name](https://www.ams.org/profession/leaders/culture/JointResearchandItsPublicationfinal.pdf).
* For collaboration, I prefer [Supercollaboration style](https://supercollaboration.org), which is mainly about the following two rules:
  1. Authorship on papers that result from supercollaboration is self-determined by each participant and generally in alphabetical order.
  2. The unsolved problems and resulting discussion are confidential within the group, and can be shared with others only if the group agrees to it (or when the results get published).
* My [Erdős number](https://en.wikipedia.org/wiki/Erd%C5%91s_number) is 2, by two papers with Prof. [David Avis](http://cgm.cs.mcgill.ca/~avis/Kyoto/).

-----

* [DBLP]({{ site.dblp_url }}). 
* [Google Scholar]({{ site.googlescholar_url }}).
* Eprints on [arXiv]({{ site.arxiv_url }}).


<!--

* [Researchmap]({{ site.researchmap_url }}). 
* [zbMATH]({{ site.zbmath_url }}).
* [MathSciNet]({{ site.mathscinet_url }}).
* [BibBase]({{ site.bibbase_url }}).

-->

{% unless page.bibbase %}

<div class="publication">

{% bibliography --template pub_style --style pub_style --file pubs.bib --group_by pubtype %}

</div>

{% else %}

* This page uses [BibBase](https://bibbase.org/) for rendering a list of publications and therefore requires JavaScript for properly displaying.

{% endunless %}

-----

Our (my coauthors and I) manuscripts have been rejected from the following venues. The numbers inside parentheses indicate the number of manuscripts rejected from each venue. 

* Journal:
  * [Australasian Journal of Combinatorics](https://ajc.maths.uq.edu.au/) (2)
  * [Discrete Applied Mathematics](https://www.sciencedirect.com/journal/discrete-applied-mathematics) (1)
  * [Discrete Mathematics](https://www.sciencedirect.com/journal/discrete-mathematics) (1)
  * [Discussiones Mathematicae Graph Theory](https://eudml.org/journal/10318) (1)
  * [Graphs and Combinatorics](https://link.springer.com/journal/373) (1)
  * [The Electronic Journal of Combinatorics](https://www.combinatorics.org/) (1)
  * [Theoretical Computer Science](https://www.sciencedirect.com/journal/theoretical-computer-science) (1)
* Refereed InternationalConference:
  * [CIAC](https://dblp.org/db/conf/ciac/index.html) (2)
  * [ISAAC](https://dblp.org/db/conf/isaac/index.html) (3)
  * [IWOCA](https://dblp.org/db/conf/iwoca/index.html) (1)
  * [LATIN](https://dblp.org/db/conf/latin/index.html) (1)
  * [MFCS](https://dblp.org/db/conf/mfcs/index.html) (1)
  * [SOFSEM](https://dblp.org/db/conf/sofsem/index.html) (1)
  * [SWAT](https://dblp.org/db/conf/swat/index.html) (2)
  * [WALCOM](https://dblp.org/db/conf/walcom/index.html) (2)
  * [WG](https://dblp.org/db/conf/wg/index.html) (1)