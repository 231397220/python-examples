
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import requests
from pathlib import Path
import sleep

'''
（需提交代码作业）不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，
实现服务端和客户端可以传输单个文件的功能。

（需提交代码作业）使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容
 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
 
通过课程代码，熟练掌握 HTTP 协议头、返回码、HTML 等知识点，
这些在后面开发 Web 服务端程序时会频繁使用到。
'''

# 常量
TIME_FORMAT = "%Y-%m-%d"

# 变量


# 获取ip地址
def get_host_ip_add():
    ip_add = requests.get("http://ipconfig.me")
    logging.info(f"host ip add is {ip_add}")
    return ip_add

# 获取log目录


def get_logs(log_dir_date_value):
    create_logging_dir(log_dir_date_value)
    log_dir = f"/Users/Sam/samtest/python-{log_dir_date_value}"
    logs = f"{log_dir}/sam-test.log"
    return logs

# 生成logging配置


def create_logging_config(logs):
    create_logging_dir(logs)
    logging.basicConfig(filename=logs,
                        level=logging.INFO)

# 创建日志目录


def create_logging_dir(logs):
    p = Path(logs)
    if not p.parent.exists():
        try:
            # todo: 获取root权限
            p.parent.mkdir(parents=True)
        except Exception as err:
            print(err)

# 主函数


def main():
    log_dir_date_value = time.strftime(TIME_FORMAT)
    logs = get_logs(log_dir_date_value)
    while True:
        create_logging_config(logs)
        get_host_ip_add()
        time.sleep(5)


if __name__ == "__main__":
    main()
