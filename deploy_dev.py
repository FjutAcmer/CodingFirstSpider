# -*- coding:utf-8 -*-
import os

# 进入当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 激活conda环境“web”，如果没有请忽略
# os.system("activate web")
# 开启Scrapyd服务
os.system("start /b scrapyd")
# 部署项目到服务中
os.system("scrapyd-deploy")
