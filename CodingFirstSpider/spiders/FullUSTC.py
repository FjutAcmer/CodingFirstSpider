# -*- coding: utf-8 -*-
import json

import scrapy
import time

import scrapy
from CodingFirstSpider.items import ProblemInfoItem


class FullUSTCSpider(scrapy.Spider):
    name = 'FullUSTC'
    allowed_domains = ["oj.ustc.edu.cn", "ustcoj.applinzi.com"]
    # 基本页码url
    base_url = "https://ustcoj.applinzi.com/api/problem/?page=%s&per_page=%s"
    # 爬虫开始url
    start_urls = ["https://ustcoj.applinzi.com/api/problem/"]
    # 题目详情前端url
    problem_show_url = "https://oj.ustc.edu.cn/#/problems/%s/"
    # 题目详情后端url
    problem_detail_url = "https://ustcoj.applinzi.com/api/problem/%s"

    # 测试url
    # start_urls = [""]

    # 测试输出
    # def parse(self, response):
    # pass

    # 爬虫入口函数。首先拿到可用页码
    def parse(self, response):
        # 先检查USTC后端api是否正常
        _html_status = response.status
        if _html_status == 200:
            # 猜测的可查询总页数
            guess_total_page = 10
            # 每页页数
            pre_pages = 100
            for i in range(1, guess_total_page + 1):
                url = self.base_url % (i, pre_pages)
                yield scrapy.Request(url, callback=self.parse_problem_id)
        else:
            return

    # 从可用页码中爬取题目ID
    def parse_problem_id(self, response):
        body = json.loads(response.body)
        problem_list = body['data']['problem_list']
        if len(problem_list) == 0:
            return
        else:
            for problem in problem_list:
                url = self.problem_detail_url % problem['problem_id']
                yield scrapy.Request(url, callback=self.parse_problem_detail)

    # 进入题目详情页爬取题目详细内容
    def parse_problem_detail(self, response):
        ustc = ProblemInfoItem()
        body = json.loads(response.body)
        problem = body['data']['problem']
        ustc['spider_name'] = "FullUSTC"
        ustc['insert_time'] = time.time()
        ustc['from_website'] = self.allowed_domains[0]
        ustc['problem_url'] = self.problem_show_url % problem['problem_id']
        ustc['problem_id'] = problem['problem_id']
        ustc['problem_title'] = problem['problem_title']
        ustc['problem_memory_limit'] = problem['memory_limit']
        ustc['problem_time_limit'] = problem['time_limit']
        ustc['problem_description'] = problem['description']
        ustc['problem_input'] = problem['input_description']
        ustc['problem_output'] = problem['output_description']
        # 数据库设计问题，只取一个样例
        ustc['problem_sample_input'] = problem['input_sample'][0]
        # 数据库设计问题，只取一个样例
        ustc['problem_sample_output'] = problem['output_sample'][0]
        yield ustc
