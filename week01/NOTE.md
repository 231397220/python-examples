# 学习笔记

## vscode

### 快捷键
- 格式化代码: option+shift+F
- 左右移动单词: option+左右方向
- 左右移动行头尾: command+左右方向
- 将本行上下移动: option+上下方向


## pip初始化
> pip切换阿里云源
```
pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple 
pip3.7 config set install.trusted-host mirrors.aliyun.com 
pip3.7 config list
```

## python ci标准

### 常见问题
 - 依赖第三方包版本不一致
 - 开发环境混乱,无法确认具体使用的第三方包
 - 开发环境和生产环境无法统一

### 解决方法

#### 创建虚拟开发环境,环境名称: sam-dev
```bash
python3 -m venv sam-dev
# check
ll ./sam-dev
ll ./sam-dev/bin
```

#### 激活或注销虚拟环境
```bash
# 激活
source ./sam-dev/bin/actite
# check
which python3
python3 -V

# 注销
deactivate
# check
whick python3
python3 -V
```

#### 查看虚拟环境中的第三方依赖包

```bash
source ./sam-dev/bin/actite
pip3 freeze > requirements.txt
```

### python CI过程 Dokcerfile
 - 拷贝python代码到指定目录
 - pip install -r ./requirements.txt

```Dockerfile
FROM python:3-alpine
WORKDIR /usr/local/server
COPY requirements.txt  ./requirements.txt
RUN  sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && apk add --no-cache --virtual .build-deps vim curl \
    && pip install --no-cache-dir -r requirements.txt 

COPY . ./
ENTRYPOINT python3 server.py

 ```
## [基础数据类型文档](https://zhuanlan.zhihu.com/p/26079855)
 
## [高级数据类型文档](https://docs.python.org/zh-cn/3.7/library/collections.html)

## [标准库文档](https://docs.python.org/zh-cn/3.7/library)
