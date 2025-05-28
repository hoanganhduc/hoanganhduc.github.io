---
layout: blog-post
title:  Tạo proxy truy cập Telegram
author: "Duc A. Hoang"
lang: vi
categories: 
  - linux
last_modified_at: 2025-05-28
description: Hướng dẫn cách tạo và thiết lập proxy để truy cập Telegram khi bị chặn hoặc hạn chế.
keywords: Telegram, proxy, truy cập Telegram, tạo proxy, thiết lập proxy, vượt chặn, chặn Telegram, vượt rào cản địa lý, an toàn trực tuyến, bảo mật, 
<!--published: false-->
---

# Chuẩn bị

Để tạo 1 địa chỉ Proxy riêng, sử dụng cho cá nhân, bạn cần có 1 VPS có cấu hình cài được Linux, có thể thuê ở [Vultr](https://www.vultr.com/), [Digital Ocean](https://www.digitalocean.com), [Linode](https://www.linode.com), v.v. 

# MTProto Proxy

## Cài đặt

Các bước thực hiện từ [https://github.com/alexbers/mtprotoproxy](https://github.com/alexbers/mtprotoproxy).

1. Clone mã nguồn từ GitHub và truy cập vào thư mục:
```bash
git clone -b stable https://github.com/alexbers/mtprotoproxy.git
cd mtprotoproxy
```

2. Chỉnh sửa tệp cấu hình (khuyến nghị):
```bash
# Mở và chỉnh sửa file config.py, thiết lập PORT, USERS và AD_TAG
nano config.py
```

Nếu `PORT` chưa mở thì sử dụng `ufw` để mở cổng, ví dụ mở cổng 443:
```bash
sudo ufw allow 443/tcp
sudo ufw allow 443/udp
sudo ufw reload
```

3. Khởi động proxy:
```bash
# Sử dụng Docker
docker-compose up -d
# Hoặc sử dụng Python nếu không dùng Docker
# python3 mtprotoproxy.py
```

4. Lấy link chia sẻ proxy (tùy chọn):
```bash
docker-compose logs
```

Để sử dụng mà không cần Docker và tự động chạy khi VPS khởi động, thực hiện theo hướng dẫn sau:

## Tự động khởi động khi hệ thống boot

Hướng dẫn này áp dụng cho Linux có `systemd` (hầu hết các hệ điều hành hiện đại như Ubuntu, Debian, CentOS, RHEL, Gentoo, v.v). Bạn cần cài đặt `Python3` và `git`.

1. Tải mã nguồn và truy cập vào thư mục:
```bash
git clone -b stable https://github.com/alexbers/mtprotoproxy.git /mtprotoproxy; cd /mtprotoproxy
```

2. (tùy chọn, khuyến nghị) Chỉnh sửa file `config.py`, thiết lập `PORT`, `USERS` và `AD_TAG`

3. Tạo người dùng `tgproxy`:
```bash
useradd --no-create-home -s /sbin/nologin tgproxy
```

4. (tùy chọn, khuyến nghị) Cài đặt module `cryptography`:
```bash
sudo apt install python3-cryptography
```

5. (tùy chọn) Cài đặt module `uvloop`:
```bash
sudo apt install python3-uvloop
```

6. Tạo file `/etc/systemd/system/mtprotoproxy.service` với nội dung sau:
```
[Unit]
    Description=Async MTProto proxy for Telegram
    After=network-online.target
    Wants=network-online.target

[Service]
    ExecStart=/mtprotoproxy/mtprotoproxy.py
    AmbientCapabilities=CAP_NET_BIND_SERVICE
    LimitNOFILE=infinity
    User=tgproxy
    Group=tgproxy
    Restart=on-failure

[Install]
    WantedBy=multi-user.target
```

7. Bật tự động khởi động khi hệ thống boot:
```bash
sudo systemctl enable mtprotoproxy
```

8. (tùy chọn, khởi động proxy):
```bash
sudo systemctl start mtprotoproxy
```

9. (tùy chọn, lấy link để chia sẻ proxy):
```bash
sudo journalctl -u mtprotoproxy | cat
```

## Sử dụng

Lấy link chia sẻ proxy có dạng `tg://proxy?server=IP-VPS&port=xxx&secret=xxxxxxxxxx` và truy cập từ trình duyệt.

# SOCKS5 Proxy

## Cài đặt

1. Trên server Ubuntu , gõ lệnh:

```bash
sudo apt update
sudo apt install dante-server -y
```

2. Kiểm tra tên Card mạng của Server là gì bằng lệnh `ip a`. Kiểm tra interface mạng hiện tại có thể là `esns3`, `enp0s3`, `eth0`, v.v. Ghi nhớ tên Card mạng để cấu hình SOCK5. Ví dụ sau thực hiện với tên Card mạng là `eth0`.

3. Xóa `/etc/danted.conf` và tạo file mới với nội dung sau:

```
logoutput: syslog

internal: eth0 port = 1080
external: eth0

socksmethod: none
clientmethod: none

user.notprivileged: nobody

client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: connect disconnect error
}

socks pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    socksmethod: none
    log: connect disconnect error
}
```

3. Mở cổng:

```bash
sudo ufw allow 1080/tcp
sudo ufw reload
```

4. Khởi động dịch vụ SOCKS5:

```bash
sudo systemctl enable danted
sudo systemctl start danted
```

## Sử dụng

Để sử dụng SOCKS5 proxy, bạn cần cấu hình ứng dụng hoặc trình duyệt của mình để kết nối đến địa chỉ IP của VPS và cổng 1080. Ví dụ IP Server là `51.79.123.222` thì bạn truy cập vào link `tg://proxy?server=51.79.123.222&port=1080` hoặc `https://t.me/proxy?server=51.79.123.222&port=1080`. Có thể thêm thủ công vào Telegram bằng cách vào `Setting -> Advance -> Connection Type`, xem chỗ `Use custom proxy -> Add proxy`.