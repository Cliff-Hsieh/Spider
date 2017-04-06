# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http.request import Request
from scrapy.selector import Selector

class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["sports.yahoo.com"]
    start_urls = ['http://sports.yahoo.com/mlb/teams/chc/roster/']

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="D(ib) Va(m) Py(cell-padding-y)"]/a/@href').extract()

        for site in sites:
            if 'http://' not in site:
                site = response.urljoin(site)
                yield Request( site, callback=self.parse_detail_page)


    def parse_detail_page(self, response):
        item = playerProp()
        item['name'] = response.xpath('//span[@data-reactid="10"]/text()').extract()
        item['team'] = response.xpath('//div[@data-reactid="21"]/a[@data-reactid="22"]/text()').extract()
        item['num'] = response.xpath('//span[@data-reactid="16"]/text()').extract()[0].split("#")[1]
        item['pos'] = response.xpath('//span[@data-reactid="18"]/text()').extract()[0]

        pitcher = ["SP", "RP"]
        if item['pos'] not in pitcher:
            item['avg'] = response.xpath('//div[@data-reactid="26"]/text()').extract()
            item['hr'] = response.xpath('//div[@data-reactid="29"]/text()').extract()
            item['rbi'] = response.xpath('//div[@data-reactid="32"]/text()').extract()
            item['run'] = response.xpath('//div[@data-reactid="35"]/text()').extract()
        else:
            item['win'] = response.xpath('//div[@data-reactid="26"]/text()').extract()
            item['era'] = response.xpath('//div[@data-reactid="32"]/text()').extract()
            item['so'] = response.xpath('//div[@data-reactid="35"]/text()').extract()
            item['bb'] = response.xpath('//div[@data-reactid="38"]/text()').extract()

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
    win = scrapy.Field()
    era = scrapy.Field()
    so  = scrapy.Field()
    bb  = scrapy.Field()
