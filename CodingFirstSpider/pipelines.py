# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class HduPipeline(object):
    full_json = ''

    def __init__(self):
        self.filename = open("hdu.json", "wb+")
        self.filename.write("[".encode("utf-8"))

    def process_item(self, item, spider):
        json_text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.full_json += json_text
        return item

    def close_spider(self, spider):
        self.filename.write(self.full_json.encode("utf-8"))
        self.filename.write("]".encode("utf-8"))
        self.filename.close()
