#!/bin/bash
# 1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

# 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
# 将增加远程用户的 SQL 语句作为作业内容提交


# docker 启动mysql 
docker run --name some-mysql  -v ./mysql/conf.d:/etc/mysql/conf. -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.32 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


# 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
# alter database testdb character set utf8mb4;


# 将增加远程用户的 SQL 语句作为作业内容提交
# CREATE USER 'testroot'@'%' IDENTIFIED BY 'testpass';
# GRANT ALL PRIVILEGES ON testdb.* TO 'root' @'%';