---
layout: default
title: "VNU-HUS MAT3508 - Bài tập nhóm"
last_modified_at: 2026-09-21
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">

<h1>Giới thiệu</h1>

Trang này hướng dẫn chuẩn bị và đăng ký chủ đề bài tập nhóm cho môn "Nhập môn Trí tuệ Nhân tạo (VNU-HUS MAT3508)" trong Học kỳ 1 năm học 2026-2027. Các đề xuất và cập nhật được ghi nhận trên [bảng chủ đề MAT3508](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues) riêng tư của học phần.

</div>

## Về Bài tập nhóm

Sử dụng [kho mẫu dự án dành cho sinh viên](https://github.com/VNU-HUS/introai-final-project-template). Đọc [hướng dẫn nộp bài chi tiết](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) và xem [ví dụ hoàn chỉnh về đề xuất chủ đề](https://github.com/VNU-HUS/introai-final-project-template/tree/main/examples/topic-proposal) trước khi bắt đầu. Dự án được chấm thủ công theo [tiêu chí đánh giá](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md); Classroom50 không chấm điểm bài tập này.

## Cách Đăng ký Chủ đề Bài tập nhóm

**Bảng chủ đề đã sẵn sàng cho thành viên học phần.** [Xem các chủ đề](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues), rồi dùng [biểu mẫu Project topic proposal](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues/new?template=project-proposal.yml) sau khi nhóm có kho Classroom50 riêng tư và commit đề xuất đã được mọi thành viên thống nhất. Đăng nhập bằng tài khoản GitHub đã đăng ký; quyền truy cập yêu cầu thành viên thuộc nhóm sinh viên MAT3508 trên Classroom50. Nếu GitHub hiển thị lỗi 404, liên hệ giảng viên để kiểm tra tư cách thành viên nhóm của học phần.

Liên kết nhận bài `final-project` trên Classroom50 đã được công bố ở bước 2 bên dưới và bắt đầu nhận bài từ **13:00 ngày 11/09/2026, giờ ICT (UTC+7)**. Trước khi nhận bài, hãy lập nhóm, đọc hướng dẫn và các chủ đề đã có, rồi chuẩn bị ý tưởng. Không mở issue đăng ký chủ đề trong kho mẫu dành cho sinh viên và không nộp issue giữ chỗ khi chưa có commit đề xuất bắt buộc.

1. **Lập nhóm và chọn một người khởi tạo (founder).** Thống nhất từ một đến năm sinh viên cùng học phần và kiểm tra tên người dùng GitHub của từng thành viên. Xem các đề xuất đã có trên bảng chủ đề trước khi chọn bài toán cụ thể.
2. **Chỉ người khởi tạo nhận bài `final-project` trên Classroom50.** Sử dụng liên kết của đúng học phần. **Các thành viên khác không nhận bài riêng:** thao tác này có thể tạo nhiều kho dự án trùng nhau.<br>**Classroom50:** [Final Examination Mini-Project](https://classroom50.org/VNU-HUS/vnu-hus-mat3508-winter-2026/assignments/final-project/accept)
3. **Khởi tạo nội dung kho riêng tư của nhóm và thêm thành viên.** Làm theo [hướng dẫn đưa mẫu vào kho](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) để sao chép nội dung mẫu vào kho trống do Classroom50 tạo. Không tạo kho dự án thứ hai và không đẩy nội dung lên kho mẫu. Thêm các thành viên đã thống nhất làm cộng tác viên, rồi điền [`team.json`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/team.json) và README ở thư mục gốc của kho riêng tư với họ tên đầy đủ, mã sinh viên và tên người dùng GitHub của từng người.
4. **Cùng chuẩn bị đề xuất.** Xem [ví dụ đề xuất đã điền](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/proposal.example.md), rồi hoàn thành [`proposal/proposal.md`](https://github.com/VNU-HUS/introai-final-project-template/blob/main/proposal/proposal.md) của nhóm, nêu rõ bài toán cụ thể, phạm vi và phần không thực hiện, phương pháp và kết quả dự kiến. [Một số ý tưởng dự án](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Mini-Project%20Ideas.md) chỉ là gợi ý tham khảo. Sửa tệp đề xuất và danh sách thành viên thật của nhóm, không sửa các tệp ví dụ; không nộp nguyên văn ví dụ.
5. **Thống nhất, kiểm tra tùy chọn, rồi commit và push.** Mọi thành viên có tên trong nhóm phải đồng ý với đề xuất và phiên bản nộp. Có thể chạy `python3 check_project_files.py proposal` bằng [công cụ kiểm tra cấu trúc tùy chọn](https://github.com/VNU-HUS/introai-final-project-template/blob/main/check_project_files.py). Sau khi push, lưu URL cố định của commit trên GitHub hoặc mã SHA đầy đủ gồm 40 ký tự.
6. **Đăng ký bằng một issue trên [bảng chủ đề MAT3508](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues).** Tìm theo đúng URL kho của nhóm và tên người dùng GitHub của người khởi tạo. Tiếp tục dùng issue đã có; bổ sung issue chưa đầy đủ thay vì mở issue khác, và hỏi giảng viên khi chưa rõ issue nào là chính thức. Nếu nhóm chưa có issue, người khởi tạo mở [biểu mẫu Project topic proposal](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues/new?template=project-proposal.yml), điền mọi trường và liên kết commit đề xuất cụ thể. Tham khảo [ví dụ issue đã điền](https://github.com/VNU-HUS/introai-final-project-template/blob/main/examples/topic-proposal/topic-issue.example.md).
7. **Tiếp tục sử dụng cùng issue chính thức.** Mọi lần sửa đề xuất, xử lý trùng bài toán, trao đổi lịch trình và nộp bài cuối cùng đều thực hiện trong issue đó. Push mỗi bản đề xuất sửa đổi và đăng URL commit hoặc SHA mới tại đây. Đổi người đại diện không tạo issue mới; ghi nhận việc bàn giao đã được nhóm thống nhất trong issue hiện có.

### Những điểm quan trọng

<div class="alert alert-warning" markdown="1">

**Nhận bài không đồng nghĩa với đăng ký chủ đề.** Mỗi nhóm sử dụng **một kho Classroom50 riêng tư và một issue chính thức trên bảng chủ đề**. Người khởi tạo thực hiện các thao tác hành chính, nhưng không được tự quyết định thay đổi thành viên, bài toán, phạm vi, đề xuất hoặc commit nộp; mọi thành viên phải đồng ý.

**Bảo vệ thông tin cá nhân và xác định đúng phiên bản.** Họ tên đầy đủ và mã sinh viên chỉ lưu trong kho riêng tư; issue mà lớp xem được chỉ định danh thành viên bằng tên người dùng GitHub. Dùng URL cố định của commit hoặc SHA đầy đủ, không dùng liên kết nhánh, ảnh chụp màn hình hay liên kết đến tệp mới nhất.

**Ghi nhận chủ đề không phải là phê duyệt học thuật.** `status: submitted` nghĩa là đang chờ kiểm tra trùng bài toán cụ thể. `status: recorded` nghĩa là tại thời điểm giảng viên kiểm tra, không phát hiện bài toán trùng chính xác đã được đăng ký trước; đây không phải là phê duyệt hay bảo đảm về tính khả thi, tính đúng đắn, chất lượng hoặc điểm đạt. Với `status: duplicate-problem`, nhóm phải điều chỉnh bài toán và đăng commit đề xuất mới trong **cùng issue**. Đề xuất là bắt buộc nhưng không chấm điểm; công cụ kiểm tra tùy chọn không cho điểm và không đánh giá chất lượng dự án.

</div>

### Hạn nộp

| Nội dung phải nộp | Hạn nộp (ICT, UTC+7) |
|---|---|
| Đăng ký chủ đề, đề xuất ban đầu và hoàn thiện hồ sơ | **23:59 ngày 27/09/2026** |
| Bản sửa khi trùng bài toán, nếu được yêu cầu | **23:59 ngày 27/09/2026** |
| Commit cuối cùng và bình luận `FINAL SUBMISSION` trong cùng issue | **23:59 ngày 04/11/2026** |

Hạn nộp cuối cùng áp dụng chung cho mọi nhóm; việc sửa đề xuất và thứ tự thuyết trình không làm thay đổi hạn này. Xem [hướng dẫn nộp bài](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Submission%20Guide.md) để biết toàn bộ lịch trình và mẫu bình luận.

## Báo cáo, Thuyết trình và Đánh giá

Làm theo [hướng dẫn báo cáo](https://github.com/VNU-HUS/introai-final-project-template/blob/main/report/README.md) và [hướng dẫn slide](https://github.com/VNU-HUS/introai-final-project-template/blob/main/slides/README.md). Mọi thành viên phải tham gia thuyết trình. Hoàn thành các tệp riêng tư về [đóng góp của thành viên](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/CONTRIBUTIONS.md), [khai báo sử dụng AI](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/AI_USAGE.md) và [khai báo tài nguyên bên ngoài](https://github.com/VNU-HUS/introai-final-project-template/blob/main/docs/EXTERNAL_RESOURCES.md). Giảng viên đánh giá theo [tiêu chí chấm thủ công](https://github.com/VNU-HUS/introai-final-project-template/blob/main/Rubrics.md).

## Giảng viên tham gia đánh giá

* Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`)
  * GitHub Username: [hoanganhduc](https://github.com/hoanganhduc)
* Lê Huy Hùng (Đại học KHTN, ĐHQG Hà Nội)
  * Email: `lehuyhung94[at]gmail.com` (thay `[at]` bằng `@`)
  * GitHub Username: [HuyHung0](https://github.com/HuyHung0)

<a id="recorded-topics"></a>

## Các Chủ Đề Đề Xuất

[Bảng chủ đề riêng tư](https://github.com/VNU-HUS/mat3508-2026-project-topics/issues) tiếp tục là hồ sơ đăng ký và cập nhật chính thức. Chỉ những hồ sơ đã được kiểm tra đạt yêu cầu và hiện có nhãn **status: recorded** mới được công bố dưới đây. Số Group theo thời điểm gắn nhãn này gần nhất, sắp từ sớm đến muộn; nhãn bị gỡ rồi gắn lại thì dùng thời điểm gắn lại. Vì vậy, số Group có thể thay đổi. Ghi nhận không phải phê duyệt học thuật hay bảo đảm chất lượng. Lịch thuyết trình cụ thể sẽ thông báo sau. Liên kết kho nhóm vẫn riêng tư và chỉ tài khoản có quyền mới truy cập được.

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

<!-- END RECORDED MINI-PROJECTS -->
