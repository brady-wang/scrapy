# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from img.items import ImgItem

class LabSpider(CrawlSpider):
    name = 'lab'
    allowed_domains = ['scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    rules = (
        Rule(LinkExtractor(allow=r'archives/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        try:

            item = ImgItem()
            imgurls = response.xpath('//*[@id="main"]/article/div//img/@src').extract()
            item['imgurl'] = imgurls
            yield item
        except Exception as e:
            print(str(e))
