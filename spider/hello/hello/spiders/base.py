#encoding=utf-8
import io

import scrapy

class BaseSpider(scrapy.Spider):
    name = 'base'
    allowed_domains = ['scrapyd.cn']
    start_urls = [
                'http://lab.scrapyd.cn/page/1/',
            ]

    def parse(self, response):
        content = response.xpath("//div[@class='quote post']//span[@class='text']/text()").extract()
        with io.open("lab.html", 'w', encoding='utf-8') as f:
            for i in content:
                f.write(i+"\n")
                print ('保存文件: lab.html')
            f.close()