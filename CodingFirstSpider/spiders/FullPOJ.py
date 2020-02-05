# -*- coding: utf-8 -*-
import scrapy


class FullPOJSpider(scrapy.Spider):
    name = 'FullPOJ'
    allowed_domains = ['poj.openjudge.cn']
    start_urls = ['http://poj.openjudge.cn/practice/']

    def parse(self, response):
        pass
