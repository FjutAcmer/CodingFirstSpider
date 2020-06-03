# -*- coding:utf-8 -*-
import os

# 进入当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 部署项目到服务中
os.system("scrapyd-deploy")
