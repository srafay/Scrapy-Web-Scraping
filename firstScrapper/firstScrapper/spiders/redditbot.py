# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.u1yomz-1.dbIjBo::text').extract()
        votes = response.css('.s15nnxl5-1.bIKsmY::text').extract()
        times = response.css('.s1oavwx2-5.fCgWlW::text').extract()
        comments = response.css('.jb5xhx-1.jlbfUu::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
