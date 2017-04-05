# -*- coding: utf-8 -*-
import scrapy


class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["sports.yahoo.com"]
    start_urls = ['http://sports.yahoo.com/']

    def parse(self, response):
        pass
