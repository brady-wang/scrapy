# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Lab1Spider(CrawlSpider):
    name = 'lab1'
    allowed_domains = ['scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'/tag/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/page/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/archives/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        with open("lab1.html", 'a', encoding='utf-8') as f:
            author = response.xpath('//*[@id="main"]/article/h1/a/text()').extract_first()
            content = response.xpath('//*[@id="main"]/article/div//p/text()').extract_first()
            tag = response.xpath('//*[@id="main"]/article/p//a/text()').extract()
            tag = ','.join(tag)
            f.write(content)
            f.write('\n作者：' + author)
            f.write('\n')
            f.write('标签：' + tag)
            f.write('\n-----------------------------------------\n')
            print(content)
        f.close()
