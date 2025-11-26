---
layout: default
title: "VNU-HUS MAT3500: Toán rời rạc"
last_modified_at: 2025-11-26
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">
Đây là trang web hỗ trợ cho môn "Toán rời rạc (VNU-HUS MAT3500 3)" tôi tham gia giảng dạy ở Đại học KHTN, ĐHQG Hà Nội trong Học kỳ 1 năm học 2025-2026.

* TOC
{:toc}
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thử nghiệm AI hỗ trợ học tập</h1>
Từ ngày 22/09/2025, tôi sẽ thử nghiệm sử dụng AI (Google Gemini) để hỗ trợ học tập trong môn học này. Sinh viên có thể đặt câu hỏi về nội dung bài giảng, bài tập, các khái niệm liên quan đến môn học, v.v. qua [https://gemini.google.com/gem/16115a96defa](https://gemini.google.com/gem/16115a96defa). 

Sinh viên có thể sử dụng bằng cách đăng nhập tài khoản Google. Nếu dùng tài khoản của HUS thì sẽ được sử dụng Gemini 2.5 Pro, phiên bản được cho là tập trung nhiều hơn vào lý luận logic, toán học, và code. Nếu dùng tài khoản Google thông thường thì cũng có thể dùng bản này nhưng sẽ bị giới hạn số lần prompt. 

Mọi góp ý về việc sử dụng AI trong học tập, cũng như các vấn đề phát sinh trong quá trình sử dụng, xin vui lòng gửi email cho tôi.
</div>

<div class="alert alert-primary" role="alert" markdown="1">
Sinh viên muốn nghỉ học cần thông báo qua form [https://forms.office.com/r/LtZRGLGUFN](https://forms.office.com/r/LtZRGLGUFN) **trước khi buổi học bắt đầu**. Các hình thức thông báo khác (email, tin nhắn, nhờ người khác xin nghỉ, ...) **không được chấp nhận**.
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thông báo</h1>

<!-- <h2 style="color:red;">Kiểm tra giữa kỳ: 29/10/2025 (Thứ 4), 07:00 -- 07:50 (Tiết 1), Phòng 105-T5</h2> -->
<h2 style="color:red;">Thi vấn đáp cuối kỳ: 8:00 -- 12:30, ngày 10/01/2026, Phòng 102-T5</h2>

* **26/11/2025:**
  * Cập nhật nội dung môn học
    * Lý thuyết đồ thị II: Đường đi ngắn nhất, Đồ thị phẳng, Tô màu đồ thị
    * Thông tin thi cuối kỳ (vấn đáp)
* **19/11/2025:**
  * Cập nhật nội dung môn học
    * Lý thuyết đồ thị I: Giới thiệu, Biểu diễn đồ thị và sự đẳng cấu, Tính liên thông
* **02/11/2025:**
  * Cập nhật nội dung môn học
    * Các phương pháp đếm

Xem các thông báo cũ [ở đây](#lịch-sử-các-thông-báo).

</div>

# Các thông tin cơ bản
 
* **Trường:** Đại học KHTN, ĐHQG Hà Nội
* **Mã học phần:** MAT3500
* **Mã lớp học phần:** MAT3500 3
* **Số tín chỉ:** 4
* **Thời gian:** Học kỳ 1 năm học 2024-2026
  * **Lý thuyết:** 
    * Thứ 5, 13:00 -- 15:40 (Tiết 7--9), Phòng 105-T5
  * **Bài tập:** 
    * Thứ 4, 07:00 -- 08:45 (Tiết 1--2), Phòng 105-T5
* **Giảng viên:** 
  * **Lý thuyết:** Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội, `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`))
  * **Bài tập:** Lê Quang Hàm (Viện Khoa học giáo dục Việt Nam, `hamlq2022[at]gmail.com` (thay `[at]` bằng `@`))
* **Nội dung:** Cung cấp các kiến thức toán học cơ sở cho ngành công nghệ thông tin bao gồm các cấu trúc toán học rời rạc và các nguyên lí toán học áp dụng cho các cấu trúc này (cơ sở của lô gíc toán học, lí thuyết tập hợp, hàm và quan hệ, lí thuyết số, lí thuyết đếm, lí thuyết đồ thị, phép tính xác suất, đại số Boole và mạch tổ hợp, ôtô mát, ngôn ngữ hình thức và khả năng tính toán) 
* **Trang web hỗ trợ:** [{{ site.website_full }}{{ page.url }}]({{ page.url }})
* **Canvas:** [JF8GAK](https://canvas.instructure.com/enroll/JF8GAK)
  * **Chú ý:** Sinh viên điền thông tin ở [https://forms.office.com/r/AvRmSZT9vS](https://forms.office.com/r/AvRmSZT9vS) để được mời tham gia lớp trên Canvas.
  * **Chú ý:** Sinh viên cần để tên hiển thị là **họ và tên đầy đủ bằng tiếng Việt có dấu**, ví dụ như "Nguyễn Văn Tuấn". Đồng thời, sinh viên cần thiết lập múi giờ (Timezone) trong Canvas là **Hanoi** (GMT+7). Xem [cách đổi tên hiển thị](https://community.canvaslms.com/t5/Troubleshooting/Updating-my-displayed-name-in-Canvas/ta-p/853) và [cách thay đổi múi giờ](https://community.canvaslms.com/t5/Canvas-Basics-Guide/How-do-I-set-a-time-zone-in-my-user-account/ta-p/615318).
* **Kiểm tra, đánh giá:**
  * **Phần tự học, tự nghiên cứu, bài tập:** 20%
  * **Thi giữa kỳ:** 20%
  * **Thi cuối kỳ:** 60%

# Giáo trình, tài liệu tham khảo

* **Học liệu bắt buộc:**
  * Kenneth H. Rosen (2018), *Discrete Mathematics and Its applications*, 8th edition, McGraw-Hill <span style="color:red">[Tài liệu giảng dạy chính]</span>  
    * Trang web hỗ trợ của McGraw-Hill: [8th edition](https://highered.mheducation.com/sites/125967651x/information_center_view0/), [7th edition](https://highered.mheducation.com/sites/0073383090)
    * Google Drive: [bản tiếng Anh](https://drive.google.com/file/d/1ih0TbsAnGfU01spxlxdrxmhy2Fx1usxR/view?usp=sharing), [bản dịch tiếng Việt phiên bản cũ](https://drive.google.com/file/d/17BZhae7BeGvK1rI8ksjA8o4uZyLr-I_4/) (cần tài khoản với email đuôi `@hus.edu.vn`)
    * VNU-LIC: [bản tiếng Anh](https://bookworm.vnu.edu.vn/EDetail.aspx?id=96731), [bản dịch tiếng Việt phiên bản cũ](https://bookworm.vnu.edu.vn/EDetail.aspx?id=35151), [Student's solutions guide](https://bookworm.vnu.edu.vn/EDetail.aspx?id=49071) (cần tài khoản VNU)
  * Tom Jenkyns, Ben Stephenson (2018), *Fundamentals of Discrete Math for Computer Science: A Problem-Solving Primer*, 2nd edition, Springer-Verlag London, [doi:10.1007/978-3-319-70151-6](https://doi.org/10.1007/978-3-319-70151-6)
* **Học liệu tham khảo thêm:**
  * Nguyễn Hữu Điển (2019), *Toán rời rạc và ứng dụng*, NXB Đại học Quốc gia Hà Nội
    * [Google Drive](https://drive.google.com/file/d/1Nd7FPnn1y-h8WNio4ALidmHVpGZxbiPM/)
  * Vũ Đình Hòa (2010), *Toán rời rạc*, NXB Đại học Sư Phạm Hà Nội
    * [Bài giảng Toán rời rạc](http://fit.hnue.edu.vn/~hoavd/Bai%20giang/TRR.rar) của cùng tác giả
  * Oscar Levin (2021), *Discrete Mathematics: An Open Introduction*, 3rd edition, [https://discrete.openmathbooks.org/](https://discrete.openmathbooks.org/)
  * Thomas VanDrunen (2013), *Discrete Mathematics and Functional Programming*, Franklin, Beedle and Associates, [https://cs.wheaton.edu/~tvandrun/dmfp/](https://cs.wheaton.edu/~tvandrun/dmfp/)
  * Harry Lewis and Rachel Zax (2019), *Essential Discrete Mathematics for Computer Science*, Princeton University Press
  * Mordechai Ben-Ari (2012), *Mathematical Logic for Computer Science*, 3rd edition, Springer, London, [doi:10.1007/978-1-4471-4129-7](https://doi.org/10.1007/978-1-4471-4129-7)
* **Một số tài liệu khác**
  * [How to Solve It: A New Aspect of Mathematical Method](https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it), by George Pólya
    * [Google Drive](https://drive.google.com/file/d/1_4eB52t3KopsqN7Lsyc4eKDFSznKj2dJ/) (cần tài khoản với email đuôi `@hus.edu.vn`)
    * [Bản dịch tiếng Việt](https://drive.google.com/file/d/1MMJ6aNDv6i4eC0uGh07CBfxtEb9GlAYa/) (cần tài khoản với email đuôi `@hus.edu.vn`)
  * [Math Study Tips](https://www.math.uvic.ca/faculty/gmacgill/Pointers2.pdf), by Gary MacGillivray
  * [Lời khuyên cho các sinh viên trong lớp Math 412]({{ site.baseurl }}/translation/Advice_DBWest_MAT412.pdf), by Douglas B. West (Bản dịch tiếng Việt thực hiện bởi Hoàng Anh Đức)
    * **2024-05-27:** Xem [bản dịch khác]({{ site.baseurl }}/translation/Advice_DBWest_MAT412_NguyenTrongDuc_K68A5_VNU-HUS.pdf) của Nguyễn Trọng Đức, lớp K68A5 (KHDL), Đại học Khoa học Tự nhiên, ĐHQG Hà Nội.

# Tài liệu từ các năm trước

* **Học kỳ hè, năm học 2024-2025:** [MAT3500](https://hoanganhduc.github.io/teaching/VNU-HUS/2025/summer/MAT3500/)
* **Học kỳ 2, năm học 2024-2025:** [MAT3500](https://hoanganhduc.github.io/teaching/VNU-HUS/2025/spring/MAT3500/)
* **Học kỳ 1, năm học 2024-2025:** [MAT3500 2](https://hoanganhduc.github.io/teaching/VNU-HUS/2024/winter/MAT3500-2/)
* **Học kỳ hè, năm học 2023-2024:** [MAT3500 1](https://hoanganhduc.github.io/teaching/VNU-HUS/2024/summer/MAT3500/)
* **Học kỳ 2, năm học 2023-2024:** [MAT3500 1](https://hoanganhduc.github.io/teaching/VNU-HUS/2024/MAT3500-1/), [MAT3500 2](https://hoanganhduc.github.io/teaching/VNU-HUS/2024/MAT3500-2/)
* **Học kỳ 2, năm học 2022-2023:** [MAT3500 2](https://hoanganhduc.github.io/teaching/VNU-HUS/2023/MAT3500-2), [MAT3500 3](https://hoanganhduc.github.io/teaching/VNU-HUS/2023/MAT3500-3)

# Nội dung

## Bài giảng và bài tập

* **Chú ý:** Một phần các bài giảng dựa trên các slides của [Jan Stelovsky](http://www2.hawaii.edu/~janst/) cho môn [ICS141: Discrete Mathematics for Computer Science I](http://www2.hawaii.edu/~janst/141/lecture) ở Đại học Hawaii mùa thu năm 2011.

| **Chủ đề** | **Tài liệu** | **Ghi chú** |
|:--------------|:-----------|:--------------|
| Giới thiệu | [slides]({{ page.url | append: "intro.pdf" }}) |
| Lôgic và Chứng minh | [slides]({{ page.url | append: "Logic_and_Proofs.pdf" }}) | Chương 1, 1.1--1.5, 1.7 (Rosen) |
| Các cấu trúc cơ bản: Tập hợp, Hàm, Dãy, Tổng/Tích |  [slides]({{ page.url | append: "Basic_Structures.pdf" }}) | Chương 2, 2.1--2.5 (Rosen) |
| Quy nạp và Đệ quy | [slides]({{ page.url | append: "Induction_and_Recursion.pdf" }}) | Chương 5, 5.1--5.3, Chương 8, 8.1--8.4 (Rosen) |
| Thuật toán I: Mô tả, chứng minh, đánh giá thuật toán; Tìm kiếm và sắp xếp | [slides]({{ page.url | append: "Algorithms_I.pdf" }}) | Chương 3, 3.1--3.3, Chương 5, 5.5 (Rosen) |
| Thuật toán II: Thuật toán đệ quy, thuật toán tham lam | [slides]({{ page.url | append: "Algorithms_II.pdf" }}) | Chương 5, 5.4 (Rosen) |
| Lý thuyết số cơ bản | [slides]({{ page.url | append: "Basic_Number_Theory.pdf" }}) | Chương 4, 4.1--4.4 (Rosen) | 
| Các phương pháp đếm | [slides]({{ page.url | append: "Counting.pdf" }}) | Chương 6, 6.1--6.5 (Rosen) |
| Lý thuyết đồ thị I: Giới thiệu, Biểu diễn đồ thị và sự đẳng cấu, Tính liên thông | [slides]({{ page.url | append: "Graphs_I.pdf" }}) | Chương 10, 10.1--10.4 (Rosen) |
| Lý thuyết đồ thị II: Đường đi ngắn nhất, Đồ thị phẳng, Tô màu đồ thị | [slides]({{ page.url | append: "Graphs_II.pdf" }}) | Chương 10, 10.5--10.8 (Rosen) |

<!-- | Lý thuyết đồ thị III: Cây | [slides]({{ page.url | append: "Graphs_III.pdf" }}) | Chương 11, 11.1--11.5 (Rosen) | -->
<!-- | Đại số Boole | [slides]({{ page.url | append: "Boolean_Algebra.pdf" }}) | Chương 12, 12.1--12.4 (Rosen) | -->

<!-- | Tổng hợp | [slides]({{ page.url | append: "VNU-HUS_MAT3500_Lectures.pdf" }}), [bài tập]({{ page.url | append: "VNU-HUS_MAT3500_Exercises.pdf" }}) | | -->

## Kiểm tra, đánh giá

<!-- * **Kiểm tra giữa kỳ:** [thông tin cần biết]({{ page.url | append: "midterm.pdf" }}), [đề + đáp án]({{ page.url | append: "Midtermsol.pdf" }}) -->
* **Kiểm tra cuối kỳ:** [thông tin cần biết]({{ page.url | append: "final.pdf" }})

-----

# Lịch sử các thông báo

* **19/10/2025:**
  * Cập nhật nội dung môn học
    * Lý thuyết số cơ bản
* **16/10/2025:**
  * Cập nhật nội dung môn học
    * Thuật toán II: Thuật toán đệ quy, thuật toán tham lam
* **08/10/2025**:
  * Cập nhật nội dung môn học
    * Thuật toán I: Mô tả, chứng minh, đánh giá thuật toán; Tìm kiếm và sắp xếp
* **01/10/2025:**
  * Sinh viên được nghỉ buổi học ngày 01/10/2025 do ảnh hưởng của bão số 10 (Bualoi).
* **22/09/2025:**
  * Thử nghiệm dùng AI (Google Gemini) để hỗ trợ học tập
  * Cập nhật nội dung môn học
    * Quy nạp và Đệ quy
* **17/09/2025:**
  * Cập nhật nội dung môn học
    * Các cấu trúc cơ bản: Tập hợp, Hàm, Dãy, Tổng/Tích
* **28/08/2025:**
  * Khởi tạo trang web.
  * Sinh viên đăng ký lớp MAT3500 3 điền thông tin vào form [https://forms.office.com/r/AvRmSZT9vS](https://forms.office.com/r/AvRmSZT9vS) **trước 23:59 ngày 18/09/2025** để được mời vào lớp trên Canvas. 
  * Cập nhật nội dung môn học
    * Lôgic và Chứng minh