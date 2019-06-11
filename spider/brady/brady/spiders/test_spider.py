#coding:utf-8
import scrapy

class test_spider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]


        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        page = response.url.split('/')[-2]
        file_name = "e:/crawl/test_%s.html" % page
        with open(file_name,'wb') as f:
            f.write(response.body)
        self.log("save file success:%s" % file_name)
        print("save file success:%s" % file_name)


