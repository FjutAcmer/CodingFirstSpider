# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import copy

import pymysql
from twisted.enterprise import adbapi


class Pipeline(object):

    # 采用异步机制写入mysql
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 从配置文件拿配置
    @classmethod
    def from_settings(cls, settings):
        args = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASS'],
            cursorclass=pymysql.cursors.DictCursor,  # 指定cursor类型
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **args)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 爬虫爬取效率较插入快，item变量会被刷新，故使用深复制item来替代原item
        copy_item = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self.do_insert, copy_item)
        query.addErrback(self.handle_error, copy_item, spider)  # 处理异常

    @staticmethod
    def handle_error(failure):
        # 处理异步插入的异常
        if failure:
            print(failure)

    @staticmethod
    def do_insert(cursor, item):
        # 执行具体的插入
        insert_sql = """
            INSERT INTO `t_spider_get_problem_info`
            (`spider_name`, 
            `spider_job`,
            `from_website`, 
            `problem_url`, 
            `problem_id`, 
            `problem_title`, 
            `problem_time_limit`, 
            `problem_memory_limit`, 
            `problem_description`, 
            `problem_input`, 
            `problem_output`, 
            `problem_sample_input`, 
            `problem_sample_output`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        # 可以只使用execute，而不需要再使用commit函数
        cursor.execute(insert_sql,
                       (item['spider_name'],
                        item['spider_job'],
                        item['from_website'],
                        item['problem_url'],
                        item['problem_id'],
                        item['problem_title'],
                        item['problem_time_limit'],
                        item['problem_memory_limit'],
                        item['problem_description'],
                        item['problem_input'],
                        item['problem_output'],
                        item['problem_sample_input'],
                        item['problem_sample_output']
                        ))

    def close_spider(self, spider):
        pass
