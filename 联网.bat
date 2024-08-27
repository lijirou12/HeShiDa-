@echo off
setlocal enabledelayedexpansion

REM 获取本机IP地址
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| findstr IPv4') do (
    set ip=%%i
    set ip=!ip:~1!
)

REM 构建带有IP的完整链接
set baseLink=http://211.138.1.146:8888/showLogin.do?wlanuserip=
set fullLink=%baseLink%!ip!%

REM 打开浏览器并访问链接
start "" "%fullLink%&wlanacname=0021.0311.311.00%"

exit
