# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['www.86pm25.com']
    start_urls = ['http://www.86pm25.com/city/beijing.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        weilai = response.xpath('//div[@class="weilai"]/table/tbody/tr/descendant-or-self::*/text()').extract()
        for d in weilai:
            print d
        pass
