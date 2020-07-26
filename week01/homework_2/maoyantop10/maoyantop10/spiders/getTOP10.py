# -*- coding: utf-8 -*-
import scrapy
from week01.homework_2.maoyantop10.maoyantop10.items  import Maoyantop10Item
from scrapy.selector import Selector


class Gettop10Spider(scrapy.Spider):
    name = 'getTOP10'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def start_requests(self):		# 固定的名字
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)	


    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # for movie in movies:
        for i in range(10):
            item = Maoyantop10Item()
            movie_name = movies[i].xpath('./div/span/text()').extract_first()
            
            movie_type_rawlist = movies[i].xpath('./div[2]/text()').extract()
            movie_type = movie_type_rawlist[1].strip()
           
            movie_start_time_rawlist = movies[i].xpath('./div[4]/text()').extract()
            movie_start_time = movie_start_time_rawlist[1].strip()

            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_start_time'] = movie_start_time
            yield item