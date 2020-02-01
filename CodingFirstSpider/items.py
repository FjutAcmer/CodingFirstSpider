# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 　爬取题目基础信息类
class ProblemInfoItem(scrapy.Item):
    fromWebsite = scrapy.Field()
    problemUrl = scrapy.Field()
    problemId = scrapy.Field()
    problemTitle = scrapy.Field()
    spiderJob = scrapy.Field()
    insertTime = scrapy.Field()
