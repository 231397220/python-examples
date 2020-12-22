
'''
参考文档:  https: // docs.python.org/zh-cn/3.7/library/re.html

应用场景
1 匹配字符串类型(手机号,密码复杂度)
2 字符串查找
3 替换(数据分析时常用)
'''

import re

# 匹配

content='123218621321'
pattern="^123"
result = re.match(pattern, content).group()
# stdout = 123

result = re.match(pattern, content).span()
# stdout = (0, 3)

re.match("(.*)@(.*)","123@qq.com").group(1)
# stdout = 123

re.match("(.*)@(.*)", "123@qq.com").group(2)
# stdout = qq.com


# 查找
if re.search("@", "123@qq.com"):
    print("mail")
# stdout = True

re.findall("21", content)
# stdout = ['21', '21', '21']

# 替换
re.sub("^12", "45", content)
# stdout= 453218621321

# 分割
re.split("@", "123@qq.com")
# stdout = ['123', 'qq.com']
re.split("(@)", "123@qq.com")
# stdout = ['123', '@', 'qq.com']
