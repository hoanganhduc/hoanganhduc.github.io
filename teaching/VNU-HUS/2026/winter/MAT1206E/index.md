---
layout: default
title: "VNU-HUS MAT1206E: Introduction to Artificial Intelligence"
last_modified_at: 2026-09-04
lang: "en"
katex: true
---

<div class="alert alert-info" markdown="1">
This is the website for the course "Introduction to Artificial Intelligence (VNU-HUS MAT1206E)" I am participating in teaching at the University of Science, Vietnam National University, Hanoi in Semester 1 of the 2026-2027 academic year.

* TOC
{:toc}

<h1>Announcements</h1>

* **01/09/2026:**
  * Website initialized.
</div>

# Basic information
 
* **University:** University of Science, Vietnam National University, Hanoi
* **Course code:** MAT1206E
* **Section codes:** MAT1206E 1, 2, 3
* **Class:** K69A3
* **Credits:** 3
* **Schedule:** Semester 1, Academic year 2026-2027
  * **Theory:** Friday, 13:00 -- 14:45 (Periods 7--8), Room 102-T4
  * **Exercise, Lab:** Monday, Room 508-T5
    * MAT1206E 1: 07:00 -- 08:45 (Periods 1--2)
    * MAT1206E 2: 07:00 -- 08:45 (Periods 1--2)
    * MAT1206E 3: 08:50 -- 10:40 (Periods 3--4)
* **Instructor:**
  * **Theory:** Hoàng Anh Đức (University of Science, VNU Hanoi, `hoanganhduc[at]hus.edu.vn` (replace `[at]` with `@`), GitHub Username: `hoanganhduc`)
  * **Exercise, Lab:**
    * MAT1206E 1 and MAT1206E 3: Hoàng Anh Đức (University of Science, VNU Hanoi, `hoanganhduc[at]hus.edu.vn` (replace `[at]` with `@`), GitHub Username: `hoanganhduc`)
    * MAT1206E 2: Lê Huy Hùng (University of Science, VNU Hanoi, GitHub Username: `HuyHung0`)
* **Content:** The course provides learners with knowledge about knowledge representation and representation of knowledge, together with reasoning techniques on knowledge. Some AI systems are introduced as expert systems. Through those systems, students experiment with AI programming languages or practice with open-source systems to design and build knowledge processing systems.
* **Google Classroom and Classroom50:**
  * Students must sign in with both a Google account, preferably an HUS email account, and a GitHub account to complete the [registration form](https://hoanganhduc.github.io/forms/#/f/mat1206e_26-27) and be added to the course on both Google Classroom and Classroom50.
* **Assessment, grading:**
  * **Regular (20%)** [Exercises, Lab, Attendance]
  * **Midterm (20%)** [Written Test]
  * **Final (60%)** [[Mini Project Report + Presentation]({% link teaching/VNU-HUS/2026/winter/MAT1206E/mini-projects.md %})]

# Textbook, references

* Wolfgang Ertel. *Introduction to Artificial Intelligence*. 3rd edition. Springer, 2025 <span style="color:red">[Main textbook]</span>
  * [Book homepage](http://www.hs-weingarten.de/~ertel/de/b%C3%BCcher/artificial%20intelligence)
  * [Google Drive](https://drive.google.com/file/d/1BJqgschRX77ys9kJH8FyyKVkF7xkzGNj/) (requires HUS email account)
  * [Prof. W. Ertel's AI lectures at Ravensburg-Weingarten University in 2011](https://www.youtube.com/playlist?list=PL39B5D3AFC249556A) (Chapters 1 and 6-10)
* Stuart J. Russell, Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th edition. Pearson, 2021.
  * [Book homepage](https://aima.cs.berkeley.edu)
  * [Google Drive](https://drive.google.com/file/d/1DcyyfFyLyGho4o9V4gZK3gO8Akx_9APi/) (requires HUS email account)
  * [Code](https://github.com/aimacode)

* Supplementary materials for the course
  * [Some materials for the course "Introduction to AI" at VNU-HUS](https://github.com/hoanganhduc/VNU-HUS-IntroAI-Exercises)
  * [Sample code and instructions for running it in GitHub Codespaces]({% link teaching/VNU-HUS/2026/winter/MAT1206E/samplecode.md %})

# Materials from previous years

* **Semester 1, academic year 2025-2026:** [MAT1206E](https://hoanganhduc.github.io/teaching/VNU-HUS/2025/winter/MAT1206E/)
* **Semester 2, academic year 2024-2025:** [MAT1206E](https://hoanganhduc.github.io/teaching/VNU-HUS/2025/spring/MAT1206E/)

# Lectures, exercises

**Note:** Part of the lecture content is based on the slides of Prof. Wolfgang Ertel used in lectures at Ravensburg-Weingarten University, Germany.

**Mini-project timeline:** Students work on their mini-projects throughout Weeks 0--9, starting in Week 0. During Weeks 8--9, students may use both theory and exercise/lab class time to discuss and work on their mini-projects.

| **Week** | **Course activities** | **Preparation for next week** |
|:---------|:----------------------|:------------------------------|
| 0 | **Theory:** [Preliminaries]({{ page.url }}/Preliminaries.pdf)<br>**Exercise, Lab:** Help students set up for the course | [Introduction]({{ page.url }}/Introduction.pdf); [Introduction: In-class Discussion]({{ page.url }}/Discussion/Introduction.pdf)<br>Chapter 1 of the textbook |
| 1 | **Theory:** In-class Discussion; Introduction<br>**Exercise, Lab:** Exercises in Chapter 1 of the textbook | Propositional Logic<br>Chapter 2 of the textbook |
| 2 | **Theory:** Discussion; Propositional Logic<br>**Exercise, Lab:** Exercises in Chapter 2 of the textbook | First-order Predicate Logic<br>Chapter 3 of the textbook |
| 3 | **Theory:** Discussion; First-order Predicate Logic<br>**Exercise, Lab:** Exercises in Chapter 3 of the textbook<br>[Sample code for Chapter 3]({% link teaching/VNU-HUS/2026/winter/MAT1206E/samplecode.md %}#chapter-3-first-order-predicate-logic) | Limitations of Logic<br>Chapter 4 of the textbook |
| 4 | **Theory:** Discussion; Limitations of Logic<br>**Exercise, Lab:** Exercises in Chapter 4 of the textbook | Logic Programming with PROLOG<br>Chapter 5 of the textbook |
| 5 | **Theory:** Discussion; Logic Programming with PROLOG<br>**Exercise, Lab:** Exercises in Chapter 5 of the textbook<br>[Sample code for Chapter 5]({% link teaching/VNU-HUS/2026/winter/MAT1206E/samplecode.md %}#chapter-5-logic-programming-with-prolog) | Search, Games, and Problem Solving<br>Chapter 6 of the textbook<br>Prof. Ertel's lectures: Introduction; Uninformed Search; Heuristic Search; Games with Opponents |
| 6 | **Theory:** Discussion; Search, Games, and Problem Solving<br>**Exercise, Lab:** Exercises in Chapter 6 of the textbook | Reasoning with Uncertainty<br>Chapter 7 of the textbook<br>Prof. Ertel's lectures: Computing with Probabilities; Maximum Entropy; LEXMED; Bayesian Networks |
| 7 | **Theory:** Discussion; Reasoning with Uncertainty<br>**Exercise, Lab:** Exercises in Chapter 7 of the textbook | |
| 8--9 | Students may use both theory and exercise/lab class time to discuss and work on their mini-projects. | |
| 10--14 | Mini-project presentations and evaluations. | |

# Exams

-----

# History of announcements
