---
layout: blog-post
title:  Mẫu lý lịch khoa học
author: "Duc A. Hoang"
lang: vi
categories: 
  - tex
<!--comment: true-->
last_modified_at: 2020-11-25
description: Mẫu lý lịch khoa học bằng LaTeX dựa theo mẫu tại Thông tư số 08/2011/TT-BGDĐT ngày 17/02/2011 của Bộ trưởng Bộ GDĐT
keywords: lý lịch khoa học, latex, overleaf, template, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Tóm tắt</h1>
Trong nhiều trường hợp, bên cạnh CV tiếng Anh, tôi cần sử dụng CV (lý lịch khoa học) tiếng Việt. 
Sau một thời gian tìm kiếm, tôi thấy một trong số các mẫu được sử dụng khá nhiều bởi các nhà khoa học cũng như các trường đại học ở Việt Nam là mẫu kèm theo [Thông tư số 08/2011/TT-BGDĐT ngày 17/02/2011 của Bộ trưởng Bộ GDĐT](http://vanban.chinhphu.vn/portal/page/portal/chinhphu/hethongvanban?class_id=1&_page=1&mode=detail&document_id=100339).
Bản Word (*.doc) của mẫu này có rất nhiều và có thể dễ dàng tìm kiếm trên mạng (bản gốc `Phụ lục V.doc` được nén trong [106138_TT8BGDDT2.RAR](http://datafile.chinhphu.vn/file-remote-v2/DownloadServlet?filePath=vbpq/2011/05/106138_TT8BGDDT2.RAR)).
Tôi quen thuộc với LaTeX hơn nên muốn tự tạo mẫu này bằng LaTeX để phục vụ cho mục đích sử dụng của bản thân.
Bài viết này ghi lại quá trình tự tạo mẫu CV tiếng Việt của tôi. 
Bạn cũng có thể tải và chỉnh sửa mẫu này từ [Overleaf](https://www.overleaf.com/latex/templates/ly-lich-khoa-hoc/tgxzgkzdsbpk).
</div>

# LaTeX class

Tôi sử dụng `article` class. 
Đây là một trong số các class thông dụng khi sử dụng LaTeX.

```latex
\documentclass[a4paper, 11pt]{article}
```

# Tiếng Việt trong LaTeX

Để sử dụng tiếng Việt trong LaTeX, tôi sử dụng các gói (package) sau:

```latex
% Vietnamese in LaTeX

\usepackage[utf8]{inputenc}
\usepackage[vietnamese,american]{babel}
```

# Định nghĩa lại `\maketitle`

Tôi muốn định nghĩa lại lệnh `\maketitle` để chèn thêm hai dòng chữ: "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" và "Độc lập - Tự do - Hạnh phúc". 
Do đây không phải văn bản hành chính theo đúng nghĩa, tôi thấy việc trình bày có thể không cần theo đúng quy chuẩn (định nghĩa ở [đây](http://www.moj.gov.vn/vbpq/lists/vn%20bn%20php%20lut/view_detail.aspx?itemid=26230)).
Tôi sử dụng cỡ chữ 11pt cho cả hai dòng trên, và dùng lệnh `\underline` cho dòng "Độc lập - Tự do - Hạnh phúc".

```latex
% Redefine Maketitle

\makeatletter
\def\@maketitle{
  \newpage
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\bf CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM \\
    			\underline{Độc lập -- Tự do -- Hạnh phúc} 
    }
    \vskip 1.5em%
    {\Large\bf \@title \par}%
    \vskip 2em%
  \end{center}%
  \par
  \vskip 1.5em}
\makeatother
```

# Gói `tabularx` và `multirow`

Để đơn giản, tôi dự định chuyển tất cả các nội dung cần điền sang dạng bảng.
Tôi sử dụng môi trường `tabularx` thay vì `tabular` để tận dụng tính năng căn chỉnh theo chiều rộng của trang giấy của `tabularx`.

```latex
% Table
\usepackage{tabularx}
\usepackage{multirow}
```

# Định nghĩa lại cách đánh số `\section` và `\subsection`

Các mục lớn (`\section`) được đánh số La Mã, trong khi các mục nhỏ (`\subsection`) được đánh số Ả Rập.

```latex
% Section/Subsection Numbering

\renewcommand\thesection{\Roman{section}.}
\renewcommand\thesubsection{\arabic{subsection}.}
```

# Căn lề trang giấy

```latex
% Adjust paper's margins

\usepackage{geometry}
\geometry{
a4paper,
total={170mm,257mm},
left=20mm,
top=20mm,
}
```

# Chèn một số thông tin cơ bản của CV đối với bản PDF

Tôi muốn thêm một số thông tin cơ bản vào bản PDF của CV tiếng Việt của tôi.
Việc này không ảnh hưởng gì đến bản in trên giấy.
Tôi cũng thay đổi màu của các URL trong CV để tiện phân biệt.

```latex
%% Hyperlinks
\usepackage{hyperref, color}								% to use hyperlinks
\definecolor{linkcolour}{rgb}{0,0.2,0.6}			% hyperlinks setup
\hypersetup{colorlinks,
			breaklinks,
			urlcolor=linkcolour, 
			linkcolor=linkcolour, 
			unicode=true,
			pdfauthor={Hoàng Anh Đức},
			pdftitle={Lý lịch khoa học: Hoàng Anh Đức},
			pdfsubject={Lý lịch khoa học: Hoàng Anh Đức},
			pdfkeywords={Hoàng Anh Đức, Lý lịch khoa học},
			pdfproducer={LaTeX},
			pdfcreator={pdflatex}}	
```

# Danh sách các công trình khoa học đã công bố

Tôi thường liệt kê tất cả các công bố của mình trong một file `pubs.bib`.
Tôi sửa [mẫu CV của Rob J. Hyndman](https://robjhyndman.com/hyndsight/cv/) để phù hợp với danh sách công bố của tôi.
Cụ thể, trong LaTeX preamble, tôi làm như sau (các bạn có thể copy nguyên hoặc sửa chữa cho phù hợp với bản thân):

```latex
% Bibliography formatting

\usepackage[sorting=ydnt,citestyle=authoryear,bibstyle=alphabetic,firstinits=false,defernumbers=true,maxnames=20,giveninits=false, bibencoding=utf8,doi=true,isbn=false,natbib=true,backend=biber]{biblatex}

\DeclareFieldFormat{url}{\url{#1}}
\DeclareFieldFormat[article]{pages}{#1}
\DeclareFieldFormat[inproceedings]{pages}{\lowercase{pp.}#1}
\DeclareFieldFormat[incollection]{pages}{\lowercase{pp.}#1}
\DeclareFieldFormat[article]{volume}{\mkbibbold{#1}}
\DeclareFieldFormat[article]{number}{\mkbibparens{#1}}
\DeclareFieldFormat[article]{title}{\MakeCapital{#1}}
\DeclareFieldFormat[article]{url}{}
\DeclareFieldFormat[inproceedings]{title}{#1}
\DeclareFieldFormat{shorthandwidth}{#1}
\DeclareFieldFormat{extradate}{}

% No dot before number of articles
\usepackage{xpatch}
\xpatchbibmacro{volume+number+eid}{\setunit*{\adddot}}{}{}{}

% Remove In: for an article.
\renewbibmacro{in:}{
  \ifentrytype{article}{}{
  \printtext{\bibstring{in}\intitlepunct}}}

% Bibliography categories
\def\makebibcategory#1#2{\DeclareBibliographyCategory{#1}\defbibheading{#1}{\textcolor{blue}{\noindent\large #2}}}
\makebibcategory{books}{Books}
\makebibcategory{papers}{Tạp chí khoa học}
\makebibcategory{chapters}{Book chapters}
\makebibcategory{conferences}{Kỷ yếu hội thảo}
\makebibcategory{techreports}{Unpublished working papers}
\makebibcategory{bookreviews}{Book reviews}
\makebibcategory{editorials}{Editorials}
\makebibcategory{phd}{Luận văn tiến sĩ}
\makebibcategory{subpapers}{Submitted papers}
\makebibcategory{curpapers}{Current projects}
\makebibcategory{software}{Software (R packages)}

\setlength{\bibitemsep}{2.3pt}
\setlength{\bibhang}{.9cm}
%\renewcommand{\bibfont}{\fontsize{12}{14}}

\renewcommand*{\bibitem}{\addtocounter{papers}{1}\item \mbox{}\hskip-0.9cm\hbox to 0.9cm{\hfill\arabic{papers}.~\,}}
\defbibenvironment{bibliography}
{\list{}
  {\setlength{\leftmargin}{\bibhang}%
   \setlength{\itemsep}{\bibitemsep}%
   \setlength{\parsep}{\bibparsep}}}
{\endlist}
{\bibitem}

\newenvironment{publications}{\subsection{Các công trình khoa học đã công bố}\label{papersstart}
}{\label{papersend}\addtocounter{sumpapers}{-1}\refstepcounter{sumpapers}\label{sumpapers}}

\def\printbib#1{\printbibliography[category=#1,heading=#1]\lastref{sumpapers}}
%\renewcommand{\bibfont}{\normalfont\fontsize{10}{12.4}\rmfamily}
% Counters for keeping track of papers
\newcounter{papers}\setcounter{papers}{0}
\newcounter{sumpapers}\setcounter{sumpapers}{0}
\def\lastref#1{\addtocounter{#1}{\value{papers}}\setcounter{papers}{0}}

% Add all papers in the bib file.
\nocite{*}

\bibliography{pubs}

\DeclareSourcemap{
  \maps[datatype=bibtex, overwrite]{
    \map{
      \step[fieldset=month, null]
    }
  }
}

\makebibcategory{inprogress}{Preprint}

\addtocategory{papers}{
  % ref-key,
  journals-tcs-DemaineDFHIOOUY15,
}

\addtocategory{conferences}{
  conf-walcom-HoangFU17,
  conf-isaac-HoangU16,
  conf-isaac-Fox-EpsteinHOU15,
  conf-isaac-DemaineDFHIOOUY14,
  }

%\addtocategory{inprogress}{
%  
%}

\addtocategory{phd}{
Hoang2018phd,
}
```

Ở đây, `journals-tcs-DemaineDFHIOOUY15` là từ khóa tham khảo (citation key) của một bài báo tôi đã công bố, `conf-isaac-HoangU16` là citation key của một bài báo trong kỷ yếu của một hội thảo quốc tế.
Nếu bạn quen thuộc với BibTeX thì không khó để hiểu quá trình này.
Ngược lại, nếu bạn không quen thuộc với BibTeX, bạn có thể tự liệt kê các công bố, ví dụ như bằng cách sử dụng môi trường `itemize` hoặc `enumerate`.

# Title

```latex
\title{LÝ LỊCH KHOA HỌC \\ \tiny\emph{(Dựa theo mẫu tại Thông tư số 08/2011/TT-BGDĐT ngày 17/02/2011 của Bộ trưởng Bộ GDĐT)}}
```

# Nội dung cụ thể

Phần nội dung cụ thể (đặt trong môi trường `document`) như sau.
Các bạn có thể tự điền các thông tin cho phù hợp.

```latex
\selectlanguage{vietnamese}
\maketitle

\section{LÝ LỊCH SƠ LƯỢC}

\begin{tabularx}{\columnwidth}{XXXX}
\multicolumn{2}{l}{Họ và tên:} & \multicolumn{2}{l}{Giới tính:}\\
\multicolumn{2}{l}{Ngày, tháng, năm sinh:} & \multicolumn{2}{l}{Nơi sinh:} \\ 
\multicolumn{2}{l}{Quê quán:} & \multicolumn{2}{l}{Dân tộc:} \\
\multicolumn{2}{l}{Học vị cao nhất:} & \multicolumn{2}{l}{Năm, nơi nhận học vị:}\\
\multicolumn{2}{l}{Chức danh khoa học cao nhất: } & \multicolumn{2}{l}{Năm bổ nhiệm:} \\
\multicolumn{4}{l}{Chức vụ (hiện tại hoặc trước khi nghỉ hưu):} \\
\multicolumn{4}{l}{Đơn vị công tác (hiện tại hoặc trước khi nghỉ hưu):} \\
\multicolumn{4}{l}{Chỗ ở riêng hoặc địa chỉ liên lạc:} \\
Điện thoại liên hệ: & CQ: & NR: & DĐ: \\
\multicolumn{2}{l}{Fax:} & \multicolumn{2}{l}{Email:} \\
Số CMND: & Nơi cấp: & Ngày cấp: & \\
\end{tabularx}

\section{QUÁ TRÌNH ĐÀO TẠO}

\subsection{Đại học}

\begin{tabularx}{\columnwidth}{XX}
Ngành học: & Hệ đào tạo:\\
\multicolumn{2}{l}{Nơi đào tạo:} \\
Nước đào tạo: & Năm tốt nghiệp: \\
\end{tabularx}

\subsection{Sau đại học}

\begin{tabularx}{\columnwidth}{p{0.1cm}p{12cm}X}
$-$ & \multicolumn{2}{l}{Thạc sĩ chuyên ngành: }\\
 & Nơi đào tạo: & Năm cấp bằng: \\
 & \multicolumn{2}{l}{Tên luận văn: }\\
$-$ & \multicolumn{2}{l}{Tiến sĩ chuyên ngành: }\\
 & Nơi đào tạo:  & Năm cấp bằng: \\
 & \multicolumn{2}{l}{Tên luận văn:}\\
\end{tabularx}

\subsection{Ngoại ngữ}

\begin{tabularx}{\columnwidth}{p{0.1cm}XX}
1. &  & Mức độ sử dụng: \\
\end{tabularx}

\section{QUÁ TRÌNH CÔNG TÁC}

\begin{tabularx}{\columnwidth}{|X|X|X|}
\hline
Thời gian & Nơi công tác & Công việc đảm nhiệm \\
\hline
& & \\
\hline
\end{tabularx}

\section{QUÁ TRÌNH NGHIÊN CỨU KHOA HỌC}

\subsection{Các đề tài nghiên cứu khoa học đã và đang tham gia}

\begin{tabularx}{\columnwidth}{|p{0.5cm}|X|X|X|}
\hline
TT & Năm bắt đầu/Năm hoàn thành & Đề tài cấp (NN, Bộ, ngành, trường) & Trách nhiệm tham gia trong đề tài \\
\hline
& & & \\
\hline
\end{tabularx}

%% Publications

\begin{publications}

%\printbib{books}
\printbib{papers}
%\printbib{chapters}
\printbib{conferences}
\printbib{inprogress}
%\printbib{bookreviews}
%\printbib{editorials}
\printbib{phd}
\end{publications}

\vskip 1em

\begin{flushright}
\begin{tabularx}{0.5\columnwidth}{c}
Hà Nội, \today \\
{\bf Người khai ký tên} \\
(Ghi rõ chức danh khoa học, học vị) \\
\\
\\
\\
\\
\\
\end{tabularx}
\end{flushright}
```

# Tạo file PDF

Các lệnh cụ thể tôi thường dùng như sau (giả sử tên file là `CV-vi.tex`). 

```bash
pdflatex CV-vi.tex
biber CV-vi.bcf
pdflatex CV-vi.tex
```

Để thực hiện lệnh này, các bạn cần cài đặt các phầm mềm liên quan đến việc sử dụng LaTeX và BibLaTeX (với `backend=biber`).
Có rất nhiều hướng dẫn trên mạng (cả tiếng Việt lẫn tiếng Anh).
Một trong những phần mềm soạn thảo LaTeX nổi tiếng cho người Việt là [VieTeX](https://nhdien.wordpress.com/) của thầy Nguyễn Hữu Điển.
Ở trang chủ của VieTeX bạn cũng có thể tìm được rất nhiều các hướng dẫn cài đặt cũng như sử dụng TeX, kể cả cho người mới dùng cũng như người dùng lâu năm.
Các bạn cũng có thể tham khảo cách tôi cài các phần mềm liên quan đến LaTeX trên [Ubuntu 16.04]({% post_url 2018-05-26-install-and-configure-ubuntu-16-04-lts %}#texlive-2017) hoặc [Arch Linux]({% post_url 2018-05-26-some-notes-on-installing-and-using-arch-linux %}#vanilla-texlive-2017).

Các bạn cũng có thể xem [bản lý lịch khoa học của tôi]({{ site.baseurl }}/CV-vi.pdf) được tạo bởi phương pháp tương tự như trên.

# Bỏ đánh số trang

Nếu muốn bỏ đánh số trang, có thể thêm `\pagestyle{empty}` ngay sau `\begin{document}` và thêm `\thispagestyle{empty}` ngay sau `\maketitle` (nếu không thêm dòng này thì trang đầu sẽ bị đánh số do `\maketitle` sử dụng mặc định pagestyle `plain`).
