# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class A163Spider(CrawlSpider):
    name = '163'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath('//*[@id="g-topbar"]/div[1]/div/h1/a/text()').extract_first()
        print(i)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
