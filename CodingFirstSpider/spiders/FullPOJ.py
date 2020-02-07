# -*- coding: utf-8 -*-
import scrapy
import re
import time
from CodingFirstSpider.items import ProblemInfoItem


# 　HDU爬虫
class FullPOJSpider(scrapy.Spider):
    name = 'FullPOJ'
    allowed_domains = ['poj.openjudge.cn']
    base_url = 'http://poj.openjudge.cn/practice/?page=%s'
    start_urls = ['http://poj.openjudge.cn/practice/']
    problem_detail_url = 'http://poj.openjudge.cn/practice/%s'

    # # 测试输出
    # def parse(self, response):
    #     url = 'http://poj.openjudge.cn/practice/1001'
    #     yield scrapy.Request(url, callback=self.parse_problem_detail)

    # 爬虫入口函数。首先拿到可用页码
    def parse(self, response):
        # POJ只能拿到除当前页码外的其他页码
        real_pages = response.xpath("//span[@class='pages']/a/text()").extract()
        # 特例化，从1开始到最大的页码
        for page in range(1, int(max(real_pages)) + 1):
            url = self.base_url % page
            yield scrapy.Request(url, callback=self.parse_problem_id)

    # 从可用页码中爬取题目ID
    def parse_problem_id(self, response):
        problem_list = response.xpath("//tbody/tr/td[@class='problem-id']/a/text()").extract()
        for problem_id in problem_list:
            url = self.problem_detail_url % problem_id
            yield scrapy.Request(url, callback=self.parse_problem_detail)

    # 进入题目详情页爬取题目详细内容
    def parse_problem_detail(self, response):
        poj = ProblemInfoItem()
        poj['spider_job'] = ""
        poj['insert_time'] = time.time()
        poj['from_website'] = self.allowed_domains[0]
        pid = str.split(response.request.url, "/")[-1]
        poj['problem_url'] = response.request.url
        poj['problem_id'] = pid
        _temp_id_title = response.xpath("//div[@id='pageTitle']/h2/text()").extract()[0]
        poj['problem_title'] = _temp_id_title[str.find(_temp_id_title, ":") + 1:]
        poj['problem_memory_limit'] = response.xpath("//dl[@class='problem-params']/dd/text()").extract()[1]
        poj['problem_time_limit'] = response.xpath("//dl[@class='problem-params']/dd/text()").extract()[0]
        _temp_des_title_str = response.xpath("//dl[@class='problem-content']/dt/text()").extract()
        _temp_des_info_str = response.xpath("//dl[@class='problem-content']/dd").extract()
        des_dict = dict(zip(_temp_des_title_str, _temp_des_info_str))
        poj['problem_description'] = des_dict.get('描述')
        poj['problem_input'] = des_dict.get('输入')
        poj['problem_output'] = des_dict.get('输出')
        poj['problem_sample_input'] = des_dict.get('样例输入')
        poj['problem_sample_output'] = des_dict.get('样例输出')
        # print(poj)
        yield poj
