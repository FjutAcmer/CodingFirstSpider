# -*- coding: utf-8 -*-
import time

import scrapy
from CodingFirstSpider.items import ProblemInfoItem


# FIXME: 全站爬取受限
class FullPOJOneSpider(scrapy.Spider):
    name = "FullPOJ1"
    allowed_domains = ["poj.org"]
    # 基本页码url
    base_url = "http://poj.org/problemlist?volume=%s"
    # 爬虫开始url
    start_urls = ["http://poj.org/problemlist"]
    # 题目详情url
    problem_detail_url = "http://poj.org/problem?id=%s"

    # 爬虫入口函数。首先拿到可用页码
    def parse(self, response):
        _html_status = response.status
        if _html_status == 200:
            # POJ可以拿到全部有效页码
            real_pages = response.xpath("//a/font[@size='5']/text()").extract()
            # 特例化，从1开始到最大的页码
            for page in real_pages:
                url = self.base_url % page
                yield scrapy.Request(url, callback=self.parse_problem_id)
        else:
            return

    # 从可用页码中爬取题目ID
    def parse_problem_id(self, response):
        problem_list = response.xpath("//table[@class='a']/tr/td[1]/text()").extract()
        for problem_id in problem_list:
            url = self.problem_detail_url % problem_id
            yield scrapy.Request(url, callback=self.parse_problem_detail)

    # 进入题目详情页爬取题目详细内容
    def parse_problem_detail(self, response):
        poj = ProblemInfoItem()
        poj['spider_job'] = "FullPOJ1"
        poj['insert_time'] = time.time()
        poj['from_website'] = self.allowed_domains[0]
        pid = str.split(response.request.url, "=")[-1]
        poj['problem_url'] = response.request.url
        poj['problem_id'] = pid
        poj['problem_title'] = response.xpath("//div[@class='ptt']/text()").extract()[0]
        poj['problem_memory_limit'] = str(response.xpath("//div[@class='plm']/table/tr/td/text()").extract()[1]).lstrip(
            " ")
        poj['problem_time_limit'] = str(response.xpath("//div[@class='plm']/table/tr/td/text()").extract()[0]).lstrip(
            " ")
        _temp_des_title_str = response.xpath("//table[2]/tr/td/p[@class='pst']/text()").extract()
        _temp_des_info_str = response.xpath(
            "//table[2]/tr/td/div[@class='ptx'] | //table[2]/tr/td/pre[@class='sio']").extract()
        des_dict = dict(zip(_temp_des_title_str, _temp_des_info_str))
        poj['problem_description'] = des_dict.get('Description')
        poj['problem_input'] = des_dict.get('Input')
        poj['problem_output'] = des_dict.get('Output')
        poj['problem_sample_input'] = des_dict.get('Sample Input')
        poj['problem_sample_output'] = des_dict.get('Sample Output')
        yield poj
