---
layout: default
title: "VNU-HUS MAT3500: Toán rời rạc"
last_modified_at: 2024-09-09
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">
Đây là trang web hỗ trợ cho môn "Toán rời rạc (VNU-HUS MAT3500 2)" tôi tham gia giảng dạy ở Đại học KHTN, ĐHQG Hà Nội trong Học kỳ 1 năm học 2024-2025.

* TOC
{:toc}
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thông báo</h1>

<!-- <h2 style="color:red;">Kiểm tra cuối kỳ: 19/06/2024 (Thứ 4), 08:30 – 10:30</h2>  -->

<!-- <h2 style="color:red;">Ngày 08/05/2024 (Thứ 4), lớp Toán rời rạc học ở giảng đường 514-T4 (từ 13:00 - 15:50) thay vì 506-T3 như bình thường</h2> -->

<!-- <h2 style="color:red;">Ngày 10/4/2024 (Thứ 4), lớp Toán rời rạc học ở giảng đường 103-T5 (từ 13:00 - 15:50) thay vì 506-T3 như bình thường</h2> -->

<!--
<h2 style="color:red;">Do GV đi công tác, các lớp Toán rời rạc trong tuần từ 26/2/2024 - 1/3/2024 được nghỉ</h2>

<h2 style="color:red;">Kiểm tra giữa kỳ: 28/03/2024 (Thứ 5), 10:00 – 10:50 (Tiết 4), Phòng 513-T5</h2>
-->

* **4/9/2024:**
  * Khởi tạo trang web
  * <span style="color:red; font-weight: bold;">[Chú ý]</span> Các bạn đăng ký học môn này điền các thông tin cần thiết vào form [https://forms.office.com/r/AvRmSZT9vS](https://forms.office.com/r/AvRmSZT9vS)
  * Cập nhật nội dung môn học
    * Giới thiệu
    * Lôgic và Chứng minh

Xem các thông báo cũ [ở đây](#lịch-sử-các-thông-báo).

</div>

# Các thông tin cơ bản
 
* **Trường:** Đại học KHTN, ĐHQG Hà Nội
* **Mã học phần:** MAT3500
* **Mã lớp học phần:** MAT3500 2 (KHMT&TT)
* **Số tín chỉ:** 4
* **Thời gian:** Học kỳ 1 năm học 2024-2025
  * **Lý thuyết:** Thứ 5, 09:00 – 11:50 (Tiết 3-5), Phòng 107-T5
  * **Bài tập:** Thứ 3, 16:00 – 17:50 (Tiết 9–10), Phòng 105-T5
* **Giảng viên (Lý thuyết + Bài tập):** Hoàng Anh Đức (Đại học KHTN, ĐHQG Hà Nội, `hoanganhduc[at]hus.edu.vn` (thay `[at]` bằng `@`))
* **Nội dung:** Cung cấp các kiến thức toán học cơ sở cho ngành công nghệ thông tin bao gồm các cấu trúc toán học rời rạc và các nguyên lí toán học áp dụng cho các cấu trúc này (cơ sở của lô gíc toán học, lí thuyết tập hợp, hàm và quan hệ, lí thuyết số, lí thuyết đếm, lí thuyết đồ thị, phép tính xác suất, đại số Bool và mạch tổ hợp, ôtô mát, ngôn ngữ hình thức và khả năng tính toán) 
* **Trang web hỗ trợ:** [{{ site.website_full }}{{ page.url }}]({{ page.url }})
* **Canvas:** [BJYRBH](https://canvas.instructure.com/enroll/BJYRBH)
* **Kiểm tra, đánh giá:**
  * **Phần tự học, tự nghiên cứu, bài tập:** 20%
  * **Thi giữa kỳ:** 20%
  * **Thi cuối kỳ:** 60%

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
    * **2024-05-27:** Xem [bản dịch khác]({{ site.baseurl }}/translation/Advice_DBWest_MAT412_NguyenTrongDuc_K68A5_VNU-HUS.pdf) của Nguyễn Trọng Đức, lớp K68A5 (KHDL), Đại học Khoa học Tự nhiên, ĐHQG Hà Nội.

# Tài liệu từ các năm trước

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

<!-- | Các cấu trúc cơ bản: Tập hợp, Hàm, Dãy, Tổng |  [slides]({{ page.url | | append: "Basic_Structures.pdf" }}), [bài tập]({{ page.url | append: "Basic_Structures.pdf" }}) | Chương 2, 2.1--2.5 (Rosen) | -->
<!-- | Quy nạp và Đệ quy | [slides]({{ page.url | | append: "Induction_and_Recursion.pdf" }}), [bài tập]({{ page.url | append: "Induction_and_Recursion.pdf" }}) | Chương 5, 5.1–5.3 (Rosen) | -->
<!-- | Thuật toán I: Giới thiệu, một số thuật toán tìm kiếm và sắp xếp, độ tăng của hàm | [slides]({{ page.url | | append: "Algorithms_I.pdf" }}), [bài tập]({{ page.url | append: "Algorithms_I.pdf" }}) | Chương 3, 3.1--3.2 (Rosen) | -->
<!-- | Thuật toán II: Độ phức tạp tính toán, thuật toán tham lam, thuật toán đệ quy | [slides]({{ page.url | | append: "Algorithms_II.pdf" }}), [bài tập]({{ page.url | append: "Algorithms_II.pdf" }}) | Chương 3, 3.1, 3.3, Chương 5, 5.4, Chương 8, 8.1--8.4 (Rosen) | -->
<!-- | Lý thuyết số cơ bản | [slides]({{ page.url | | append: "Basic_Number_Theory.pdf" }}), [bài tập]({{ page.url | append: "Basic_Number_Theory.pdf" }}) | Chương 4, 4.1--4.4 (Rosen) |  -->
<!-- | Các phương pháp đếm | [slides]({{ page.url | | append: "Counting.pdf" }}), [bài tập]({{ page.url | append: "Counting.pdf" }}) | Chương 6, 6.1--6.5 (Rosen) | -->
<!-- | Lý thuyết đồ thị I: Giới thiệu, Biểu diễn đồ thị và sự đẳng cấu, Tính liên thông | [slides]({{ page.url | | append: "Graphs_I.pdf" }}), [bài tập]({{ page.url | append: "Graphs_I.pdf" }}) | Chương 10, 10.1--10.4 (Rosen) | -->
<!-- | Lý thuyết đồ thị II: Đường đi ngắn nhất, Đồ thị phẳng, Tô màu đồ thị | [slides]({{ page.url | | append: "Graphs_II.pdf" }}), [bài tập]({{ page.url | append: "Graphs_II.pdf" }}) | Chương 10, 10.5--10.8 (Rosen) | -->
<!-- | Lý thuyết đồ thị III: Cây | [slides]({{ page.url | | append: "Graphs_III.pdf" }}), [bài tập]({{ page.url | append: "Graphs_III.pdf" }}) | Chương 11, 11.1--11.5 (Rosen) | -->
<!-- | Đại số Boole | [slides]({{ page.url | | append: "Boolean_Algebra.pdf" }}), [bài tập]({{ page.url | append: "Boolean_Algebra.pdf" }}) | Chương 12, 12.1--12.4 (Rosen) | -->
<!-- | Tổng hợp | [slides]({{ page.url | | append: "VNU-HUS_MAT3500_Lectures.pdf" }}), [bài tập]({{ page.url | append: "VNU-HUS_MAT3500_Exercises.pdf" }}) | | -->

## Kiểm tra, đánh giá

-----

# Lịch sử các thông báo



