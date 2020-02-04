# -*- coding: utf-8 -*-
import scrapy
import re
import time
from CodingFirstSpider.items import ProblemInfoItem


class HduSpider(scrapy.Spider):
    name = 'FullHDU'
    allowed_domains = ['acm.hdu.edu.cn']
    # 请求延迟
    # download_delay = 1
    base_url = 'http://acm.hdu.edu.cn/listproblem.php?vol=%s'
    start_urls = ['http://acm.hdu.edu.cn/listproblem.php']
    problem_detail_url = 'http://acm.hdu.edu.cn/showproblem.php?pid=%s'

    # # 测试输出
    # def parse(self, response):
    #   pass

    def parse(self, response):
        # 首先拿到可用页码
        real_pages = response.xpath('//p[@class="footer_link"]/font/a/text()').extract()
        for page in real_pages:
            url = self.base_url % page
            yield scrapy.Request(url, callback=self.parse_problem_id)

    def parse_problem_id(self, response):
        problem_list = response.xpath('//script/text()').extract()
        problems = str.split(problem_list[1], ";")
        for item in problems:
            if str.isspace(item) or len(item) == 0:
                break
            p = re.compile(r'[(](.*)[)]', re.S)
            str1 = re.findall(p, item)
            problem_id = str.split(str1[0], ",")[1]
            url = self.problem_detail_url % problem_id
            yield scrapy.Request(url, callback=self.parse_problem_detail)

    def parse_problem_detail(self, response):
        hdu = ProblemInfoItem()
        hdu['spider_job'] = ""
        hdu['insert_time'] = time.time()
        hdu['from_website'] = self.allowed_domains[0]
        pid = str.split(response.request.url, "=")[1]
        hdu['problem_url'] = self.problem_detail_url % pid
        hdu['problem_id'] = pid
        hdu['problem_title'] = response.xpath('//h1/text()').extract()[0]
        _temp_limit_str = response.xpath("//span/text()").extract()[0]
        hdu['problem_memory_limit'] = str.split(_temp_limit_str, ":")[2].strip(' ')
        hdu['problem_time_limit'] = _temp_limit_str[0: str.find(_temp_limit_str, "    Memory Limit")]
        _temp_des_title_str = response.xpath("//div[@class='panel_title']/text()").extract()
        _temp_des_info_str = response.xpath("//div[@class='panel_content']").extract()
        des_dict = dict(zip(_temp_des_title_str, _temp_des_info_str))
        hdu['problem_description'] = des_dict.get('Problem Description')
        hdu['problem_input'] = des_dict.get('Input')
        hdu['problem_output'] = des_dict.get('Output')
        hdu['problem_sample_input'] = des_dict.get('Sample Input')
        hdu['problem_sample_output'] = des_dict.get('Sample Output')
        # print(hdu)
        yield hdu