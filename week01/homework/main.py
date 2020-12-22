
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import requests
from pathlib import Path

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

# 生成logging配置
def create_logging_config(log_dir_date_value):
    create_logging_dir(log_dir_date_value)
    log_dir = f"/var/log/python-{log_dir_date_value}"
    logs = f"{log_dir}/sam-test.log"

    logging.basicConfig(filename=logs,
                        encoding='utf-8', level=logging.INFO)

# 创建日志目录
def create_logging_dir(log_dir_date_value):
    p = Path(log_dir_date_value)
    if not p.parent.exists() :
        try:
            # todo: 获取root权限
            p.parent.mkdir(parents=True)
        except Exception as err :
            print(err)

# 主函数
def main():
    log_dir_date_value=time.strftime(TIME_FORMAT)
    create_logging_config(log_dir_date_value)
    get_host_ip_add()

if __name__ == "__main__":
    main()
