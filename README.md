# crawl_canhme

Tạo môi trường 

```
python3 -m venv venv
source ~/venv/bin/activate
```

Clone code

```
cd /var/
git clone https://github.com/niemdinhtrong/crawl_canhme.git
```

Cài các gói yêu cầu

```
cd /var/crawl_canhme
pip install -r requirements.txt
```

Tạo database

```
mysql -u root -p
create database canhme;
create user 'canhme'@'localhost' identified by 'Nhanhoa2020@';
grant all privileges on canhme.* to 'canhme'@'localhost';
create table site (idsite int NOT NULL AUTO_INCREMENT primary key, links varchar(200) not null, tieude varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci);
create table comment (idcomment char(50) primary key, idsite int, username varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci, nd_comment varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci, times TIMESTAMP);
```

Khai báo lại thông tin file `setting`

Chạy thử

```
