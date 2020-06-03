# 一码当先爬虫系统 Coding First Spider

## 介绍

一码当先 | CodingFirst 题目资源爬虫是 “一码当先” 在线编程教育系统的一个组成部分。
项目采用Python的Scrapy框架进行编写，同时采用Scrapyd框架以满足使用API进行调用的需求。

本站共爬取 **4** 个在线编程类网站题库，所有爬取的题目数据均为公开内容。详情如下：

获取网站主体 | 网站简称 |网站地址 | 获取方式 | 题量 | 全站爬取 | 指定爬取 
---|---|---|---|---|---|---
杭州电子科技大学 | HDU | acm.hdu.edu.cn | 静态页面 | 5601 | 支持 | 支持
北京大学 | POJ1 | poj.org | 静态页面 | 4054  | 获取受限 | 暂未开发
北京大学 | POJ2 | poj.openjudge.cn | 静态页面 | 136 |  支持 | 暂未开发
中国科学技术大学 | USTC | oj.ustc.edu.cn | API接口 | 338 | 支持 |暂未开发


## 软件架构

1. 项目采用Python语言编写，版本为3.6.x **（不要采用其他版本Python运行，会出现严重Bug）**；
2. 项目采用Scrapy爬虫框架，并集成到Scrapyd中，提供API接口调用；
3. 关系型数据库采用MySQL 8.0.15。

## 开发教程

1. 下载并安装PyCharm，配置好开发环境。注意，Python版本必须为3.6.x，否则会出现未知Bug；
2. 强烈建议采用Anaconda3进行Python环境划分。安装好对应版本的环境后，进入对应的环境使用pip安装必要的包，如下：
```
 pip install twisted
 pip install scrapy
 pip install scrapyd
 pip install scrapyd-client
 pip install pymysql
```
3. 下载并安装MySQL 8.0.15和MySQL可视化工具，项目运行时保持MySQL链接正常；
4. 在MySQL中建立数据库，并在对应的库下执行 项目根目录/db 目录下的 init.sql建立数据表；
5. 更改 项目根目录/CodingFirstSpider/ 下的settings.py 内的数据库链接配置；
6. 采用Anaconda环境下的Python.exe运行 项目根目录下的 deploy_dev.py 进行本地部署。

## 部署教程
> 采用CentOS7进行了实际的部署测试，如果采用其他版本的Linux，同理即可
1. 建议在部署服务器中安装Anaconda3，以便切换Python版本。如果不使用，请安装Python3。并参考开发教程中的说明完成必要包的安装；
2. 按照开发教程中的指示完成MySQL数据库的安装以及数据库、数据库表的建立；
3. 更改 项目根目录/CodingFirstSpider/ 下的settings.py 内的数据库链接配置；
4. 进入Anaconda的对应环境后，运行 项目根目录下的deploy.sh文件，完成部署。

## 参与贡献
1. Fork 本仓库到分仓库中
2. 提交代码到分仓库中
3. 新建 Pull Request，提交请求
4. 完成合并，修改内容生效