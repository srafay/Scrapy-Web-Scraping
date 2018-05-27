# -*- coding: utf-8 -*-
import scrapy


class GetsubcategoriesSpider(scrapy.Spider):
    name = 'getSubCategories'
    allowed_domains = ['www.alternativeto.net/category/games/']
    start_urls = ['http://alternativeto.net/category/games//']

    def parse(self, response):
        pass
