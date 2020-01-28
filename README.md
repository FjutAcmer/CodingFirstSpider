# 爬虫部署教程
## 1. 如何以进程的方式运行爬虫服务
- 使用Anaconda3，所以需要进入对应的环境，我这里的环境名是 web
```
activate web
```

- 在 项目根目录下（scrapy.cfg同级目录）运行scrapyd服务
```
scrapyd
```

- 进入下一级爬虫目录并部署爬虫
```
cd CodingFirstSpider
scrapyd-deploy
```

## 2.如何直接运行爬虫
- 在 项目根目录/CodingFirstSpider/ 目录下执行
```
scrapy crawl [爬虫名]
```