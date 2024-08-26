# 河北师范大学校园网自动登录脚本

这是一个自动登录河北师范大学校园网的 Python 脚本。可能很多人和我一样，连接到CMCC时常会遇到无法正常跳转到登陆界面的问题通过分析其网页跳转链接，写出了这个简单的Python脚本

## 功能
- 自动打开CMCC对应的登陆页面
- 自动填写用户名和密码
- 自动点击登录按钮

## 使用说明

1. 确保你已经安装了 [Python](https://www.python.org/) 和浏览器[Edge](https://www.microsoft.com/zh-cn/edge/)。Python版本推荐3.10

2. 下载脚本（启动.py）在脚本中替换你的用户名和密码。
3. 运行脚本以自动登录校园网。

## 安装依赖

```bash
pip install selenium
