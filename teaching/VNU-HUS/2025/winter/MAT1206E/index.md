---
layout: default
title: "VNU-HUS MAT1206E: Introduction to Artificial Intelligence"
last_modified_at: 2025-09-09
lang: "en"
katex: true
---

<div class="alert alert-info" markdown="1">
This is the website for the course "Introduction to Artificial Intelligence (VNU-HUS MAT1206E)" I am participating in teaching at the University of Science, Vietnam National University, Hanoi in Semester 1 of the 2025-2026 academic year.

* TOC
{:toc}

<h1>Announcements</h1>

* **09/09/2025:**
  * Course content updated
    * Week 1
* **31/08/2025:**
  * Website initialized
  * Students registering for MAT1206E 3 should fill in the form [https://forms.office.com/r/wcsWncHtny](https://forms.office.com/r/wcsWncHtny) **before 23:59 on 17/09/2025** to be invited to the Canvas course. 
  * Course content updated
    * Week 0

See older announcements [here](#history-of-announcements).
</div>

<div class="alert alert-primary" role="alert" markdown="1">
Students who wish to be absent must notify via the form [https://forms.office.com/r/RY6LnDk2wv](https://forms.office.com/r/RY6LnDk2wv) **before the class starts**. Other forms of notification (email, message, asking someone else to request leave, ...) **are not accepted**.
</div>

# Basic information
 
* **University:** University of Science, Vietnam National University, Hanoi
* **Course code:** MAT1206E
* **Section codes:** MAT1206E 1, 2, 3
* **Credits:** 4
* **Schedule:** Semester 1, Academic year 2025-2026
  * **Theory:** Wednesday, 08:50 - 10:40 (Periods 3-4), Room 303-T4
  * **Exercise, Lab:** Thursday, 13:00 -- 18:30 (Periods 7-12), Room 509-T5
    * MAT1206E 1: 13:00 - 14:45 (Periods 7-8)
    * MAT1206E 2: 14:50 - 16:40 (Periods 9-10)
    * MAT1206E 3: 16:45 - 18:30 (Periods 11-12)
* **Instructor:**
  * **Theory:** Hoàng Anh Đức (University of Science, VNU Hanoi, `hoanganhduc[at]hus.edu.vn` (replace `[at]` with `@`))
  * **Exercise, Lab:** Phạm Ngọc Hải (University of Science, VNU Hanoi, `harito.work[at]gmail.com` (replace `[at]` with `@`))
* **Canvas:** [GHGYGK](https://canvas.instructure.com/enroll/GHGYGK)
  * **Note:** Students should fill in the information at [https://forms.office.com/r/wcsWncHtny](https://forms.office.com/r/wcsWncHtny) to be invited to the Canvas course.
  * **Note:** Students must set their display name to their full Vietnamese name, e.g. "Nguyễn Văn Tuấn". Also set the timezone in Canvas to **Hanoi** (GMT+7). See [how to change displayed name](https://community.canvaslms.com/t5/Troubleshooting/Updating-my-displayed-name-in-Canvas/ta-p/853) and [how to change timezone](https://community.canvaslms.com/t5/Canvas-Basics-Guide/How-do-I-set-a-time-zone-in-my-user-account/ta-p/615318).
* **Content:** The course provides learners with knowledge about knowledge representation and representation of knowledge, together with reasoning techniques on knowledge. Some AI systems are introduced as expert systems. Through those systems, students experiment with AI programming languages or practice with open-source systems to design and build knowledge processing systems.
* **Assessment, grading:**
  * **Regular (10%)** [Exercises, Lab, Attendance]
  * **Midterm (20%)** [Mini-Project Presentation + Extra Online Learning Activities]
  * **Final (70%)** [Mini Project Report]

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
  * [Mini-Project Guidelines and Templates](https://github.com/hoanganhduc/VNU-HUS-IntroAI-MiniProject), including [Rubrics for Mini-Project Evaluation](https://github.com/hoanganhduc/VNU-HUS-IntroAI-MiniProject/blob/master/Rubrics.md), [Proposed Topic Template](https://github.com/hoanganhduc/VNU-HUS-IntroAI-MiniProject/blob/master/Proposed%20Topic%20Template.md), and [Some Mini-Project Ideas](https://github.com/hoanganhduc/VNU-HUS-IntroAI-MiniProject/blob/master/Mini-Project%20Ideas.md)

# Lectures, exercises

**Note:** Part of the lecture content is based on [the slides of Prof. Wolfgang Ertel](https://www.hs-weingarten.de/~ertel/de/b%C3%BCcher/artificial%20intelligence/aibook-ertel-slides.pdf) used in lectures at Ravensburg-Weingarten University, Germany.

## Week 0

* **Theory:** [Preliminaries]({{ page.url }}/Preliminaries.pdf)
* **Exercise, Lab:** Help students to set up for the course
* **Preparation for next week:** 
  * [Introduction]({{ page.url }}/Introduction.pdf) and [Introduction: In-class Discussion]({{ page.url }}/Discussion/Introduction.pdf)
  * Chapter 1 of the textbook
  * Prof. Ertel's Introduction Lecture at Ravensburg-Weingarten University in 2011 [[YouTube](https://youtu.be/katiy95_mxo)]
  * A recent conversation (April 2025) between Johann Schumann and Prof. Ertel (retired) [[AI at the Crossroads: Symbolic Logic, Impact on Society, and the Future of Work](https://youtu.be/LDWu3oXnezc)]

## Week 1

* **Theory:** 
  * [In-class Discussion]({{ page.url }}/Discussion/Introduction.pdf)
  * [Introduction]({{ page.url }}/Introduction.pdf)
* **Exercise, Lab:** Exercises in Chapter 1 of the textbook
* **Preparation for next week:** 
  * [Propositional Logic]({{ page.url }}/Propositional_Logic.pdf)
  * Chapter 2 of the textbook

<!--
## Week 2

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/Propositional_Logic.pdf)
  * [Propositional Logic]({{ page.url }}/Propositional_Logic.pdf)
* **Exercise, Lab:** Exercises in Chapter 2 of the textbook
* **Preparation for next week:** 
  * [First-order Predicate Logic]({{ page.url }}/First-order_Predicate_Logic.pdf)
  * Chapter 3 of the textbook

## Week 3

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/First-order_Predicate_Logic.pdf)
  * [First-order Predicate Logic]({{ page.url }}/First-order_Predicate_Logic.pdf)
* **Exercise, Lab:** Exercises in Chapter 3 of the textbook
* **Preparation for next week:** 
  * [Limitations of Logic]({{ page.url }}/Limitations_of_Logic.pdf)
  * Chapter 4 of the textbook

## Week 4

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/Limitations_of_Logic.pdf)
  * [Limitations of Logic]({{ page.url }}/Limitations_of_Logic.pdf)
* **Exercise, Lab:** Exercises in Chapter 4 of the textbook
* **Preparation for next week:** 
  * [Logic Programming with PROLOG]({{ page.url }}/Logic_Programming_with_PROLOG.pdf)
  * Chapter 5 of the textbook

## Week 5

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/Logic_Programming_with_PROLOG.pdf)
  * [Logic Programming with PROLOG]({{ page.url }}/Logic_Programming_with_PROLOG.pdf)
* **Exercise, Lab:** Exercises in Chapter 5 of the textbook
* **Preparation for next week:** 
  * [Search, Games, and Problem Solving]({{ page.url }}/Search_Games_and_Problem_Solving.pdf)
  * Chapter 6 of the textbook
  * Prof. Ertel’s Lectures at Ravensburg-Weingarten University in 2011
    - [Introduction (about Search, Games, and Problem Solving)](https://youtu.be/RRO9-QXR0ss&t=2210)
    - [Uninformed Search — Breadth-First Search, Depth-First Search, Iterative Deepening](https://youtu.be/rwefoi__Fk4)
    - [Heuristic Search — Greedy Search, A*-Search, IDA*-Search](https://youtu.be/THZ3YxHAwno)
    - [Games with Opponents — Heuristic Evaluation Functions](https://youtu.be/IW-HI0Pqgsk)

## Week 6

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/Search_Games_and_Problem_Solving.pdf)
  * [Search, Games, and Problem Solving]({{ page.url }}/Search_Games_and_Problem_Solving.pdf)
* **Exercise, Lab:** Exercises in Chapter 6 of the textbook
* **Preparation for next week:** 
  * [Reasoning with Uncertainty]({{ page.url }}/Reasoning_with_Uncertainty.pdf)
  * Chapter 7 of the textbook
  * Prof. Ertel’s Lectures at Ravensburg-Weingarten University in 2011
    - [Computing with Probabilities](https://youtu.be/IW-HI0Pqgsk&t=4455)
    - [Computing with Probabilities — The Principle of Maximum Entropy](https://youtu.be/wbbAA8og4D8)
    - [The Maximum Entropy Method](https://youtu.be/MWAWjCUuDUs)
    - [The Maximum Entropy Method — LEXMED](https://youtu.be/sQLzN6zWosY)
    - [LEXMED — Reasoning with Bayesian Networks](https://youtu.be/xfv8xIk1-x4)
    - [Reasoning with Bayesian Networks](https://youtu.be/z-WrA1xbkdY)
    - [Reasoning with Bayesian Networks](https://youtu.be/gMjuL5vMo04)

## Week 7

* **Theory:** 
  * [Discussion]({{ page.url }}/Discussion/Reasoning_with_Uncertainty.pdf)
  * [Reasoning with Uncertainty]({{ page.url }}/Reasoning_with_Uncertainty.pdf)
* **Exercise, Lab:** Exercises in Chapter 7 of the textbook

## Weeks 8-9

In-class time is used for students to work on their mini-projects

## Weeks 10-14

Mini-project presentations and evaluations

-->

-----

# History of announcements