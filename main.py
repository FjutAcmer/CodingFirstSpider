# -*- coding:utf-8 -*-

from scrapy import cmdline

import os

# Anaconda3的环境名，切换Python环境
PYTHON_ENV_NAME = "web"
# 爬虫项目名
PROJECT_NAME = "CodingFirstSpider"

# 进入项目根目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("activate web")
deploy_model = input("输入部署模式（scrapyd / normal）：")
# scrapyd部署模式
if deploy_model == "scrapyd":
    os.system("start /b scrapyd")
    os.system("scrapyd-deploy")
    spider_name = input("启动爬虫（ [爬虫名] / no）：")
    if spider_name == 'no':
        pass
    else:
        url = "curl http://localhost:6800/schedule.json -d project={} -d spider={}".format(PROJECT_NAME, spider_name)
        print(url)
        os.system(url)
# 单独使用爬虫
elif deploy_model == "normal":
    spider_name = input("启动爬虫（ [爬虫名] / no）：")
    if spider_name == 'no':
        pass
    else:
        cmdline.execute(["scrapy", "crawl", spider_name])
