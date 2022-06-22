---
layout: blog-post
title: Cài đặt VieTeX trong Windows 10 với Chocolatey
author: Duc A. Hoang
lang: "vi"
categories:
  - "tex"
  - "windows"
<!--comment: true-->
last_modified_at: 2021-04-15
description: Bài viết này ghi lại cách cài đặt VieTeX và các phần mềm liên quan trong Windows 10 với Chocolatey 
keywords: vietex, windows, cài đặt, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Tóm tắt</h1>
Bài viết này ghi lại các bước cài đặt [VieTeX](https://nhdien.wordpress.com/) và một số phần mềm liên quan trong Windows 10 với [Chocolatey](https://chocolatey.org/). 
</div>

# Cài đặt Chocolatey

Các yêu cầu cần thiết cho việc cài đặt Chocolatey có ở [đây](https://chocolatey.org/install/).
Tải tệp [installchocolatey.cmd](https://chocolatey.org/installchocolatey.cmd) hoặc tạo một tệp tên `installchocolatey.cmd` với nội dung như sau:

```
@echo off

SET DIR=%~dp0%

::download install.ps1
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "((new-object net.webclient).DownloadFile('https://chocolatey.org/install.ps1','%DIR%install.ps1'))"
::run installer
%systemroot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%DIR%install.ps1' %*"
```

và chạy `installchocolatey.cmd` với quyền Admin.

{% include image.html name="installchocolatey.gif" caption="Quá trình tôi cài đặt Chocolatey trong Windows 10 ghi lại bằng <a href='https://terminalizer.com/'>Terminalizer</a>: <code>PowerShell -Command \"Invoke-WebRequest -Uri https://chocolatey.org/installchocolatey.cmd -OutFile installchocolatey.cmd\"</code> tải tệp <code>installchocolatey.cmd</code> về thư mục hiện tại; <code>type installchocolatey.cmd</code> in ra màn hình nội dung của tệp đã tải về; và <code>installchocolatey.cmd</code> cài đặt Chocolatey" width="85%" %}

Bạn có thể xem thêm chi tiết về các cách cài đặt khác ở [đây](https://docs.chocolatey.org/en-us/choco/setup/).

Chú ý rằng việc cài đặt với Chocolatey chủ yếu là làm đơn giản hóa quá trình cài phần mềm trong Windows cho bạn. 
Thay vì phải ngồi tìm phần mềm, tải về, và bấm vào tệp cài đặt, bạn chỉ cần gõ một lệnh với Chocolatey, và phần mềm sẽ tự động thực hiện các thao tác trên cho bạn.
Nếu bạn quen thuộc với các trình quản lý gói trong Linux, ví dụ như `apt-get` (Ubuntu, Debian), `yum` (Fedora, Red Hat, CentOS), `pacman` (Arch Linux), v.v.. thì sẽ thấy rằng Chocolatey cũng có thể xem là một trình quản lý gói cho Windows.

# Cài đặt VieTeX và các phần mềm liên quan

Hướng dẫn cài đặt VieTeX và các phần mềm liên quan có ở [đây](https://nhdien.wordpress.com/cai-d%e1%ba%b7t/).
Các link để tải các phần mềm có ở [đây](https://nhdien.wordpress.com/t%e1%ba%a3i-xu%e1%bb%91ng/).
Các hướng dẫn khá chi tiết, nên tôi không nhắc lại.
Có thể tải hướng dẫn sử dụng VieTeX 4.0 ở [đây](http://www.scribd.com/doc/209273897/helpvietex40).
Tôi liệt kê một số phần mềm đã có ở Chocolatey mà bạn có thể cài.

**Chú ý:** Các lệnh dưới đây, nếu không có chú thích gì thêm, đều **chạy trong `cmd` hoặc `powershell` với quyền Admin**.

## VieTeX

Tôi đóng gói [VieTeX](https://chocolatey.org/packages/vietex/4.0) ở Chocolatey. 
Quá trình cài đặt đơn giản là tải tệp mà thầy Nguyễn Hữu Điển đã cung cấp ở [trang này](https://nhdien.wordpress.com/t%e1%ba%a3i-xu%e1%bb%91ng/) và giải nén tại thư mục `C:\vietex`, và sau đó tạo một shortcut ở Desktop. 
Để cài đặt, bạn chạy lệnh sau:

```
choco install -y vietex
```

hoặc ngắn gọn hơn

```
cinst -y vietex
```

Ngoài VieTeX, các trình soạn thảo TeX khác như [TeXstudio](https://chocolatey.org/packages/texstudio), [TeXMaker](https://chocolatey.org/packages/texmaker), [TeXmacs](https://chocolatey.org/packages/texmacs), [LyX](https://chocolatey.org/packages/lyx), hay [TeXnicCenter](https://chocolatey.org/packages/texniccenter) cũng có ở Chocolatey.

## MikTeX

Đã có người đóng gói [MikTeX](https://chocolatey.org/packages/miktex) ở Chocolatey.
Việc cài đặt MikTeX với bộ `basic` đơn giản chỉ là chạy 

```
cinst -y miktex
```

Có thể xem tệp `chocolateyinstall.ps1` ở [đây](https://community.chocolatey.org/packages/miktex.install) nếu muốn biết cụ thể quá trình cài đặt.
Về cơ bản, việc cài đặt MikTeX với Chocolatey được thực hiện dựa theo các hướng dẫn về việc sử dụng [MiKTeX setup utility](https://docs.miktex.org/manual/miktexsetup.html) (tệp `miktexsetup_standalone.exe`) để [cài đặt MikTeX trên nhiều máy tính cùng lúc thông qua giao diện dòng lệnh](https://miktex.org/howto/deploy-miktex).
Nếu muốn cài MikTeX với [toàn bộ các gói đã có](https://miktex.org/packages), chạy

```
cinst -y miktex --package-parameters "'/Set:complete'"
```

Việc cài MikTeX với toàn bộ các gói đã có chiếm dung lượng ổ cứng khá lớn. 
Tôi kiến nghị cài bộ `basic` (bao gồm các gói phổ biến) hoặc `essential` (bao gồm các gói không thể thiếu) (bỏ phần `/Set:complete` hoặc thay nó bằng `/Set:essential`) nếu tốc độ mạng Internet yếu hoặc ổ cứng dung lượng ít, sau đó cần gói nào có thể cài thêm.
Có thể xem [trang này](https://tex.stackexchange.com/a/539327) nếu muốn tìm hiểu xem các gói nào thuộc bộ nào.

**Chú ý:** Có thể làm như sau để cài MikTeX với toàn bộ các gói đã có nếu tốc độ mạng Internet không cao và muốn tránh việc cài đặt bị gián đoạn (tôi chưa thử, nhưng có lẽ có thể): Trước tiên tải toàn bộ các gói MikTeX, ví dụ như từ [CTAN](http://mirror.ctan.org/systems/win32/miktex/tm/packages), hoặc cũng có thể tải [proTeXt](https://www.tug.org/protext/) (kích thước tệp `protext.zip` khoảng hơn 1GB) và giải nén để lấy các gói kèm theo, hoặc [lấy sẵn các gói thầy Nguyễn Hữu Điển đã nén và đưa lên Mediafire](https://vietex.blog.fc2.com/blog-entry-5.html). Sau khi lấy được các gói thì sao chép toàn bộ vào thư mục `%localappdata%\Temp\chocolatey\MiKTeX-repository` và sau đó chạy lệnh `cinst -y miktex --package-parameters "'/Set:complete'"`. Nếu không muốn mất công chép các gói thì có thể dùng lệnh `cinst -y miktex --package-parameters '"/Set:complete /RepoPath:""C:\Shared Files\MiKTeX-Repo"""'`, trong đó thay `C:\Shared Files\MiKTeX-Repo` bằng đường dẫn tới thư mục chứa các gói đã tải về.

Ngoài ra, [TeX Live](https://chocolatey.org/packages/texlive) cũng có ở Chocolatey.

## Ghostscript

```
cinst -y ghostscript
```

**Chú ý:** GsView 5.0 cũng [có ở Chocolatey](https://chocolatey.org/packages/GSView/5.0.0.20170414) nhưng không cài được do họ không tiếp tục cập nhật link tải. Bạn có thể tải ở [đây](http://www.ghostgum.com.au/software/gsview.htm).

## Sumatra PDF

```
cinst -y sumatrapdf
```

Cần đặt lại tùy chọn trong VieTeX như sau. 
Mở VieTeX, chọn `Options > Configuration... > Set Program`.
Ở ô bên trái, chọn `25. Sumatra view pdf`.
Sau đó ở ô `Command:` ở bên phải, chọn đường dẫn `C:\Users\<username>\AppData\Local\SumatraPDF\SumatraPDF\SumatraPDF.exe`, trong đó`<username>` là tên đăng nhập của bạn trong Windows 10 (nếu bạn không biết thì chạy lệnh `echo %USERNAME%` trong `cmd`).

## Adobe Reader DC

```
cinst -y adobereader
```

Cần đặt lại tùy chọn trong VieTeX như sau. 
Mở VieTeX, chọn `Options > Configuration... > Set Program`.
Ở ô bên trái, chọn `8. Acrobat view PDF`.
Sau đó ở ô `Command:` ở bên phải, chọn đường dẫn tới tệp `AcroRd32.exe` (với Windows 10 64-bit là `C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe`).

## Bộ gõ Unikey

```
cinst -y unikey
```

**Chú ý:** Unikey chỉ có *một trang chủ duy nhất* là [unikey.org](https://www.unikey.org/). Trên thực tế, khi cài với Chocolatey, tệp cài đặt sẽ được tải trực tiếp từ trang này. Có thể xem về cách [chứng thực Unikey với chữ ký điện tử](https://www.unikey.org/certificate.html) để chắc chắn rằng chương trình là do chính tác giả Phạm Kim Long cung cấp.

## Vẽ hình

Thầy Nguyễn Hữu Điển có giới thiệu hai chương trình công cụ để vẽ hình là WinTpic và TpX (xem [trang này](https://nhdien.wordpress.com/cai-d%e1%ba%b7t/)). 
Tôi không quen thuộc với các chương trình này.
Theo tôi được biết thì có thể tải WinTpic ở [đây](http://aogaeru-lab.my.coocan.jp/sub1.html) và TpX (phiên bản từ 1.5 trở xuống) ở [đây](https://sourceforge.net/projects/tpx/files/tpx/) hoặc từ [CTAN](https://ctan.org/pkg/tpx).

Cá nhân tôi chủ yếu sử dụng [Ipe extensible drawing editor](http://ipe.otfried.org/), và tôi do đó cũng đóng gói phần mềm này ở Chocolatey.
Để cài đặt Ipe, chạy lệnh sau:

```
cinst -y ipe --version 7.2.21
```

Toàn bộ chương trình Ipe có ở `C:\ipe-7.2.21`. Nếu muốn cài phiên bản mới nhất thì bỏ phần `--version 7.2.21`.

Tôi cũng đóng gói [TpX](https://chocolatey.org/packages/tpx) và [WinTpic](https://chocolatey.org/packages/wintpic) ở Chocolatey. 
Quá trình cài đặt TpX tương tự như với VieTeX: tải TpX từ [trang này](https://sourceforge.net/projects/tpx/files/tpx/) và giải nén tại thư mục `C:\tpx`, và sau đó tạo một shortcut ở Desktop. 

Để cài đặt TpX, chạy

```
cinst -y tpx
```

Với TpX, cần đặt lại tùy chọn trong VieTeX như sau. 
Mở VieTeX, chọn `Options > Configuration... > Set Program`.
Ở ô bên trái, chọn `20. TpX`.
Sau đó ở ô `Command:` ở bên phải, chọn đường dẫn tới tệp `TpX.exe`, cụ thể là `C:\tpx\TpX.exe`.
Nếu không muốn cài đặt lại tùy chọn trong VieTeX thì thay vì lệnh trên, bạn sử dụng:

```
cinst -y tpx --package-parameters "'/InstallDir:C:\vietex\tpx'"
```

Tương tự như với VieTeX và TpX, để cài đặt WinTpic, chạy

```
cinst -y wintpic
```

Với WinTpic, cần đặt lại tùy chọn trong VieTeX như sau. 
Mở VieTeX, chọn `Options > Configuration... > Set Program`.
Ở ô bên trái, chọn `21. WinTpic`.
Sau đó ở ô `Command:` ở bên phải, chọn đường dẫn tới tệp `WTPIC.exe`, cụ thể là `C:\wintpic\WTPIC.exe`.
Nếu không muốn cài đặt lại tùy chọn trong VieTeX thì thay vì lệnh trên, bạn sử dụng:

```
cinst wintpic --package-parameters "'/InstallDir:C:\vietex\template\wintpic'"
```

**Chú ý:** WinTpic mặc định sử dụng giao diện tiếng Nhật, do tác giả Masashi Horii là người Nhật Bản. 
Để đổi sang giao diện tiếng Anh, mở WinTpic một lần rồi đóng lại, sau đó mở tệp `WTPIC.ini` trong thư mục cài đặt WinTpic (mặc định là `C:\wintpic`) và đổi `Language=1` (tiếng Nhật) thành `Language=0` (tiếng Anh).

# Cài toàn bộ (hoặc một phần trong số) các phần mềm trên chỉ với một dòng lệnh

Tải {% include files.html name="packages.config" %} hoặc tạo một tệp `packages.config` (hoặc bất kể tên nào với đuôi `.config` đều được) với thông tin về các phần mềm bạn muốn cài như sau (xem một ví dụ khác ở [đây](https://docs.chocolatey.org/en-us/choco/commands/install#packages.config))

```
<?xml version="1.0" encoding="utf-8"?>
<packages>
   <package id="vietex" version="4.0" />
   <package id="miktex" version="20.11.0.20201119" packageParameters="/Set:basic" />
   <package id="Ghostscript" version="9.53.3" />
   <package id="sumatrapdf" version="3.2" />
   <package id="adobereader" version="2020.013.20074" />
   <package id="unikey" version="4.3.200929" />
   <package id="Ipe" version="7.2.21" />
   <package id="tpx" version="1.5" packageParameters="/InstallDir:C:\vietex\tpx" />
   <package id="wintpic" version="4.32" packageParameters="/InstallDir:C:\vietex\template\wintpic" />
</packages>
```

Với tệp trên, các phiên bản tương ứng của các phần mềm đã giới thiệu đều sẽ được cài đặt, và bạn không cần thay đổi các tùy chọn gốc của VieTeX cho TpX và WinTpic.
Chú ý rằng nếu cài theo nội dung của `packages.config` như trên thì khi muốn gỡ bỏ VieTeX với lệnh `choco uninstall vietex`, bạn cần phải gỡ bỏ TpX và WinTpic trước, vì các thư mục cài đặt của các phần mềm này nằm trong thư mục cài đặt mặc định `C:\vietex` của VieTeX.
Bạn có thể thêm, bớt, hoặc chỉnh sửa tùy thích. 
Để cài đặt, chỉ cần chạy `cinst -y packages.config`.

{% include image.html name="installvietex.gif" caption="Quá trình tôi cài đặt các phần mềm nói trên trong Windows 10 ghi lại bằng <a href='https://terminalizer.com/'>Terminalizer</a>: <code>type packages.config</code> in ra màn hình nội dung của tệp <code>packages.config</code>; và <code>cinst -y packages.config</code> cài đặt các phần mềm" width="85%" %}
