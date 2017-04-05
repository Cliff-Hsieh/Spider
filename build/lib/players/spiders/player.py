# -*- coding: utf-8 -*-
import scrapy


class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["sports.yahoo.com"]
    start_urls = ['http://sports.yahoo.com/']

    def parse(self, response):
        item = playerProp()

class playerProp(scrapy.Item):
    name = scrapy.Field()
    team = scrapy.Field()
    num = scrapy.Field()
    pos = scrapy.Field()
    avg = scrapy.Field()
    hr  = scrapy.Field()
    rbi = scrapy.Field()
    run = scrapy.Field()
