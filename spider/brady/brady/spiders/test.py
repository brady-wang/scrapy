# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class test(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
        ]


        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):

        items = response.xpath('//*[@class="quote post"]').extract();
        with open("test.html",'w',encoding='utf-8') as f :

            for item in items:
                content = Selector(text=item).xpath('//span[1]/text()').extract_first()
                author  = Selector(text=item).xpath('//span[2]/small/text()').extract_first()
                tag  = Selector(text=item).xpath("//div[@class='tags']/a/text()").extract()
                tag = ','.join(tag)
                f.write(content)
                f.write('   作者：' + author)
                f.write('\n')
                f.write('标签：' + tag)
                f.write('\n-----------------------------------------\n')
                print(content)
        f.close()


