# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.title::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
