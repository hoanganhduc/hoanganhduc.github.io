---
layout: default
title: "VNU-HUS MAT1206E - Mini Projects"
last_modified_at: 2026-09-21
lang: "en"
katex: true
---

<div class="alert alert-info" markdown="1">

<h1>About</h1>

This page explains how to prepare and register a mini-project topic for "Introduction to Artificial Intelligence (VNU-HUS MAT1206E)" during Semester 1 of the 2026-2027 academic year. Proposed topics and updates are recorded on the private [MAT1206E topic board](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues).

</div>

## About the Mini Projects

Use the [student project template](https://github.com/VNU-HUS/introai-final-project-template). Read the [detailed submission guide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) and study the [worked topic-proposal example](https://github.com/VNU-HUS/introai-final-project-template/tree/main/examples/topic-proposal) before starting. The project is graded manually according to the [mini-project rubric](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md); Classroom50 does not grade this assignment.

## How to Register a Mini-Project Topic

**The course topic board is available to course members.** [Browse topics](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues), then use the [Project topic proposal form](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues/new?template=project-proposal.yml) after your group has its private Classroom50 repository and an agreed proposal commit. Sign in with your registered GitHub account; access requires membership of the MAT1206E Classroom50 student team. If GitHub shows a 404, ask the lecturers to check your course-team membership.

The Classroom50 `final-project` acceptance link is published in step 2 below and starts accepting on **September 11, 2026 at 13:00 ICT (UTC+7)**. Before you accept, form your group, read the guide and existing topics, and prepare your ideas. Do not open a topic-registration issue in the student-template repository, and do not submit a placeholder issue without the required proposal commit.

1. **Form the group and choose one founder.** Agree on one to five students from the same course and verify everyone's GitHub username. Review existing proposals on the course topic board before settling on a precise problem.
2. **Only the founder accepts `final-project` in Classroom50.** Use this course's acceptance link. **Other members must not accept separately:** this can create duplicate project repositories.<br>**Classroom50:** [Final Examination Mini-Project](https://classroom50.org/VNU-HUS/vnu-hus-mat1206e-winter-2026/assignments/final-project/accept)
3. **Initialize the group's private repository and add members.** Follow the [bootstrap instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) to copy the starter into the empty repository created by Classroom50. Do not create a second project repository or push to the starter. Add the other agreed members as collaborators, then complete [`team.json`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/team.json) and the private root README with each member's full name, student ID, and GitHub username.
4. **Prepare the proposal together.** Study the [completed proposal example](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/proposal.example.md), then complete your own [`proposal/proposal.md`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/proposal/proposal.md), including a precise selected problem, scope and non-goals, method, and expected output. [Mini-Project Ideas](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Mini-Project%20Ideas.md) offers optional inspiration. Edit the real proposal and membership files, not the example files; do not submit the example verbatim.
5. **Review, optionally check, then commit and push.** Every listed member must agree to the proposal and submitted version. You may run `python3 check_project_files.py proposal` using the [optional structural checker](https://github.com/VNU-HUS/introai-final-project-template/blob/main/check_project_files.py). Save the permanent GitHub commit URL or complete 40-character SHA after pushing.
6. **Register through one [MAT1206E topic-board issue](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues).** Search for your exact group-repository URL and the founder's GitHub username. Reuse an existing group issue; repair an incomplete issue rather than opening another, and ask staff if the canonical issue is unclear. If no group issue exists, the founder opens the [Project topic proposal form](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues/new?template=project-proposal.yml), completes every field, and links the exact proposal commit. Follow the [completed issue example](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/topic-issue.example.md).
7. **Continue in the same canonical issue.** Keep proposal revisions, exact-duplicate corrections, scheduling communication, and final submission in that issue. Push each revised proposal and post its new commit URL or SHA there. Changing the representative does not create a new issue; record the agreed handover in the existing issue.

### Important Notices

<div class="alert alert-warning" markdown="1">

**Acceptance is not topic registration.** Each group uses **one private Classroom50 repository and one canonical topic-board issue**. The founder handles administrative actions, but cannot unilaterally change membership, the selected problem, scope, proposal, or submitted commit; every member must agree.

**Protect private identities and identify the exact version.** Full names and student IDs stay in the private repository; identify members in the class-visible issue by GitHub username only. Use an immutable commit URL or full SHA, not a branch link, a screenshot, or a link to the latest file.

**Registration is not academic approval.** `status: submitted` means awaiting the exact-duplicate check. `status: recorded` means no earlier exact duplicate was found when staff reviewed the issue; it is not approval or a guarantee of feasibility, correctness, quality, or a passing grade. `status: duplicate-problem` requires a revised problem and a new proposal commit in the **same issue**. The proposal is required but ungraded; the optional checker gives no score and does not evaluate project quality.

</div>

### Deadlines

| Required submission | Deadline (ICT, UTC+7) |
|---|---|
| Topic registration, initial proposal and required corrections | **September 27, 2026 at 23:59** |
| Exact-duplicate correction, when required | **September 27, 2026 at 23:59** |
| Final commit and `FINAL SUBMISSION` comment in the same issue | **November 4, 2026 at 23:59** |

The final deadline is the same for all groups; proposal revisions and presentation order do not extend it. See the [submission guide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) for the complete calendar and comment formats.

## Final Report, Presentation, and Evaluation

Follow the [report instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/report/README.md) and [slide instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/slides/README.md). Every group member participates in the presentation. Complete the private [contribution record](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/CONTRIBUTIONS.md), [AI-use declaration](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/AI_USAGE.md), and [external-resource declaration](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/EXTERNAL_RESOURCES.md). Evaluation follows the [manual grading rubric](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md).

## Lecturers Involved in Evaluation

* Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `hoanganhduc[at]hus.edu.vn` (replace `[at]` with `@`)
  * GitHub Username: [hoanganhduc](https://github.com/hoanganhduc)
* Lê Huy Hùng (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `lehuyhung94[at]gmail.com` (replace `[at]` with `@`)
  * GitHub Username: [HuyHung0](https://github.com/HuyHung0)

<a id="recorded-topics"></a>

## Proposed Topics

The private [topic board](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues) remains the official record for registration and updates. Only reviewed registrations currently labeled **status: recorded** are published below. Group numbers follow the most recent assignment of that label, from earliest to latest; removing and reapplying the label changes the ordering timestamp. Numbers may therefore change. Recording is not academic approval or a guarantee of quality. Presentation times will be announced separately. Repository links remain private and require the appropriate access.

<!-- BEGIN RECORDED MINI-PROJECTS -->

1. <a id="topic-6aa2ca71bc2a"></a><a id="group-1"></a>**Group 1:** Traffic Sign Recognition for Autonomous Driving Using Deep Learning
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002016-cpu](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002016-cpu)

2. <a id="topic-50deedf3ef96"></a><a id="group-4"></a>**Group 2:** Hanoi Explorer Chatbot
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-binhlee1910](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-binhlee1910)

3. <a id="topic-9df1fec598dc"></a><a id="group-5"></a>**Group 3:** Phân loại chữ số viết tay bằng học máy
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-baongoc2405-2](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-baongoc2405-2)

4. <a id="topic-a9b4bdf8cf69"></a><a id="group-6"></a>**Group 4:** Developing an Intelligent Agent for Gomoku using Minimax with Alpha-Beta Pruning and Heuristic Evaluation
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenha122676](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenha122676)

5. <a id="topic-2d07227ee943"></a><a id="group-7"></a>**Group 5:** ChessMind: A Reinforcement Learning-Based Chess AI
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-tranmanhthangg](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-tranmanhthangg)

6. <a id="topic-6e894db53af8"></a>**Group 6:** Autonomous Driving in a Simulation Environment Using Object Detection and Reinforcement Learning
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002072-cloud](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002072-cloud)

7. <a id="topic-fa6a923d1dba"></a>**Group 7:** Hệ thống AI hỗ trợ phát hiện sớm và chuẩn đoán tổn thương ung thư vòm họng &amp; khoang miệng
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-haduy2k6](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-haduy2k6)

<!-- END RECORDED MINI-PROJECTS -->
