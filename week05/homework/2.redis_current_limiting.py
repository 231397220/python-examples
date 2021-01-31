#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
作业二：在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
已知有如下函数：

复制代码
def sendsms(telephone_number: int, content: string, key=None)：
    # 短信发送逻辑, 作业中可以使用 print 来代替
    pass
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    pass
    print("发送成功")
期望执行结果：

sendsms(12345654321, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 发送成功
…
sendsms(88887777666, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 1 分钟内发送次数超过 5 次, 请等待 1 分钟
sendsms(88887777666, content=“hello”) # 发送成功

选做：
1.content 为短信内容，超过 70 个字自动拆分成两条发送
2. 为 sendsms() 函数增加装饰器 send_times()，通过装饰器方式实现限制手机号最多发送次数，如：

复制代码
@send_times(times=5)
sendsms()
'''
import random
import logging
import sys
import redis
from time import sleep
from random import randint, choices
from datetime import datetime

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    password='passwd')
content = "hello"


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def sendsms(phone_number: int, content: str):
    print('waitting for send...')
    sleep(1)
    first_time = redis_client.hget(phone_number, 'time_circle').decode()
    now_count = int(redis_client.hget(phone_number, 'count_circle').decode())
    success = True
    if first_time == '0':
        redis_client.hmset(phone_number, {'time_circle': str(
            datetime.now()), 'count_circle': 1})
    else:
        time_delta = datetime.now() - datetime.fromisoformat(first_time)
        if time_delta.seconds <= 60 and now_count >= 5:
            success = False
        elif time_delta.seconds > 60:
            redis_client.hmset(phone_number, {'time_circle': str(
                datetime.now()), 'count_circle': 1})
        else:
            redis_client.hincrby(phone_number, 'count_circle')
    if success:
        print(f"发送成功给{phone_number}！内容：{content}")
    else:
        print("每分钟只能发送5条，请稍后再试！")



def main():
    telephone_numbers = []
    for i in range(3):
        telephone_number=create_phone()
        redis_client.hmset(
            telephone_number, {'time_circle': 0, 'count_circle': 0})
        telephone_numbers.append(telephone_number)
    while True:
        for telephone_number in telephone_numbers:
            logging.debug(f"准备给{telephone_number}发送短信")
            sendsms(telephone_number, content)
    # 检查手机号1分钟内发送短信次数
    # 判断是否触发短信发送限制上线
    # 发送失败,输出log
    # else
    # 发送成功
    pass


if __name__ == "__main__":
    main()
