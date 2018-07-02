# -*- coding: utf-8 -*-
import scrapy, cookielib
from scrapy.http.request import Request



class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/search?q=zakir%20khan']

    def __init__(self, *args, **kwargs):
        self.proxy_pool = ['200.255.122.174:8080', '175.196.224.242:8080', '80.150.65.6:808', '81.211.3.114:8080', '182.74.34.134:8080', '45.113.66.33:8080', '115.178.99.91:53281']

    def parse(self, response):
        # for tweet in response.css('.tweet-container'):
        url = response.url

        cookieJar = cookielib.CookieJar()
        headers = [
            ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]
        
        yield{
            'tweets': response.css('.tweet-container').extract()
        }

    		
