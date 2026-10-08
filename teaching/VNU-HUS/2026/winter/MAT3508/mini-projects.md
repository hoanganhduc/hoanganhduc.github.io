---
layout: default
title: "VNU-HUS MAT3508 - Bài tập nhóm"
last_modified_at: 2026-10-08
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">

<h1>Giới thiệu</h1>

Trang này hướng dẫn chuẩn bị và đăng ký chủ đề bài tập nhóm cho môn "Nhập môn Trí tuệ Nhân tạo (VNU-HUS MAT3508)" trong Học kỳ 1 năm học 2026-2027. Các đề xuất và cập nhật được ghi nhận trên [bảng chủ đề MAT3508](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues) riêng tư của học phần.

</div>

<div class="alert alert-warning" id="registration-closed" markdown="1">

**Đã đóng đăng ký.** Hạn chốt cuối cùng cho đăng ký, hoàn thiện hồ sơ và xác nhận tiếp tục là **23:59 ngày 07/10/2026 (ICT, UTC+7)**. Từ ngày 08/10, [bảng chủ đề](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues) đã được lưu trữ (archived), chỉ còn quyền đọc. Không tiếp nhận đăng ký mới, thay đổi hồ sơ đăng ký hoặc xác nhận tiếp tục sau hạn. Danh sách cuối cùng bên dưới gồm **20 nhóm**. Kho bài làm của sinh viên vẫn hoạt động; hạn sản phẩm cuối cùng nay là **23:59 ngày 22/11/2026 (ICT, UTC+7)**; xem [các mốc đã chốt](#project-milestones) bên dưới, có ghi kèm mốc cũ.

</div>

## Về Bài tập nhóm

Sử dụng [kho mẫu dự án dành cho sinh viên](https://github.com/VNU-HUS/introai-final-project-template). Đọc [hướng dẫn nộp bài chi tiết](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) và xem [ví dụ hoàn chỉnh về đề xuất chủ đề](https://github.com/VNU-HUS/introai-final-project-template/tree/main/examples/topic-proposal) trước khi bắt đầu. Dự án được chấm thủ công theo [tiêu chí đánh giá](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md); Classroom50 không chấm điểm bài tập này.

## Quy trình Đăng ký trước khi đóng (chỉ để tham khảo)

**Bảng chủ đề đã đóng đăng ký và chỉ còn quyền đọc.** [Xem hồ sơ đăng ký đã lưu trữ](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues). Quyền truy cập vẫn giới hạn trong học phần. Các bước đăng ký cũ bên dưới chỉ được giữ để tham khảo, không mở lại đăng ký và không cho phép lập nhóm mới hoặc tạo kho thay thế.

Liên kết nhận bài `final-project` trên Classroom50 đã được công bố ở bước 2 bên dưới và bắt đầu nhận bài từ **13:00 ngày 11/09/2026, giờ ICT (UTC+7)**. Trước khi nhận bài, hãy lập nhóm, đọc hướng dẫn và các chủ đề đã có, rồi chuẩn bị ý tưởng. Không mở issue đăng ký chủ đề trong kho mẫu dành cho sinh viên và không nộp issue giữ chỗ khi chưa có commit đề xuất bắt buộc.

1. **Lập nhóm và chọn một người khởi tạo (founder).** Thống nhất từ một đến năm sinh viên cùng học phần và kiểm tra tên người dùng GitHub của từng thành viên. Xem các đề xuất đã có trên bảng chủ đề trước khi chọn bài toán cụ thể.
2. **Chỉ người khởi tạo nhận bài `final-project` trên Classroom50.** Sử dụng liên kết của đúng học phần. **Các thành viên khác không nhận bài riêng:** thao tác này có thể tạo nhiều kho dự án trùng nhau.<br>**Classroom50:** [Final Examination Mini-Project](https://classroom50.org/VNU-HUS/vnu-hus-mat3508-winter-2026/assignments/final-project/accept)
3. **Khởi tạo nội dung kho riêng tư của nhóm và thêm thành viên.** Làm theo [hướng dẫn đưa mẫu vào kho](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) để sao chép nội dung mẫu vào kho trống do Classroom50 tạo. Không tạo kho dự án thứ hai và không đẩy nội dung lên kho mẫu. Thêm các thành viên đã thống nhất làm cộng tác viên, rồi điền [`team.json`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/team.json) và README ở thư mục gốc của kho riêng tư với họ tên đầy đủ, mã sinh viên và tên người dùng GitHub của từng người.
4. **Cùng chuẩn bị đề xuất.** Xem [ví dụ đề xuất đã điền](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/proposal.example.md), rồi hoàn thành [`proposal/proposal.md`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/proposal/proposal.md) của nhóm, nêu rõ bài toán cụ thể, phạm vi và phần không thực hiện, phương pháp và kết quả dự kiến. [Một số ý tưởng dự án](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Mini-Project%20Ideas.md) chỉ là gợi ý tham khảo. Sửa tệp đề xuất và danh sách thành viên thật của nhóm, không sửa các tệp ví dụ; không nộp nguyên văn ví dụ.
5. **Thống nhất, kiểm tra tùy chọn, rồi commit và push.** Mọi thành viên có tên trong nhóm phải đồng ý với đề xuất và phiên bản nộp. Có thể chạy `python3 check_project_files.py proposal` bằng [công cụ kiểm tra cấu trúc tùy chọn](https://github.com/VNU-HUS/introai-final-project-template/blob/main/check_project_files.py). Sau khi push, lưu URL cố định của commit trên GitHub hoặc mã SHA đầy đủ gồm 40 ký tự.
6. **Đăng ký bằng một issue trên [bảng chủ đề MAT3508](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues).** Tìm theo đúng URL kho của nhóm và tên người dùng GitHub của người khởi tạo. Tiếp tục dùng issue đã có; bổ sung issue chưa đầy đủ thay vì mở issue khác, và hỏi giảng viên khi chưa rõ issue nào là chính thức. Nếu nhóm chưa có issue, người khởi tạo mở biểu mẫu Project topic proposal (nay đã đóng), điền mọi trường và liên kết commit đề xuất cụ thể. Tham khảo [ví dụ issue đã điền](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/topic-issue.example.md).
7. **Quy trình cập nhật trong cùng issue đã kết thúc khi bảng đóng.** Bảng đã lưu trữ không nhận chỉnh sửa hoặc bình luận mới, kể cả `FINAL SUBMISSION`. Không tạo issue đăng ký thay thế. Kho bài làm của sinh viên không bị lưu trữ.

### Những điểm quan trọng

<div class="alert alert-warning" markdown="1">

**Nhận bài không đồng nghĩa với đăng ký chủ đề.** Mỗi nhóm sử dụng **một kho Classroom50 riêng tư và một issue chính thức trên bảng chủ đề**. Người khởi tạo thực hiện các thao tác hành chính, nhưng không được tự quyết định thay đổi thành viên, bài toán, phạm vi, đề xuất hoặc commit nộp; mọi thành viên phải đồng ý.

**Bảo vệ thông tin cá nhân và xác định đúng phiên bản.** Họ tên đầy đủ và mã sinh viên chỉ lưu trong kho riêng tư; issue mà lớp xem được chỉ định danh thành viên bằng tên người dùng GitHub. Dùng URL cố định của commit hoặc SHA đầy đủ, không dùng liên kết nhánh, ảnh chụp màn hình hay liên kết đến tệp mới nhất.

**Ghi nhận chủ đề không phải là phê duyệt học thuật.** `status: submitted` nghĩa là đang chờ kiểm tra trùng bài toán cụ thể. `status: recorded` nghĩa là tại thời điểm giảng viên kiểm tra, không phát hiện bài toán trùng chính xác đã được đăng ký trước; đây không phải là phê duyệt hay bảo đảm về tính khả thi, tính đúng đắn, chất lượng hoặc điểm đạt. Với `status: duplicate-problem`, nhóm phải điều chỉnh bài toán và đăng commit đề xuất mới trong **cùng issue**. Đề xuất là bắt buộc nhưng không chấm điểm; công cụ kiểm tra tùy chọn không cho điểm và không đánh giá chất lượng dự án.

</div>

<a id="hạn-nộp"></a>
<a id="project-milestones"></a>

### Các mốc và hạn nộp đã chốt

| Mốc công việc | Thời gian đã chốt (ICT, UTC+7) |
|---|---|
| Hạn chốt cuối cùng cho đăng ký, hoàn thiện hồ sơ và xác nhận tiếp tục (đã đóng) | **23:59 ngày 07/10/2026** |
| Bản sửa khi trùng bài toán, nếu được yêu cầu (đã đóng) | **23:59 ngày 07/10/2026** |
| Hoàn thành và nộp sản phẩm mini-project cuối cùng (mọi nhóm) | **23:59 ngày 22/11/2026** (mốc dự kiến cũ: **06/11/2026**) |
| Rà soát hồ sơ, chuẩn bị đánh giá trước buổi thuyết trình đầu tiên | Ngày 23--24/11/2026 |
| Bắt đầu thuyết trình MAT3508 | **Ngày 25/11/2026, tiết 3** |
| Kết thúc thuyết trình và đánh giá MAT3508 | **10:40 ngày 16/12/2026**, hết tiết 4 (thay mốc kết thúc dự kiến cũ: **06/11/2026**) |
| Kết thúc toàn bộ đợt thuyết trình của MAT1206E và MAT3508 | 10:40 ngày 16/12/2026 |

**Mốc nộp sản phẩm 04/11/2026 từng hiển thị trên website cũng được thay thế bằng 23:59 ngày 22/11/2026.** Hạn mới áp dụng chung cho cả hai môn và mọi nhóm, không phụ thuộc ngày trình bày. Giảng viên đánh giá phiên bản cuối cùng đã nộp tại hạn chung; trình bày muộn hơn hoặc đổi ca không làm tăng thời gian hoàn thiện sản phẩm đã nộp. Đăng ký vẫn đóng.

**Các mốc thời gian và deadlines áp dụng theo website môn học, không theo hướng dẫn nộp bài ban đầu. Các phần khác vẫn thực hiện theo [hướng dẫn nộp bài đã đăng](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md).** Bản cập nhật thời gian này không thay thế các hướng dẫn khác về chuẩn bị và nộp sản phẩm.

**Lưu ý về việc đóng bảng topic đã thông báo:** không thể đăng bình luận `FINAL SUBMISSION` khi bảng đã được lưu trữ. Bảng vẫn chỉ đọc; bản cập nhật này không mở lại bảng hoặc thiết lập kênh nộp thay thế.

## Báo cáo, Thuyết trình và Đánh giá

Làm theo [hướng dẫn báo cáo](https://github.com/VNU-HUS/introai-final-project-template/blob/main/report/README.md) và [hướng dẫn slide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/slides/README.md). Mọi thành viên phải tham gia thuyết trình. Hoàn thành các tệp riêng tư về [đóng góp của thành viên](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/CONTRIBUTIONS.md), [khai báo sử dụng AI](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/AI_USAGE.md) và [khai báo tài nguyên bên ngoài](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/EXTERNAL_RESOURCES.md). Giảng viên đánh giá theo [tiêu chí chấm thủ công](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md).

<a id="presentation-schedule"></a>

## Lịch thuyết trình đã chốt

**Mỗi nhóm có tổng cộng một tiết**, gồm thuyết trình, minh họa sản phẩm và hỏi đáp. Mọi thành viên đều tham gia. Bốn tiết thực hành và hai tiết lý thuyết mỗi tuần được dùng làm các ca thuyết trình chung của môn: nhóm thực hiện theo ca được xếp bên dưới, không giới hạn vào ca thực hành cũ của từng thành viên. Số Group, đề tài và thành viên giữ nguyên.

**Khung giờ theo thời khóa biểu (ICT, UTC+7):** Thứ Tư, tiết 1--2: 07:00--08:45; tiết 3--4: 08:50--10:40, phòng 508-T5. Thứ Sáu, tiết 9--10: 14:50--16:40, phòng 502-T3. Đây là các khung hai tiết; mỗi dòng bên dưới chỉ dành đúng một tiết được ghi cho một nhóm.

Bấm vào số Group để xem đề tài và kho bài làm tương ứng.

| Ngày | Thứ | Tiết | Group | Phòng |
|---|---|---:|---|---|
| 25/11/2026 | Thứ Tư | 3 | [Group 3](#topic-3c803bcf4a0a) | 508-T5 |
| 25/11/2026 | Thứ Tư | 4 | [Group 14](#topic-91fdcc3a5035) | 508-T5 |
| 27/11/2026 | Thứ Sáu | 9 | [Group 18](#topic-53e854ad316a) | 502-T3 |
| 27/11/2026 | Thứ Sáu | 10 | [Group 5](#topic-df48fa058583) | 502-T3 |
| 02/12/2026 | Thứ Tư | 1 | [Group 1](#topic-e37ca8cee302) | 508-T5 |
| 02/12/2026 | Thứ Tư | 2 | [Group 15](#topic-95a73f17d5b0) | 508-T5 |
| 02/12/2026 | Thứ Tư | 3 | [Group 6](#topic-a9d0cef043b7) | 508-T5 |
| 02/12/2026 | Thứ Tư | 4 | [Group 19](#topic-2b8328740fd0) | 508-T5 |
| 04/12/2026 | Thứ Sáu | 9 | [Group 10](#topic-7423cb94dd8c) | 502-T3 |
| 04/12/2026 | Thứ Sáu | 10 | [Group 13](#topic-d373a75885df) | 502-T3 |
| 09/12/2026 | Thứ Tư | 1 | [Group 4](#topic-6ad253f2cc96) | 508-T5 |
| 09/12/2026 | Thứ Tư | 2 | [Group 8](#topic-f10de72d858e) | 508-T5 |
| 09/12/2026 | Thứ Tư | 3 | [Group 11](#topic-c785bc81285c) | 508-T5 |
| 09/12/2026 | Thứ Tư | 4 | [Group 2](#topic-474e7e58ac01) | 508-T5 |
| 11/12/2026 | Thứ Sáu | 9 | [Group 16](#topic-cc93e2bc449f) | 502-T3 |
| 11/12/2026 | Thứ Sáu | 10 | [Group 20](#topic-8d5b340e97e1) | 502-T3 |
| 16/12/2026 | Thứ Tư | 1 | [Group 17](#topic-d76d7d94a065) | 508-T5 |
| 16/12/2026 | Thứ Tư | 2 | [Group 7](#topic-e52684eec25c) | 508-T5 |
| 16/12/2026 | Thứ Tư | 3 | [Group 12](#topic-115877b203fb) | 508-T5 |
| 16/12/2026 | Thứ Tư | 4 | [Group 9](#topic-1e500271315d) | 508-T5 |

Tổng cộng 20 tiết thuyết trình. Tiết 1--2 ngày 25/11 không xếp thuyết trình trong lịch này. Ca cuối kết thúc **lúc 10:40 ngày 16/12/2026**, hết tiết 4.

### Hoán đổi ca thuyết trình

Hai nhóm **trong cùng môn** được hoán đổi nguyên ca khi thực sự cần. Hai nhóm phải cùng đồng ý, kiểm tra mọi thành viên đều tham gia được ca mới, và gửi lý do cùng hai ca cần đổi qua Google Classroom **trước ca sớm hơn trong hai ca**. Chỉ được đổi sau khi giảng viên xác nhận. Việc đổi chỉ áp dụng cho ngày/tiết trình bày (và phòng tương ứng với ca), không đổi số Group, đề tài, thành viên, hạn nộp chung 22/11 hoặc ngày kết thúc thuyết trình của môn. Không sửa bảng topic đã lưu trữ để xin đổi ca.

## Giảng viên tham gia đánh giá

* Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`)
  * GitHub Username: [hoanganhduc](https://github.com/hoanganhduc)
* Lê Huy Hùng (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `lehuyhung94[at]gmail.com` (thay `[at]` bằng `@`)
  * GitHub Username: [HuyHung0](https://github.com/HuyHung0)

<a id="recorded-topics"></a>

## Các Chủ Đề Đề Xuất

[Bảng chủ đề đã lưu trữ](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues) giữ lịch sử đăng ký chính thức. **Danh sách cuối cùng gồm 20 nhóm** bên dưới khớp quyết định chốt và nhãn **status: recorded** đã kiểm chứng khi đóng bảng. Các nhóm còn lại giữ nguyên số Group và anchor chủ đề. Ghi nhận không phải phê duyệt học thuật hay bảo đảm chất lượng hoặc điểm đạt. [Lịch thuyết trình đã chốt](#presentation-schedule) được công bố bên trên. Liên kết kho nhóm vẫn riêng tư và chỉ tài khoản có quyền mới truy cập được.

<!-- BEGIN RECORDED MINI-PROJECTS -->

1. <a id="topic-e37ca8cee302"></a><a id="group-2"></a>**Group 1:** Implement Stable Diffusion v1.5 from scratch and Fine-Tuning with LoRA
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nqk-ishr](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nqk-ishr)

2. <a id="topic-474e7e58ac01"></a><a id="group-1"></a>**Group 2:** VSS — Video Search and Summarization
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-tienanhnguyen0101nd-ctrl](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-tienanhnguyen0101nd-ctrl)

3. <a id="topic-3c803bcf4a0a"></a><a id="group-5"></a>**Group 3:** Evaluating Transfer Learning and CNN Explainability for Recyclable Waste Image Classification
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-pdt37012-blip](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-pdt37012-blip)

4. <a id="topic-6ad253f2cc96"></a><a id="group-6"></a>**Group 4:** Genome Detective: AI-Based Bacterial Identification from Sequencing Reads
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nguyenhaiyenedu06](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nguyenhaiyenedu06)

5. <a id="topic-df48fa058583"></a><a id="group-7"></a>**Group 5:** Ứng dụng nhận diện bệnh trên lá cà chua bằng MobileNetV2
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-doanh9a246-afk](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-doanh9a246-afk)

6. <a id="topic-a9d0cef043b7"></a><a id="group-8"></a>**Group 6:** CView - Doanh nghiệp nào cần bạn?
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-uyennbu](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-uyennbu)

7. <a id="topic-e52684eec25c"></a><a id="group-9"></a>**Group 7:** AI TechPulse: An Intelligent Tech News Aggregation &amp; Q&amp;A Platform Powered by RAG
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-anhtuan-hus](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-anhtuan-hus)

8. <a id="topic-f10de72d858e"></a>**Group 8:** Phân tích kiến trúc và mô phỏng mô hình DeepSeek thu nhỏ
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-qtunggg](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-qtunggg)

9. <a id="topic-1e500271315d"></a>**Group 9:** Financial News Intelligence
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-vietthang2006](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-vietthang2006)

10. <a id="topic-7423cb94dd8c"></a>**Group 10:** Phân tích thực nghiệm các phương pháp tiếp cận bài toán Sliding Puzzle (N-puzzle) quy mô lớn và đề xuất hướng tối ưu hóa kết hợp
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-luong-dung](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-luong-dung)

11. <a id="topic-c785bc81285c"></a>**Group 11:** HUS Student Personal Assistant
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-tuanthichcode100](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-tuanthichcode100)

12. <a id="topic-115877b203fb"></a>**Group 12:** Hệ thống kiểm tra chất lượng bao bì và hạn sử dụng sản phẩm tự động
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-kakaotake](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-kakaotake)

13. <a id="topic-d373a75885df"></a>**Group 13:** Phishing URL Detection Using Machine Learning and Explainable AI
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-vudinhloc2712-ui](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-vudinhloc2712-ui)

14. <a id="topic-91fdcc3a5035"></a>**Group 14:** MemoRise - Know What You're About to Forget
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-24001674](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-24001674)

15. <a id="topic-95a73f17d5b0"></a>**Group 15:** Xây dựng mô hình nhận dạng ngôn ngữ ký hiệu Tiếng Việt đơn lẻ
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-qanhngx99](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-qanhngx99)

16. <a id="topic-cc93e2bc449f"></a>**Group 16:** Intelligent Football Analysis System
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-lymsious](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-lymsious)

17. <a id="topic-d76d7d94a065"></a>**Group 17:** Food Image Classification and Calories Estimation Using Transfer Learning
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nminz17](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-nminz17)

18. <a id="topic-53e854ad316a"></a>**Group 18:** Phân loại bệnh trên lá lúa bằng mạng nơ-ron tích chập (CNN) sử dụng học sâu
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-ngocq6867-png](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-ngocq6867-png)

19. <a id="topic-2b8328740fd0"></a>**Group 19:** Xây dựng mô hình AI nhận diện người đeo khẩu trang
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-letrongtuananht67-debug](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-letrongtuananht67-debug)

20. <a id="topic-8d5b340e97e1"></a>**Group 20:** Mô hình hóa và dự báo sự tích tụ vi nhựa trong hệ sinh thái
    * GitHub: [https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-23001539-lab](https://github.com/VNU-HUS/vnu-hus-mat3508-winter-2026-final-project-23001539-lab)

<!-- END RECORDED MINI-PROJECTS -->
