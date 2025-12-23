---
layout: blog-post
title: "Bảng Tiêu Chuẩn Giáo Sư, Phó Giáo Sư"
author: Duc A. Hoang
lang: vi
categories: 
    - research
last_modified_at: 2025-12-20
description: Bảng tiêu chuẩn xét Giáo sư, Phó Giáo sư năm 2025 theo Quyết định 37/2018/QĐ-TTg và Quyết định 25/2020/QĐ-TTg
keywords: giáo sư, phó giáo sư, tiêu chuẩn, xét duyệt
<!--published: false-->
<!--javascript: true-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Tóm tắt</h1>
Bài viết ghi lại bảng tiêu chuẩn xét Giáo sư, Phó Giáo sư năm 2025 theo [Quyết định 37/2018/QĐ-TTg](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=194778) và [Quyết định 25/2020/QĐ-TTg](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=200876) của Thủ tướng Chính phủ Việt Nam. Bảng này được tổng hợp từ các nguồn chính thức và cung cấp chi tiết về các tiêu chí cần thiết để xét đạt chức danh Giáo sư và Phó Giáo sư. Phần lớn các nội dung bắt nguồn từ tài liệu {% include files.html name="Tieu-chuan-va-quy-trinh-xet-GS-PGS-danh-cho-ung-vien-nam-2025.pdf" text="Tiêu chuẩn và quy trình xét công nhận đạt tiêu chuẩn chức danh giáo sư, phó giáo sư năm 2025" %}. Các mẫu đề cập trong bảng có tại tài liệu {% include files.html name="Phu-luc-II.doc" text="Phu-luc-II.doc" %}.
</div>

<table border="1" cellpadding="5" cellspacing="0">
        <thead>
                <tr>
                        <th>Tiêu chuẩn</th>
                        <th>Chi tiết cho Giáo sư (GS)</th>
                        <th>Chi tiết cho Phó Giáo sư (PGS)</th>
                        <th>Nguồn tham khảo</th>
                        <th>Tài liệu/Minh chứng</th>
                        <th>Ghi chú</th>
                </tr>
        </thead>
        <tbody>
                {% for group in site.data.gspgs %}
                        <tr>
                                <td colspan="7"><strong>{{ group.group }}</strong></td>
                        </tr>
                        {% for item in group.items %}
                                <tr>
                                        <td>{{ item.num }}. {{ item.name }}</td>
                                        <td>{{ item.gs }}</td>
                                        <td>{{ item.pgs }}</td>
                                        <td>{{ item.source }}</td>
                                        <td>{{ item.evidence }}</td>
                                        <td>{{ item.note }}</td>
                                </tr>
                        {% endfor %}
                {% endfor %}
        </tbody>
</table>

<h2>Chú thích</h2>

<div style="column-count:2; -webkit-column-count:2; -moz-column-count:2; column-gap:2em;">
<ul>
        <li>GS: Giáo sư</li>
        <li>PGS: Phó Giáo sư</li>
        <li>CTKH: Công trình khoa học</li>
        <li>QĐ: Quyết định</li>
        <li>TTg: Thủ tướng</li>
        <li>KHSK: Khoa học sức khỏe</li>
        <li>KT&CN: Kinh tế và công nghệ</li>
        <li>KHXH&NV: Khoa học xã hội và nhân văn</li>
        <li>NT: Nghệ thuật</li>
        <li>TDTT: Thể dục thể thao</li>
        <li>CK: Chuyên khảo</li>
        <li>BSNT: Bác sĩ nội trú</li>
        <li>HV: Học viên</li>
        <li>HVCH: Học viên cao học</li>
        <li>NCS: Nghiên cứu sinh</li>
        <li>ThS: Thạc sĩ</li>
        <li>TS: Tiến sĩ</li>
        <li>CTKH: Công trình khoa học</li>
        <li>SC: Sáng chế</li>
        <li>GPHI: Giải pháp hữu ích</li>
        <li>CTĐT: Chương trình đào tạo</li>
        <li>QT: Quốc tế</li>
        <li>NXB: Nhà xuất bản</li>
        <li>IF: Impact Factor</li>
</ul>
</div>