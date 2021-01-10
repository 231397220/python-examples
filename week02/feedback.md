1. 代码中推荐用 logging 代替 print 输出日志内容
2. socket 逻辑中没有异常处理，可能会引起在异常关闭，而没有正常关闭连接，建议使用 try except finally 逻辑来正常关闭socket，或用 with 来处理连接
3. 多线程操作文件写操作时需要加锁，建议封装一个线程安全写文件类
4. 爬虫可以学习使用多线程，队列来处理。密集IO型使用线程模型会提高爬取效率
5. 复杂字符串拼接尽量使用字符串格式来实现，不要用 + 
6. html 页面推荐用 bs4 或 xpath 来分析提取内容比 re 在代码可读性上更好
7. Python 代码风格不规范，代码规范可以参考一下这篇文章
https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/