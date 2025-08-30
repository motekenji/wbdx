微博、B站、抖音、小红书实时监控脚本--WBDXmonitor
===========================================

[![PyPI version](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) 

实时关注微博、B站、抖音、小红书某用户更新动态，并及时通过微信提醒

详见文章：https://www.blain.top/p/wbdxmonitor/

有问题可通过博客内联系方式进行留言

![image-20241129134540933](assets/image-20241129134540933.png)

![image-20241129134645936](assets/image-20241129134645936.png)



此脚本的用途
====

监控微博、B站、抖音、小红书关注之人的动态，并及时通过微信进行提醒

使用方法
====

一、安装

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/Bla1n/WBDXmonitor.git
cd WBDXmonitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开4个monitor，修改文件内容（有注释）

![image-20241129140633567](assets/image-20241129140633567.png)

二、免费注册使用WxPusher微信消息推送服务

https://wxpusher.zjiecode.com/

注册完成后在“应用管理--appToken”中生成一个自己的凭证，**并修改start.py中对应位置**

![image-20241129135535161](assets/image-20241129135535161.png)

三、使用方法

周期性执行以下命令，可使用宝塔或者crontab设置定时任务

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 start.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


![image-20241129134229907](assets/image-20241129134229907.png)

![image-20241129134259965](assets/image-20241129134259965.png)
