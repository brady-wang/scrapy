# -*- coding: utf-8 -*-
import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['test2.com']
    start_urls = ['http://test2.com/']

    def parse(self, response):
        pass
