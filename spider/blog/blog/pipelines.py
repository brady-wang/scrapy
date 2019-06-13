# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class BlogPipeline(object):
    def __init__(self):
        self.file = open('a.html', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        print(item)
        self.file.write(item['title'])
        self.file.write(' 时间'+item['time'])
        self.file.write('\n')
        self.file.write(item['subcontent'])
        self.file.write('\n -------------------- \n')
        return item
