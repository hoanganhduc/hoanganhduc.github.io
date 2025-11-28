---
layout: default
title: "Publications"
permalink: /publications/
mathjax: true
last_modified_at: 2025-11-28
description: This page contains a list of Duc A. Hoang's publications
keywords: publication, journal, conference, preprint, research, Duc A. Hoang
#bibbase: "https://bibbase.org/show?bib=https://hoanganhduc.github.io/pubs.bib&theme=default&groupby=pubtype&authorFirst=1&jsonp=1"
---

* I have been collaborated with the following coauthors (in alphabetical order by last name): {% for author in site.data.coauthors %}{% if author.homepage != "" %}{% if author == site.data.coauthors.last %}<a href="{{ author.homepage }}">{{ author.name}}</a>. {% else %}<a href="{{ author.homepage }}">{{ author.name}}</a>, {% endif %}{% else %}{% if author == site.data.coauthors.last %}{{ author.name | append: ". " }}{% else %}{{ author.name | append: ", " }}{% endif %}{% endif %}{% endfor %}
* Traditionally, in most areas of mathematics and theoretical computer science, [authors are listed in alphabetical order by last name](https://www.ams.org/profession/leaders/culture/JointResearchandItsPublicationfinal.pdf).

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
