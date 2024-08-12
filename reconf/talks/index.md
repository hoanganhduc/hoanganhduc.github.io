---
layout: default
title: "Talks related to Combinatorial Reconfiguration"
mathjax: true
last_modified_at: 2024-04-20
description: This page contains information about some talks related to Combinatorial Reconfiguration
keywords: reconfiguration, talks
redirect_to: https://reconf.wikidot.com/talks/
---

<div class="alert alert-info" markdown="1">

This page contains information about some talks made by researchers regarding their work on problems related to [Combinatorial Reconfiguration](https://en.wikipedia.org/wiki/Reconfiguration). Some of them are also listed in [a YouTube playlist](https://www.youtube.com/playlist?list=PL7G0wYDBSwEb_YmR0ZGD7tD2lSh_mqlmG&jct=cqvVvwehJAQit-UzU87vGTbGnhiEuQ).

* TOC
{:toc}

</div>

# Talks at WALCOM 2024 (2024-03)

For more information, see the [conference's website](https://www.kono.cis.iwate-u.ac.jp/~yamanaka/walcom2024/).

* **[Invited Talk]** Naomi Nishimura. **Reasons to Fall (More) in Love with Combinatorial Reconfiguration**.
* Guilherme D. Da Fonseca, Yan Gerard and Bastien Rivier. **Short Flip Sequences to Untangle Segments in the Plane**.
* Yuya Yamada, Mutsunori Banbara, Katsumi Inoue, Torsten Schaub and Ryuhei Uehara. **Combinatorial Reconfiguration with Answer Set Programming: Algorithms, Encodings, and Empirical Analysis**.
* Naoki Domon, Akira Suzuki, Yuma Tamura and Xiao Zhou. **The Shortest Path Reconfiguration Problem Based on Relaxation of Reconfiguration Rules**.
* Jeffrey Kam, Shahin Kamali, Avery Miller and Naomi Nishimura. **Reconfiguration of Multisets with Applications to Bin Packing**.

# Reconfiguration Problems, Hardness of Approximation, and Gap Amplification: What Are They?, by Naoto Ohsaka, at the AFSA & MI CS Seminar (2024-01-19)

For more information, see [this page](https://kklab.nii.ac.jp/seminars/2023/12/reconfiguration-problems-hardness-of-approximation-and-gap-amplification-what-are-they.html). Here we provide the abstract and link to the slides of the talk.

* **Abstract:** In this talk, I will present my paper titled "Gap Amplification for Reconfiguration Problems," recently presented at 35th Annu. ACM-SIAM Symp. Discrete Algorithms (SODA), 2024. Combinatorial Reconfiguration---the subject of this paper---is a relatively new area in Theoretical CS, which studies the reachability and connectivity over the space of feasible solutions for a combinatorial problem. Before going into the details of the paper, I would like to explain what reconfiguration problems are and what is meant by their hardness of approximation (my STACS 2023 paper). A full version of this paper is available from https://arxiv.org/abs/2310.14160, whose abstract is shown below.
  In this paper, we demonstrate gap amplification for reconfiguration problems. In particular, we prove an explicit factor of PSPACE-hardness of approximation for three popular reconfiguration problems only assuming Reconfiguration Inapproximability Hypothesis (RIH) due to Ohsaka (STACS 2023). Our main result is that under RIH, Maxmin Binary CSP Reconfiguration is PSPACE-hard to approximate within a factor of $0.9942$. Moreover, the same result holds even if the constraint graph is restricted to $(d,\lambda)$-expander for arbitrarily small $\frac{\lambda}{d}$. The crux of its proof is an alteration of the gap amplification technique due to Dinur (J. ACM, 2007), which amplifies the $1$ vs. $1-\epsilon$ gap for arbitrarily small $\epsilon > 0$ up to the $1$ vs. $1-0.0058$ gap. As an application of the main result, we demonstrate that Minmax Set Cover Reconfiguration and Minmax Dominating Set Reconfiguration are PSPACE-hard to approximate within a factor of $1.0029$ under RIH. Our proof is based on a gap-preserving reduction from Label Cover to Set Cover due to Lund and Yannakakis (J. ACM, 1994). However, unlike Lund--Yannakakis' reduction, the expander mixing lemma is essential to use. We finally complement the main result by showing that it is NP-hard to approximate Maxmin Binary CSP Reconfiguration within a factor better than $\frac{3}{4}$. 
* **Slides:** [https://todo314.github.io/slide/gapampreconf_afsa24_slide.pdf](https://todo314.github.io/slide/gapampreconf_afsa24_slide.pdf).



# Combinatorial reconfiguration in plane graphs - a short overview and some open problems, by Oswin Aichholzer, at the Graph Drawing and Combinatorial Geometry Workshop (2023-11-16)

For more information, see the [workshop's website](https://erdoscenter.renyi.hu/events/graph-drawing-and-combinatorial-geometry-workshop).
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:** Reconfiguration is the process of changing a structure into another - either through continuous motion or through discrete changes. We will concentrate on plane graphs and discrete reconfiguration steps of bounded complexity, like exchanging one edge of the graph for another edge, which is often called a flip. The flip graph is defined as the graph having a vertex for each configuration and an edge for each flip. Three questions are central: studying the connectivity of the flip graph, its diameter, and the complexity of finding the shortest flip sequence between two given configurations. Many classic and new results are known, for example for flips in triangulations or the transformation of plane spanning trees. We will give an overview of these results and mention several, (old and new) open problems in this area.
* **Recorded Video:** [https://video.renyi.hu/video/combinatorial-reconfiguration-in-plane-graphs-a-short-overview-and-some-open-problems-732](https://video.renyi.hu/video/combinatorial-reconfiguration-in-plane-graphs-a-short-overview-and-some-open-problems-732).

# Shortest Dominating Set Reconfiguration under Token Sliding, by Jan Matyáš Křišťan, at G2OAT Seminar (2023-10-23)

For more information, see the [seminar's website](https://ggoat.fit.cvut.cz/seminar.html).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Jan Matyáš Křišťan and Jakub Svoboda. [Shortest Dominating Set Reconfiguration Under Token Sliding](https://doi.org/10.1007/978-3-031-43587-4_24). Proceedings of FCT 2023, LNCS 14292, pp. 333-347. (Preprint: [arXiv:2307.10847](http://arxiv.org/abs/2307.10847)).
* **Abstract:** We present novel algorithms that efficiently compute a shortest reconfiguration sequence between two given dominating sets in trees and interval graphs under the Token Sliding model. In this problem, a graph is provided along with its two dominating sets, which can be imagined as tokens placed on vertices. The objective is to find a shortest sequence of dominating sets that transforms one set into the other, with each set in the sequence resulting from sliding a single token in the previous set. While identifying any sequence has been well studied, our work presents the first polynomial algorithms for this optimization variant in the context of dominating sets.
* **Recorded Video:** [https://www.youtube.com/watch?v=TDwRouXgHh4](https://www.youtube.com/watch?v=TDwRouXgHh4).

# Talks at IWONT 2023 (2023-07)

For more information, see the [conference's website](https://www.icms.org.uk/workshops/2023/international-workshop-optimal-network-topologies).

* **[Invited Talk]** Miguel Ángel Fiol. **On the algebra of token graphs**. [[slides](https://www.icms.org.uk/sites/default/files/downloads/Workshops/2023/June-2023/Erskine/IWONT%20July%202023%20FIOL.pdf)]
* Cristina Dalfó. **On the spectra and spectral radii of token graphs**. [[slides](https://www.icms.org.uk/sites/default/files/downloads/Workshops/2023/June-2023/Erskine/spectral%20radius%20token-IWONT2023%20Dalfo.pdf)]

# Talks at Extremal Graphs arising from Designs and Configurations (Banff 23w5125) (2023-05)

For more information, see the [workshop's website](https://www.birs.ca/events/2023/5-day-workshops/23w5125).

* Mónica A. Reyes. **On the spectra of token graphs of a cycle - Part I**. [[slides](https://drive.google.com/file/d/1KALgxuK5GlyfuBRCib5odvKj3_0krpYT/)] [[video](https://videos.birs.ca/2023/23w5125/202305170900-Dalfo.mp4)]
* Cristina Dalfó. **On the spectra of token graphs of a cycle - Part II**. [[slides](https://drive.google.com/file/d/1t9MUTwM3Bj03FweZilDzmqQ7jnUNmZ_W/)] [[video](https://videos.birs.ca/2023/23w5125/202305170930-Fiol.mp4)]
* Miquel Àngel Fiol. **On the spectra of token graphs of a cycle - Part III**. [[slides](https://drive.google.com/file/d/1-elNL9yfvm2i45Y9n_z-bdRstDdaepoF/)] [[video](https://videos.birs.ca/2023/23w5125/202305171000-Reyes.mp4)]

# Talks at WALCOM 2023 (2023-03)

* Rin Saito, Hiroshi Eto, Takehiro Ito, and Ryuhei Uehara: **Reconfiguration of vertex-disjoint shortest paths on graphs**.
* Duc A. Hoang: **On the Complexity of Distance-d Independent Set Reconfiguration**. [[slides](https://hoanganhduc.github.io/events/WALCOM2023/slides.pdf)] [[video](https://youtu.be/aTMiWYge4rw)]
* Yusuke Yanagisawa, Akira Suzuki, Yuma Tamura, and Xiao Zhou: **Parameterized Complexity of Optimizing List Vertex-Coloring Through Reconfiguration**.

# Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement, by Dorian Rudolph, at ITCS 2023 (2023-01-05)

For more information, see the [conference's website](http://itcs-conf.org/).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Sevag Gharibian and Dorian Rudolph. [Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement](https://doi.org/10.4230/LIPIcs.ITCS.2023.53). Proceedings of ITCS 2023, LIPIcs 251, pp. 53.1-53.23.
* **Abstract:** A celebrated result in classical complexity theory is Savitch’s theorem, which states that non-deterministic polynomial-space computations (NPSPACE) can be simulated by deterministic poly-space computations (PSPACE). In this work, we initiate the study of a quantum analogue of NPSPACE, denoted Streaming-QCMASPACE (SQCMASPACE), in which an exponentially long classical proof is streamed to a poly-space quantum verifier. We first show that a quantum analogue of Savitch’s theorem is unlikely to hold, in that SQCMASPACE = NEXP. For completeness, we also introduce the companion class Streaming-QMASPACE (SQMASPACE) with an exponentially long streamed quantum proof, and show SQMASPACE = QMAEXP (the quantum analogue of NEXP). Our primary focus, however, is on the study of exponentially long streaming classical proofs, where we next show the following two main results. The first result shows that, in strong contrast to the classical setting, the solution space of a quantum constraint satisfaction problem (i.e. a local Hamiltonian) is always connected when exponentially long proofs are permitted. For this, we show how to simulate any Lipschitz continuous path on the unit hypersphere via a sequence of local unitary gates, at the expense of blowing up the circuit size. This shows that quantum error-correcting codes can be unable to detect one codeword erroneously evolving to another if the evolution happens sufficiently slowly, and answers an open question of [Gharibian, Sikora, ICALP 2015] regarding the Ground State Connectivity problem. Our second main result is that any SQCMASPACE computation can be embedded into "unentanglement", i.e. into a quantum constraint satisfaction problem with unentangled provers. Formally, we show how to embed SQCMASPACE into the Sparse Separable Hamiltonian problem of [Chailloux, Sattath, CCC 2012] (QMA(2)-complete for 1/poly promise gap), at the expense of scaling the promise gap with the streamed proof size. As a corollary, we obtain the first systematic construction for obtaining QMA(2)-type upper bounds on arbitrary multi-prover interactive proof systems, where the QMA(2) promise gap scales exponentially with the number of bits of communication in the interactive proof. Our construction uses a new technique for exploiting unentanglement to simulate quadratic Boolean functions, which in some sense allows history states to encode the future.
* **Recorded Video:** [https://www.youtube.com/watch?v=bA2WPdZaDB8](https://www.youtube.com/watch?v=bA2WPdZaDB8)

# Vizing's Conjecture Holds, by Jonathan Narboni, at TCS Seminar at Jagiellonian (2023-01-11)

For more information, see [the seminar's website](https://www.tcs.uj.edu.pl/en_GB/informatyka-teoretyczna).
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:** In 1964 Vizing proved that to properly color the edges of a graph $G$, one need at most $\Delta+1$ colors, where $\Delta$ is the maximum degree of $G$. In his paper, Vizing actually proves that one can transform any proper edge coloring into a $(\Delta+1)$-edge-coloring using only Kempe changes. Soon after his paper, he asked the following question: is an optimal edge-coloring always reachable from any proper edge-coloring using only Kempe changes? Bonamy et al. proved that the conjecture holds for triangle free graphs, following their work, we prove that it holds for all graphs.
* **Recorded Video:** [https://youtu.be/-4m3DzbVIOw](https://youtu.be/-4m3DzbVIOw).

# The algebraic connectivity of token graphs, by Cristina Dalfó, at Algebraic Graph Theory International Webinar (2022-12-27)

For more information, see [this page](http://euler.doa.fmph.uniba.sk/AGTIW.html).
Here we provide the corresponding paper, abstract, and link to the slides and video recording of the talk.

* **Corresponding Paper:** C. Dalfó, M. A. Fiol. On the algebraic connectivity of token graphs. (Preprint: [arXiv:2209.01030](https://arxiv.org/abs/2209.01030)).
* **Abstract:** We study the algebraic connectivity (or second Laplacian eigenvalue) of token graphs, also called symmetric powers of graphs. The $k$-token graph $F_k(G)$ of a graph $G$ is the graph whose vertices are the $k$-subsets of vertices from $G$, two of which being adjacent whenever their symmetric difference is a pair of adjacent vertices in $G$. Recently, it was conjectured that the algebraic connectivity of $F_k(G)$ equals the algebraic connectivity of $G$. In this paper, we prove the conjecture for new infinite families of graphs, such as trees and graphs with maximum degree large enough. In these families are included the following graphs: the cocktail party graph, the complement graph of a cycle, the complete multipartite graph, etc. We also show the conjecture for cycles $C_n$ when $k=2$ for most cases of $n$.
* **Slides:** [http://euler.doa.fmph.uniba.sk/CristinaDec2022.pdf](http://euler.doa.fmph.uniba.sk/CristinaDec2022.pdf).
* **Recorded Video:** [https://unilj-my.sharepoint.com/:v:/g/personal/primoz_potocnik_fmf_uni-lj_si1/EdynaoL9ziFIuhPrSfiZjPEBwRi1BtChIxtX9gjWXbT0VQ?e=aRHVZL](https://unilj-my.sharepoint.com/:v:/g/personal/primoz_potocnik_fmf_uni-lj_si1/EdynaoL9ziFIuhPrSfiZjPEBwRi1BtChIxtX9gjWXbT0VQ?e=aRHVZL).

# The precise diameter of reconfiguration graphs, by Stijn Cambie, at IBS Discrete Math Seminar (2022-05-23)

For more information, see [this page](https://dimag.ibs.re.kr/event/2022-05-23/).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Stijn Cambie, Wouter Cames van Batenburg, and Daniel W. Cranston. Optimally Reconfiguring List and Correspondence Colourings. (Preprint: [arXiv:2204.07928](https://arxiv.org/abs/2204.07928)).
* **Abstract:** Reconfiguration is about changing instances in small steps. For example, one can perform certain moves on a Rubik’s cube, each of them changing its configuration a bit. In this case, in at most 20 steps, one can end up with the preferred result. One could construct a graph with as nodes the possible configurations of the Rubik’s cube (up to some isomorphism) and connect two nodes if one can be obtained by applying only one move to the other. Finding an optimal solution, i.e. a minimum number of moves to solve a Rubik’s cube is now equivalent to finding the distance in the graph.
  We will wonder about similar problems in reconfiguration, but applied to list- and DP-colouring. In this case, the small step consists of recolouring precisely one vertex. Now we will be interested in the diameter of the reconfiguration graph and show that sometimes we can determine the precise diameters of these.
  As such, during this talk, we present some main ideas of [arXiv:2204.07928].
* **Recorded Video:** [https://www.youtube.com/watch?v=guO0z4IrGeM](https://www.youtube.com/watch?v=guO0z4IrGeM).

# Talks at CoRe 2022 (2022-05)

The conference was held in Banff, Canada from May 8 - 13, 2022. For more information, see the [conference's website](http://www.birs.ca/events/2022/5-day-workshops/22w5090). Here, we provide links to some materials presented in the conference.

* Takehiro Ito: Invited tutorial: **Invitation to Combinatorial Reconfiguration**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205091037-Ito.html)
* Daniel Cranston: **Kempe Equivalent List Colorings**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205091538-Cranston.html)
* Thomas Suzan: **Reconfiguration of digraph homomorphisms**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205091610-Suzan.html)
* Guilherme Gomes: **Some results on Vertex Separator Reconfiguration**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205091642-Gomes.html)
* Sajed Haque: **Labelled Token Sliding Reconfiguration of Independent Sets on Forests**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205091717-Haque.html)
* Jun Kawahara: Invited talk: **A ZDD-based solver for combinatorial reconfiguration problems**. [slides](https://www.birs.ca/workshops/2022/22w5090/files/Jun%20Kawahara/20220510_kawahara.pdf)
* Abhiruk Lahiri: **Reconfiguring Shortest Paths in Graphs**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205101034-Lahiri.html)
* Henning Fernau: **Order Reconfiguration under Width Constraints**. [slides](https://www.birs.ca/workshops/2022/22w5090/files/Henning%20Fernau/BIRS-AFOW-slides.pdf)
* Amer Mouawad: Invited tutorial: **Parameterized algorithms for reconfiguration problems**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205101302-Mouawad.html)
* Catherine Greenhill: Invited tutorial: **Markov chains, mixing time and connections with reconfiguration**. [slides](https://www.birs.ca/workshops/2022/22w5090/files/Catherine%20Greenhill/Banff-GreenhillTutorial.pdf) [slides (annotated)](https://www.birs.ca/workshops/2022/22w5090/files/Catherine%20Greenhill/Banff-GreenhillTutorial-annotated.pdf) [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205101630-Greenhill.html)
* Rin Saito: Mentoring session: **Reconfiguration of vertex-disjoint shortest paths on split graphs**.
* Hany Ibrahim: Mentoring session: **Edge Contraction and Forbidden Induced Graphs**.
* Hiroshi Eto: **Reconfiguration of Regular Induced Subgraphs**. [slides](https://www.birs.ca/workshops/2022/22w5090/files/Hiroshi%20Eto/HiroshiEto_Reconfiguration_of%20_Regular_Induced_Subgraph.pdf) [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205111030-Eto.html)
* Sevag Gharibian: **Reconfiguration in the quantum setting**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205111101-Gharibian.html)
* Kshitij Gajjar: Mentoring session: **Revisiting shortest path reconfiguration**.
* Jeffrey Kam: Mentoring session: **Extension of subgraph reconfiguration**.
* Jonathan Narboni: Invited talk: **Vizing's conjecture holds**.
* Arnott Kidner: **Gamma-Switchable Homomorphisms**. [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205121409-Kidner.html)
* Stephanie Maaz: **Parameterized Complexity of Reconfiguration of Atoms**. [slides](https://www.birs.ca/workshops/2022/22w5090/files/Stephanie%20Maaz/Parameterized_Complexity_of_Atoms_Reconfiguration.pdf) [video](https://www.birs.ca/events/2022/5-day-workshops/22w5090/videos/watch/202205121430-Maaz.html)
* Hugo Akitaya: **Mentoring session: Reconfiguration of District Maps**.
* Reza Bigdeli: Mentoring session: **Disconnecting the Triangulation Flip Graph of Points in the Plane by Forbidding Edges**.

# Parity Property of Hexagonal Sliding Puzzles, by Erika Roldàn, at WinCom SMM Distinguished Speaker Series (2022-03-31)

For more information, see [this page](https://www.womenincombinatorics.com/colloquium-smm).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Ray Karpman and Erika Roldan. Parity Property of Hexagonal Sliding Puzzles. (Preprint: [arXiv:2201.00919](https://arxiv.org/abs/2201.00919)).
* **Abstract:** We study the puzzle graphs of hexagonal sliding puzzles of various shapes and with various numbers of holes. The puzzle graph is a combinatorial model which captures the solvability and the complexity of sequential mechanical puzzles. Questions relating to the puzzle graph have been previously studied and resolved for the 15 Puzzle which is the most famous, and unsolvable, square sliding puzzle of all times. The puzzle graph is also a discrete model for the configuration space of hard tiles (hexagons or squares) moving on different tessellation-based domains. Understanding the combinatorics of the puzzle graph leads to understanding some aspects of the topology of these configuration spaces.
* **Recorded Video:** [https://www.youtube.com/watch?v=n_WddtYudwQ](https://www.youtube.com/watch?v=n_WddtYudwQ).

# Talks at WALCOM 2022 related to Reconfiguration (2022-03)

For more information, see the [conference's website](https://walcom2022.unej.ac.id/).

* **[Invited Talk]** Takehiro Ito. **Invitation to Combinatorial Reconfiguration**. [[video](https://youtu.be/gwrIyuT3F8w?t=21308)]
* Alexandre Cooper, Stephanie Maaz, Amer Mouawad and Naomi Nishimura. **Parameterized complexity of reconfiguration of atoms**. [[video](https://youtu.be/gwrIyuT3F8w?t=17527)]
* Rahnuma Islam Nishat, Venkatesh Srinivasan and Sue Whitesides. **$1$-Complex $s,t$ Hamiltonian Paths: Structure and Reconfiguration in Rectangular Grids**. [[video](https://youtu.be/ldf20uvV1fQ?t=9157)]
* Joshua Ani, Erik D. Demaine, Yevhenii Diomidov, Dylan Hendrickson and Jayson Lynch. **Traversability, Reconfiguration, and Reachability in the Gadget Framework**. [[video](https://youtu.be/ldf20uvV1fQ?t=7978)]
* Hiroshi Eto, Takehiro Ito, Yasuaki Kobayashi, Yota Otachi and Kunihiro Wasa. **Reconfiguration of Regular Induced Subgraphs**. [[video](https://youtu.be/ldf20uvV1fQ?t=6774)]

# An Analogue of Mohar's Conjecture for List Coloring, by Daniel W. Cranston, at Bordeaux graph theory seminar (2022-03-25)

For more information, see [this page](https://webconf.u-bordeaux.fr/b/mar-ef4-zed).
Here we provide the corresponding paper and link to the video recording of the talk.

* **Corresponding Paper:** Daniel W. Cranston and Reem Mahmoud. Kempe Equivalent List Colorings. (Preprint: arXiv:2112.07439).
* **Recorded Video:** [https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1648212148863](https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1648212148863).

# An Analogue of Mohar's Conjecture for List Coloring, by Daniel W. Cranston, at ISU Discrete Math Seminar (2022-02-15)

For more information, see the [ISU Discrete Math Seminar's homepage](https://seminar.mathematicaster.org/).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Daniel W. Cranston and Reem Mahmoud. Kempe Equivalent List Colorings. (Preprint: [arXiv:2112.07439](http://arxiv.org/abs/2112.07439)).
* **Abstract:** This paper is about moving between any two colorings of a graph via Kempe swaps. This problem has been studied intensively, and we generalize one of the major results from colorings to list-colorings. (This is joint work with Reem Mahmoud.)
* **Recorded Video:** [https://www.youtube.com/watch?v=lvL4BOAPIjI](https://www.youtube.com/watch?v=lvL4BOAPIjI).

# Reconfiguration Graphs for Dominating Sets, by Margaret-Ellen Messinger, at Atlantic Graph Theory Seminars (2022-02-09)

For more information, see [the seminar's website](https://sites.google.com/view/atlanticgraphtheoryseminars/).
[This page](https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTSeminar.html) contains a list of slides and videos. Here we provide the corresponding paper, links to the slides and the video recording of the talk.

* **Corresponding Paper:** Kira Adaricheva, Chassidy Bozeman, Nancy E. Clarke, Ruth Haas, Margaret-Ellen Messinger, Karen Seyffarth, and Heather C. Smith. [Reconfiguration Graphs for Dominating Sets](https://doi.org/10.1007/978-3-030-77983-2_6), Research Trends in Graph Theory and Applications, AWMS 25, pp. 119-135, Springer.
* **Slides:** [https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTS-02-09-22-messinger.pdf](https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTS-02-09-22-messinger.pdf).
* **Recorded Video:** [https://mathstat.dal.ca/~brown/sound/AARMS/AARMS-GTSeminar-02-09-22-messinger.mp4](https://mathstat.dal.ca/~brown/sound/AARMS/AARMS-GTSeminar-02-09-22-messinger.mp4).

# Distributed Vertex Cover Reconfiguration, by Yannic Maus, at ITCS 2022 (2022-02-01)

For more information, see [the conference's website](http://itcs-conf.org/itcs22).
Here we provide the link to the corresponding paper and the recorded video of the talk.

* **Corresponding Paper:** Keren Censor-Hillel, Yannic Maus, Shahar Romem-Peled, and Tigran Tonoyan. [Distributed Vertex Cover Reconfiguration](https://doi.org/10.4230/LIPIcs.ITCS.2022.36), Proceedings of ITCS 2022, LIPIcs 215, pp. 36:1-36:23. (Preprint: [arXiv:2109.06601](https://arxiv.org/abs/2109.06601)).
* **Recorded Video:** [https://www.youtube.com/watch?v=WAYZDjx96W4](https://www.youtube.com/watch?v=WAYZDjx96W4).

# Brief Announcement: Distributed Reconfiguration of Spanning Trees, by Yukiko Yamauchi, at SSS 2021 (2021-11-20)

For more information, see [the conference's website](https://www.cse.chalmers.se/~elad/SSS2021/).
Here we provide the link to the corresponding paper and the recorded video of the talk.

* **Corresponding Paper:** Yukiko Yamauchi, Naoyuki Kamiyama, and Yota Otachi. [Distributed Reconfiguration of Spanning Trees](https://doi.org/10.1007/978-3-030-91081-5_40), Proceedings of SSS 2021, LNCS 13046, pp. 516-520.
* **Recorded Video:** [https://youtu.be/E9CejPHTZCk](https://youtu.be/E9CejPHTZCk).

# Reconfiguration: How Martin Gardner Inspired an Area of Theoretical Computer Science, by Robert A. Hearn, at G4G’s Celebration of Mind (2021-10-22)

For more information, see [this page](https://www.gathering4gardner.org/g4gs-celebration-of-mind-2021-10/).
Here we provide the abstract and link to the recorded video of the talk.

* **Abstract:** A popular area in theoretical computer science for the past ten or fifteen years is known as "combinatorial reconfiguration", or just "reconfiguration". What is not widely appreciated is the debt this field owes to Martin Gardner. As I will show, the foundational problem in reconfiguration - essentially, a coin-sliding puzzle - originated as an exchange gift for G4G6!
* **Recorded Video:** [https://www.youtube.com/watch?v=4cWVjhBTDSY](https://www.youtube.com/watch?v=4cWVjhBTDSY).

# Kempe recoloring version of Hadwiger's conjecture, by Clément Legrand-Duchesne, at Bordeaux graph theory seminar (2021-10-15)

For more information, see [this page](https://webconf.u-bordeaux.fr/b/mar-ef4-zed).
Here we provide the link to the corresponding paper and the recorded video of the talk.

* **Corresponding Paper:** Marthe Bonamy, Marc Heinrich, Clément Legrand-Duchesne, and Jonathan Narboni. On a recolouring version of Hadwiger's conjecture. (Preprint: [arXiv:2103.10684](https://arxiv.org/abs/2103.10684)).
* **Recorded Video:** [https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1634298113752](https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1634298113752)

# Talks at EuroComb 2021 related to Reconfiguration (2021-09)

For more information, see [the conference's website](https://eurocomb2021.upc.edu/).

* Therese Biedl, Anna Lubiw and Owen Merkel. **Building a larger class of graphs for efficient reconfiguration of vertex colouring**.
* Marthe Bonamy, Vincent Delecroix and Clément Legrand-Duchesne. **Kempe changes in bounded treewidth graphs**.

# TS-Reconfiguration of Dominating Sets in Circle and Circular-Arc Graphs, by Nicolas Bousquet, at FCT 2021 (2021-09-14)

For more information, see [the conference's website](https://www.corelab.ntua.gr/fct2021/).
Here we provide the corresponding paper and link to the video recording of the talk.

* **Corresponding Paper:** Nicolas Bousquet and Alice Joffard. [TS-Reconfiguration of Dominating Sets in circle and circular-arc graphs](https://doi.org/10.1007/978-3-030-86593-1_8), Proceedings of FCT 2021, LNCS 12867, pp. 114-134. (Preprint: [arXiv:2102.10568](https://arxiv.org/abs/2102.10568)).
* **Recorded Video:** [https://www.youtube.com/watch?v=-BFzcy_Sd04](https://www.youtube.com/watch?v=-BFzcy_Sd04).

# Talks at MFCS 2021 related to Reconfiguration (2021-08)

For more information, see [the conference's website](https://compose.ioc.ee/mfcs/).

* Emmanuel Arrighi, Henning Fernau, Mateus De Oliveira Oliveira and Petra Wolf. **Order Reconfiguration under Width Constraints**.
* Marcin Briański, Stefan Felsner, Jędrzej Hodor and Piotr Micek. **Reconfiguring independent sets on interval graph**.

# Talks at Workshop on Combinatorial Reconfiguration, affiliated with ICALP 2021 (2021-07-12)

For more information, see [the conference's website](http://www.dais.is.tohoku.ac.jp/coreworkshop.html).

* **\[Invited Talk\]** Nicolas Bousquet. **Independent Set Reconfiguration - Which Price for Locality?**.
* Kshitij Gajjar, Agastya Vibhuti Jha, Manish Kumar and Abhiruk Lahiri. **Reconfiguring Shortest Paths in Graphs**.
* Tetsuo Asano. **Finding Multiple Rounds of Transportations That Meet All Needs**.
* Vladimir Gurvich, Matjaž Krnc, Martin Milanič and Mikhail Vyalyi. **Shifting any path to an avoidable one**.
* **\[Invited Talk\]** Torsten Mütze. **Combinatorial Generation via Permutation Languages**.
* Takehiro Ito, Yuni Iwamasa, Naonori Kakimura, Naoyuki Kamiyama, Yusuke Kobayashi, Yuta Nozaki, Yoshio Okamoto and Kenta Ozeki. **Reconfiguration of Envy-Free Item Allocations**.
* Vincent Pilaud. **Acyclic reorientation lattices and their lattice quotients**.
* James Watson, Johannes Bausch and Sevag Gharibian. **Reconfiguration in the quantum setting: Translationally invariant systems**.
* Fedor Fomin and Petr Golovach. **Reconfiguration by Whitney Switches**.
* **\[Invited Talk\]** Akira Suzuki. **Combinatorial Reconfiguration Applied to Power Distribution Systems**.
* Marthe Bonamy, Vincent Delecroix and Clément Legrand-Duchesne. **Kempe changes on $\Delta$\-colourings**.
* Valentin Bartier, Nicolas Bousquet, Carl Feghali, Marc Heinrich, Benjamin Moore and Théo Pierron. **Some advances related to recoloring planar graphs**.
* Takehiro Ito, Yuni Iwamasa, Yasuaki Kobayashi, Yu Nakahata, Yota Otachi and Kunihiro Wasa. **Reconfiguring Directed Trees in a Digraph**.
* Hugo Akitaya, Matthew Jones, Matias Korman, Oliver Korten, Christopher Meierfrankenfeld, Michael Munje, Diane Souvaine, Csaba Toth and Michael Thramann. **Reconfiguration of Connected Graph Partitions: Single Siwitches and Recombinations**.
* **\[Invited Talk\]** Anna Lubiw. **Geometric Reconfiguration**.
* Arturo Merino and Torsten Mütze. **Efficient generation of rectangulations via permutation languages**.
* Hugo Akitaya, Maarten Löffler, Anika Rounds and Giovanni Viglietta. **Compaction Games**.
* Joshua Ani, Yevhenii Diomidov, Erik D. Demaine, Dylan Hendrickson and Jayson Lynch. **Reconfiguration in the Gadgets Framework**.

# Talks at IWOCA 2021 related to Reconfiguration (2021-07-07)

For more information, see [the conference's website](https://iwoca2021.eecs.uottawa.ca/).
Here we provide some links to the video recordings of the talks.

* Rahnuma Islam Nishat. **Reconfiguring Simple $s,t$ Hamiltonian Paths in Rectangular Grid Graphs**. \[[video](https://youtu.be/xNpw5JvjIdo)\]
* Colin Cooper. **A triangle process on regular graphs**. \[[video](https://youtu.be/bh_cHCotBtw)\]
* **\[Invited Talk\]** Anna Lubiw. **Token Swapping**. \[[video](https://www.youtube.com/watch?v=7fBUPvQbQaI)\]

# Exploring the space of colourings with Kempe changes, by Marthe Bonamy, at TCS Seminar at Jagiellonian (2021-02-06)

For more information, see [the seminar's website](https://www.tcs.uj.edu.pl/en_GB/informatyka-teoretyczna).
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:** Given a solution to a problem, we can try and apply a series of elementary operations to it, making sure to remain in the solution space at every step. What kind of solutions can we reach this way? How fast? This is motivated by a variety of applications, from statistical physics to real-life scenarios, including enumeration and sampling. In this talk, we will discuss various positive and negative results, in the special case of graph colouring.
* **Recorded Video:** [https://www.youtube.com/watch?v=QWx1J0Aehp8](https://www.youtube.com/watch?v=QWx1J0Aehp8).

# Exploring the space of colourings with Kempe changes, by Marthe Bonamy, at the 14th QMUL/LSE Colloquia in Combinatorics (2021-05-13)

For more information, see [the conference's website](https://www.lse.ac.uk/Colloquia-in-Combinatorics).  
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:** Kempe changes were introduced in 1879 in an attempt to prove the 4-colour theorem. They are a convenient if not crucial tool to prove various colouring theorems. Here, we consider how to navigate from a colouring to another through Kempe changes. When is it possible? How fast?
* **Recorded Video:** [https://lse.zoom.us/rec/play/td0VDN\_s38DWXXtLPzBck3PznPiZ-L5TZ\_H\_DX0p7a\_lFc3TRnRi2XS48dkdhzNK3WuJTfYAb4jNg-1V.6Dnv\_CHuCRguWY6w](https://lse.zoom.us/rec/play/td0VDN_s38DWXXtLPzBck3PznPiZ-L5TZ_H_DX0p7a_lFc3TRnRi2XS48dkdhzNK3WuJTfYAb4jNg-1V.6Dnv_CHuCRguWY6w).

# Reconfiguration of Connected Graph Partitions via Recombination, by Hugo A. Akitaya, at CIAC 2021 (2021-05-11)

For more information, see [the conference's website](http://easyconferences.eu/ciac2021).  
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Hugo A. Akitaya, Matias Korman, Oliver Korten, Diane L. Souvaine, and Csaba D. Tóth. [Reconfiguration of Connected Graph Partitions via Recombination](https://doi.org/10.1007/978-3-030-75242-2_4), Proceedings of CIAC 2021, LNCS 12701, pp. 61-74. (Preprint: [arXiv:2011.07378](https://arxiv.org/abs/2011.07378)).
* **Abstract:** Motivated by applications in gerrymandering detection, we study a reconfiguration problem on connected partitions of a connected graph $G$. A partition of $V(G)$ is **connected** if every part induces a connected subgraph. In many applications, it is desirable to obtain parts of roughly the same size, possibly with some slack $s$. A **Balanced Connected $k$\-Partition with slack $s$**, denoted **$(k, s)$\-BCP**, is a partition of $V(G)$ into $k$ nonempty subsets, of sizes $n\_1, \dots, n\_k$ with $\vert n\_i - n/k \vert \leq s$, each of which induces a connected subgraph (when $s=0$ , the $k$ parts are perfectly balanced, and we call it **$k$\-BCP** for short).  
  A **recombination** is an operation that takes a $(k, s)$\-BCP of a graph $G$ and produces another by merging two adjacent subgraphs and repartitioning them. Given two $k$\-BCPs, $A$ and $B$, of $G$ and a slack $s \geq 0$, we wish to determine whether there exists a sequence of recombinations that transform $A$ into $B$ via $(k, s)$\-BCPs. We obtain four results related to this problem: (1) When $s$ is unbounded, the transformation is always possible using at most $6(k-1)$ recombinations. (2) If $G$ is Hamiltonian, the transformation is possible using $O(kn)$ recombinations for any $s \geq n/k$, and (3) we provide negative instances for $s \leq n/(3k)$. (4) We show that the problem is PSPACE-complete when $k \in O(n^\epsilon)$ and $s \in O(n^{1-\epsilon})$, for any constant $0 < \epsilon \leq 1$, even for restricted settings such as when $G$ is an edge-maximal planar graph or when $k \geq 3$ and $G$ is planar.
* **Recorded Video:** [https://www.youtube.com/watch?v=UFlIbW6dHEk](https://www.youtube.com/watch?v=UFlIbW6dHEk).

# Combinatorial generation via permutation languages, by Torsten Mütze, at EPC Webinar (2021-04-26)

For more information, see [this page](https://sites.google.com/view/epcwebinar/).  
Here we provide the abstract, slides, and link to the video recording of the talk.

* **Abstract:** In this talk I present a general and versatile algorithmic framework for exhaustively generating a large variety of different combinatorial objects, based on encoding them as permutations, which provides a unified view on many known results and allows us to prove many new ones. This talk gives an overview over three main applications of our framework: (1) the generation of pattern-avoiding permutations; (2) the generation of various classes of rectangulations; (3) the generation of lattice congruences of the weak order on the symmetric group and of graph associahedra.  
  This talk is based on joint work with Liz Hartung, Hung P. Hoang, and Aaron Williams (SODA 2020), and with Arturo Merino (SoCG 2021) and Jean Cardinal.
* **Slides:** [https://users.math.cas.cz/~hladky/AttachmentsEPC/Mutze.pdf](https://users.math.cas.cz/~hladky/AttachmentsEPC/Mutze.pdf).
* **Recorded Video:** [https://www.youtube.com/watch?v=ZRbXNpyiAp4](https://www.youtube.com/watch?v=ZRbXNpyiAp4), or [https://www.bilibili.com/video/BV14f4y1p7Jm/](https://www.bilibili.com/video/BV14f4y1p7Jm/).

# 5-Colorings of Most 6-Regular Triangulated Tori are Kempe Equivalent, by Reem Mahmoud, at GSCC 2021 (2021-04-24)

For more information, see [the conference's website](https://sites.google.com/view/gscc2021).  
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Daniel W. Cranston and Reem Mahmoud. In Most $6$\-regular Toroidal Graphs All $5$\-colorings are Kempe Equivalent. (Preprint: [arXiv:2102.07948](https://arxiv.org/abs/2102.07948)).
* **Abstract:** A Kempe swap in a properly colored graph recolors one component of the subgraph induced by two colors, interchanging them on that component. Two $k$\-colorings are Kempe $k$\-equivalent if we can transform one into the other by a sequence of Kempe swaps, such that each intermediate coloring uses at most $k$ colors. Meyniel proved that if $G$ is planar, then all $5$\-colorings of $G$ are Kempe $5$\-equivalent; this proof relies heavily on the fact that planar graphs are $5$\-degenerate. To prove an analogous result for toroidal graphs would require handling $6$\-regular graphs. We show that if $G$ is a $6$\-regular graph with an embedding in the torus where every non-contractible cycle has length at least $7$, then all $5$\-colorings of $G$ are Kempe $5$\-equivalent. Bonamy, Bousquet, Feghali, and Johnson asked specifically about the case that $G$ is a triangulated toroidal grid, which is formed from the Cartesian product of $C\_m$ and $C\_n$ by adding a diagonal inside each $4$\-face, with all diagonals parallel. By slightly modifying the proof of our main result, we answer their question affirmatively when $m \geq 6$ and $n \geq 6$.
* **Recorded Video:** [https://www.youtube.com/watch?v=4GCc2qJliB0](https://www.youtube.com/watch?v=4GCc2qJliB0).

# In Most 6-regular Toroidal Graphs All 5-colorings are Kempe Equivalent, by Daniel W. Cranston, at ISU Discrete Math Seminar (2021-03-11)

For more information, see the [ISU Discrete Math Seminar's homepage](https://seminar.mathematicaster.org/).
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Daniel W. Cranston and Reem Mahmoud. In Most $6$\-regular Toroidal Graphs All $5$\-colorings are Kempe Equivalent. (Preprint: [arXiv:2102.07948](https://arxiv.org/abs/2102.07948)).
* **Abstract:** A Kempe swap in a properly colored graph recolors one component of the subgraph induced by two colors, interchanging them on that component. Two $k$\-colorings are Kempe $k$\-equivalent if we can transform one into the other by a sequence of Kempe swaps, such that each intermediate coloring uses at most $k$ colors. Meyniel proved that if $G$ is planar, then all $5$\-colorings of $G$ are Kempe $5$\-equivalent; this proof relies heavily on the fact that planar graphs are $5$\-degenerate. To prove an analogous result for toroidal graphs would require handling $6$\-regular graphs. We show that if $G$ is a $6$\-regular graph with an embedding in the torus where every non-contractible cycle has length at least $7$, then all $5$\-colorings of $G$ are Kempe $5$\-equivalent. Bonamy, Bousquet, Feghali, and Johnson asked specifically about the case that $G$ is a triangulated toroidal grid, which is formed from the Cartesian product of $C\_m$ and $C\_n$ by adding a diagonal inside each $4$\-face, with all diagonals parallel. By slightly modifying the proof of our main result, we answer their question affirmatively when $m \geq 6$ and $n \geq 6$.
* **Recorded Video:** [https://www.youtube.com/watch?v=Y_NOjycYXvc](https://www.youtube.com/watch?v=Y_NOjycYXvc).

# Reconfiguration in Graph Coloring (and other contexts), by Ruth Haas, at NCUWM 2021 (2021-01-23)

For more information, see [the conference's website](https://www.math.unl.edu/~ncuwm/23rdAnnual/).  
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:** In mathematics, as in life, there are often multiple solutions to a question. Reconfiguration studies whether it is possible to move from one solution to another following a given set of rules. Is it possible? How long will it take? In this talk, we will consider reconfiguration of graph coloring as well as reconfiguring a mathematical life.  
  Here’s a mathematical description of the graph theory part of the talk: A proper coloring of a graph is an assignment of a color to each vertex of the graph so that neighboring vertices have different colors. Suppose we change the color of just one vertex in a graph coloring. Can we get from one coloring to another by a sequence of vertex changes so that each step along the way is a proper coloring? The answer is yes, if we are allowed an unlimited number of colors. But, what is the fewest colors we can have for this to work? How many steps might it take? We will look at this, related questions and variations.
* **Recorded Video:** [https://www.youtube.com/watch?v=gApwRCEC89Q](https://www.youtube.com/watch?v=gApwRCEC89Q).

# The $\gamma$-graph of a graph, by Stephen Finbow, at Atlantic Graph Theory Seminars (2021-01-13)

For more information, see [the seminar's website](https://sites.google.com/view/atlanticgraphtheoryseminars/).
[This page](https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTSeminar.html) contains a list of slides and videos.
Here we provide the abstract and links to the slides and video recording of the talk.

* **Abstract:** For a graph $G = (V, E)$, the $\gamma$-graph of $G$, $G(\gamma) = (V(\gamma), E(\gamma))$, is the reconfiguration graph whose vertex set is the collection of minimum dominating sets, or $\gamma$-sets of $G$, and two $\gamma$-sets are adjacent in $G(\gamma)$ if they differ by a single vertex and the two different vertices are adjacent in $G$. The $\gamma$-graph of $G$ was introduced by Fricke et al. in 2011 where they studied properties of $\gamma$-graphs, and raised seven questions. In this seminar we will discuss the study of $\gamma$-graphs to date with a focus on the progress of these questions. 
* **Slides:** [https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTS-01-13-21-finbow.pdf](https://mathstat.dal.ca/~brown/sound/AARMS/AARMSGTS-01-13-21-finbow.pdf).
* **Video Recording:** [https://mathstat.dal.ca/~brown/sound/AARMS/AARMS-GTSeminar-01-13-21-finbow.mp4](https://mathstat.dal.ca/~brown/sound/AARMS/AARMS-GTSeminar-01-13-21-finbow.mp4).

# A Generalized Matching Reconfiguration Problem, by Shay Solomon, at ITCS 2021 (2021-01-06)

For more information, see [the conference's website](http://itcs-conf.org/).  
Here we provide the corresponding paper, abstract, and link to the video recording of the talk.

* **Corresponding Paper:** Noam Solomon and Shay Solomon. [A Generalized Matching Reconfiguration Problem](https://doi.org/10.4230/LIPIcs.ITCS.2021.57), Proceedings of ITCS 2021, LIPIcs 185, pp. 57:1-57:20. (Preprint: [arXiv:1803.05825](https://arxiv.org/abs/1803.05825)).
* **Abstract** The goal in reconfiguration problems is to compute a gradual transformation between two feasible solutions of a problem such that all intermediate solutions are also feasible. In the Matching Reconfiguration Problem (MRP), proposed in a pioneering work by Ito et al. from 2008, we are given a graph $G$ and two matchings $M$ and $M^\prime$, and we are asked whether there is a sequence of matchings in $G$ starting with $M$ and ending at $M^\prime$, each resulting from the previous one by either adding or deleting a single edge in $G$, without ever going through a matching of size $< \min \{\vert M \vert, \vert M^\prime \vert \} - 1$. Ito et al. gave a polynomial time algorithm for the problem, which uses the Edmonds-Gallai decomposition. In this paper we introduce a natural generalization of the MRP that depends on an integer parameter $\Delta \geq 1$: here we are allowed to make $\Delta$ changes to the current solution rather than 1 at each step of the {transformation procedure}. There is always a valid sequence of matchings transforming $M$ to $M^\prime$ if $\Delta$ is sufficiently large, and naturally we would like to minimize $\Delta$. We first devise an optimal transformation procedure for unweighted matching with $\Delta = 3$, and then extend it to weighted matchings to achieve asymptotically optimal guarantees. The running time of these procedures is linear. We further demonstrate the applicability of this generalized problem to dynamic graph matchings. In this area, the number of changes to the maintained matching per update step (the recourse bound) is an important quality measure. Nevertheless, the worst-case recourse bounds of almost all known dynamic matching algorithms are prohibitively large, much larger than the corresponding update times. We fill in this gap via a surprisingly simple black-box reduction: Any dynamic algorithm for maintaining a $\beta$\-approximate maximum cardinality matching with update time $T$, for any $\beta \geq 1$, $T$ and $\epsilon > 0$, can be transformed into an algorithm for maintaining a $(\beta(1+\epsilon))$\-approximate maximum cardinality matching with update time $T + O(1/\epsilon)$ and worst-case recourse bound $O(1/\epsilon)$. This result generalizes for approximate maximum weight matching, where the update time and worst-case recourse bound grow from $T + O(1/\epsilon)$ and $O(1/\epsilon)$ to $T + O(\psi/\epsilon)$ and $O(\psi/\epsilon)$, respectively; $\psi$ is the graph aspect-ratio. We complement this positive result by showing that, for $\beta = 1+\epsilon$, the worst-case recourse bound of any algorithm produced by our reduction is optimal. As a corollary, several key dynamic approximate matching algorithms - with poor worst-case recourse bounds - are strengthened to achieve near-optimal worst-case recourse bounds with no loss in update time.
* **Recorded Video:** [https://www.youtube.com/watch?v=zHSv4uzhqgk](https://www.youtube.com/watch?v=zHSv4uzhqgk).

# On girth and the parameterized complexity of token sliding and token jumping, by Amer E. Mouawad, at Parameterized Complexity Seminar (2020-12-08)

For more information, see [Parameterized Complexity Seminar homepage](https://sites.google.com/view/pcseminar/home).  
Here we provide the corresponding paper, abstract, and link to the slides and video recording of the talk.

* **Corresponding Paper:** Valentin Bartier, Nicolas Bousquet, Clément Dallard, Kyle Lomer, and Amer E. Mouawad. [On girth and the parameterized complexity of token sliding and token jumping](https://doi.org/10.4230/LIPIcs.ISAAC.2020.44), Proceedings of ISAAC 2020, LIPIcs 181, pp. 44:1-44:17. (Preprint: [arXiv:2007.01673](https://arxiv.org/abs/2007.01673)).
* **Abstract:** In the token jumping problem we are given a graph $G$ and two independent sets $S$ and $T$ of $G$, each of size $k > 0$. If we view each independent set as a collection of tokens placed on a subset of the vertices of $G$, then the token jumping problem asks for a sequence of independent sets which transforms $S$ to $T$ by individual token jumps which maintain the independence of the sets. This problem is known to be PSPACE-complete on very restricted graph classes, e.g., planar bounded-degree graphs and graphs of bounded pathwidth. A closely related problem is the token sliding problem, where instead of allowing a token to jump to any vertex of the graph we require that a token slides along an edge of the graph. Token sliding is also known to be PSPACE-complete on the aforementioned graph classes. In this talk, we investigate the parameterized complexity of both problems on several graph classes, focusing on the effect of excluding certain cycles from the input graph.  
  Joint work with Valentin Bartier, Nicolas Bousquet, Clement Dallard, and Kyle Lomer.
* **Slides:** [https://drive.google.com/file/d/1zqytWSCZnYkGRpEo3WDAC07CkmvhMEXO](https://drive.google.com/file/d/1zqytWSCZnYkGRpEo3WDAC07CkmvhMEXO).
* **Recorded Video:** [https://www.youtube.com/watch?v=dARr3lGKwk8](https://www.youtube.com/watch?v=dARr3lGKwk8).

# Talks at JGA 2020 related to Reconfiguration (2020-11-18)

For more information, see [JGA 2020's website](https://www-sop.inria.fr/coati/events/JGA2020).  
Here we provide links to the slides and video recording (if exists) of the talks.

* **On girth and the parameterized complexity of token sliding and token jumping**, by Valentin Bartier. \[[slide](https://www-sop.inria.fr/coati/events/JGA2020/presentation/mercredi-aprem/62-Bartier.Valentin.pdf)\]
* **Linear transformations between dominating sets in the TAR-model**, by Alice Joffard. \[[slide](https://www-sop.inria.fr/coati/events/JGA2020/presentation/mercredi-aprem/63-JOFFARD.Alice.pdf)\] \[[video](https://www.dailymotion.com/video/x7xji1t) (password: petersen)\]

# Triangulation Flip Graphs of Planar Point Sets, by Emo Welzl, at NYU Geometry Seminar (2020-11-10)

For more information, see [NYU Geometry Seminar](https://math.nyu.edu/faculty/pollack/seminar/index.html).
Here we provide the abstract and link to the video recording of the talk.

* **Abstract:**  Given a finite point set $P$ in general position in the plane, a full triangulation of $P$ is a maximal straight-line embedded plane graph on $P$. In a partial triangulation some non-extreme points can be skipped, i.e., it is a full triangulation of some subset $P'$ of $P$ containing all extreme points in $P$. Flips in triangulations are minimal changes: (i) removal of an edge and replacing it by another edge, or (ii) removal of an inner point of degree 3, or (iii) insertion of a skipped point and connecting it to the three vertices of the triangle where it lands in. These flips define an adjacency relation on the set of triangulations of the given set $P$, resulting in the edge flip graph of full triangulations and the bistellar flip graph of partial triangulations. In the early seventies Lawson showed that triangulation flip graphs are always connected.

  Our goal is to investigate the structure of these graphs, with emphasis on their vertex connectivity.

  For $n:=\vert P \vert$, we show that the edge flip graph is $\lceil \frac{n}{2}-2\rceil$-vertex connected, and the bistellar flip graph is $(n-3)$-vertex connected; both results are tight and resolve, for sets in general position, a question asked in the Triangulations book by De Loera, Rambau, and Santos. The bound for partial triangulations matches the situation for the subfamily of regular triangulations (i.e., partial triangulations obtained by lifting the points to 3-space and projecting back the lower convex hull), where $(n-3)$-vertex connectivity has been known since the late eighties through the secondary polytope due to Gelfand, Kapranov, and Zelevinsky (via Balinski's Theorem).

  Joint work with Uli Wagner, IST Austria. 
* **Recorded Video:** [https://youtu.be/zzJuX6Kv34w](https://youtu.be/zzJuX6Kv34w).

# Flip distances between graph orientations, by Jean Cardinal, at LA Combinatorics and Complexity Seminar (2020-10-13)

For more information, see [Los Angeles Combinatorics and Complexity Seminar](https://www.math.ucla.edu/~pak/seminars/CCSem-Fall-2020.htm).  
Here we provide the corresponding paper, abstract, and link to the slides and video recording of the talk.

* **Corresponding Paper:** Oswin Aichholzer, Jean Cardinal, Tony Huynh, Kolja Knauer, Torsten Mütze, Raphael Steiner, and Birgit Vogtenhuber. [Flip distances between graph orientations](https://doi.org/10.1007/s00453-020-00751-1), Algorithmica, 83 (2021), pp. 116-143, January 2021. (A primary version is available in the [Proceedings of WG 2019, LNCS 11789, pp. 120-134](https://doi.org/10.1007/978-3-030-30786-8_10). Preprint: [arXiv:1902.06103](https://arxiv.org/abs/1902.06103)).
* **Abstract:** Flip graphs encode relations induced on a set of combinatorial objects by elementary, local changes. Skeletons of associahedra, for instance, are the graphs induced by quadrilateral flips in triangulations of a convex polygon. For some definition of a flip graph, a natural computational problem to consider is the flip distance: Given two objects, what is the minimum number of flips needed to transform one into the other? We consider the structure and complexity of this problem for orientations of a graph in which every vertex has a specified outdegree, and a flip consists of reversing all edges of a directed cycle.  
  Joint work with Oswin Aichholzer, Tony Huynh, Kolja Knauer, Torsten Mütze, Raphael Steiner, and Birgit Vogtenhuber.
* **Slides:** [https://www.math.ucla.edu/~pak/seminars/Slides/Cardinal.pdf](https://www.math.ucla.edu/~pak/seminars/Slides/Cardinal.pdf).
* **Recorded Video:** [https://www.youtube.com/watch?v=iIWnnYtu\_iA](https://www.youtube.com/watch?v=iIWnnYtu_iA).

# Independent Set Reconfiguration via Token Sliding, by Nicolas Bousquet, at Bordeaux graph theory seminar (2020-10-02)

For more information, see [this page](https://webconf.u-bordeaux.fr/b/mar-ef4-zed).  
Here we provide the link to the recorded video of the talk.

* **Recorded Video:** [https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1601639350957](https://visio.u-bordeaux.fr/playback/presentation/2.0/playback.html?meetingId=2300964ed37832030257d03332f1e49dfb29c699-1601639350957).

# On Vizing's edge colouring question, by Marthe Bonamy, at SFU Discrete Mathematics Seminar (2020-09-16)

For more information, see [this page](https://www.sfu.ca/math/research/discrete-mathematics/discrete-math-seminars.html).  
Here we provide the abstract and link to the recorded video of the talk.

* **Abstract:** In his 1965 seminal paper on edge colouring, Vizing proved that a $(\Delta+1)$\-edge colouring can be reached from any given proper edge colouring through a series of Kempe changes, where $\Delta$ is the maximum degree of the graph. He concludes the paper with the following question: can an optimal edge colouring be reached from any given proper edge colouring through a series of Kempe changes? In other words, if the graph is $\Delta$\-edge-colourable, can we always reach a $\Delta$\-edge-colouring? If true, this would imply a more recent conjecture of Mohar (2006) that in any graph, all $(\Delta+2)$\-edge-colourings are equivalent up to a series of Kempe changes. We discuss recent progress around these questions.
* **Recorded Video:** [https://youtu.be/74etHRGDuS0](https://youtu.be/74etHRGDuS0).

# Reconfiguration of Spanning Trees with Many or Few Leaves, by Nicolas Bousquet, at ESA 2020 (2020-08-29)

For more information, see [ESA 2020's website](http://algo2020.di.unipi.it/ESA2020/).  
Here we provide the corresponding paper, abstract, and links to the slides and recorded video of the talk.

* **Corresponding Paper:** Nicolas Bousquet, Takehiro Ito, Yusuke Kobayashi, Haruka Mizuta, Paul Ouvrard, Akira Suzuki, and Kunihiro Wasa. [Reconfiguration of Spanning Trees with Many or Few Leaves](https://doi.org/10.4230/LIPIcs.ESA.2020.24), Proceedings of ESA 2020, LIPIcs 173, pp. 24:1-24:15. (Preprint: [arXiv:2006.14309](https://arxiv.org/abs/2006.14309)).
* **Abstract:** Let $G$ be a graph and $T\_1, T\_2$ be two spanning trees of $G$. We say that $T\_1$ can be transformed into $T\_2$ via an edge flip if there exist two edges $e \in T\_1$ and $f$ in $T\_2$ such that $T\_2 = (T\_1 \setminus e) \cup f$. Since spanning trees form a matroid, one can indeed transform a spanning tree into any other via a sequence of edge flips, as observed in \[Takehiro Ito et al., 2011\]. We investigate the problem of determining, given two spanning trees $T\_1, T\_2$ with an additional property $\Pi$, if there exists an edge flip transformation from $T\_1$ to $T\_2$ keeping property $\Pi$ all along. First we show that determining if there exists a transformation from $T\_1$ to $T\_2$ such that all the trees of the sequence have at most $k$ (for any fixed $k \geq 3$) leaves is PSPACE-complete. We then prove that determining if there exists a transformation from $T\_1$ to $T\_2$ such that all the trees of the sequence have at least $k$ leaves (where $k$ is part of the input) is PSPACE-complete even restricted to split, bipartite or planar graphs. We complete this result by showing that the problem becomes polynomial for cographs, interval graphs and when $k = n-2$.
* **Slides:** [https://drive.google.com/file/d/1rLrEaBQ1gw8RxG6QWhiQEdUkcP3WEuxY](https://drive.google.com/file/d/1rLrEaBQ1gw8RxG6QWhiQEdUkcP3WEuxY).
* **Recorded Video:** [https://youtu.be/SMFCEREV3m8](https://youtu.be/SMFCEREV3m8).

# Reconfiguring sliding squares in-place by flooding, by Joel Moreno, at EuroCG 2020 (2020-03-17)

For more information, see [EuroCG 2020's website](https://www1.pub.informatik.uni-wuerzburg.de/eurocg2020).  
Here we provide the corresponding paper, abstract, and link to the recorded video of the talk.

* **Corresponding Paper:** Joel Moreno and Vera Sacristán. Reconfiguring sliding squares in-place by flooding. [at EuroCG 2020](https://www1.pub.informatik.uni-wuerzburg.de/eurocg2020/data/uploads/papers/eurocg20_paper_32.pdf).
* **Abstract:** We present a new algorithm that reconfigures between any two edge-connected configurations of $n$ sliding squares within their bounding boxes. The algorithm achieves the reconfiguration by means of $\Theta(n^2)$ slide moves. A visual simulator and a set of experiments allows us to compare the performance over different shapes, showing that in many practical cases the number of slide moves grows significantly slower than in others as $n$ increases.
* **Recorded Video:** [https://youtu.be/OyNLJ1TqLF0](https://youtu.be/OyNLJ1TqLF0).

# Approximating Shortest Connected Graph Transformation for Trees, by Alice Joffard, at SOFSEM 2020 (2020-01-21)

For more information, see [SOFSEM 2020's website](https://cyprusconferences.org/sofsem2020/).  
Here, we provide the corresponding paper, abstract, and links to the slides and recorded video of the talk.

* **Corresponding Paper:** Nicolas Bousquet and Alice Joffard. [Approximating Shortest Connected Graph Transformation for Trees](https://doi.org/10.1007/978-3-030-38919-2_7), Proceedings of SOFSEM 2020, LNCS 12011, pp. 76-87. (Preprint: [hal-02358489](https://hal.archives-ouvertes.fr/hal-02358489/)).
* **Abstract:** Let $G$, $H$ be two connected graphs with the same degree sequence. The aim of this paper is to find a transformation from $G$ to $H$ via a sequence of flips maintaining connectivity. A flip of $G$ is an operation consisting in replacing two existing edges $uv$, $xy$ of $G$ by $ux$ and $vy$.  
  Taylor showed that there always exists a sequence of flips that transforms $G$ into $H$ maintaining connectivity. Bousquet and Mary proved that there exists a $4$\-approximation algorithm of a shortest transformation. In this paper, we show that there exists a $2.5$\-approximation algorithm running in polynomial time. We also discuss the tightness of the lower bound and show that, in order to drastically improve the approximation ratio, we need to improve the best known lower bounds.
* **Slides:** [https://perso.liris.cnrs.fr/ajoffard/SBR.pdf](https://perso.liris.cnrs.fr/ajoffard/SBR.pdf).
* **Recorded Video:** [https://tinyurl.com/y2e79tta](https://tinyurl.com/y2e79tta). (Password: petersen).

# Talks at JGA 2019 related to Reconfiguration (2019-11)

For more information, see [JGA 2019's website](http://di.ulb.ac.be/algo/jga2019/).  
Here we provide links to the slides of the talks.

* **Graph Recoloring - From statistical physics to graph theory**, by Nicolas Bousquet. \[[slide](http://di.ulb.ac.be/algo/jga2019/bousquet.pdf)\]
* **Approximating Shortest Connected Graph Transformation for Trees**, by Alice Joffard. \[[slide](http://di.ulb.ac.be/algo/jga2019/joffard.pdf)\]
* **The Perfect Matching Reconfiguration Problem**, by Marc Heinrich. \[[slide](http://di.ulb.ac.be/algo/jga2019/heinrich.pdf)\]
* **Linear transformations between colorings in chordal graphs**, by Valentin Bartier. \[[slide](http://di.ulb.ac.be/algo/jga2019/bartier.pdf)\]
* **Recoloration distribuée dans les arbres**, by Paul Ouvrard. \[[slide](http://di.ulb.ac.be/algo/jga2019/ouvrard.pdf)\]

# Distributed Reconfiguration of Graph Problems, by Mikael Rabie, at Seminat in Laboratory of Information, Networking and Communication Sciences, Paris, France (2019-09-25)

For more information, see [this page](https://www.lincs.fr/events/distributed-reconfiguration-of-graph-problems/).  
Here, we provide the corresponding paper, abstract and link to the recorded video of the talk.

* **Corresponding Paper:** Marthe Bonamy, Paul Ouvrard, Mikaël Rabie, Jukka Suomela and Jara Uitto. [Distributed Recoloring](https://doi.org/10.4230/LIPIcs.DISC.2018.12), Proceedings of DISC 2018, LIPIcs 121, pp. 12:1-12:17. (Preprint: [arXiv:1802.06742](https://arxiv.org/abs/1802.06742)).
* **Abstract:** In Graph Theory, a reconfiguration problem is as following: given two solutions of a problem and a transition definition, is there a path of acceptable solutions from the first to the second using a transition one after another? What is the length of the shortest reconfiguration path? What complexities are involved? For example, a recoloration problem asks if we can go from a coloration to another, by changing the color of a node at each transition (with the coloring still valid in the intermediate steps). In this talk, the goal would be to consider distributed version of two reconfiguration problems: recoloring, and reconfiguring independent sets. To parallelise the process, we will accept to change the state of different nodes at once, under certain hypothesis (for example, we will recolor an independent set of nodes). The questions will be, using the LOCAL model, how much communication is needed (i.e. how much a node needs knowledge of its neighborhood) in order to produce a reconfiguration schedule of a given length. For the distributed recoloring (DISC 2019), we prove that the addition of colors for the intermediate steps is needed for some cases in order to have a solution. I will provide the analysis of trees, where we want to go from a 3-coloring to another with the use of a 4th color. II will show that a constant schedule can be found after $O(D+\log^\* n)$ communications. For the reconfiguration of independent sets (ICALP 2019 Best Paper), we will present different transitions from the centralized settings, to then justify the one we use. We prove that a constant schedule can be found after $O(D+\log^\* n)$ communications, and a linear schedule can be found after a constant number of communications.  
  Those works are the result of collaborations with Marthe Bonamy, Keren Censor-Hillel, Paul Ouvrard, Jara Uitto and Jukka Suomela.
* **Recorded Video:** [https://youtu.be/RCb2f7Ie6TA](https://youtu.be/RCb2f7Ie6TA).

# Talks at ARDA 2019 related to Reconfiguration (2019-08)

The conference was held on August 30, 2019 as a satellite workshop of [MFCS 2019](https://tcs.rwth-aachen.de/mfcs2019/) at [RWTH Aachen](https://www.rwth-aachen.de/go/id/a/?lidx=1). For more information, see the [conference's website](https://people.inf.ethz.ch/dkomm/arda2019/). Here, we provide links to the abstracts of the talks appeared in "Reconfiguration and Temporal Graph" session.

* Till Fluschnik, Rolf Niedermeier, Valentin Rohm, and Philipp Zschoche. **Multistage vertex cover**. \[[abstract](https://people.inf.ethz.ch/dkomm/arda2019/abstracts/ARDA2019-Fluschnik_Niedermeier_Rohm_Zschoche.pdf)\]  
* Thomas Erlebach, Frank Kammer, Kelin Luo, Andrej Sajenko, and Jakob Spooner. **Two moves per time step make a difference**. \[[abstract](https://people.inf.ethz.ch/dkomm/arda2019/abstracts/ARDA2019-Erlebach_Kammer_Luo_Sajenko_Spooner.pdf)\]  
* Dennis Fischer and Janosch Fuchs. **Color reconfiguration with token swapping**. \[[abstract](https://people.inf.ethz.ch/dkomm/arda2019/abstracts/ARDA2019-Fischer_Fuchs.pdf)\]

# Talks at CoRe 2019 (2019-05)

The conference was held on May 12-17, 2019 in Aussois, France. For more information, see the [conference's website](http://oc.inpg.fr/conf/core2019/Main/HomePage). Here, we provide links to some materials presented in the conference.
    
* **Tutorials**
  * Anna Lubiw. **Geometric Reconfiguration**. \[[Part 1](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/geometric-reconfig-1.pdf)\], \[[Part 2](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/geometric-reconfig-2.pdf)\]  
  * Amer Mouawad. **Algorithmic Aspects of Reconfiguration: Upper and Lower Bounds**. \[[Part 1](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Mouawad_part1.pdf)\], \[[Part 2](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Mouawad_part2.pdf)\]  
        
* **Contributed Talks**
  * Valentin Bartier. **Linear transformations between colorings in chordal graphs**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Bartier_CoRe2019.pdf)\]  
  * Nicolas Bousquet. **Graph recoloring: From statistical physics to graph theory**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Bousquet_CoRe2019.pdf)\]  
  * Richard Brewster. **Reconfiguration of homomorphisms to reflexive digraph cycles**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/BrewsterCoRE2019.pdf)\]  
  * Carl Feghali. **Reconfiguring colourings of graphs with bounded maximum average degree**.  
  * Marc Heinrich. **A polynomial version of Cereceda's conjecture**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Heinrich_CoRe2019.pdf)\]  
  * Duc A. Hoang. **Shortest Reconfiguration Sequence for Sliding Tokens on Spiders**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Hoang_CoRe2019.pdf)\]  
  * Jonathan Noel. **Reconfiguring Graph Homomorphisms**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/NoelCoRe2019.pdf)\]  
  * Arnaud Mary. **Reconfiguration of solutions to find them all**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/mary_core2019.pdf)\]  
  * Haruka Mizuta. **Reconfiguration of Steiner trees in specific graph classes**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/mizuta_core2019.pdf)\]  
  * Vijay Subramanya. **Reconfiguration of graph minors**. \[[slide](https://pagesperso.g-scop.grenoble-inp.fr/~bousquen/CoRe_2019/Subramanya_core2019.pdf)\]

# Talks at JGA 2018 related to Reconfiguration (2018-11-16)

For more information, see [JGA 2018's website](https://oc.g-scop.grenoble-inp.fr/conf/jga2018).  
Here we provide links to the slides of the talks.

* **Combinatorial Reconfiguration**, by Marthe Bonamy. \[[slide](https://oc.g-scop.grenoble-inp.fr/conf/slides/bonamy.pdf)\]
* **Optimisation décrémentale de la reconfiguration de dominants**, by Alexandre Blanché. \[[slide](https://oc.g-scop.grenoble-inp.fr/conf/slides/blanche.pdf)\]

# The Reconfiguration Problem for Graph Homomorphisms, by Mark Siggers, at KAIST Discrete Math Seminar 2018 (2018-04-03)

For more information, see [this page](http://vod.mathnet.or.kr/sub2_2.php?no=5109).  
Here, we provide the corresponding paper, abstract and link to the recorded video of the talk.

* **Corresponding Paper:** Richard C. Brewster, Jae-Baek Lee, Benjamin Moore, Jonathan A. Noel and Mark Siggers. Graph Homomorphism Reconfiguration and Frozen $H$\-Colourings. (Preprint: [arXiv:1712.00200](https://arxiv.org/abs/1712.00200)).
* **Abstract:** For problems with a discrete set of solutions, a reconfiguration problem defines solutions to be adjacent if they meet some condition of closeness, and then asks for two given solutions it there is a path between them in the set of all solutions. The reconfiguration problem for graph homomorphisms has seen fair activity in recent years. Fixing a template, the problem $Recol(H)$ for a graph $H$ asks if one can get from one $H$\-colouring of a graph $G$ to another by changing one vertex at a time, always remaining an $H$\-colouring. If the changed vertex has a loop, it must move to an adjecent vertex. Depending on $H$, the problem seems to be either polynomial time solvable or PSPACE-complete. We discuss many recent results in the area and work towards conjecturing for which the problem is PSPACE-complete.  
  This is joint work with Rick Brewster, Jae-baek Lee, Ben Moore and Jon Noel.
* **Recorded Video:** [http://mp4.mathnet.or.kr/201804/MarkSiggers(20180403).mp4](http://mp4.mathnet.or.kr/201804/MarkSiggers(20180403).mp4) or [https://youtu.be/WSandwsj0pg](https://youtu.be/WSandwsj0pg).

# Reconfiguration of Triangulations of a Planar Point Set, by Anna Lubiw, at PIMS-UManitoba Distinguished Lecture (2018-02-15)

For more information, see [this page](http://www.mathtube.org/lecture/video/reconfiguration-triangulations-planar-point-set).  
Here, we provide a copy of the abstract of the talk and the link to the recorded video.

* **Abstract:** In a reconfiguration problem, the goal is to change an initial configuration of some structure to a final configuration using some limited set of moves. Examples include: sorting a list by swapping pairs of adjacent elements; finding the edit distance between two strings; or solving a Rubik’s cube in a minimum number of moves. Central questions are: Is reconfiguration possible? How many moves are required? In this talk I will survey some reconfiguration problems, and then discuss the case of triangulations of a point set in the plane. A move in this case is a flip that replaces one edge by the opposite edge of its surrounding quadrilateral when that quadrilateral is convex. In joint work with Zuzana Masárová and Uli Wagner we characterize when one edge-labelled triangulation can be reconfigured to another via flips. The proof involves combinatorics, geometry, and topology.
* **About Anna Lubiw:** [Anna Lubiw](https://cs.uwaterloo.ca/~alubiw/Site/Anna_Lubiw.html) is a professor in the Cheriton School of Computer Science, University of Waterloo. She has a PhD from the University of Toronto (1986) and a Master of Mathematics degree from the University of Waterloo (1983). Her research is in the areas of Computational Geometry, Graph Drawing and Graph Algorithms. She was named the Ross and Muriel Cheriton Faculty Fellow in 2014, received the University of Waterloo outstanding performance award in 2012 and was named a Distinguished Scientist by the Association for Computing Machinery in 2009. She serves on the editorial boards of the Journal of Computational Geometry and the Journal of Graph Algorithms and Applications.
* **Download:** The recored video of this talk can be downloaded at [http://www.mathtube.org/sites/default/files/videos/converted/Lubiw-2018\_02\_15.mp4](http://www.mathtube.org/sites/default/files/videos/converted/Lubiw-2018_02_15.mp4) [https://mathtube.org/sites/default/files/videos/converted/5629/Lubiw-2018\_02\_15\_html5\_mp4\_1587572367.mp4](https://mathtube.org/sites/default/files/videos/converted/5629/Lubiw-2018_02_15_html5_mp4_1587572367.mp4).

# Reconfiguration of Common Independent Sets of Matroids, by Moritz Mühlenthaler, at Aussois C.O.W. 2018 (2018-01-11)

The talk was presented by [Moritz Mühlenthaler](https://www12.informatik.uni-erlangen.de/people/muehlenthaler/) at [Aussois C.O.W. 2018](http://www.iasi.cnr.it/aussois/web/home/program/year/2018).  
Here, we provide the abstract and link to the presentation slides.

* **Abstract:** We consider solution graphs of combinatorial problems that arise from certain natural adjacency relations on the solution sets. Such graphs are typically too large to be stored explicitly. After a brief overview of what is known about the complexity of the st-reachability problem on such graphs, our focus will be solution graphs that can be characterized in terms of common independent sets of matroids. We will showcase the following recent dichotomy result: For common independent sets of at most two matroids, the corresponding st-reachability problem can be solved in polynomial time, while for three or more matroids the problem is PSPACE-complete.
* **Slides:** [http://www.iasi.cnr.it/aussois/web/uploads/2018/slides/muhlenthalerm.pdf](http://www.iasi.cnr.it/aussois/web/uploads/2018/slides/muhlenthalerm.pdf).

# Introduction to Reconfiguration, by Naomi Nishimura, at CanaDAM 2017's Mini-symposia on Reconfiguration (2017-06-14)

Here, we provide the abstract and link to the slides of the talk.

* **Abstract:** Reconfiguration is concerned with relationships among solutions to a problem instance, where the reconfigration of one solution to another is a sequence of steps such that each step produces an intermediate feasible solution. The solution space can be represented as a graph, where vertices representing two solutions are adjacent if one can be formed from the other in a single step. Work in the area encompasses both structural questions (Is the reconfiguration graph connected?) and algorithmic ones (How can one find the shortest sequence of steps between two solutions?) This talk introduces techniques, results, and future directions in the area.
* **Slides:** [http://cs.uwaterloo.ca/~nishi/reconfcanadam2017slides.pdf](http://cs.uwaterloo.ca/~nishi/reconfcanadam2017slides.pdf).

# Tight Exact and Approximate Algorithmic Results on Token Swapping, by Tillmann Miltzow (2017-02-01)

The information of this talk by [Tillmann Miltzow](https://sites.google.com/view/miltzow) comes from [his publication page](https://sites.google.com/view/miltzow/publications).  
As we have no specific information, we put the date of the uploaded video as the date of this talk.  
Here, we provide details of the corresponding paper, and the link to the recorded video.

* **Corresponding Paper:** Tillmann Miltzow, Lothar Narins, Yoshio Okamoto, Günter Rote, Antonis Thomas and Takeaki Uno. [Approximation and Hardness of Token Swapping](https://doi.org/10.4230/LIPIcs.ESA.2016.66), Proceedings of ESA 2016, LIPIcs 57, pp. 66:1-66:15. (Preprint: [arXiv:1602.05150](https://arxiv.org/abs/1602.05150)).
* **Recorded Video:** [https://youtu.be/g52apOjT17Y](https://youtu.be/g52apOjT17Y).

# Other Talks at CoRe 2017 (2017-01)

Here, we provide links to some of the materials presented at CoRe 2017.

* Naomi Nishimura, Takehiro Ito, Amer Mouawad. **Workshop's Final Report**. \[[PDF](http://www.birs.ca/workshops/2017/17w5066/report17w5066.pdf)\]  
* Takehiro Ito. **Invitation to Combinatorial Reconfiguration**. \[[slide](http://www.ecei.tohoku.ac.jp/alg/core/page/170123CoRe2017_talk.pdf)\]  
* Karen Seyffarth. **Reconfiguring Vertex Colourings of $2$\-Trees**. \[[slide](http://www.birs.ca/workshops/2017/17w5066/files/seyffarth.pdf)\]  
* Ruth Haas. **Reconfiguration of Dominating sets**. \[[slide](http://www.birs.ca/workshops/2017/17w5066/files/haas-Reconfig.pdf)\]

# Token-sliding Problems, by Jan van den Heuvel, at CoRe 2017 (2017-01-26)

Here, we provide the links to the slides of the talk and the recorded video.

* **Slides:** [http://www.birs.ca/workshops/2017/17w5066/files/van\_den\_Heuvel-talk-BIRS.pdf](http://www.birs.ca/workshops/2017/17w5066/files/van_den_Heuvel-talk-BIRS.pdf).
* **Recorded Video:** [http://videos.birs.ca/2017/17w5066/201701261043-vandenHeuvel.mp4](http://videos.birs.ca/2017/17w5066/201701261043-vandenHeuvel.mp4).
* **Other Resources:** [http://hdl.handle.net/2429/62434](http://hdl.handle.net/2429/62434).

# Kempe Equivalence in Regular Graphs, by Matthew Johnson, at CoRe 2017 (2017-01-25)

Here, we provide the links to the slides of the talk and the recorded video.

* **Slides:** [http://www.birs.ca/workshops/2017/17w5066/files/matthewjohnson.pdf](http://www.birs.ca/workshops/2017/17w5066/files/matthewjohnson.pdf).
* **Recorded Video:** [http://videos.birs.ca/2017/17w5066/201701251108-Johnson.mp4](http://videos.birs.ca/2017/17w5066/201701251108-Johnson.mp4).
* **Other Resources:** [http://hdl.handle.net/2429/62424](http://hdl.handle.net/2429/62424).

# Token Sliding on Chordal Graphs, by Nicolas Bousquet, at CoRe 2017 (2017-01-24)

Here, we provide details of the corresponding paper, and the link to the recorded video.

* **Corresponding Paper:** Marthe Bonamy and Nicolas Bousquet. [Token Sliding on Chordal Graphs](https://doi.org/10.1007/978-3-319-68705-6_10), Proceedings of WG 2017, LNCS 10520, pp. 127-139. (Preprint: [arXiv:1605.00442](https://arxiv.org/abs/1605.00442)).
* **Abstract:** Let $I$ be an independent set of a graph $G$. Imagine that a token is located on any vertex of $I$. We can now move the tokens of $I$ along the edges of the graph as long as the set of tokens still defines an independent set of $G$. Given two independent sets $I$ and $J$, the Token Sliding problem consists in deciding whether there exists a sequence of independent sets which transforms $I$ into $J$ so that every pair of consecutive independent sets of the sequence can be obtained via a token move. This problem is known to be PSPACE-complete even on planar graphs. Demaine et al. \[ISAAC'14\] asked whether the Token Sliding reconfiguration problem is polynomial time solvable on interval graphs and more generally in chordal graphs. Yamada and Uehara \[WALCOM'16\] showed that a polynomial time transformation can be found in proper interval graphs. We answer the first question of Demaine et al. and generalize the result of Yamada and Uehara by showing that we can decide in polynomial time whether two independent sets of an interval graph are in the same connected component. Moreover, we answer similar questions by showing that: (i) determining if there exists a token sliding transformation between every pair of $k$\-independent sets in an interval graph can be decided in polynomial time; (ii) deciding this problem becomes co-NP-hard and even co-W\[2\]-hard (parameterized by the size of the independent set) on split graphs, a sub-class of chordal graphs.
* **Slides:** [http://www.birs.ca/workshops/2017/17w5066/files/bousquet.pdf](http://www.birs.ca/workshops/2017/17w5066/files/bousquet.pdf).
* **Recorded Video:** [http://videos.birs.ca/2017/17w5066/201701240907-Bousquet.mp4](http://videos.birs.ca/2017/17w5066/201701240907-Bousquet.mp4).
* **Other Resources:** [http://hdl.handle.net/2429/62409](http://hdl.handle.net/2429/62409).

# Complexity of Token Swapping and its Variants, by Paweł Rzążewski (2016-09-08)

The information of this talk by [Paweł Rzążewski](http://www.mini.pw.edu.pl/~rzazewsk/www/) comes from [Tillmann Miltzow's publication page](https://sites.google.com/view/miltzow/publications).  
As we have no specific information, we put the date of the uploaded video as the date of this talk.  
Here, we provide details of the corresponding paper, and the link to the recorded video.

* **Corresponding Paper:** Édouard Bonnet, Tillmann Miltzow and Paweł Rzążewski. [Complexity of Token Swapping and its Variants](https://doi.org/10.1007/s00453-017-0387-0), Algorithmica, Special Issue dedicated to the 60th Birthday of Gregory Gutin, pp. 1-27, October 2017. (A primary version is available in the [Proceedings of STACS 2017, LIPIcs 66, pp. 16:1–16:14](https://doi.org/10.4230/LIPIcs.STACS.2017.16). Preprint: [arXiv:1607.07676](https://arxiv.org/abs/1607.07676)).  
    
* **Recorded Video:** [https://youtu.be/dSyuIUWMKWg](https://youtu.be/dSyuIUWMKWg).  

# Talks at Mini-symposium on Combinatorial Reconfiguration, SIAM DM'16 (2016-06-07)

For more information, see the [conference's website](http://www.labri.fr/perso/mbonamy/SIAMDM16.html).  
Here, we provide links to some materials presented in the conference.

* Takehiro Ito. **Invitation to Combinatorial Reconfiguration**. \[[slide](http://www.labri.fr/perso/mbonamy/takehiro_ito_invitation.pptx)\]  
* Carl Feghali. **Kempe Equivalence of Colourings of Graphs**. \[[slide](http://www.labri.fr/perso/mbonamy/carl_feghali_kempe.pdf)\]  
* Jesus Salas. **Kempe reconfiguration and Potts antiferromagnets**. \[[slide](http://www.labri.fr/perso/mbonamy/jesus_salas_kempe.pdf)\]  
* Amer Mouawad. **Shortest reconfiguration paths in the solution space of Boolean formulas**. \[[slide](http://www.labri.fr/perso/mbonamy/amer_mouawad_boolean.pdf)\]  
* Jonathan Noel. **Reconfiguring Graph Homomorphisms and Colourings**. \[[slide](http://www.labri.fr/perso/mbonamy/jon_noel_homomorphism.pdf)\]


