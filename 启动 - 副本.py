import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("作者-molisang 项目地址https://github.com/lijirou12/HeShiDa-")

# 获取本机的IPv4地址
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# 构建完整的URL
url = f"http://211.138.1.146:8888/showLogin.do?wlanuserip={ip_address}&wlanacname=0021.0311.311.00"

# 设置Edge浏览器驱动
driver = webdriver.Edge()

# 打开指定链接
driver.get(url)

# 等待页面加载
time.sleep(3)  # 根据网络情况调整等待时间

# 定位用户名输入框并输入用户名
driver.find_element(By.ID, 'bpssUSERNAME').send_keys('你的账户名称')

# 定位密码输入框并输入密码
driver.find_element(By.ID, 'bpssBUSPWD').send_keys('密码')

# 提交表单
button_element = driver.find_element(By.XPATH, '//a[@onclick="return checkLogin();"]')

button_element.click()
# 可选：等待几秒钟以确保页面完成加载
time.sleep(5)

# 关闭浏览器
driver.quit()

