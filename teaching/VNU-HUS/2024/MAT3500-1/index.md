---
layout: default
title: "VNU-HUS MAT3500: Toán rời rạc"
last_modified_at: 2024-01-23
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">
Đây là trang web hỗ trợ cho môn "Toán rời rạc (VNU-HUS MAT3500)" tôi tham gia giảng dạy ở Đại học KHTN, ĐHQG Hà Nội trong Học kỳ 2 năm học 2023-2024.

* TOC
{:toc}
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thông báo</h1>

* **20/1/2024:**
  * Khởi tạo trang web
  * <span style="color:red; font-weight: bold;">[Chú ý]</span> Các bạn đăng ký học môn này điền các thông tin cần thiết vào Google Form [https://forms.gle/MDyS9xvaD4QuNCip9](https://forms.gle/MDyS9xvaD4QuNCip9)
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Giới thiệu
    * Lôgic và Chứng minh

<!--
<h2 style="color:red;">Kiểm tra cuối kỳ: 29/05/2023 (Thứ 2), 08:30 – </h2>
<h2 style="color:red;">Kiểm tra giữa kỳ: 27/03/2023 (Thứ 2), 09:00 – 09:50 (Tiết 3), Phòng 204-T4</h2>
-->

Xem các thông báo cũ [ở đây](#lịch-sử-các-thông-báo).

</div>

# Các thông tin cơ bản
 
* **Trường:** Đại học KHTN, ĐHQG Hà Nội
* **Mã học phần:** MAT3500
* **Mã lớp học phần:** MAT3500 (KHDL)
* **Số tín chỉ:** 4
* **Thời gian:** Học kỳ 2 năm học 2023-2024
  * **Lý thuyết:** Thứ 4, 07:00 – 08:50 (Tiết 1–3), Phòng 203-T5
  * **Bài tập:** Thứ 5, 16:00 – 17:50 (Tiết 9–10), Phòng 206-T5 
* **Giảng viên (Lý thuyết + Bài tập):** Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội, `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`))
* **Nội dung:** Cung cấp các kiến thức toán học cơ sở cho ngành công nghệ thông tin bao gồm các cấu trúc toán học rời rạc và các nguyên lí toán học áp dụng cho các cấu trúc này (cơ sở của lô gíc toán học, lí thuyết tập hợp, hàm và quan hệ, lí thuyết số, lí thuyết đếm, lí thuyết đồ thị, phép tính xác suất, đại số Bool và mạch tổ hợp, ôtô mát, ngôn ngữ hình thức và khả năng tính toán) 
* **Trang web hỗ trợ:** [{{ site.website_full }}{{ page.url }}]({{ page.url }})
* **Google Classroom:** [7gnoxt2](https://classroom.google.com/c/NjM5NDQ0OTg4OTcx?cjc=7gnoxt2)
* **Kiểm tra, đánh giá:**
  * **Phần tự học, tự nghiên cứu, bài tập:** 10%
  * **Thi giữa kỳ:** 20%
  * **Thi cuối kỳ:** 70%

# Giáo trình, tài liệu tham khảo

* **Học liệu bắt buộc:**
  * K. H. Rosen (2012), *Discrete Mathematics and Its applications*, 7th edition, Mc Graw-Hill, [https://highered.mheducation.com/sites/0073383090](https://highered.mheducation.com/sites/0073383090) <span style="color:red">[Tài liệu giảng dạy chính]</span>   
    * Google Drive: [bản tiếng Anh](https://drive.google.com/file/d/1TB1rK5zyccrFBsg43AfVdaDF27Qw3-Dv/), [bản dịch tiếng Việt phiên bản cũ](https://drive.google.com/file/d/17BZhae7BeGvK1rI8ksjA8o4uZyLr-I_4/) (cần tài khoản với email đuôi `@hus.edu.vn`)
    * VNU-LIC: [bản tiếng Anh 8th edition](https://bookworm.vnu.edu.vn/EDetail.aspx?id=96731), [bản dịch tiếng Việt phiên bản cũ](https://bookworm.vnu.edu.vn/EDetail.aspx?id=35151), [Student's solutions guide](https://bookworm.vnu.edu.vn/EDetail.aspx?id=49071) (cần tài khoản VNU)
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
  * [Math Study Tips](https://www.math.uvic.ca/faculty/gmacgill/Pointers2.pdf), by Gary MacGillivray
  * [Lời khuyên cho các sinh viên trong lớp Math 412]({{ site.baseurl }}/translation/Advice_DBWest_MAT412.pdf), by Douglas B. West (Bản dịch tiếng Việt thực hiện bởi Hoàng Anh Đức)

# Tài liệu từ các năm trước

* **Học kỳ 2, năm học 2022-2023:** [MAT3500 2](https://hoanganhduc.github.io/teaching/VNU-HUS/2023/MAT3500-2), [MAT3500 3](https://hoanganhduc.github.io/teaching/VNU-HUS/2023/MAT3500-3)

# Nội dung

## Bài giảng và bài tập

* **Chú ý:** Một phần các bài giảng dựa trên các slides của [Jan Stelovsky](http://www2.hawaii.edu/~janst/) cho môn [ICS141: Discrete Mathematics for Computer Science I](http://www2.hawaii.edu/~janst/141/lecture) ở Đại học Hawaii mùa thu năm 2011.

| **Chủ đề** | **Tài liệu** | **Ghi chú** |
|:--------------|:-----------|:--------------|
| Giới thiệu | [slides]({{ page.url | append: "intro.pdf" }}) |
| Lôgic và Chứng minh | [slides]({{ page.url | remove: "-1" | append: "Lectures/" | append: "Logic_and_Proofs.pdf" }}), [bài tập]({{ page.url | remove: "-1" | append: "Exercises/" | append: "Logic_and_Proofs.pdf" }}) | Chương 1, 1.1--1.5, 1.7 (Rosen) |

## Kiểm tra, đánh giá

## Lời giải các bài tập

-----

# Lịch sử các thông báo


