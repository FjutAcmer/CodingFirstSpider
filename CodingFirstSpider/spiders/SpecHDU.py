# -*- coding: utf-8 -*-

import time
import scrapy

from CodingFirstSpider.items import ProblemInfoItem


class SpecHduSpider(scrapy.Spider):
    name = "SpecHDU"
    allowed_domains = ["acm.hdu.edu.cn"]
    start_urls = ["http://acm.hdu.edu.cn/listproblem.php"]
    problem_detail_url = "http://acm.hdu.edu.cn/showproblem.php?pid=%s"

    # 爬虫初始化，拿到参数并初始化
    def __init__(self, problems=None, **kwargs):
        super().__init__(problems=None, **kwargs)
        self.needToGetProblems = problems

    # 爬虫入口函数。首先拿到参数中的题目ID列表
    def parse(self, response):
        _html_status = response.status
        problems = str.split(self.needToGetProblems, ",")
        if _html_status == 200:
            print('problems:', problems)
            for item in problems:
                url = self.problem_detail_url % item
                yield scrapy.Request(url, callback=self.parse_problem_detail)

    # 进入题目详情页爬取题目详细内容
    def parse_problem_detail(self, response):
        hdu = ProblemInfoItem()
        hdu['spider_name'] = "SpecHDU"
        hdu['insert_time'] = time.time()
        hdu['from_website'] = self.allowed_domains[0]
        pid = str.split(response.request.url, "=")[1]
        hdu['problem_url'] = self.problem_detail_url % pid
        hdu['problem_id'] = pid
        hdu['problem_title'] = response.xpath('//h1/text()').extract()[0]
        _temp_limit_str = response.xpath("//span/text()").extract()[0]
        hdu['problem_memory_limit'] = str.split(_temp_limit_str, ":")[2].strip(' ')
        hdu['problem_time_limit'] = _temp_limit_str[11: str.find(_temp_limit_str, "    Memory Limit")]
        _temp_des_title_str = response.xpath("//div[@class='panel_title']/text()").extract()
        _temp_des_info_str = response.xpath("//div[@class='panel_content']").extract()
        des_dict = dict(zip(_temp_des_title_str, _temp_des_info_str))
        hdu['problem_description'] = des_dict.get('Problem Description')
        hdu['problem_input'] = des_dict.get('Input')
        hdu['problem_output'] = des_dict.get('Output')
        hdu['problem_sample_input'] = des_dict.get('Sample Input')
        hdu['problem_sample_output'] = des_dict.get('Sample Output')
        yield hdu
