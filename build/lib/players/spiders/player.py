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
