---
layout: blog-post
title: Xây dựng trang cá nhân với Jekyll
author: Duc A. Hoang
lang: vi
categories:
  - "jekyll"
  - "linux"
  - "windows"
<!--comment: true-->
last_modified_at: 2021-12-09
description: Bài viết này mô tả quá trình xây dựng trang cá nhân với Jekyll
keywords: trang cá nhân, jekyll, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Tóm tắt</h1>
Trong bài viết này, tôi mô tả quá trình xây dựng trang cá nhân (personal webpage) của tôi với Jekyll. Tôi xây dựng trang cá nhân với mục đích chủ yếu để lưu trữ thông tin về quá trình làm việc của tôi và các sở thích khác liên quan. Nếu bạn không xây dựng trang cá nhân theo hướng này, vậy các phần trình bày ở đây thường không có tác dụng nhiều lắm với bạn.

<strong>Cập nhật (2020-02-14):</strong> Tôi thay đổi thiết kế của trang cá nhân sang giao diện đơn giản hơn. Tuy nhiên, các hướng dẫn ghi lại ở đây đôi khi vẫn có ích.
</div>

# Dự định

Những dự định của tôi khi xây dựng một trang cá nhân với [Jekyll](https://jekyllrb.com/):

* Sử dụng GitHub để [host trang cá nhân](https://pages.github.com/).
  * Khi bạn [đăng ký tài khoản GitHub](https://github.com/join), bạn có thể tạo một trang cá nhân ở địa chỉ `username.github.io`, trong đó `username` là tên đăng nhập bạn đăng ký vói GitHub.
  * Để tạo trang cá nhân, bạn cần tạo một repository với tên `username.github.io`. Tôi dự định tạo hai branch: `master` và `source`.
    * Branch `master` chứa các sản phẩm sinh bởi Jekyll.
    * Branch `source` chứa mã nguồn sẽ được sử dụng bởi Jekyll.
* Cài đặt Jekyll trên máy tính cá nhân để sinh và kiểm tra nội dung của trang cá nhân trước khi đưa lên GitHub.
* (Tùy chọn) Sử dụng [Travis CI](https://travis-ci.org/) để sinh tự động trang cá nhân mỗi khi có cập nhật từ branch `source`. Để làm được điều này, bạn cần đăng nhập Travis CI với tài khoản GitHub.  
* (Tùy chọn) Sử dụng [GitHub Actions](https://github.com/features/actions) để sinh tự động trang cá nhân mỗi khi có cập nhật từ branch `source`.

# Môi trường làm việc

## Jekyll

Tôi sử dụng hệ điều hành [Arch Linux](https://www.archlinux.org/) phiên bản 64-bit. 
Việc cài đặt Jekyll trong Arch Linux được tiến hành như sau:

```bash
sudo pacman -S --needed --noconfirm ruby rubygems ruby-docs ruby-rdoc
echo "export PATH=$PATH:/home/hoanganhduc/.gem/ruby/2.5.0/bin;" >> .bashrc 
source .bashrc
gem install bundler
wget https://raw.githubusercontent.com/username/username.github.io/source/Gemfile
wget https://raw.githubusercontent.com/username/username.github.io/source/Gemfile.lock
bundle install
```

Các bạn cũng có thể tham khảo quá trình tôi cài Jekyll trong [Ubuntu 16.04 LTS]({% post_url 2018-05-26-install-and-configure-ubuntu-16-04-lts %}#jekyll) hoặc [Windows 10]({% post_url 2018-05-26-setup-jekyll-in-windows %}). Tuy nhiên, tôi đề nghị các bạn nên cài đặt Ubuntu 16.04 trong Windows 10 thông qua [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
Tôi ghi lại các bước cài đặt trong Ubuntu ở đây.

```bash
sudo apt install ruby rubygems
gem install bundler
wget https://raw.githubusercontent.com/username/username.github.io/source/Gemfile
wget https://raw.githubusercontent.com/username/username.github.io/source/Gemfile.lock
bundle install
```

Nội dung các tệp `Gemfile` và `Gemfile.lock` tính đến thời gian tôi viết bài này là như sau.

Tệp <code>Gemfile</code>

```bash
source 'https://rubygems.org'

gem 'jekyll'
gem 'rouge'
gem 'kramdown'
gem 'rake'
gem 'jekyll-scholar'
gem 'pygments.rb'
gem 'jekyll-sitemap'
gem 'jekyll-feed'
gem 'jekyll-email-protect'
gem 'jekyll-last-modified-at'
```

Tệp <code>Gemfile.lock</code>

```bash
GEM
  remote: https://rubygems.org/
  specs:
    addressable (2.5.2)
      public_suffix (>= 2.0.2, < 4.0)
    bibtex-ruby (4.4.7)
      latex-decode (~> 0.0)
    citeproc (1.0.9)
      namae (~> 1.0)
    citeproc-ruby (1.1.10)
      citeproc (~> 1.0, >= 1.0.9)
      csl (~> 1.5)
    colorator (1.1.0)
    concurrent-ruby (1.1.3)
    csl (1.5.0)
      namae (~> 1.0)
    csl-styles (1.0.1.9)
      csl (~> 1.0)
    em-websocket (0.5.1)
      eventmachine (>= 0.12.9)
      http_parser.rb (~> 0.6.0)
    eventmachine (1.2.7)
    eventmachine (1.2.7-x64-mingw32)
    eventmachine (1.2.7-x86-mingw32)
    ffi (1.9.25)
    ffi (1.9.25-x64-mingw32)
    ffi (1.9.25-x86-mingw32)
    forwardable-extended (2.6.0)
    http_parser.rb (0.6.0)
    i18n (0.9.5)
      concurrent-ruby (~> 1.0)
    jekyll (3.8.5)
      addressable (~> 2.4)
      colorator (~> 1.0)
      em-websocket (~> 0.5)
      i18n (~> 0.7)
      jekyll-sass-converter (~> 1.0)
      jekyll-watch (~> 2.0)
      kramdown (~> 1.14)
      liquid (~> 4.0)
      mercenary (~> 0.3.3)
      pathutil (~> 0.9)
      rouge (>= 1.7, < 4)
      safe_yaml (~> 1.0)
    jekyll-email-protect (1.1.0)
    jekyll-feed (0.11.0)
      jekyll (~> 3.3)
    jekyll-last-modified-at (1.0.1)
      jekyll (~> 3.3)
      posix-spawn (~> 0.3.9)
    jekyll-sass-converter (1.5.2)
      sass (~> 3.4)
    jekyll-scholar (5.14.0)
      bibtex-ruby (~> 4.0, >= 4.0.13)
      citeproc-ruby (~> 1.0)
      csl-styles (~> 1.0)
      jekyll (~> 3.0)
    jekyll-sitemap (1.2.0)
      jekyll (~> 3.3)
    jekyll-watch (2.1.2)
      listen (~> 3.0)
    kramdown (1.17.0)
    latex-decode (0.3.1)
    liquid (4.0.1)
    listen (3.1.5)
      rb-fsevent (~> 0.9, >= 0.9.4)
      rb-inotify (~> 0.9, >= 0.9.7)
      ruby_dep (~> 1.2)
    mercenary (0.3.6)
    multi_json (1.13.1)
    namae (1.0.1)
    pathutil (0.16.2)
      forwardable-extended (~> 2.6)
    posix-spawn (0.3.13)
    public_suffix (3.0.3)
    pygments.rb (1.2.1)
      multi_json (>= 1.0.0)
    rake (12.3.1)
    rb-fsevent (0.10.3)
    rb-inotify (0.9.10)
      ffi (>= 0.5.0, < 2)
    rouge (3.3.0)
    ruby_dep (1.5.0)
    safe_yaml (1.0.4)
    sass (3.7.2)
      sass-listen (~> 4.0.0)
    sass-listen (4.0.0)
      rb-fsevent (~> 0.9, >= 0.9.4)
      rb-inotify (~> 0.9, >= 0.9.7)

PLATFORMS
  ruby
  x64-mingw32
  x86-mingw32

DEPENDENCIES
  jekyll
  jekyll-email-protect
  jekyll-feed
  jekyll-last-modified-at
  jekyll-scholar
  jekyll-sitemap
  kramdown
  pygments.rb
  rake
  rouge

BUNDLED WITH
   1.17.1
```

Chú ý là việc cài đặt các gem này là để phục vụ cho việc **sinh trang cá nhân của tôi**. Các bạn có thể cài thêm các gem khác, hoặc bỏ bớt đi, tùy theo nhu cầu của mỗi người.

## Git + GnuPG + OpenSSH + Travis CI CLI

* Trong Arch Linux, việc cài đặt các gói [Git](https://wiki.archlinux.org/index.php/Git), [GnuPG](https://wiki.archlinux.org/index.php/GnuPG), và [OpenSSH](https://wiki.archlinux.org/index.php/OpenSSH) được thực hiện đơn giản thông qua lệnh `sudo pacman -S --needed --noconfirm git gnupg openssh`. Trong Ubuntu, bạn sử dụng lệnh `sudo apt install git gnupg2 ssh`. **Việc sử dụng GnuPG và OpenSSH hay không là tùy bạn**.
  * Sử dụng SSH key với GitHub:
    * Tạo một SSH key bằng lệnh `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"` (thay `your_email@example.com` bằng địa chỉ email của bạn) nếu bạn chưa có. Khi bạn được hỏi `Enter a file in which to save the key`, nhấn <kbd>Enter</kbd> để chấp nhận vị trí lưu key mặc định `$HOME/.ssh/id_rsa`. Tiếp đó, nhập passphrase bất kỳ để kết thúc quá trình tạo key. Để sử dụng key với GitHub, mở tệp `$HOME/.ssh/id_rsa` bằng một trình soạn thảo văn bản nào đó (tôi dùng `gedit`) và chép tất cả nội dung vào GitHub (bằng cách đăng nhập vào GitHub, sau đó truy cập tới địa chỉ [https://github.com/settings/keys](https://github.com/settings/keys) và nhấn vào nút `New SSH key`).
    * Để kiểm tra, gõ lệnh `ssh -T git@github.com` và nhập passphrase bạn khởi tạo khi tạo SSH key. Nếu bạn thấy dòng `Hi username! You've successfully authenticated, but GitHub does not provide shell access` thì tức là bạn đã cài đặt thành công.
  * Sử dụng GnuPG với GitHub:
    * Tạo một GPG key bằng lệnh `gpg --full-generate-key` (với `gnupg >= 2.1.17`) nếu bạn chưa có. 
    * Để liệt kê tất cả các GPG secret key (tức là gồm cả private và public key) bạn đang có, sử dụng lệnh `gpg --list-secret-keys --keyid-format LONG`.
    * Xác định ID của key bạn muốn sử dụng với GitHub, ví dụ `3AA5C34371567BD2`, sau đó export public key của key này bằng lệnh `gpg --armor --export 3AA5C34371567BD2`, và chép phần bắt đầu từ `-----BEGIN PGP PUBLIC KEY BLOCK-----` và kết thúc bởi `-----END PGP PUBLIC KEY BLOCK-----` vào GitHub (bằng cách đăng nhập vào GitHub, sau đó truy cập tới địa chỉ [https://github.com/settings/keys](https://github.com/settings/keys) và nhấn vào nút `New GPG key`).
    * Chú ý là trong Ubuntu, bạn cần dùng lệnh `gpg2` thay vì `gpg`.
  * Một số cài đặt mặc định cho Git.
	```bash
	git config --global user.name "username" # pick any name you like
	git config --global user.email "your_email@example.com" # pick any email address you like
	git config --global gpg.program gpg2 # if you use GnuPG
	git config --global user.signingkey your-gpg-key-id # if you use GnuPG
	```

* Tôi cũng sử dụng [Travis CI CLI](https://github.com/travis-ci/travis.rb#command-line-client). Việc cài đặt được thực hiện thông qua lệnh `gem install travis`.

## Một số cài đặt khác

* Thư mục gốc của tôi được đặt ở Dropbox. 
* Tôi tạo thư mục `$HOME/username.github.io` và hai thư mục con `$HOME/username.github.io/master` và `$HOME/username.github.io/source` tương ứng với các branch `master` và `source` tôi tạo ra trên GitHub. Branch `master` được mặc định khi bạn tạo repository `username.github.io` của mình. Để tạo branch `source`, bạn mở trang chính của repossitory (URL thường có dạng `https://github.com/username/username.github.io/`), chọn menu thả xuống `Branch` và gõ tên `source` để tạo branch mới. 
* Trong thư mục `$HOME/username.github.io/master`, tôi khởi tạo như sau: 
```bash
cd $HOME/username.github.io/master
git init
git remote add origin git@github.com:username/username.github.io.git
git pull origin master
```

* Trong thư mục `$HOME/username.github.io/source`, tôi khởi tạo như sau: 
```bash
cd $HOME/username.github.io/source
git init
git remote add origin git@github.com:username/username.github.io.git
git symbolic-ref HEAD refs/heads/source
git clean -fdx
git pull origin source
```

# Xây dựng trang cá nhân

Các bạn có thể tham khảo mã nguồn của trang cá nhân của tôi ở [https://github.com/hoanganhduc/hoanganhduc.github.io/tree/source](https://github.com/hoanganhduc/hoanganhduc.github.io/tree/source). Để tự tạo trang cá nhân cho mình, các bạn nên tải mã nguồn về, tự sinh trang web thử bằng Jekyll, và tự sửa cho phù hợp với bản thân mình. Ở đây tôi chỉ giải thích qua một số phần tôi cho là quan trọng.

## Cấu trúc 

Mã nguồn trang cá nhân của tôi tính đến thời điểm hiện tại có cấu trúc như sau:

```bash

.
├── _bibliography
│   ├── publications
│   │   ├── conferences.bib
│   │   ├── journals.bib
│   │   ├── preprints.bib
│   │   └── thesis.bib
│   └── references.bib
├── build.sh
├── co-authors.md
├── _config.yml
├── _courses
│   ├── Toan-roi-rac-K61CNTN-Toan-HK12018.md
│   └── Toan-roi-rac-K61CN-Toan-HK12018.md
├── courses
│   └── 2018
│       ├── MAT3302
│       │   ├── basiccounting.pdf
│       │   ├── exam1.pdf
│       │   ├── genpermcomb.pdf
│       │   ├── graph1.pdf
│       │   ├── graph2.pdf
│       │   ├── graph3.pdf
│       │   ├── pigeon_inclexcl.pdf
│       │   ├── rec.pdf
│       │   └── tree.pdf
│       └── MAT3302-2TNT
│           ├── KiemTraCNTN_20181010.pdf
│           ├── ps10.pdf
│           ├── ps1.pdf
│           ├── ps2.pdf
│           ├── ps3.pdf
│           ├── ps4.pdf
│           ├── ps5.pdf
│           ├── ps6.pdf
│           ├── ps7.pdf
│           ├── ps8.pdf
│           └── ps9.pdf
├── CV.pdf
├── CV-vi.pdf
├── _data
│   ├── coauthors.yaml
│   ├── navbar.yaml
│   └── news.yaml
├── _drafts
│   └── .gitignore
├── events
│   ├── CoRe2015
│   │   ├── abstract.pdf
│   │   ├── poster.pdf
│   │   └── slide.pptx
│   ├── ISAAC2014
│   │   └── slide.pptx
│   ├── ISAAC2015
│   │   └── slide.pdf
│   ├── ISAAC2016
│   │   └── slide.pdf
│   ├── JCDCGG2014
│   │   ├── abstract.pdf
│   │   └── slide.pptx
│   ├── LASymposium2015winter
│   │   ├── paper.pdf
│   │   └── slide.pdf
│   ├── PhD-Thesis-Defense
│   │   ├── Duc_FinalDefense_20180507_handout.pdf
│   │   └── Duc_FinalDefense_20180507.pdf
│   ├── SIGAL-157
│   │   └── slide.pdf
│   ├── WAAC2018
│   │   ├── abstract.pdf
│   │   └── slide.pdf
│   └── WALCOM2017
│       └── slide.pdf
├── events.md
├── Gemfile
├── Gemfile.lock
├── _includes
│   ├── author-info.html
│   ├── disqus.html
│   ├── files.html
│   ├── footer.html
│   ├── header.html
│   ├── head.html
│   ├── image.html
│   ├── intensedebate.html
│   ├── news.html
│   ├── search-form.html
│   └── version.html
├── index.md
├── keybase.txt
├── _latex-template
│   ├── Beamer-Santiago.md
│   ├── HUS-Beamer.md
│   ├── JAIST-Doctoral-Thesis.md
│   ├── LIPIcs-Template.md
│   ├── MIT-Lecture-Note.md
│   ├── Name-Card.md
│   ├── Preprint-Elsevier.md
│   ├── Springer-LNCS.md
│   └── Vietnamese-CV.md
├── latex-template
│   ├── Beamer-Santiago
│   │   ├── Beamer-Santiago.zip
│   │   ├── .DS_Store
│   │   └── Santiago2008.pdf
│   ├── HUS-Beamer
│   │   ├── HUS-Beamer.pdf
│   │   └── HUS-Beamer.zip
│   ├── JAIST-Doctoral-Thesis
│   │   ├── abstract.pdf
│   │   ├── doctor-is.zip
│   │   └── paper.pdf
│   ├── MIT-Lecture-Note
│   │   ├── alg-comb-lecture-n.pdf
│   │   └── alg-comb-lecture-n.zip
│   ├── Name-Card
│   │   ├── main.pdf
│   │   └── Name-Card.zip
│   ├── Preprint-Elsevier
│   │   ├── main.pdf
│   │   └── Preprint-Elsevier.zip
│   └── Vietnamese-CV
│       └── Vietnamese-CV.zip
├── latex-template.md
├── _layouts
│   ├── bib.html
│   ├── blog-post.html
│   ├── collection_item.html
│   ├── collection_main.html
│   ├── page.html
│   ├── post.html
│   ├── pub_style.html
│   └── search.html
├── LICENSE.txt
├── misc.html
├── pdf
│   ├── .gitignore
│   └── ShortestReconfigurationSequenceforSlidingTokensonSpiders.pdf
├── _plugins
│   ├── hook-add-last-modified-date.rb
│   └── version_reporter.rb
├── _posts
│   ├── 2018-05-26-install-and-configure-ubuntu-16-04-lts.md
│   ├── 2018-05-26-install-latex2html-in-windows.md
│   ├── 2018-05-26-setup-jekyll-in-windows.md
│   ├── 2018-05-26-some-beamer-tips.md
│   ├── 2018-05-26-some-notes-on-installing-arch-linux.md
│   ├── 2018-06-11-download-windows-iso.md
│   ├── 2018-06-24-phd-degree-conferment-ceremony.md
│   ├── 2018-06-29-mẫu-lý-lịch-khoa-học.md
│   ├── 2018-08-08-my-first-experience-with-android-phones.md
│   ├── 2018-11-24-xây-dựng-trang-cá-nhân-với-jekyll.md
│   └── .gitignore
├── publications.md
├── pub_style.csl
├── README.md
├── robots.txt
├── search.html
├── services.md
├── slides
│   ├── .gitignore
│   ├── HUS_20180831.pdf
│   └── HUS_20181012.pdf
├── springer-lncs.csl
├── static
│   ├── css
│   │   ├── custom.css
│   │   ├── LaTeXMLstyle.css
│   │   ├── solarized-dark.css
│   │   └── solarized-light.css
│   ├── files
│   │   ├── other-writings
│   │   │   └── Needleman_2009_Làm toán để tìm được công việc tốt.pdf
│   │   └── posts
│   │       ├── mẫu-lý-lịch-khoa-học
│   │       │   └── ly-lich-khoa-hoc.pdf
│   │       └── some-notes-on-installing-arch-linux
│   │           └── linuxsslvpn.gz
│   ├── img
│   │   ├── Duc.ico
│   │   ├── Duc.jpg
│   │   └── posts
│   │       ├── my-first-experience-with-android-phones
│   │       │   ├── screen1.png
│   │       │   ├── screen2.png
│   │       │   ├── screen3.png
│   │       │   └── screen4.png
│   │       ├── phd-degree-conferment-ceremony
│   │       │   ├── Duc_Uehara_01.JPG
│   │       │   ├── Duc_Uehara_02.JPG
│   │       │   ├── Duc_Uehara_03.JPG
│   │       │   ├── Duc_Uehara_04.JPG
│   │       │   ├── Duc_Uehara_05.JPG
│   │       │   ├── Uehara_Duc_Asano.JPG
│   │       │   └── With_Tung_and_Others.jpg
│   │       └── some-notes-on-installing-arch-linux
│   │           └── fp_jaistvpn1and2.png
│   └── js
│       ├── lunr.min.js
│       └── search.js
├── teaching.md
└── .travis.yml

48 directories, 153 files

```

Ở đây, tôi giải thích vai trò của một số tệp và thư mục.

<div class="table-responsive" markdown="1">

{:.table .table-striped .table-bordered}
|     Tệp/Thư mục         | Vai trò |
|:-----------------------:|:--------|
| <span class="text-monospace">_config.yml</span> | Chứa các thông tin cấu hình trang cá nhân. Khi sinh (generate) trang cá nhân, Jekyll sẽ sử dụng các cấu hình trong tệp này |
| <span class="text-monospace">static</span> | Chứa các tệp và thư mục cần thiết để xây dựng trang cá nhân. Các tệp trong thư mục `static/css` được sử dụng để tùy chỉnh các cách hiển thị trang cá nhân (font chữ, màu, v.v...). Các tệp trong thư mục `static/js` là một số mã Javascript được sử dụng trong trang cá nhân. Các tệp trong thư mục `static/img` chứa các hình ảnh được sử dụng trong trang cá nhân. Các tệp trong thư mục `static/files` chứa các tệp liên quan đến các bài viết (blog posts). |
| <span class="text-monospace">_includes</span> | Chứa các thành phần cần thiết (tệp dạng `*.html`), ví dụ như đầu trang (`head.html`), thanh di chuyển (`navbar`, được đặt trong `header.html`), cuối trang (`footer.html`), v.v... để xây dựng một cấu trúc hoàn chỉnh, ví dụ như một trang (page), một bài viết (blog post), v.v... Bạn có thể thêm nội dung bất kỳ một tệp nào trong thư mục này vào một tệp khác bằng cách sử dụng Liquid tag, ví dụ như <code>{% raw %}{% include head.html %} {% endraw %} </code> |
| <span class="text-monospace">_layouts</span> | Các cấu trúc hoàn chỉnh (tệp dạng `*.html`), ví dụ như một trang (page), một bài viết (blog post), được xây dựng phần lớn các cấu trúc ở thư mục `_includes` |
| <span class="text-monospace">_plugins</span> | Chứa các plugins tôi cần: `hook-add-last-modified-date.rb` để lấy thời gian chỉnh sửa tệp cuối cùng, và `version_reporter.rb` để lấy phiên bản Jekyll tôi đang sử dụng |
| <span class="text-monospace">index.md</span> | Trang chủ (Home) |
| <span class="text-monospace">_posts</span> | Chứa các bài viết (blog post). Tên tệp thường có dạng `YYYY-MM-DD-name-of-blog-post.md` |
| <span class="text-monospace">search.html</span> | Chứa bộ máy tìm kiếm nội dung các bài viết trong trang cá nhân. |
| <span class="text-monospace">_drafts</span> | Chứa bản nháp (chưa publish) của các bài viết (blog post). Tên tệp thường có định dạng `name-of-blog-post.md` |
| <span class="text-monospace">misc.html</span> | Liệt kê các bài viết (blog posts) và các thứ linh tinh khác mà tôi thích |
| <span class="text-monospace">_data</span> | Chứa một số tệp dữ liệu nhỏ định dạng `*.yml` để xây dựng một số phần, ví dụ như danh sách các tin tức mới (news), hay danh sách các đồng tác giả (co-authors), hay danh sách các thành phần của thanh di chuyển (navigation bar items), v.v...  | 
| <span class="text-monospace">_bibliography</span> | Chứa các tệp dạng `*.bib` phục vụ cho mục đích trích dẫn tài liệu tham khảo (lấy từ tệp `_bibliography/references.bib`) hoặc xây dựng danh sách các ấn phẩm khoa học (list of publications) của tôi (lấy từ các tệp trong thư mục `_bibliography/publications`) sử dụng [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar) | 
| <span class="text-monospace">pub_style.csl</span>, <span class="text-monospace">springer-lncs.csl</span> | Các tệp cấu hình cách hiển thị các ấn phẩm và trích dẫn thông qua [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar) |
| <span class="text-monospace">publications.md</span> | Liệt kê các ấn phẩm (publications) và tiền ấn phẩm (preprints) của tôi thông qua [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar) (lấy thông tin từ các tệp trong thư mục `_bibliography/publications`) | 
| <span class="text-monospace">events.md</span> | Liệt kê các sự kiện (ví dụ như hội thảo, seminar, v.v...) mà tôi đã tham gia, cùng với một số tài liệu liên quan |
| <span class="text-monospace">pdf</span>, <span class="text-monospace">slides</span> | Các thư mục chứa các tài liệu dạng PDF (chủ yếu là các bản tiền ấn phẩm của tôi) và các tệp trình chiếu (Beamer, PowerPoint) |
| <span class="text-monospace">co-authors.md</span> | Danh sách các đồng tác giả (co-authors) của tôi |
| <span class="text-monospace">services.md</span> | Danh sách các vai trò (sub-reviewer, reviewer, v.v...) tôi đã đảm nhận |
| <span class="text-monospace">_latex-template</span> | Thư mục chứa các mô tả về các mẫu LaTeX tôi thường dùng. Thư mục này là một phần để xây dựng bộ sưu tập (collection) các mẫu LaTeX tôi thường dùng |
| <span class="text-monospace">latex-template</span> | Thư mục chứa các mẫu LaTeX tôi thường dùng. Thư mục này là một phần để xây dựng bộ sưu tập (collection) các mẫu LaTeX tôi thường dùng |
| <span class="text-monospace">latex-template.md</span> | Tệp liệt kê các mẫu trong bộ sưu tập (collection) các mẫu LaTeX tôi thường dùng |
| <span class="text-monospace">_courses</span> | Thư mục chứa các mô tả về một số môn học tôi tham gia giảng dạy hoặc trợ giảng | 
| <span class="text-monospace">courses</span> | Thư mục chứa các tài liệu liên quan đến một số môn học tôi tham gia giảng dạy hoặc trợ giảng | 
| <span class="text-monospace">teaching.md</span> | Liệt kê một số môn học tôi tham gia giảng dạy hoặc trợ giảng | 
| <span class="text-monospace">.travis.yml</span>, <span class="text-monospace">build.sh</span> | Cấu hình tự sinh trang cá nhân thông qua [Travis CI](https://travis-ci.org/) |
| <span class="text-monospace">keybase.txt</span> | Tệp này được sử dụng để kiểm chứng (verify) trang cá nhân thuộc sở hữu của tôi khi tôi đăng ký [tài khoản Keybase.io](https://keybase.io/username) |

</div>

## Boostrap + Font Awesome + Academicons + Solarized Dark Code Highlight

Trang cá nhân của tôi được xây dựng dựa trên nền tảng các thư viện HTML, CSS, và JS của [Bootstrap](https://getbootstrap.com/). Sử dụng các thư viện này giúp tôi tiết kiệm khá nhiều thời gian khi không phải tự tạo các thành phần và các hiệu ứng tôi cần. Tôi cũng sử dụng [Font Awesome](https://fontawesome.com/) và [Academicons](https://jpswalsh.github.io/academicons/) cho các icon trong trang cá nhân của mình, và sử dụng [Solarized Dark CSS Style](https://gist.github.com/nicolashery/5765395) (với một số chỉnh sửa nhỏ) để đánh dấu các đoạn mã.

## Tệp `_config.yml`

* Định nghĩa vai trò của một số thư mục
```yaml
# Where things are
source:       .
destination:  ./_site
plugins_dir:  ./_plugins
layouts_dir:  ./_layouts
includes_dir: ./_includes
```

* Định nghĩa phần đuôi của các tệp mã nguồn.
```yaml
# Handling Reading
markdown_ext: "markdown,mkdown,mkdn,mkd,md"
```

* Các plugin cần dùng.
```yaml
# Plugins
plugins: ['jekyll-sitemap','jekyll-feed','jekyll/scholar','pygments.rb','jekyll-email-protect','jekyll-last-modified-at']
```

* Một số cấu hình khác.
  ```yaml
  # Conversion
  markdown: kramdown
  highlighter: pygments

  # Markdown Processors
  kramdown:
    input: GFM
    syntax_highlighter: pygments
  
  # Serving
  port:    4000
  host:    127.0.0.1
  baseurl: "" # does not include hostname
  ```

* Thông tin cá nhân (sẽ sử dụng ở các phần sau).

* Thông thường, Jekyll sẽ bỏ qua các tệp và thư mục có tên bắt đầu bằng `_`. Đối với các thư mục khác, để Jekyll không sao chép các thư mục này khi xây dựng trang cá nhân, các bạn có thể thêm tên tệp/thư mục vào phần `exclude` trong tệp `_config.yml`, ví dụ như sau
```yaml
# Exclude file/folder
exclude: ['Gemfile*','Makefile','Curriculum Vitae','Business Card','*.bat','*.csl','exclude_copy*','gitlab-ci.yml','README*','LICENSE.txt','combinatorial-reconfiguration','Demo-LaTeXML','travis.yml','vendor','build.sh']
```
  Chú ý rằng việc thêm `vendor` vào mục `exclude` là cần thiết nếu bạn muốn làm việc với Travis CI.

* Liệt kê các collection.
```yaml
collections:
  posts:
    output: true
    permalink: "/misc/:categories/:year/:title/"
  courses:
    output: true
  latex-template:
    output: true
```

* Cấu hình [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar).
  ```yaml
  # Jekyll-scholar configuration
  scholar:
    style: springer-lncs
    locale: en
  
    sort_by: year
    order: asscending
    bibliography_list_tag: ol

    group_by: none
    group_order: ascending

    source: ./_bibliography
    bibliography: references.bib
    bibliography_template: bib

    replace_strings: true
    join_strings:    true
    
    reference_tagname: div

    use_raw_bibtex_entry: true
    bibtex_filters:
    - superscript
    - latex
  
    query: "@*"
  ```

## Thư mục `_includes`

### Tệp `head.html`

* Tất cả các phần sau đây được đặt giữa `<head>` và `</head>`.

* Phần đầu tiên
  ```html
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  ```
nhằm mục đích phục vụ tốt hơn việc hiển thị trang cá nhân trên các loại thiết bị và trình duyệt khác nhau.

* Tiếp đó là phần hiển thị tiêu đề trang và các thông tin cần thiết (meta data) để phục vụ việc truy xuất thông tin từ các bộ máy tìm kiếm như Google, Bing, Yahoo, DuckDuckGo, v.v... Ở đây tôi sử dụng Liquid Tag để phân biệt việc hiển thị thông tin trên trang chủ và trên các trang khác.
  
  ```html
  {% raw %}
  <title> {{ page.title }} </title>
  {% if page.url == "/" %}
  <meta name="description" content="{{ site.author }}'s personal webpage" />
  <meta name="author" content="{{ site.author }}" />
  <meta name="keywords" content="{{ site.keywords }}" />
  {% else %}
  {% if page.description %}
  <meta name="description" content="{{ page.description }}" />
  {% endif %}
  {% if page.author %}
  <meta name="author" content="{{ page.author }}" />
  {% endif %}
  {% if page.keywords %}
  <meta name="keywords" content="{{ page.keywords }}" />
  {% endif %}
  {% endif %}
  <meta name="generator" content="Jekyll {% include version.html %}, Bootstrap 4.1.1, Font Awsome, MathJax" />
  {% endraw %}
  ```
  
  Chú ý rằng các thông tin này sẽ được lấy từ phần nằm ngay đầu tiên của mỗi tệp nguồn (giữa hai dấu `---`) và có thể là cả từ tệp `_config.yml`. Một ví dụ từ tệp nguồn của bài viết này (`_posts/2018-11-24-xây-dựng-trang-cá-nhân-với-jekyll.md`) là:
```md
---
layout: blog-post
title: Xây dựng trang cá nhân với Jekyll
author: Duc A. Hoang
categories:
  - "jekyll"
  - "linux"
  - "windows"
comment: true
description: Bài viết này mô tả quá trình xây dựng trang cá nhân với Jekyll
keywords: trang cá nhân, jekyll, Duc A. Hoang
<!--published: false-->
---
```

  Trong ví dụ trên, bài viết này sẽ được sinh với layout `blog-post` (nằm ở `_layouts/blog-post.html`). Các thông tin meta data về tiêu đề (title), tác giả (author), mô tả (description), từ khóa (keywords) đều có thể được truy cập lần lượt thông qua Liquid Tag tương ứng `{% raw %}{{ page.title }}{% endraw %}`, `{% raw %}{{ page.author }}{% endraw %}`, `{% raw %}{{ page.description }}{% endraw %}`, `{% raw %}{{ page.keywords }}{% endraw %}`. Thông tin về thể loại (categories) được sử dụng khi liệt kê các bài viết (xem tệp `misc.html`). Để hiển thị hộp thoại comment cuối trang/bài viết, đặt `comment: true` (ngược lại, đặt `comment: false`, hoặc đặt `comment: true` giữa hai dấu `<!--` và `-->`). Tương tự như thế, nếu bạn không muốn hiển thị trang/bài viết (chẳng hạn do bạn chưa hoàn thành quá trình xây dựng trang/bài viết đó), thì bạn có thể đặt `published: false`. Chú ý rằng việc hiển thị bài viết hay không được cài đặt mặc định trong Jekyll, và bạn có thể sử dụng `published: false` hoặc `published: true` (mặc định) trong tất cả các trang/bài viết, trong khi phần hộp thoại comment thì do tôi cài đặt trong các layout tôi tự xây dựng.

* Dòng tiếp theo

  ```html
  <meta name="google-site-verification" content="kVN3FDkRoOErNs0auO3-jBDYtW4xzFqVGBCiugmymHM" />
  ```

  được sử dụng để kiểm tra (verify) rằng tôi là chủ của trang cá nhân khi tôi đăng ký với [Google Search Console](https://support.google.com/webmasters/answer/6332964?hl=en&ref_topic=4564315). Các bạn có thể bỏ dòng này đi.

* Tiếp theo đó là phần khai báo các thư viện JS và CSS cần thiết. Một phần không thể thiếu là sử dụng [MathJax](https://www.mathjax.org/) để hiển thị các công thức toán.

  ```html
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>

  <!-- Fonts -->
  <!--	<link href="https://fonts.googleapis.com/css?family=Cousine|Nunito" rel="stylesheet">-->

  <!-- Personal CSS configuration -->
  <link rel="stylesheet" href="{{ site.baseurl }}/static/css/custom.css">

  <!-- MathJax -->
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  <script type="text/x-mathjax-config">
	  MathJax.Hub.Config({
	  tex2jax: {
	  inlineMath: [['$','$'], ['\\(','\\)']],
	  processEscapes: true
	  }
	  });
  </script>

  <!-- Enable Popover -->
  <script>
  $(function () {
  $('[data-toggle="popover"]').popover()
  })
  </script>

  <!-- Enable Tooltips -->
  <script>
  $(function () {
  $('[data-toggle="tooltip"]').tooltip()
  })
  </script>
  ```

  Chú ý rằng phần sử dụng Popover và Tooltip chỉ hoạt động nếu các bạn sử dụng các thư viện của [Bootstrap](https://getbootstrap.com/). Việc khai báo `jquery-3.3.1.slim.min.js` trước `bootstrap.min.js` cũng là cần thiết để tránh một số xung đột giữa hai thư viện. Tất cả các cấu hình liên quan đến CSS đều nằm trong tệp `static/css/custom.css`.

* Phần

  ```html
  <!-- Favicon -->
  <link rel="shortcut icon" href="{{ site.baseurl }}/static/img/Duc.ico" type='image/x-icon'>

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->    
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
  ```

  được sử dụng để hiện thị favicon (ở đây tôi sử dụng tệp `static/img/Duc.ico`) và cấu hình khi xem trang cá nhân với trình duyệt Internet Explorer.

* Phần cuối 

  ```html
  {% raw %}
  {% feed_meta %}
  {% endraw %}
  ```

  được sử dụng bởi plugin `jekyll-feed` để sinh tệp RSS feed `feed.xml` cho các bài viết (blog posts).

### Tệp `header.html`

* Tất cả các phần sau đây được đặt giữa `<header>` và `</header>`.

* Phần 

  ```html
  {% raw %}
  <nav class="navbar-expand-lg navbar-light fixed-top">
  <div class="container">
	  <!-- Brand and toggle get grouped for better mobile display -->
  <!--	<a class="navbar-brand" href="#">Navbar</a>-->
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
	  <span class="navbar-toggler-icon"></span>
  	  </button>
	
	  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	  <ul class="navbar-nav mr-auto">
	  {% for nav in site.data.navbar %}
	  {% if nav.sub-item != null %}
	  <li class="nav-item dropdown">
		  <a class="nav-link dropdown-toggle" href="{{ nav.href }}" id="navbarDropdown{{ nav.title | replace:' ','' }}" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
		  <i class="{{ nav.fa-icon }}" aria-hidden="true"></i> {{ nav.title }}
		  </a>
		  <div class="dropdown-menu" aria-labelledby="navbarDropdown{{ nav.title | replace:' ','' }}">
		  {% for item in nav.sub-item %}
		  <a class="dropdown-item" href="{{ item.sub-href }}"><i class="{{ item.sub-fa-icon }}" aria-hidden="true"></i> {{ item.sub-title }}</a>
		  {% endfor %}
		  </div>
	  </li>
	  {% else %}
		  {% if page.url == nav.href %}
		  <li class="nav-item active"><a class="nav-link" href="{{ nav.href }}"><i class="{{ nav.fa-icon }}" aria-hidden="true"></i> {{ nav.title }}</a></li>
		  {% else %}
		  <li class="nav-item"><a class="nav-link" href="{{ nav.href }}"><i class="{{ nav.fa-icon }}" aria-hidden="true"></i> {{ nav.title }}</a></li>
		  {% endif %}
	  {% endif %}
	  {% endfor %}
	  </ul>
  <!--	  <ul class="navbar-nav">-->
  <!--	  <li class="nav-item"><a class="nav-link" href="https://github.com/username/username.github.io/tree/source" data-toggle="tooltip" data-placement="bottom" title="Source"><i class="fas fa-download"></i></a></li>-->
  <!--	  <li class="nav-item"><a class="nav-link" href="{{ site.baseurl }}/feed.xml" data-toggle="tooltip" data-placement="bottom" title="Blog RSS Feed"><i class="fas fa-rss-square"></i></a></li>-->
  <!--	  <li class="nav-item"><a class="nav-link" href="{{ site.baseurl }}/sitemap.xml" data-toggle="tooltip" data-placement="bottom" title="Sitemap"><i class="fas fa-sitemap"></i></a></li>-->
  <!--	  </ul>-->
	  </div>
  </div>
  </nav> 
  {% endraw %}
  ```

  được sử dụng để xây dựng navigation bar với các thư viện của [Bootstrap](https://getbootstrap.com/) và các icon từ [Font Awesome](https://fontawesome.com/). Các dữ liệu cần thiết được lấy từ `_data/navbar.yml` thông qua `site.data.navbar`. Ví dụ tệp `_data/navbar.yml` của tôi chứa các dữ liệu như sau

  ```yaml
  - title: "Home"
    fa-icon: "fa fa-home"
    href: "/"
  - title: "Research"
    fa-icon: "fa fa-folder"
    href: "#"
    sub-item:
      - sub-title: "PhD Thesis (2018-06)"
        sub-fa-icon: "fa fa-file-pdf"
        sub-href: "http://hdl.handle.net/10119/15431"
      - sub-title: "Publications"
        sub-fa-icon: "fa fa-book"
        sub-href: "/publications/"
      - sub-title: "Co-authors"
        sub-fa-icon: "fa fa-group"
        sub-href: "/co-authors/"
      - sub-title: "Participated Events"
        sub-fa-icon: "fa fa-calendar"
        sub-href: "/events/"
      - sub-title: "Professional Services"
        sub-fa-icon: "fa fa-pencil-square"
        sub-href: "/services/"
      - sub-title: "Reconfiguration Bibliography"
        sub-fa-icon: "fa fa-list"
        sub-href: "/combinatorial-reconfiguration/"
  - title: "Teaching"
    fa-icon: "fa fa-graduation-cap"
    href: "/teaching/"
  - title: "Misc"
    fa-icon: "fa fa-box-open"
    href: "/misc/"
  ```

### Tệp `author-info.html`

Tệp này được sử dụng để cài đặt việc hiển thị các thông tin cơ bản được lấy từ trong tệp `_config.yml` của tôi.

(Một phần) tệp <code>_config.yml</code>

```yaml
# Personal information
url: http://hoanganhduc.github.io
author: Duc A. Hoang
title: Welcome to Đức's personal webpage!
auth_current_position:
email_personal_user: anhduc.hoang1990
email_personal_domain: gmail.com
email_work_user: hoanganhduc
email_work_domain: jaist.ac.jp
website: hoanganhduc.github.io
website_full: http://hoanganhduc.github.io
keywords: Duc A. Hoang, JAIST, anhduc.hoang1990, hoanganhduc, personal webpage
orcid: 0000-0002-8635-8462
institute_address: Japan Advanced Institute of Science and Technology, 1-1 Asahidai, Nomi, Ishikawa, 923-1292 Japan
```

Việc lấy từng thông tin tương ứng, ví dụ như `url`, được thực hiện thông qua Liquid Tag <code>{% raw %}{{ site.url }}{% endraw %}</code>. Nội dung của tệp <code>_includes/author-info.html</code> 

```html
{% raw %}
<div class="row">
<div class="text-center col-xs-12 col-sm-3 col md-3 col-lg-3">
<img src="{{ site.baseurl }}/static/img/Duc.jpg" class="img-thumbnail" alt="" title="Duc A. Hoang" style="width:190px;">
</div>
<div class="col-xs-12 col-sm-9 col-md-9 col-lg-9" style="margin-top:0px;">
<h2>{{ site.auth_current_position }}</h2>
<p>
 <i class="fa fa-envelope" aria-hidden="true"></i> 
  <a href="mailto:{{ site.email_work_user | append:'@' | append: site.email_work_domain | encode_email }}">  
 {{ site.email_work_user }}<i class="fa fa-at"></i>{{ site.email_work_domain }}</a>.  
<br /><i class="fa fa-envelope" aria-hidden="true"></i>
 <a href="mailto:{{ site.email_personal_user | append:'@' | append: site.email_personal_domain | encode_email }}">
{{ site.email_personal_user }}<i class="fa fa-at"></i>{{ site.email_personal_domain }}</a>.
</p>
<p>
<i class="fa fa-globe" aria-hidden="true"></i> <a href="{{ site.website_full }}">{{ site.website }}</a>.
</p>
 <address> 
 <i class="fa fa-institution" aria-hidden="true"></i> {{ site.institute_address }}. 
 </address> 
<p>
<i class="fa fa-file-pdf-o" aria-hidden="true"></i> Duc A. Hoang's Curriculum Vitae [<a href="{{ site.baseurl }}/CV.pdf">English</a>] [<a href="{{ site.baseurl }}/CV-vi.pdf">Tiếng Việt</a>].
</p>
<p>
<i class="ai ai-orcid" aria-hidden="true"></i> <a href="https://orcid.org/{{ site.orcid }}" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;">orcid.org/{{ site.orcid }}</a>.
</p>
</div>

</div>
{% endraw %}
```

Chú ý rằng ở đây tôi sử dụng [Boostrap Grid System](https://getbootstrap.com/docs/4.1/layout/grid/). Nếu bạn không sử dụng Boostrap thì việc hiển thị trang cá nhân của bạn có thể không giống với trang cá nhân của tôi.

### Tệp `news.html`

Tệp này được sử dụng để hiển thị các tin tức tôi muốn. Ở đây tôi sử dụng [Bootstrap List Group](https://getbootstrap.com/docs/4.1/components/list-group/) để hiển thị từng thông tin. Các thông tin cần thiết được lấy từ `_data/news.yml`. 
Nội dung của <code>_includes/news.html</code> 

```html
{% raw %}
<ul class="list-group" style="height:250px; overflow:auto; overflow-y:scroll;">
{% for new in site.data.news %}
{% case new.pub-type %}
  {% when "conference" %}
  <li class="list-group-item list-group-item-secondary">
  {% when "journal" %}
  <li class="list-group-item list-group-item-success">
  {% when "award" %}
  <li class="list-group-item list-group-item-primary">
  {% when "info" %}
  <li class="list-group-item list-group-item-info">
{% endcase %}
  <strong>{{ new.time }}: </strong> {{ new.text }}
  </li>
{% endfor %}
</ul>
<br />
{% endraw %}
```
và <code>_data/news.yml</code>

```yaml
- time: "July 17, 2018"
  text: "A list of some publications related to \"Combinatorial Reconfiguration\" is <a href='https://hoanganhduc.github.io/combinatorial-reconfiguration/'>available online</a>. Prior to this date, it was hosted at <a href='http://www.jaist.ac.jp/~s1520016/combinatorial-reconfiguration/'>my personal webpage at JAIST</a>."
  pub-type: "info"
- time: "June 22, 2018"
  text: "Awarded JAIST <a href='http://www.jaist.ac.jp/english/education/degree/awards.html' data-toggle='tooltip' data-placement='top' title='The outstanding performance award will be granted to the students who complete the master’s/doctoral program with excellent academic performance'>Outstanding Performance Award</a> for doctoral students."
  pub-type: "award"
- time: "May 07, 2018"
  text: "Completed PhD final defense at JAIST. Download my presentation slide <a href='/events/PhD-Thesis-Defense/Duc_FinalDefense_20180507.pdf'>here</a> (or <a href='/events/PhD-Thesis-Defense/Duc_FinalDefense_20180507_handout.pdf'>here</a> for a compressed version with unnecessary animation removed)."
  pub-type: "info"
- time: "March 14, 2018"
  text: "Mariana Teatini Ribeiro and <a href='http://homepages.dcc.ufmg.br/%7eviniciussantos/'>Vinícius Fernandes dos Santos</a> informed us about a flaw in the proof of Proposition 6 of our paper \"Sliding Tokens on Block Graphs\"."
  pub-type: "info"
- time: "December 04, 2016"
  text: "A manuscript entitled \"Sliding Tokens on Block Graphs\" has been accepted to <a href='http://walcom2017.nctu.edu.tw/' data-toggle='tooltip' data-placement='top' title='The 11th International Conference and Workshops on Algorithms and Computation, Hsinchu, Taiwan, March 29-31, 2017'>WALCOM 2017</a> (joint work with Eli Fox-Epstein and Ryuhei Uehara)."
  pub-type: "conference"
- time: "August 31, 2016"
  text: "A manuscript entitled \"Sliding Tokens on a Cactus\" has been accepted to <a href='http://rp-www.cs.usyd.edu.au/~visual/isaac2016/' data-toggle='tooltip' data-placement='top' title='The 27th International Symposium on Algorithms and Computation, Sydney, Australia, December 12-14, 2016'>ISAAC 2016</a> (joint work with Ryuhei Uehara)."
  pub-type: "conference"
- time: "August 31, 2015"
  text: "A manuscript entitled \"Sliding Token on Bipartite Permutation Graphs\" has been accepted to <a href='http://www.al.cm.is.nagoya-u.ac.jp/isaac2015/' data-toggle='tooltip' data-placement='top' title='The 26th International Symposium on Algorithms and Computation, Nagoya, Japan, December 9-11, 2015'>ISAAC 2015</a> (joint work with Eli Fox-Epstein, Yota Otachi, and Ryuhei Uehara)."
  pub-type: "conference"
- time: "July 16, 2015"
  text: "A manuscript entitled \"Linear-Time Algorithm for Sliding Tokens on Trees\" has been accepted to <a href='http://www.journals.elsevier.com/theoretical-computer-science/' data-toggle='tooltip' data-placement='top' title='Theoretical Computer Science'>Theoretical Computer Science</a> (joint work with Erik D. Demaine, Martin L. Demaine, Eli Fox-Epstein, Takehiro Ito, Hirotaka Ono, Yota Otachi, Ryuhei Uehara, and Takeshi Yamada)."
  pub-type: "journal"
- time: "March 20, 2015"
  text: "Awarded JAIST <a href='http://www.jaist.ac.jp/english/education/degree/awards.html' data-toggle='tooltip' data-placement='top' title='The outstanding performance award will be granted to the students who complete the master’s/doctoral program with excellent academic performance'>Outstanding Performance Award</a> for master’s students."
  pub-type: "award"
- time: "August 29, 2014"
  text: "A manuscript entitled \"Polynomial-Time Algorithm for Sliding Tokens on Trees\" has been accepted to <a href='http://tcs.postech.ac.kr/isaac2014/' data-toggle='tooltip' data-placement='top' title='The 25th International Symposium on Algorithms and Computation, Jeonju, Korea, December 15-17, 2014'>ISAAC 2014</a> (joint work with Erik D. Demaine, Martin L. Demaine, Eli Fox-Epstein, Takehiro Ito, Hirotaka Ono, Yota Otachi, Ryuhei Uehara, and Takeshi Yamada)."
  pub-type: "conference"  
```

### Tệp `disqus.html` và `intensedebate.html`

Các tệp này sử dụng để cấu hình các hộp thoại comment từ [Disqus](https://disqus.com/) và [IntenseDebate](https://www.intensedebate.com/). Tôi trước kia sử dụng Disqus nhưng sau đó chuyển sang IntenseDebate do IntenseDebate [có hỗ trợ comment và hiển thị các công thức toán học](https://gist.github.com/christianp/6376614) (mặc dù vẫn có lỗi và bạn thường phải refresh trang/bài viết để hiển thị đúng). Việc sử dụng các công cụ này khá đơn giản. Bạn chỉ cần đăng ký tài khoản và chèn đoạn mã HTML họ cung cấp vào các trang/bài viết bạn muốn. Ở đây tôi chèn các đoạn mã này vào các tệp tương ứng, và chèn vào các trang/bài viết thông qua Liquid Tag, ví dụ như 

```html
{% raw %}
{% if page.comment %}
{% include intensedebate.html %} 
{% endif %} 
{% endraw %}
```

### Tệp `files.html` và `image.html`

Tệp `files.html` được sử dụng để chèn các đường dẫn đến các tệp và thư mục con của thư mục `static/files/posts/name-of-blog-post`, với `name-of-blog-post` là một phần tên bài viết bạn đặt (chú ý là mỗi bài viết có mã nguồn với tên dạng `YYYY-MM-DD-name-of-blog-post.md`). Ví dụ nếu sử dụng đoạn mã <code>{% raw %}{% include files.html name="your-file.pdf" text="your file" %}{% endraw %}</code> trong bài viết này thì nó sẽ chèn đường dẫn đến tệp `static/files/posts/xây-dựng-trang-cá-nhân-với-jekyll/your-file.pdf`, cụ thể như {% include files.html name="your-file.pdf" text="your-file" %}.

Tương tự như `files.html`, tệp `image.html` được sử dụng để chèn các tệp hình ảnh của thư mục `static/img/posts/name-of-blog-post`, với `name-of-blog-post` là một phần tên bài viết bạn đặt. Một ví dụ về sử dụng `image.html` là <code>{% raw %} {% include image.html name=your-figure.png" caption="This is the caption for your figure" width="70%" %} {% endraw %}</code>.

### Tệp `footer.html`

Chứa các thông tin ở phần cuối của trang/bài viết. 
Ví dụ, nội dung của <code>_includes/footer.html</code> 

```html
{% raw %}
<footer class="footer text-right">
	<span class="text-muted credit">
		<a href="#" class="back-to-top" style="display: inline; text-decoration:none;">
		Back to Top <i class="fa fa-arrow-circle-up"></i>
		</a>
		<br />Last Modified: {{ site.time | date: '%B %-d, %Y' }}
		<br />The content on this site is shared under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0 license</a>, unless otherwise noted
	</span>
</footer>
{% endraw %}
```

### Tệp `search-form.html`

Chứa search form để tìm kiếm trong nội dung của các bài viết.

Ví dụ, nội dung tệp <code>_includes/search-form.html</code> 

```html
{% raw %}
<form action="/search/index.html" method="get">
<div class="form-group">
<div class="row">
<div class="col-xs-12 col-sm-8 col-md-8 col-lg-8">
<input type="text" class="form-control form-control-lg" id="search-box" name="query" placeholder="type any keyword here">
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
<input type="submit" role="button" class="btn btn-lg btn-primary" value="search all posts">
</div>
</div>
</form>
<br />
{% endraw %}
```

## Thư mục `_layouts`

Chứa các layout định sẵn cho từng trang/bài viết. 

### Tệp `blog-post.html`, `page.html`, `post.html`, `collection_main.html`, và `collection_item.html`

Một ví dụ về việc xây dựng layout như trong tệp <code>_layouts/blog-post.html</code> của tôi như sau
```html
{% raw %}
<!DOCTYPE html>
<html lang="en">

{% include head.html %}

<body>

<div class="container">
{% include header.html %}
<div class="row">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
<h1 class="display-4">{{ page.title }}</h1>
<h5 class="text-monospace">
{% if page.author %}
<i class="fas fa-user"></i> {{ page.author }}
{% endif %}
<i class="fas fa-user-clock"></i> {{ page.date | date_to_string }}
<i class="fas fa-user-edit"></i> {{ page.last_modified_at | date_to_string }} 
{% if page.categories %}
<i class="fas fa-user-tag"></i> {{ page.categories | join: ', ' }}
{% endif %}
</h5>
<hr>
{{ content }}

{% if page.comment %}
{% include intensedebate.html %} 
{% endif %} 

<hr>

{% include footer.html %}
	
</div>
</div>
</div>

</body>
</html>
{% endraw %}
```

Hoàn toàn tương tự, bạn có thể xây dựng các layout khác (`_layouts/page.html`, `_layouts/post.html`, `_layouts/collection_main.html`, `_layouts/collection_item.html`) bằng cách thêm hoặc bớt các phần không cần thiết, hoặc là tạo các tệp mới trong thư mục `_includes` và thêm vào layout, hoặc thêm trực tiếp các đoạn mã HTML vào layout.

### Tệp `pub_style.html` và `bib.html`

Một dạng layout đặc biệt là layout sử dụng để liệt kê các ấn phẩm (publications) của tôi. Layout này được xây dựng trong tệp `_layouts/pub_style.html` như sau.

```html
{% raw %}
---
---

{{ reference }}

{% if entry.note %}
<p><span style="color:#ff0000">Note:</span> {{ entry.note }}</p>
{% endif %}

<p>
{% if entry.abstract %}
<a class="btn-lg my-btn-link" data-toggle="collapse" href="#{{ key }}-abstract"> Abstract </a>
{% endif %}
{% if entry.doi %}
<a class="btn-lg my-btn-link" href="{{ entry.doi | prepend: 'http://dx.doi.org/'}}" data-toggle="tooltip" title="{{ entry.doi | prepend: 'doi:'}}">DOI</a>
{% endif %}
{% if entry.eprint %}
<a class="btn-lg my-btn-link" href="{{ entry.eprint | prepend: 'https://arxiv.org/abs/'}}" data-toggle="tooltip" title="{{ entry.eprint | prepend: 'arXiv:'}}">ArXiv</a>
{% endif %}
{% if entry.hdl %}
<a class="btn-lg my-btn-link" href="{{ entry.hdl | prepend: 'http://hdl.handle.net/'}}" data-toggle="tooltip" title="{{ entry.hdl | prepend: 'hdl:'}}">HDL</a>
{% endif %}
{% if entry.slide %}
<a class="btn-lg my-btn-link" href="{{ site.baseurl }}/events/{{ entry.slide }}">
Slide 
</a>
{% endif %}
{% if entry.pdf %}
<a class="btn-lg my-btn-link" href="{{ site.baseurl }}/pdf/{{ entry.pdf }}">
PDF 
</a>
{% endif %}
</p> 
{% if entry.abstract %}
<p id="{{ key }}-abstract" class="collapse text-muted">
	{{ entry.abstract }}
</p>
{% endif %}

{% endraw %}
```

Tương tự, bạn có thể xây dựng layout để hiển thị các tài liệu tham khảo khi trích dẫn chúng trong một bài viết như ở tệp <code>_layouts/bib.html</code> sau.

```html
{% raw %}

---
---

{{reference}}

<span>
{% if entry.doi %}
<span><a href="{{ entry.doi | prepend: 'https://doi.org/' }}">{{entry.doi | prepend: 'doi:'}}</a>.</span>
{% endif %}
{% if entry.eprint %}
<span><a href="{{ entry.eprint | prepend: 'https://arxiv.org/abs/' }}">{{entry.eprint | prepend: 'arXiv:'}}</a>.</span>
{% endif %}
{% if entry.hdl %}
<span><a href="{{ entry.hdl | prepend: 'http://hdl.handle.net/' }}">{{entry.hdl | prepend: 'hdl:'}}</a>.</span>
{% endif %}
{% if entry.hal_id %}
<span><a href="{{ entry.hal_id | prepend: 'http://hal.inria.fr/' }}">{{entry.hal_id | prepend: 'hal:'}}</a>.</span>
{% endif %}
</span>

{% endraw %}
```

### Tệp `search.html`

Một layout khác là layout được sử dụng để hiển thị kết quả tìm kiếm nội dung các bài viết, ví dụ như ở tệp <code>_layouts/search.html</code>

```html
{% raw %}

---
layout: page
---
<div class="search">
	{{ content }}
</div>

{% endraw %}
```

## Tệp `misc.html` -- Liệt kê danh sách các bài viết

Một phần quan trọng trong tệp này là phần liệt kê các bài viết theo thể loại.

```html
{% raw %}

{% for category in site.categories %}
  <h3 id="{{ category[0] }}"><i class="fas fa-user-tag"></i> {{ category[0] }} ({{ category[1].size }})</h3>
  <ul>
    {% assign pages_list = category[1] %}
    {% for post in pages_list %}
      {% if post.title != null %}
      {% if group == null or group == post.group %}
      <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a> <time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished" class="text-muted">({{ post.date | date: "%B %d, %Y" }})</time></li>
      {% endif %}
      {% endif %}
    {% endfor %}
    {% assign pages_list = nil %}
    {% assign group = nil %}
  </ul>
{% endfor %}

{% endraw %}
```

## Tệp `publications.md` -- Liệt kê danh sách các ấn phẩm (publications)

Ví dụ, để liệt kê danh sách các tiền ấn phẩm (preprints), tôi làm như sau:

```html
{% raw %}

<div class="publication">

{% bibliography --template pub_style --style pub_style --file publications/preprints.bib %}

</div>

{% endraw %}
```

Tên tệp `pub_style` sau `--template` là để chỉ tệp `_layouts/pub_style.html`, còn tên tệp `pub_style` sau `--style` là để chỉ tệp `pub_style.csl`.
Tất cả các tiền ấn phẩm của tôi được liệt kê trong tệp `_bibliography/publications/preprints.bib`.
Bạn có thể làm hoàn toàn tương tự với các phần khác.

## Tệp `latex-template.md` -- Liệt kê các phần tử trong một collection

Để liệt kê các LaTeX template tôi thường dùng, tôi làm như sau (trong tệp `latex-template.md`)


```html
{% raw %}

<div class="table-responsive">
<table class="table table-striped table-bordered">
<thead>
<tr>
	<th>Template</th>
	<th>Type</th>
</tr>
</thead>
<tbody>
{% assign latex-template = site.latex-template | sort: 'date' | reverse %}
{% for template in latex-template %}
<tr>
	<td><a href="{{ template.url }}">{{ template.title }}</a></td>
	<td>{{ template.type }}</td>
</tr>
{% endfor %}
</tbody>
</table>

{% endraw %}
```

# Sinh (generate) trang cá nhân với Jekyll và host trang cá nhân với GitHub

* Sinh trang cá nhân từ mã nguồn đã tạo.

  ```bash
  bundle exec jekyll build --config _config.yml
  ```

  Bạn cũng có thể sử dụng lệnh `bundle exec jekyll serve` và truy cập tới địa chỉ [http://localhost:4000](http://localhost:4000) để kiểm tra nội dung trang cá nhân trước khi tiến hành các bước tiếp theo.

* Đồng bộ mã nguồn với thư mục `$HOME/username.github.io/source` và commit nội dung lên branch `source` của GitHub repository `username.github.io`. Ở đây, tôi sử dụng [rsync](https://wiki.archlinux.org/index.php/rsync).

  ```bash
  rsync -arv --exclude-from exclude_copy.txt . $HOME/username.github.io/source
  cd $HOME/username.github.io/source
  git add --all .
  git commit -S -m "Source Files @ $(date +'%Y-%m-%d  %H:%M:%S')"
  git push -u origin source
  ```

Ở đây, tệp `exclude_copy.txt` chứa các thư mục và tệp tôi không muốn commit lên branch `source` (bao gồm chính bản thân tệp đó, do đó bạn sẽ không tìm được tệp này trong mã nguồn của trang cá nhân của tôi).

* Đồng bộ nội dung trang cá nhân với thư mục `$HOME/username.github.io/master` và commit nội dung lên branch `master` của GitHub repository `username.github.io`. Ở đây, tôi sử dụng [rsync](https://wiki.archlinux.org/index.php/rsync) và [tree](https://www.archlinux.org/packages/extra/x86_64/tree/).

  ```bash
  rsync -arv --exclude "README*" --exclude "LICENSE.txt" ./_site/* $HOME/username.github.io/master
  cd $HOME/username.github.io/master
  tree -H '.' --noreport --charset utf-8 -h -D -T "HTML Sitemap" -I "*.html" --timefmt "%b %d, %Y %H:%M" -t > sitemap.html
  git add --all .
  git commit -S -m "Local Build @ $(date +'%Y-%m-%d  %H:%M:%S')"
  git push -u origin master
  ```

# Cài đặt quá trình tự động với Travis CI

* Tạo tệp `.travis.yml` có nội dung như sau:

  ```bash
  dist: xenial
  language: ruby
  rvm:
    - 2.5
  addons:
    apt:
      packages:
      - libcurl4-openssl-dev
      - tree
  sudo: false # route your build to the container-based infrastructure for a faster build
  cache: bundler
  before_script:
   - "chmod +x build.sh" # or do this locally and commit
   - "gem install bundler"
   - "bundle install"
   - "git config --global user.name 'your-username'"
   - "git config --global user.email 'your_email@example.com'"
  script:
  - "./build.sh"
  ```

* Tạo tệp `build.sh` có nội dung như sau.

  ```bash
  #! /bin/bash

  set -e

  DEPLOY_REPO="https://${DEPLOY_BLOG_TOKEN}@github.com/username/username.github.io.git"

  function clone_source_repo () {
	  git clone https://${DEPLOY_BLOG_TOKEN}@github.com/username/username.github.io.git site
  }

  function build_jekyll_site () {
	  bundle exec jekyll build --config _config.yml
  }

  function deploy () {
	  rsync -arv --exclude "README*" --exclude "site" ./_site/* site
	  cd site
	  tree -H '.' --noreport --charset utf-8 -h -D -T "HTML Sitemap" -I "*.html" --timefmt "%b %d, %Y %H:%M" -t > sitemap.html
	  git add --all .
	  git commit -m "Travis CI Build $TRAVIS_BUILD_NUMBER @ $(TZ=':Asia/Ho_Chi_Minh' date +'%Y-%m-%d  %H:%M:%S')"
	  git push -u origin master
	  cd ..
  }

  function clean () {
	  rm -rf *
  }

  main () {
	  build_jekyll_site
	  clone_source_repo
	  deploy
	  clean
  }

  main "$@"
  ```

  trong đó `DEPLOY_BLOG_TOKEN` là một khóa bí mật được thêm vào Travis CI. Khóa này được tạo từ GitHub bằng cách đăng nhập, và sau đó truy cập tới địa chỉ [https://github.com/settings/tokens](https://github.com/settings/tokens) và chọn `Generate new token`. Trong phần `Select scopes`, đánh dấu chọn mục `repo` và tất cả các mục con của nó. Sao chép lại token được sinh ra và thêm vào Travis CI bằng cách đăng nhập Travis CI với GitHub, truy cập tới địa chỉ [https://travis-ci.org/username/username.github.io/settings](https://travis-ci.org/username/username.github.io/settings), và thêm vào mục `Environment Variables` một khóa với tên (Name) là `DEPLOY_BLOG_TOKEN` và giá trị (Value) là token đã sao chép từ GitHub. Chú ý rằng để Travis CI tự động sinh trang cá nhân mỗi khi có commit từ branch `source`, trước hết bạn cần khởi động repository bằng cách truy cập tới địa chỉ [https://travis-ci.org/username/username.github.io/settings](https://travis-ci.org/username/username.github.io/settings), chọn mục `Current`, và nhấn vào nút `Activate repository` ở cuối dòng thông báo `This is not an active repository`.

# Sign commit với PGP secret key trong Travis CI

Tôi muốn sign mỗi commit từ Travis CI với [PGP public key của tôi](https://keybase.io/hoanganhduc). Để thực hiện điều này, tôi làm các bước sau:

* Bỏ passphrase từ  secret key sử dụng gói [gnupg1](https://aur.archlinux.org/packages/gnupg1/) trong Arch Linux. Xem chi tiết hướng dẫn [ở đây]({% post_url 2018-05-26-some-notes-on-installing-and-using-arch-linux %}#gnupg). Giả sử kết quả của quá trình này là một tệp tên `PGP-key.asc`.
* [Mã hóa](https://docs.travis-ci.com/user/encrypting-files) `PGP-key.asc` với [Travis CI CLI](https://github.com/travis-ci/travis.rb#readme).

  ```bash
  travis encrypt-file PGP-key.asc -r username/username.github.io
  ```

  trong đó `username` là tên đăng nhập tài khoản GitHub của bạn. Kết quả thu được có dạng như sau:

  ```bash
  encrypting PGP-key.asc for username/username.github.io
  storing result as PGP-key.asc.enc
  storing secure env variables for decryption

  Please add the following to your build script (before_install stage in your .travis.yml, for instance):

      openssl aes-256-cbc -K $encrypted_0a6446eb3ae3_key -iv $encrypted_0a6446eb3ae3_iv -in PGP-key.asc.enc -out PGP-key.asc -d

  Pro Tip: You can add it automatically by running with --add.

  Make sure to add PGP-key.asc.enc to the git repository.
  Make sure not to add PGP-key.asc to the git repository.
  Commit all changes to your .travis.yml.

  ```

  Sau khi thu được tệp đã mã hóa `PGP-key.asc.enc`, bạn có thể sao chép tệp này vào GitHub repository. Chú ý rằng **không sao chép tệp `PGP-key.asc` vào GitHub repository**. Trong quá trình mã hóa, bạn cũng sẽ thu được một thông báo yêu cầu bạn thêm dòng có dạng 

  ```bash
  openssl aes-256-cbc -K $encrypted_0a6446eb3ae3_key -iv $encrypted_0a6446eb3ae3_iv -in PGP-key.asc.enc -out PGP-key.asc -d
  ```

  vào `before_install` stage của `.travis.yml` để giải mã `PGP-key.asc.enc`. Tóm lại, tệp `.travis.yml` mới sẽ có dạng như sau

  ```yaml
  dist: xenial
  language: ruby
  rvm:
    - 2.5
  addons:
    apt:
      packages:
      - libcurl4-openssl-dev
      - tree
  sudo: false # route your build to the container-based infrastructure for a faster build
  cache: bundler
  before_script:
   - "chmod +x build.sh" # or do this locally and commit
   - "gem install bundler"
   - "bundle install"
   - openssl aes-256-cbc -K $encrypted_0a6446eb3ae3_key -iv $encrypted_0a6446eb3ae3_iv -in PGP-key.asc.enc -out PGP-key.asc -d
   - gpg2 --import PGP-key.asc
   - "git config --global user.name 'your-username'"
   - "git config --global user.email 'your_email@example.com'"
   - git config --global gpg.program gpg2
   - git config --global user.signingkey [your-PGP-key-fingerprint]
  script:
  - "./build.sh"
  ```
  
**Chú ý:** Nếu bạn muốn biết giá trị cụ thể của các khóa bí mật `encrypted_0a6446eb3ae3_key` và `encrypted_0a6446eb3ae3_iv` từ Travis CI, bạn có thể làm như sau: (Xem hướng dẫn gốc tại [đây](https://www.topcoder.com/recover-lost-travisci-variables-two-ways/).)

* Tạo một khóa bí mật mới `ENC_KEY` trong Travis CI tương tự như với `DEPLOY_BLOG_TOKEN`.

* Sửa `.travis.yml` như sau: (các phần không cần thay đổi được biểu thị bằng dấu `...`)

  ```yaml
  ...
  sudo: required
  cache: bundler
  before_script:
   - sudo apt-get install -y ccrypt
   - echo "encrypted_0a6446eb3ae3_key = $encrypted_0a6446eb3ae3_key" >> info.txt
   - echo "encrypted_0a6446eb3ae3_iv = $encrypted_0a6446eb3ae3_iv" >> info.txt
   - ccencrypt info.txt -K $ENC_KEY
   - curl --upload-file info.txt.cpt https://transfer.sh/info.txt.cpt
   - srm info.txt
   - "chmod +x build.sh" # or do this locally and commit
  ...
  ```

* Sau khi commit tệp `.travis.yml` và chạy với Travis CI, bạn xem raw log để tìm được link của tệp `info.txt.cpt` đã tải lên [transfer.sh](https://transfer.sh/).

* Để giải mã `info.txt.cpt`, cài `ccrypt` và dùng lệnh `ccrypt -d info.txt.cpt -K $ENC_KEY`.

# Cài đặt quá trình tự động với GitHub Actions

Tôi tham khảo phần lớn quá trình từ [trang này](https://bpaulino.com/entries/10-automating-your-work-with-github-actions). 
Cụ thể, tôi muốn cài đặt [GitHub Actions](https://github.com/features/actions) để thực hiện các thao tác tương tự như đã thực hiện với Travis CI: cài đặt các gói cần thiết trong Ubuntu để tạo môi trường làm việc, clone branch `source`, sử dụng Jekyll để sinh các tệp HTML, và cập nhật branch `master` với các tệp đã sinh.
Để thực hiện việc này, tôi tạo thư mục `.github` với hai thư mục con `workflows` và `actions`, trong đó thư mục `workflows` chứa tệp `deploy-workflow.yml` với miêu tả về các nhiệm vụ cần làm, và thư mục `actions` chứa các tệp cụ thể phục vụ cho quá trình đã miêu tả.
Tệp `.github/workflow/deploy-workflow.yml` của tôi có nội dung như sau

```
{% raw %}
# Original: https://bpaulino.com/entries/10-automating-your-work-with-github-actions

# This is the name of our workflow.
# Github will show it on its Website UI
name: gh-pages
# This configures our workflow to be triggered
# only when we push to the source branch
on:
  push:
    branches:
      - source

# Here is where we define our jobs. 
# Which means the tasks we want Github to execute
jobs:
  build:
    name: gh-pages
    # Here we specify in whith OS we want it to run
    runs-on: ubuntu-18.04
	# If the commit message contains '[skip-ci]', we stop
    if: "! contains(toJSON(github.event.commits.*.message), '[skip-ci]')"
    # Now we define which actions will take place.
    # One after another
    steps:
      # This is the first action. It will make sure that we have
      # all the necessary files from our repo, including our custom actions
      # This action here is actually from a remote repo available from Github itself
      - uses: actions/checkout@v1 
      # This is our custom action. Here is where we will define our git commands
      # to push our website updates to the `gh-pages` branch.
      # Notice that we are specifying the path to the action here.
      # We will create those files in a sec
      - uses: ./.github/actions/build-site
        env:
          # Now make sure you add this environment variable.
          # This token will allow us to push to github directly
          # without having to type in our password.
          # The GITHUB_TOKEN is available by default
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ENCRYPTED_0A6446EB3AE3_KEY: ${{ secrets.ENCRYPTED_0A6446EB3AE3_KEY }}
          ENCRYPTED_0A6446EB3AE3_IV: ${{ secrets.ENCRYPTED_0A6446EB3AE3_IV }}
{% endraw %}
```

Ở đây, các biến `ENCRYPTED_0A6446EB3AE3_KEY` và `ENCRYPTED_0A6446EB3AE3_IV` sẽ được sử dụng để giải mã tệp `PGP-key.asc.enc` đã được mã hóa với Travis CI ở phần trước. 
Tiếp theo, trong thư mục `actions`, tạo thư mục `build-site` với các tệp

* `action.yml`: Mô tả các công việc cần làm

  ```bash
  name: 'Deploy new version'
  description: 'Setup Ruby env and build new site version'
  author: 'Bruno Paulino'
  runs:
	using: 'docker'
	image: 'Dockerfile'
  ```
  
* `Dockerfile`: Xây dựng một [Docker](https://docs.docker.com/get-started/overview/) image để chạy Jekyll.

  ```bash
  # Create working environment for running scripts
  FROM ubuntu:18.04
  LABEL author="Duc A. Hoang"
  
  # Use /bin/bash instead of /bin/sh
  SHELL ["/bin/bash", "-c"]

  ARG DEBIAN_FRONTEND=noninteractive
  ENV TZ=Asia/Tokyo
  #ENV TZ=Asia/Ho_Chi_Minh

  # Install some necessary packages
  RUN apt-get update && \
  	  apt-get install -y --no-install-recommends \
	  build-essential \ 
	  rsync \
	  locales \
	  wget \
	  make \ 
	  git-all \ 
	  gnupg2 \
	  dirmngr \
	  curl \ 
	  ssh \ 
	  secure-delete \ 
	  libcurl4-openssl-dev \
	  ca-certificates \
	  ruby \
	  ruby-dev && \
	  rm -rf /var/lib/apt/lists/*

  # Set locale
  RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
      locale-gen
  ENV LANG en_US.UTF-8  
  ENV LANGUAGE en_US:en  
  ENV LC_ALL en_US.UTF-8 

  # Jekyll
  RUN gem install bundler --version 2.1.4

  # This is our entrypoint to our custom scripts
  # more about that in a sec
  COPY entrypoint.sh /

  # Use the entrypoint.sh file as the container entrypoint
  # when Github executes our Docker container
  ENTRYPOINT ["bash", "/entrypoint.sh"]
  ```
  
* `entrypoint.sh`: Sinh HTML từ các tệp nguồn với môi trường đã cài đặt với `Dockerfile`.

  ```bash
  #!/bin/bash

  # Original: https://bpaulino.com/entries/10-automating-your-work-with-github-actions
  # Exit immediately if a pipeline returns a non-zero status.
  set -e

  echo "🚀 Starting deployment action"

  # Here we are using the variables
  # - GITHUB_ACTOR: It is already made available for us by Github. It is the username of whom triggered the action
  # - GITHUB_TOKEN: That one was intentionally injected by us in our workflow file.
  # Creating the repository URL in this way will allow us to `git push` without providing a password
  # All thanks to the GITHUB_TOKEN that will grant us access to the repository
  REMOTE_REPO="https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

  # Setting timezone
  export TZ="Asia/Tokyo"

  # We need to clone the `source` brach which contains source files.
  # Remember, our Docker container is practically pristine at this point
  git clone --single-branch --branch source $REMOTE_REPO source
  cd source

  # Importing PGP secret key
  openssl aes-256-cbc -K ${ENCRYPTED_0A6446EB3AE3_KEY} -iv ${ENCRYPTED_0A6446EB3AE3_IV} -in PGP-key.asc.enc -out PGP-key.asc -d
  gpg2 --import PGP-key.asc
  srm PGP-key.asc

  # Install all of our dependencies inside the container
  # based on the git repository Gemfile
  echo "⚡️ Installing project dependencies..."
  bundle install

  # Build the website using Jekyll
  echo "🏋️ Building website..."
  JEKYLL_ENV=production bundle exec jekyll build --config _config.yml
  echo "Jekyll build done"

  # Jekyll generates files are stored in the _site directory
  # Now lets clone the `master` branch and copy all files from _site
  git clone $REMOTE_REPO master
  rsync -arv --delete ./_site/* master
  cd master
  find ./ -type f -exec chmod 644 {} \; 
  find ./ -type d -exec chmod 755 {} \; 

  echo "☁️ Publishing website"

  # Now we can perform a commit
  git config user.name 'Duc A. Hoang'
  git config user.email 'anhduc.hoang1990@gmail.com'
  git config gpg.program gpg2
  git config user.signingkey D4E51506
  git add --all .
  # That will create a nice commit message with something like: 
  # Github Actions @ 2019-09-06 12:32:22 JST
  git commit -S -m "Github Actions @ $(date +'%Y-%m-%d  %H:%M:%S %Z')"
  echo "Build branch ready to go. Pushing to Github..."
  # Force push this update to our `master`
  git push -u origin master
  # Now everything is ready.
  # Lets just be a good citizen and clean-up after ourselves
  rm -fr .git
  cd ../..
  rm -rf source
  yes | gpg2 --batch --yes --delete-secret-keys FBEAAAD6C193858F7D9BCFD73D544026D4E51506
  yes | gpg2 --batch --yes --delete-keys FBEAAAD6C193858F7D9BCFD73D544026D4E51506
  echo "🎉 New version deployed 🎊"
  ```

Cuối cùng, thay vì cập nhật GitHub repo và chỉnh sửa mỗi khi có lỗi, bạn có thể chạy GitHub ngay trên PC của mình với gói [act](https://aur.archlinux.org/packages/act/) của Arch. Chi tiết về cách cài đặt và sử dụng cho các hệ điều hành khác có tại [trang này](https://github.com/nektos/act).
