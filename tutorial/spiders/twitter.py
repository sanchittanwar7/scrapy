# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request


class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/search?q=zakir%20khan']

    def __init__(self, *args, **kwargs):
        self.proxy_pool = ['200.255.122.174:8080', '175.196.224.242:8080', '80.150.65.6:808', '81.211.3.114:8080', '182.74.34.134:8080', '45.113.66.33:8080', '115.178.99.91:53281']

    def parse(self, response):
        yield{
            'tweets': response.css('.tweet-container').extract()
        }

    		
