# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 　爬取题目信息类
class ProblemInfoItem(scrapy.Item):
    spider_name = scrapy.Field()
    insert_time = scrapy.Field()
    from_website = scrapy.Field()
    problem_url = scrapy.Field()
    problem_id = scrapy.Field()
    problem_title = scrapy.Field()
    problem_time_limit = scrapy.Field()
    problem_memory_limit = scrapy.Field()
    problem_description = scrapy.Field()
    problem_input = scrapy.Field()
    problem_output = scrapy.Field()
    problem_sample_input = scrapy.Field()
    problem_sample_output = scrapy.Field()



