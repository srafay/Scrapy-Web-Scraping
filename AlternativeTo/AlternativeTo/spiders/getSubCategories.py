# -*- coding: utf-8 -*-
import scrapy


class GetsubcategoriesSpider(scrapy.Spider):
    name = 'getSubCategories'
    start_urls = ['http://alternativeto.net/category/games//']

    # Entry point for the spider
    def parse(self, response):
	for href in response.css("div[class='content-box']>h2>a[href^='//alternativeto.net/category']::attr(href)"):
		url = href.extract()
		url = "https://" + url[2:]
		category = response.css("div[class='content-box']>h2>a[href^='//alternativeto.net/category']::text")
		yield scrapy.Request(url, callback=self.parse_category)

    # Method for parsing a category
    def parse_category(self, response):
	for href in response.css("a[data-link-action='DefaultSort']::attr(href)"):
		url = href.extract()
		yield scrapy.Request("https://alternativeto.net" + url, callback=self.parse_item)

    # Method for parsing an item
    def parse_item(self, response):
	name = response.css('#appHeader > div:nth-child(1) > div:nth-child(1) > h1:nth-child(2)::text').extract()
	description = response.css('.item-desc > p:nth-child(1)::text').extract()
	votes = response.css('.like-box-wrapper > div:nth-child(2) > span:nth-child(1)::text').extract()
	lic = response.css('.labels > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text').extract()
	platforms = response.css("li.label::text").extract()

        #Give the extracted content row wise
        for item in zip(name, description, votes, lic):
            #create a dictionary to store the scraped info
            scraped_info = {
                'name' : item[0],
                'description' : item[1],
                'votes' : item[2],
                'license' : item[3],
                'platforms' : str(platforms),
            }
            #yield or give the scraped info to scrapy
            yield scraped_info

