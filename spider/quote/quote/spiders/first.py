# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["toscrape.com"]

    def start_requests(self):

        urls = [
            'http://quotes.toscrape.com/',
        ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        try:

            items = response.xpath("//div[@class='quote']").extract()
            with open("data.html",'a',encoding='utf-8') as f:
                for quote in items:
                    text = Selector(text=quote).xpath("//span[@class='text']/text()").extract_first()
                    author = Selector(text=quote).xpath("//small[@class='author']/text()").extract_first()
                    f.write(text)
                    f.write('\n')
                    f.write("作者："+ author)
                    f.write('\n-------------------------\n')
                    print(text)
            print("crawl page " + response.url)
            nextPage = response.xpath("/html/body/div/div[2]/div[1]/nav/ul/li[@class='next']/a/@href").extract_first()
            if nextPage is not None:
                url = response.urljoin(nextPage)
                yield scrapy.Request(url=url,callback=self.parse)

            f.close()
        except Exception as f:
            print(f)
