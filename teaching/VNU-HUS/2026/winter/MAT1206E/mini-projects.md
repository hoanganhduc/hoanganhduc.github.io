---
layout: default
title: "VNU-HUS MAT1206E - Mini Projects"
last_modified_at: 2026-10-09
lang: "en"
katex: true
---

<div class="alert alert-info" markdown="1">

<h1>About</h1>

This page explains how to prepare and register a mini-project topic for "Introduction to Artificial Intelligence (VNU-HUS MAT1206E)" during Semester 1 of the 2026-2027 academic year. Proposed topics and updates are recorded on the private [MAT1206E topic board](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues).

</div>

<div class="alert alert-warning" id="registration-closed" markdown="1">

**Registration remains closed.** The final cutoff for registration, required corrections and continuation confirmation was **October 7, 2026 at 23:59 ICT (UTC+7)**. The [topic board](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues) is temporarily archived and read-only: new issues, edits and comments, including `FINAL SUBMISSION`, are paused. It will be reopened near the submission deadline; the exact reopening date has not been announced. Continue working in the existing student project repositories, which are not affected by this temporary topic-board archive. This does not reopen registration or permit changes to the finalized group list, membership or selected topics. The final list below contains **14 groups**. Complete and submit the final product by **November 22, 2026 at 23:59 ICT (UTC+7)**; see the [confirmed milestones](#project-milestones) and [submission procedure](#final-submission) below.

</div>

## About the Mini Projects

Use the [student project template](https://github.com/VNU-HUS/introai-final-project-template). Read the [detailed submission guide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) and study the [worked topic-proposal example](https://github.com/VNU-HUS/introai-final-project-template/tree/main/examples/topic-proposal) before starting. The project is graded manually according to the [mini-project rubric](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md); Classroom50 does not grade this assignment.

## Original Registration Procedure (Closed; Reference Only)

**Topic registration remains closed; topic-board comments are temporarily paused.** [View the official registration records](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues). Access remains limited to course members. The original registration steps below are retained for reference only; they do not reopen registration or permit a new group or replacement repository.

The Classroom50 `final-project` acceptance link is published in step 2 below and began accepting on **September 11, 2026 at 13:00 ICT (UTC+7)**. Before you accept, form your group, read the guide and existing topics, and prepare your ideas. Do not open a topic-registration issue in the student-template repository, and do not submit a placeholder issue without the required proposal commit.

1. **Form the group and choose one founder.** Agree on one to five students from the same course and verify everyone's GitHub username. Review existing proposals on the course topic board before settling on a precise problem.
2. **Only the founder accepts `final-project` in Classroom50.** Use this course's acceptance link. **Other members must not accept separately:** this can create duplicate project repositories.<br>**Classroom50:** [Final Examination Mini-Project](https://classroom50.org/VNU-HUS/vnu-hus-mat1206e-winter-2026/assignments/final-project/accept)
3. **Initialize the group's private repository and add members.** Follow the [bootstrap instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) to copy the starter into the empty repository created by Classroom50. Do not create a second project repository or push to the starter. Add the other agreed members as collaborators, then complete [`team.json`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/team.json) and the private root README with each member's full name, student ID, and GitHub username.
4. **Prepare the proposal together.** Study the [completed proposal example](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/proposal.example.md), then complete your own [`proposal/proposal.md`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/proposal/proposal.md), including a precise selected problem, scope and non-goals, method, and expected output. [Mini-Project Ideas](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Mini-Project%20Ideas.md) offers optional inspiration. Edit the real proposal and membership files, not the example files; do not submit the example verbatim.
5. **Review, optionally check, then commit and push.** Every listed member must agree to the proposal and submitted version. You may run `python3 check_project_files.py proposal` using the [optional structural checker](https://github.com/VNU-HUS/introai-final-project-template/blob/main/check_project_files.py). Save the permanent GitHub commit URL or complete 40-character SHA after pushing.
6. **Register through one [MAT1206E topic-board issue](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues).** Search for your exact group-repository URL and the founder's GitHub username. Reuse an existing group issue; repair an incomplete issue rather than opening another, and ask staff if the canonical issue is unclear. If no group issue exists, the founder opens the Project topic proposal form (during the former registration period), completes every field, and links the exact proposal commit. Follow the [completed issue example](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/topic-issue.example.md).
7. **Keep the original issue for final submission.** After the topic board is reopened, groups in the finalized list post a new `FINAL SUBMISSION` comment in their existing canonical issue, without changing the topic-registration body. Do not create a new issue or replacement repository. Follow the [final-submission procedure](#final-submission) and the deadline on this website.

### Important Notices

<div class="alert alert-warning" markdown="1">

**Acceptance is not topic registration.** Each group uses **one private Classroom50 repository and one canonical topic-board issue**. The founder handles administrative actions, but cannot unilaterally change membership, the selected problem, scope, proposal, or submitted commit; every member must agree.

**Protect private identities and identify the exact version.** Full names and student IDs stay in the private repository; identify members in the class-visible issue by GitHub username only. Use an immutable commit URL or full SHA, not a branch link, a screenshot, or a link to the latest file.

**Registration is not academic approval.** `status: submitted` means awaiting the exact-duplicate check. `status: recorded` means no earlier exact duplicate was found when staff reviewed the issue; it is not approval or a guarantee of feasibility, correctness, quality, or a passing grade. `status: duplicate-problem` requires a revised problem and a new proposal commit in the **same issue**. The proposal is required but ungraded; the optional checker gives no score and does not evaluate project quality.

</div>

<a id="deadlines"></a>
<a id="project-milestones"></a>

### Confirmed Milestones and Deadlines

| Milestone | Confirmed time (ICT, UTC+7) |
|---|---|
| Final cutoff for topic registration, required corrections and continuation confirmation (closed) | **October 7, 2026 at 23:59** |
| Exact-duplicate correction, when required (closed) | **October 7, 2026 at 23:59** |
| Complete and submit final project deliverables (all groups) | **November 22, 2026 at 23:59** (previous submission deadline: **November 4, 2026 at 23:59**) |
| Pre-presentation record review and evaluation preparation | November 23--24, 2026 |
| First MAT1206E presentation | **November 30, 2026, period 3** (previously scheduled to begin: **November 6, 2026**) |
| Last MAT1206E presentation; end of this course's presentation assessment | **December 14, 2026 at 10:40**, end of period 4 |
| End of the combined MAT1206E/MAT3508 presentation round | December 16, 2026 at 10:40 |

**The November 4, 2026 deliverable deadline in the original submission guide and previously displayed on this website is superseded by November 22, 2026 at 23:59.** The new deadline is common to both courses and all groups, regardless of presentation date. Assessment uses the final version submitted by that common deadline; presenting later or swapping slots does not provide extra time to improve the submitted product. Registration remains closed.

**All dates and deadlines follow this course website, not the original submission guide. All other requirements continue to follow the [submission guide already posted](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md).** This timeline update does not replace the other instructions for preparing and submitting the project.

<a id="final-submission"></a>

### Final submission in the original issue

**Temporary pause from October 9, 2026:** the board is archived, so comments cannot currently be posted. It will be reopened near the submission deadline. No exact reopening date has been announced. The procedure below remains in force after reopening; no alternative submission channel is introduced.

Once the board is reopened and all members agree to the final version, push it to the group's existing private repository and post the following **new comment in the original topic-registration issue by November 22, 2026 at 23:59 ICT (UTC+7)**. Use the exact permanent commit URL or complete SHA. Both the final commit and the comment must be submitted by this common deadline. This is the procedure in section 15 of the [previously posted submission guide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md), with the deadline updated according to this website.

```text
FINAL SUBMISSION

Final commit:
<permanent commit URL or complete SHA>

Report:
report/report.pdf at the final commit

Slides:
slides/slides.pdf at the final commit

All listed members agree to this submitted version: yes
```

Do not create a new issue, edit the original registration to submit, or use a Classroom50 grading/submission trigger. The comment and exact Git commit identify the submitted version. Registration remains closed; submitting a final version does not change the finalized groups, members or topics.

## Final Report, Presentation, and Evaluation

Follow the [report instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/report/README.md) and [slide instructions](https://github.com/VNU-HUS/introai-final-project-template/blob/main/slides/README.md). Every group member participates in the presentation. Complete the private [contribution record](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/CONTRIBUTIONS.md), [AI-use declaration](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/AI_USAGE.md), and [external-resource declaration](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/EXTERNAL_RESOURCES.md). Evaluation follows the [manual grading rubric](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md).

<a id="presentation-schedule"></a>

## Confirmed Presentation Schedule

**Each group has one teaching period in total**, including the presentation, demonstration and questions. Every member participates. The schedule uses the course's four lab periods and two theory periods per week as shared presentation slots: follow your assigned slot below, regardless of your original lab section. Group numbers, topics and membership remain unchanged.

**Timetable reference (ICT, UTC+7):** Monday, periods 1--2: 07:00--08:45; periods 3--4: 08:50--10:40, Room 508-T5. Friday, periods 7--8: 13:00--14:45, Room 506-T3. These are two-period timetable blocks; each row below allocates only the single numbered period to one group.

Click a Group number to view its registered topic and repository.

| Date (DD/MM/YYYY) | Day | Period | Group | Room |
|---|---|---:|---|---|
| 30/11/2026 | Monday | 3 | [Group 14](#topic-e5d07f88a08e) | 508-T5 |
| 30/11/2026 | Monday | 4 | [Group 2](#topic-9df1fec598dc) | 508-T5 |
| 04/12/2026 | Friday | 7 | [Group 11](#topic-1c1b8951abb7) | 506-T3 |
| 04/12/2026 | Friday | 8 | [Group 4](#topic-2d07227ee943) | 506-T3 |
| 07/12/2026 | Monday | 1 | [Group 8](#topic-6c402ed913a5) | 508-T5 |
| 07/12/2026 | Monday | 2 | [Group 7](#topic-dfac5a42eb1f) | 508-T5 |
| 07/12/2026 | Monday | 3 | [Group 5](#topic-6e894db53af8) | 508-T5 |
| 07/12/2026 | Monday | 4 | [Group 1](#topic-50deedf3ef96) | 508-T5 |
| 11/12/2026 | Friday | 7 | [Group 12](#topic-d4e777ea709c) | 506-T3 |
| 11/12/2026 | Friday | 8 | [Group 10](#topic-c6616b8fdb9e) | 506-T3 |
| 14/12/2026 | Monday | 1 | [Group 3](#topic-a9b4bdf8cf69) | 508-T5 |
| 14/12/2026 | Monday | 2 | [Group 13](#topic-cc74ceee36fe) | 508-T5 |
| 14/12/2026 | Monday | 3 | [Group 9](#topic-fba7c54d5b6b) | 508-T5 |
| 14/12/2026 | Monday | 4 | [Group 6](#topic-fa6a923d1dba) | 508-T5 |

There are 14 presentation periods. Periods 1--2 on November 30 are not presentation slots in this schedule. The last presentation ends at **10:40 on December 14, 2026**, at the end of period 4.

### Swapping presentation slots

Two groups **in the same course** may swap their complete slots only when genuinely necessary. Both groups must agree, check that every member can attend the new slot, and submit the reason and both affected slots through Google Classroom **before the earlier slot**. The swap takes effect only after instructor approval. It changes only the presentation date/period (and the room associated with that slot), not Group numbers, topics, membership, the common November 22 submission deadline or the course's final presentation date. Do not edit the topic-registration issue to change the presentation schedule.

## Lecturers Involved in Evaluation

* Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `hoanganhduc[at]hus.edu.vn` (replace `[at]` with `@`)
  * GitHub Username: [hoanganhduc](https://github.com/hoanganhduc)
* Lê Huy Hùng (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `lehuyhung94[at]gmail.com` (replace `[at]` with `@`)
  * GitHub Username: [HuyHung0](https://github.com/HuyHung0)

<a id="recorded-topics"></a>

## Proposed Topics

The [topic board](https://github.com/VNU-HUS/mat1206e-2026-project-topics/issues) preserves the official registration history. The **final list of 14 groups** below matches the final registration decision and the verified **status: recorded** labels at closure. The surviving groups retain their numbers and topic anchors. Recording is not academic approval or a guarantee of quality or a passing grade. The [confirmed presentation schedule](#presentation-schedule) is published above. Repository links remain private and require the appropriate access.

<!-- BEGIN RECORDED MINI-PROJECTS -->

1. <a id="topic-50deedf3ef96"></a><a id="group-4"></a>**Group 1:** Hanoi Explorer Chatbot
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-binhlee1910](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-binhlee1910)

2. <a id="topic-9df1fec598dc"></a><a id="group-5"></a>**Group 2:** Phân loại chữ số viết tay bằng học máy
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-baongoc2405-2](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-baongoc2405-2)

3. <a id="topic-a9b4bdf8cf69"></a><a id="group-6"></a>**Group 3:** Developing an Intelligent Agent for Gomoku using Minimax with Alpha-Beta Pruning and Heuristic Evaluation
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenha122676](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenha122676)

4. <a id="topic-2d07227ee943"></a><a id="group-7"></a>**Group 4:** ChessMind: A Reinforcement Learning-Based Chess AI
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-tranmanhthangg](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-tranmanhthangg)

5. <a id="topic-6e894db53af8"></a>**Group 5:** Autonomous Driving in a Simulation Environment Using Object Detection and Reinforcement Learning
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002072-cloud](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-24002072-cloud)

6. <a id="topic-fa6a923d1dba"></a>**Group 6:** Hệ thống AI hỗ trợ phát hiện sớm và chuẩn đoán tổn thương ung thư vòm họng &amp; khoang miệng
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-haduy2k6](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-haduy2k6)

7. <a id="topic-dfac5a42eb1f"></a>**Group 7:** Xây dựng Agent AI chơi Cờ Vây kích thước nhỏ (9x9) sử dụng Học có nhãn (Supervised Learning)
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-lna-1806](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-lna-1806)

8. <a id="topic-6c402ed913a5"></a>**Group 8:** Movie Recommendation System using Collaborative Filtering and Content-Based Filtering
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenthetai0012](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nguyenthetai0012)

9. <a id="topic-fba7c54d5b6b"></a>**Group 9:** Resume and Job Description Matching System
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-ngocquyendang](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-ngocquyendang)

10. <a id="topic-c6616b8fdb9e"></a>**Group 10:** Arithmetic-Aware AI Agent for Vietnamese Mathematical Chess
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-phanlab](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-phanlab)

11. <a id="topic-1c1b8951abb7"></a>**Group 11:** AI-Based Malicious URL Detection Using Machine Learning
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-snowyn-856](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-snowyn-856)

12. <a id="topic-d4e777ea709c"></a>**Group 12:** Development of an Intelligent Driver Monitoring System for Drowsiness and Distraction Detection Using Facial Biometrics.
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-khoii14](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-khoii14)

13. <a id="topic-cc74ceee36fe"></a>**Group 13:** Hệ thống AI tóm tắt tài liệu và hỗ trợ ghi nhớ kiến thức
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nttrang-hus](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-nttrang-hus)

14. <a id="topic-e5d07f88a08e"></a>**Group 14:** License-Plate-Number-Detection
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-dovanvinh28092004](https://github.com/VNU-HUS/vnu-hus-mat1206e-winter-2026-final-project-dovanvinh28092004)

<!-- END RECORDED MINI-PROJECTS -->
