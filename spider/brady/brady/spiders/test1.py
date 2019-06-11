#coding:utf-8
import scrapy

class test1(scrapy.Spider):

    name = "test1_spider"

    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        page = response.url.split('/')[-2]
        file_name = "e:/crawl/test_%s.html" % page
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log("save file success:%s" % file_name)
        print("Save file success:%s" % file_name)
