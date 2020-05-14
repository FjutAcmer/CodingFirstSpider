# -*- coding:utf-8 -*-
import os

# 进入当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("activate web")
os.system("start /b scrapyd")
os.system("scrapyd-deploy")