# -*- coding: utf-8 -*-
import scrapy


class AlternativetoSpider(scrapy.Spider):
    name = 'alternativeTo'
    allowed_domains = ['www.alternativeto.net/software/youtube/']
    start_urls = ['http://alternativeto.net/software/youtube//']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('a[data-link-action="Alternatives"]::text').extract()
	description = response.css('p[class="text"]::text').extract()
	votes = response.css('span[class="num"]::text').extract()
	license = response.css('span[class^=pricing-]::text').extract()

	#Skip the first vote because its not relevant 
	votes = votes[1:]
	#Skip the first license type because its not relevant 
	license = license[1:]
       
        #Give the extracted content row wise
        for item in zip(titles, description, votes, license):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'description' : item[1],
                'votes' : item[2],
                'license' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
