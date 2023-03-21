---
layout: default
title: "VNU-HUS MAT3500 2: Toán rời rạc"
last_modified_at: 2023-03-21
lang: "vi"
katex: true
---

<div class="alert alert-info" markdown="1">
Đây là trang web hỗ trợ cho môn "Toán rời rạc (VNU-HUS MAT3500 2)" tôi tham gia giảng dạy ở Đại học KHTN, ĐHQG Hà Nội trong Học kỳ 2 năm học 2022-2023.

* TOC
{:toc}
</div>

<div class="alert alert-success" role="alert" markdown="1">
<h1>Thông báo</h1>

<h2 style="color:red;">Kiểm tra giữa kỳ: 27/03/2023 (Thứ 2), 09:00 – 09:50 (Tiết 3), Phòng 204-T4</h2>

Xem các thông báo cũ [ở đây](#lịch-sử-các-thông-báo).
* **21/03/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Lời giải các bài tập trong slides "Thuật toán II" của bạn Phạm Hữu Vang
* **20/03/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Lý thuyết số cơ bản I
    * Bài tập Thuật toán II
* **16/03/2023:**
  * Sửa lỗi sai trong định nghĩa $\Omega$-lớn ở slides "Thuật toán I" và "Thuật toán II": hằng số $C$ phải dương ($f$ là $\Omega(g)$ nếu tồn tại các hằng số $C > 0$ và $k$ sao cho $\vert f(x)\vert \geq C\vert g(x)\vert$ với mọi $x > k$).
* **14/03/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Nội dung ôn tập cho kiểm tra giữa kỳ
* **12/03/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Thuật toán II: Độ phức tạp tính toán, thuật toán tham lam, thuật toán đệ quy
* **06/03/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Thuật toán I: Giới thiệu, một số thuật toán tìm kiếm và sắp xếp, độ tăng của hàm 

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
    * Google Drive: [bản tiếng Anh](https://drive.google.com/file/d/1TB1rK5zyccrFBsg43AfVdaDF27Qw3-Dv/), [bản dịch tiếng Việt phiên bản cũ](https://drive.google.com/file/d/17BZhae7BeGvK1rI8ksjA8o4uZyLr-I_4/) (cần tài khoản với email đuôi `@hus.edu.vn`)
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

# Nội dung

## Bài giảng và bài tập

| **Chủ đề** | **Tài liệu** | **Ghi chú** |
|:--------------|:-----------|:--------------|
| Giới thiệu | [slides]({{ page.url | append: "intro.pdf" }}), [handout]({{ page.url | append: "handout.pdf" }}) |
| Lôgic và Chứng minh | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Logic_and_Proofs.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Logic_and_Proofs.pdf" }}) | Chương 1, 1.1--1.5, 1.7 (Rosen) |
| Các cấu trúc cơ bản I: Tập hợp, Hàm | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Basic_Structures_I.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Basic_Structures_I.pdf" }}) | Chương 2, 2.1--2.3, 2.5 (Rosen) |
| Các cấu trúc cơ bản II: Dãy, Tổng | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Basic_Structures_II.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Basic_Structures_II.pdf" }}) | Chương 2, 2.4 (Rosen) |
| Quy nạp và Đệ quy | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Induction_and_Recursion.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Induction_and_Recursion.pdf" }}) | Chương 5, 5.1--5.3 (Rosen) |
| Thuật toán I: Giới thiệu, một số thuật toán tìm kiếm và sắp xếp, độ tăng của hàm | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Algorithms_I.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Algorithms_I.pdf" }}) | Chương 3, 3.1--3.2 (Rosen) |
| Thuật toán II: Độ phức tạp tính toán, thuật toán tham lam, thuật toán đệ quy | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Algorithms_II.pdf" }}), [bài tập]({{ page.url | remove: "-2" | append: "Exercises/" | append: "Algorithms_II.pdf" }}) | Chương 3, 3.1, 3.3, Chương 5, 5.4, Chương 8, 8.1--8.4 (Rosen) |
| Lý thuyết số cơ bản I | [slides]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Basic_Number_Theory_I.pdf" }}) | Chương 4.1--4.3 (Rosen) |

## Kiểm tra, đánh giá

* Kiểm tra thường xuyên 1: [đề bài]({{ page.url | append: "RegularTest1.pdf" }}), [gợi ý giải]({{ page.url | append: "RegularTest1sol.pdf" }}), [nhận xét]({{ page.url | append: "RegularTest1com.pdf" }})
* Kiểm tra giữa kỳ: [nội dung ôn tập]({{ page.url | remove: "-2" | append: "Midterm_Review.pdf" }})

## Lời giải bài tập

| **Thời gian** | **Bài tập** | **Lời giải** | **Tác giả** |
|:--------------|:--------------|:-----------|:--------------|
| 21/03/2023 | [slides "Thuật toán II"]({{ page.url | remove: "-2" | append: "Lectures/" | append: "Algorithms_II.pdf" }}) | [PDF]({{ page.url | append: "solutions/" | append: "PHVang_Algorithms-II-slides_20230321.pdf" }}) | [Phạm Hữu Vang](mailto:phamhuuvang_t67@hus.edu.vn) |  

-----

# Lịch sử các thông báo

* **01/03/2023:**
  * Sửa lỗi trong slides "Quy nạp và Đệ quy"
    * Trang 27, $0 \leq i \leq k$ => $1 \leq i \leq k$
    * Trang 28, $3 \leq i \leq k$ => $4 \leq i \leq k$
* **27/02/2023:**
  * Sửa lỗi trong slides "Quy nạp và Đệ quy"
    * Trang 10, $\displaystyle\frac{1(1+2)}{2}$ => $\displaystyle\frac{1(1+1)}{2}$
    * Trang 16, $\displaystyle \bigwedge_{j=1}^kP(j)$ => $\displaystyle \bigwedge_{j=b}^kP(j)$
    * Trang 20, $a, b \in \mathbb{Z}^+$ => $a, b \in \mathbb{Z}$
    * Trang 26, $f(n-2)$ => $f_{n-2}$
* **26/02/2023:**
  * Thêm tài liệu tham khảo
    * Ebook "Toán rời rạc và ứng dụng" (Nguyễn Hữu Điển)
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung))
    * Quy nạp và Đệ quy 
* **21/02/2023:**
  * Nhận xét về bài Kiểm tra thường xuyên 1 (xem [ở đây](#nội-dung))
* **20/02/2023:**
  * Sửa lỗi trong slides "Các cấu trúc cơ bản II" (trang 9) $\displaystyle\sum_{j=m}^na_i$ => $\displaystyle\sum_{j=m}^na_j$
  * Kiểm tra thường xuyên 1 (xem đề bài và gợi ý giải [ở đây](#nội-dung))
* **12/02/2023:**
  * Cập nhật nội dung môn học (xem [ở đây](#nội-dung)) 
    * Các cấu trúc cơ bản: Tập hợp, Hàm, Dãy và Tổng
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
