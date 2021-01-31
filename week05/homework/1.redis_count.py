#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
作业一：使用 Python+redis 实现高并发的计数器功能
需求描述:
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
请实现以下函数：

复制代码
counter()
def counter(video_id: int):
    ...
    return count_number
函数说明:

counter 函数为统计视频播放次数的函数，每调用一次，播放次数 +1
参数 video_id 每个视频的 id，全局唯一
基于 redis 实现自增操作，确保线程安全
期望执行结果：
conuter(1001) # 返回 1
conuter(1001) # 返回 2
conuter(1002) # 返回 1
conuter(1001) # 返回 3
conuter(1002) # 返回 2

启动redis
docker run -d --name myredis -p 6379:6379 redis --requirepass "passwd"
'''
import logging
import sys
import redis
from random import randint


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    password='passwd')

def get_video_id():
    default_video_id = 1000
    i = randint(1,10)
    video_id = default_video_id + i
    logging.info(f"video_id is {video_id}")
    return video_id

def counter(video_id: int):
    # 获取当前的video计数量
    before_video_id_count_number = redis_client.get(video_id)
    logging.info(
        f"before_video_id_count_number is {before_video_id_count_number}")
    # 当前的vidio数量+1
    if before_video_id_count_number is None:
        before_video_id_count_number = 0
    count_number = int(before_video_id_count_number)+1
    redis_client.set(video_id, count_number)
    logging.info(f"video_id {video_id} ,count_number is {count_number}")
    return count_number


def main():
    for i in range(100):
        video_id = get_video_id()
        counter(video_id)

if __name__ == "__main__":
    main()
