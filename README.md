# 一码当先爬虫系统 Coding First Spider

## 介绍

“一码当先” 爬虫系统是 “一码当先” 在线编程教育系统的一个组成部分。
项目采用Python的Scrapy框架进行编写，同时采用Scrapyd框架部署为进程以满足使用API进行调用。


## 软件架构

1. 项目采用Python语言编写，版本为3.7。
2. 项目采用Scrapy爬虫框架，并集成到Scrapyd中，提供API接口调用
3. 关系型数据库采用MySQL 8.0.15
4. 键值数据库采用Redis 3.2.100

## 开发教程

1. 下载并安装Idea，配置好开发环境，安装相关的插件
2. 下载并安装maven (不是必要，如果正确安装Idea会自动配置)
3. 下载Spring-2.0.0.M5 SpringBoot工具（不是必要）
4. 下载并安装MySQL 8.0.15和MySQL可视化工具，项目运行时保持MySQL链接正常 （不是必要，将开放远程测试库）
5. 下载并安装Redis 3.2.100，项目运行时保持Redis Server在本地开启
6. 在application.yml，application-dev.yml文件中修改相关字段保证本地的配置链接正确
7. 运行 CodingFirstApplication.java
8. 在浏览器中输入地址 http://localhost:[配置文件中的端口]/[配置文件中的项目名]/swagger-ui.html
进入在线接口文档 
9. 在浏览器中输入地址 http://localhost:[配置文件中的端口]/[配置文件中的项目名]/druid/index.html
，并输入用户名密码后，进入Druid管理界面

## 部署教程
 - ###  直接部署
  在 项目根目录/CodingFirstSpider/ 目录下执行
  
   ```
   scrapy crawl [爬虫名]
   ```
 
 - ### 部署到Scrapyd
 开发环境使用Anaconda3维护对应Python版本，所以需要进入对应的环境，我这里的环境名是【web】
  ```
   activate web
  ```

  在 项目根目录下（scrapy.cfg同级目录）运行scrapyd服务
   ```
   scrapyd
   ```

  在 项目根目录下（scrapy.cfg同级目录）启动scrapyd-client部署爬虫项目
  > scrapyd-client： https://github.com/scrapy/scrapyd-client
   ```
   scrapyd-deploy
   ```

## 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request