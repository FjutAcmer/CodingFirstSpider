# 一码当先爬虫系统 Coding First Spider

## 介绍

“一码当先” 爬虫系统是 “一码当先” 在线编程教育系统的一个组成部分。
项目采用Python的Scrapy框架进行编写，同时采用Scrapyd框架部署为进程以满足使用API进行调用的需求。

本站共爬取**4**个在线编程类网站题库，所有爬取数据均为公开内容。详情如下：

获取网站主体 | 网站简称 |网站地址 | 获取方式 | 题量 | 全站爬取 | 指定爬取 
---|---|---|---|---|---|---
杭州电子科技大学 | HDU | acm.hdu.edu.cn | 静态页面 | 5601 | 支持 | 暂未开发
北京大学 | POJ1 | poj.org | 静态页面 | 4054  | 获取受限 | 暂未开发
北京大学 | POJ2 | poj.openjudge.cn | 静态页面 | 136 |  支持 | 暂未开发
中国科学技术大学 | USTC | oj.ustc.edu.cn | API接口 | 338 | 支持 |暂未开发


## 软件架构

1. 项目采用Python语言编写，版本为3.7。
2. 项目采用Scrapy爬虫框架，并集成到Scrapyd中，提供API接口调用
3. 关系型数据库采用MySQL 8.0.15
4. 键值数据库采用Redis 3.2.100

## 开发教程

1. 下载并安装PyCHarm，配置好开发环境，安装相关的插件
2. 下载并安装MySQL 8.0.15和MySQL可视化工具，项目运行时保持MySQL链接正常
3. 执行 项目根目录/db 目录下的 init.sql建立数据库
4. 运行 项目根目录 下的 main.py 并根据提示运行


## 部署教程

暂未提供

## 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request