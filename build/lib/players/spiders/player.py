# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http.request import Request

class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["sports.yahoo.com"]
    start_urls = ['http://sports.yahoo.com/']

    def parse(self, response):
        yield Request("http://sports.yahoo.com/mlb/players/9558/", callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        item = playerProp()
        item['name'] = response.xpath('//span[@data-reactid="10"]/text()').extract()
        item['team'] = response.xpath('//a[@data-reactid="22"]/text()').extract()
        item['num'] = response.xpath('//span[@data-reactid="16"]/text()').extract()
        item['pos'] = response.xpath('//span[@data-reactid="18"]/text()').extract()
        item['avg'] = response.xpath('//div[@data-reactid="26"]/text()').extract()
        item['hr'] = response.xpath('//div[@data-reactid="29"]/text()').extract()
        item['rbi'] = response.xpath('//div[@data-reactid="32"]/text()').extract()
        item['run'] = response.xpath('//div[@data-reactid="35"]/text()').extract()

        yield item


class playerProp(scrapy.Item):
    name = scrapy.Field()
    team = scrapy.Field()
    num = scrapy.Field()
    pos = scrapy.Field()
    avg = scrapy.Field()
    hr  = scrapy.Field()
    rbi = scrapy.Field()
    run = scrapy.Field()
