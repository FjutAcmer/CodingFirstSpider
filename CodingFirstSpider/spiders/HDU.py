# -*- coding: utf-8 -*-
import scrapy
import re
import time
from CodingFirstSpider.items import ProblemInfoItem


class HduSpider(scrapy.Spider):
    name = 'HDU'
    allowed_domains = ['acm.hdu.edu.cn']
    # download_delay = 1
    base_url = 'http://acm.hdu.edu.cn/listproblem.php?vol=%s'
    start_urls = ['http://acm.hdu.edu.cn/listproblem.php']
    problem_detail_url = 'http://acm.hdu.edu.cn/showproblem.php?pid=%s'

    def parse(self, response):
        # 首先拿到可用页码
        real_pages = response.xpath('//p[@class="footer_link"]/font/a/text()').extract()
        for page in real_pages:
            url = self.base_url % page
            yield scrapy.Request(url, callback=self.parse_problem, priority=int(page))

    def parse_problem(self, response):
        hdu = ProblemInfoItem()
        problem_list = response.xpath('//script/text()').extract()
        problems = str.split(problem_list[1], ";")
        for item in problems:
            if str.isspace(item) or len(item) == 0:
                return
            p = re.compile(r'[(](.*)[)]', re.S)
            str1 = re.findall(p, item)
            detail = str.split(str1[0], ",")
            hdu['fromWebsite'] = self.allowed_domains[0]
            hdu['spiderJob'] = ""
            hdu['problemId'] = detail[1]
            hdu['problemUrl'] = self.problem_detail_url % detail[1]
            hdu['problemTitle'] = detail[3]
            hdu['insertTime'] = time.time()
            yield hdu
