# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BokeyuanSpider(CrawlSpider):
    name = 'bokeyuan'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/php-linux/']

    rules = (
        Rule(LinkExtractor(allow=r'php-linux/default.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        items = response.xpath("//div[@class='day']").extract()
        with open("bokeyuan.html", 'a', encoding='utf-8') as f:
            for quote in items:
                i['time']  = Selector(text=quote).xpath("//div[@class='dayTitle']/a/text()").extract_first()
                i['title'] = Selector(text=quote).xpath("//div[@class='postTitle']/a/text()").extract_first()
                i['subcontent'] = Selector(text=quote).xpath("//div[@class='postCon']/div/text()").extract_first()
        print("crawl page " + response.url)
        return i
