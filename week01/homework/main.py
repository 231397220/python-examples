
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import requests
from pathlib import Path
import sleep

'''
编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 
日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
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
    if not p.parent.exists() :
        try:
            # todo: 获取root权限
            p.parent.mkdir(parents=True)
        except Exception as err :
            print(err)

# 主函数
def main():
    log_dir_date_value=time.strftime(TIME_FORMAT)
    logs = get_logs(log_dir_date_value)
    while True:
        create_logging_config(logs)
        get_host_ip_add()
        time.sleep(5)
        

if __name__ == "__main__":
    main()
