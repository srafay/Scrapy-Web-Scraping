# -*- coding: utf-8 -*-
import scrapy

class GetsubcategoriesSpider(scrapy.Spider):
    name = 'getSubCategories'

    def __init__(self, category=None, *args, **kwargs):
	global categoryToBeScrapped
	categoryToBeScrapped = category
	super(GetsubcategoriesSpider, self).__init__(*args, **kwargs)
	self.start_urls = ['http://alternativeto.net/category/' + category]

    # Entry point for the spider
    def parse(self, response):
	subCategoryIndex = 0
	for href in response.css("div[class='content-box']>h2>a[href^='//alternativeto.net/category']::attr(href)"):
		url = href.extract()
		url = "https://" + url[2:]
		subCategory = response.css("div[class='content-box']>h2>a[href^='//alternativeto.net/category']::text").extract()[subCategoryIndex]
		subCategoryIndex = subCategoryIndex + 1
		yield scrapy.Request(url, callback=self.parse_category, meta={'subCategory': subCategory})

    # Method for parsing a category
    def parse_category(self, response):
	subCategory = response.meta.get('subCategory')
	for href in response.css("a[data-link-action='DefaultSort']::attr(href)"):
		url = href.extract()
		yield scrapy.Request("https://alternativeto.net" + url, callback=self.parse_item, meta={'subCategory': subCategory})

    # Method for parsing an item
    def parse_item(self, response):
	name = response.css('#appHeader > div:nth-child(1) > div:nth-child(1) > h1:nth-child(2)::text').extract()
	description = response.css('.item-desc > p:nth-child(1)::text').extract()
	votes = response.css('.like-box-wrapper > div:nth-child(2) > span:nth-child(1)::text').extract()
	lic = response.css('.labels > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text').extract()
	platforms = response.css("li.label::text").extract()
	subCategory = response.meta.get('subCategory')

        #Give the extracted content row wise
        for item in zip(lic, description, votes, name):
            #create a dictionary to store the scraped info
            scraped_info = {
                'license' : item[0],
                'description' : item[1],
                'votes' : item[2],
                'name' : item[3],
                'Sub-Category' : subCategory,
                'platforms' : str(platforms),
		'Category' : categoryToBeScrapped,
            }
            #yield or give the scraped info to scrapy
            yield scraped_info

