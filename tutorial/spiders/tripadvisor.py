# -*- coding: utf-8 -*-
import scrapy
import random 
from scrapy.http.request import Request
import requests

class TweetScraper(scrapy.Spider):
	name = 'tripadvisor'
	allowed_domains = ['tripadvisor.in']

	def __init__(self, location):
		self.location = location
		self.query = ''
		self.url = "https://www.tripadvisor.in/Hotels-g304552-%sShimla_Shimla_District_Himachal_Pradesh-Hotels.html"
		self.start_url = "https://www.tripadvisor.com/TypeAheadJson?action=API&types=geonbrhdhoteltheme_park&filter=&legacy_format=true&urlList=true&strictParent=true&query=%s&max=6&name_depth=3&interleaved=true&scoreThreshold=0.5&strictAnd=false&typeahead1_5=true&disableMaxGroupSize=true&geoBoostFix=true&geoPages=&injectList=&neighborhood_geos=true&details=true&rescue=true&uiOrigin=trip_search_Hotels&source=trip_search_Hotels"
		self.sno = 0
		self.custom_url = ''

	def start_requests(self):
		url = self.start_url % self.location
		r = requests.get(url=url)
		r = r.json()
		s = r[0]['url'][8:].split('-')
		dekhio = "https://www.tripadvisor.in/Hotels-" + str(s[1]) + "-%s" + str(s[2]) 
		url = 'https://www.tripadvisor.in/Hotels-g%s-Shimla_Shimla_District_Himachal_Pradesh-Hotels.html' % r[0]['value']
		self.url = dekhio
		yield scrapy.Request(url, callback=self.parse_page)

	def parse_page(self, response):
		urls = response.css('div.listing_title > a::attr(href)').extract()
		for url in urls:
			url = 'https://www.tripadvisor.in' + url
			self.custom_url = url.split('Reviews')[0] + 'Reviews%s' + url.split('Reviews')[1]
			yield scrapy.Request(url=url, callback=self.parse_reviews)

		# self.sno += 30
		# self.query = 'oa%s-' % self.sno
		# url = self.url % (self.query)
		# yield scrapy.Request(url, callback=self.parse_page)

	def parse_reviews(self, response):
		reviews = response.css('div.review-container')
		print("------------------------------------------------------")
		print(response.css('h1#HEADING::text').extract_first())
		print("------------------------------------------------------")
		pass
		for review in reviews:
			yield{
				'hotel_name': response.css('h1#HEADING::text').extract_first(),
				'user_name' : review.css('div.info_text > div::text').extract_first(),
				'user_contribution' : review.css('span.badgetext::text').extract_first(),
				'heading' : review.css('span.noQuotes::text').extract_first(),
				'review' : review.css('p.partial_entry::text').extract_first()
			}
		# offset = response.css('a.next::attr(data-offset)').extract_first()
		# if offset != None:
		# 	print(offset)
		# 	next_page_url = self.custom_url % ('-or%s' % offset)
		# 	print(next_page_url)
		# 	yield scrapy.Request(url=next_page_url, callback=self.parse_reviews)



	