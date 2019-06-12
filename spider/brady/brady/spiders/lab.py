# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LabSpider(CrawlSpider):
    name = 'lab'
    allowed_domains = ['scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'/lab.scrapyd.cn/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        print(response.url)
        items = response.xpath('//*[@class="quote post"]').extract();
        with open("lab.html", 'a', encoding='utf-8') as f:
            for item in items:
                content = Selector(text=item).xpath('//span[1]/text()').extract_first()
                author = Selector(text=item).xpath('//span[2]/small/text()').extract_first()
                tag = Selector(text=item).xpath("//div[@class='tags']/a/text()").extract()
                tag = ','.join(tag)
                f.write(content)
                f.write('\n作者：' + author)
                f.write('\n')
                f.write('标签：' + tag)
                f.write('\n-----------------------------------------\n')
                print(content)
        f.close()