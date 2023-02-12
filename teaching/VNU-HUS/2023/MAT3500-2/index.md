---
layout: default
title: "VNU-HUS MAT3500 2: Toán rời rạc"
last_modified_at: 2023-02-12
lang: "vi"
---

<div class="alert alert-info" markdown="1">
Đây là trang web hỗ trợ cho môn "Toán rời rạc (VNU-HUS MAT3500 2)" tôi tham gia giảng dạy ở Đại học KHTN, ĐHQG Hà Nội trong Học kỳ 2 năm học 2022-2023.

* TOC
{:toc}
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thông báo</h1>

Xem các thông báo cũ [ở đây](#lịch-sử-các-thông-báo).

* **12/02/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung)) 
    * Các cấu trúc cơ bản I: Tập hợp và Hàm
* **06/02/2023:** 
  * Sửa lỗi trong slides và handout "Giới thiệu": 27/03/2022 => 27/03/2023
* **05/02/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung)) 
    * Lôgic và Chứng minh
* **02/02/2023:**
  * Khởi tạo trang web
  * <span style="color:red;font-weight:bold;">[Chú ý]</span> Các bạn đăng ký học môn này điền các thông tin cần thiết vào Google Form [https://forms.gle/KqSgw1kzC8rSVNL77](https://forms.gle/KqSgw1kzC8rSVNL77).
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Giới thiệu 

</div>

# Các thông tin cơ bản
 
* **Trường:** Đại học KHTN, ĐHQG Hà Nội
* **Mã học phần:** MAT3500
* **Mã lớp học phần:** MAT3500 2 (KHMT&TT)
* **Số tín chỉ:** 4
* **Thời gian:** Học kỳ 2 năm học 2022-2023
  * **Lý thuyết:** Thứ 2, 09:00 -- 11:50, Phòng 204-T4
  * **Bài tập:** Thứ 4, 07:00 -- 08:50, Phòng 204-T4
* **Giảng viên (Lý thuyết + Bài tập):** Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội, `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`))
* **Nội dung:** Cung cấp các kiến thức toán học cơ sở cho ngành công nghệ thông tin bao gồm các cấu trúc toán học rời rạc và các nguyên lí toán học áp dụng cho các cấu trúc này (cơ sở của lô gíc toán học, lí thuyết tập hợp, hàm và quan hệ, lí thuyết số, lí thuyết đếm, lí thuyết đồ thị, phép tính xác suất, đại số Bool và mạch tổ hợp, ôtô mát, ngôn ngữ hình thức và khả năng tính toán) 
* **Trang web hỗ trợ:** [{{ site.website_full }}{{ page.url }}]({{ page.url }})
* **Google Classroom:** [a3rzf6o](https://classroom.google.com/c/NTEyODU5OTQ2MTAx?cjc=a3rzf6o)
* **Kiểm tra, đánh giá:**
  * **Phần tự học, tự nghiên cứu, bài tập:** 10%
  * **Thi giữa kỳ:** 20%
  * **Thi cuối kỳ:** 70%

# Giáo trình, tài liệu tham khảo

* **Học liệu bắt buộc:**
  * K. H. Rosen (2012), *Discrete Mathematics and Its applications*, 7th edition, Mc Graw-Hill, [https://highered.mheducation.com/sites/0073383090](https://highered.mheducation.com/sites/0073383090) <span style="color:red">[Tài liệu giảng dạy chính]</span>   
    * Google Drive: [bản tiếng Anh](https://drive.google.com/file/d/1dLiPbOBBs9zomPlOWCdXliIY6VFA8TaI/), [bản dịch tiếng Việt phiên bản cũ](https://drive.google.com/file/d/1T4JTb_6YMbfbmAELTGLbHqpdrTf4aG2X/) (cần tài khoản với email đuôi `@hus.edu.vn`)
  * Tom Jenkyns, Ben Stephenson (2018), *Fundamentals of Discrete Math for Computer Science: A Problem-Solving Primer*, 2nd edition, Springer-Verlag London, [doi:10.1007/978-3-319-70151-6](https://doi.org/10.1007/978-3-319-70151-6)
* **Học liệu tham khảo thêm:**
  * Vũ Đình Hòa (2010), *Toán rời rạc*, NXB Đại học Sư Phạm Hà Nội
    * [Bài giảng Toán rời rạc](http://fit.hnue.edu.vn/~hoavd/Bai%20giang/TRR.rar) của cùng tác giả
  * Oscar Levin (2021), *Discrete Mathematics: An Open Introduction*, 3rd edition, [https://discrete.openmathbooks.org/](https://discrete.openmathbooks.org/)
  * Thomas VanDrunen (2013), *Discrete Mathematics and Functional Programming*, Franklin, Beedle and Associates, [https://cs.wheaton.edu/~tvandrun/dmfp/](https://cs.wheaton.edu/~tvandrun/dmfp/)
  * Harry Lewis and Rachel Zax (2019), *Essential Discrete Mathematics for Computer Science*, Princeton University Press
  * Mordechai Ben-Ari (2012), *Mathematical Logic for Computer Science*, 3rd edition, Springer, London, [doi:10.1007/978-1-4471-4129-7](https://doi.org/10.1007/978-1-4471-4129-7)

# Nội dung

| **Chủ đề** | **Tài liệu** | **Ghi chú** |
|:--------------|:-----------|:--------------|
| Giới thiệu | [slides]({{ page.url | append: "intro.pdf" }}), [handout]({{ page.url | append: "handout.pdf" }}) |
| Lôgic và Chứng minh | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Logic_and_Proofs.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Logic_and_Proofs.pdf" }}) | Chương 1, 1.1--1.5, 1.7 (Rosen) |
| Các cấu trúc cơ bản I: Tập hợp, Hàm | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Basic_Structures_I.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Basic_Structures_I.pdf" }}) | Chương 2, 2.1--2.3, 2.5 (Rosen) |
| Các cấu trúc cơ bản II: Dãy, Tổng | slides, bài tập | Chương 2, 2.4 (Rosen) | 

# Lịch sử các thông báo
