# -*- coding: utf-8 -*-
import scrapy


class NamzadibotSpider(scrapy.Spider):
    name = 'namzadiBot'
    #allowed_domains = ['https://www.ninisite.com/discussion/forum/115/%d9%86%d8%a7%d9%85%d8%b2%d8%af%db%8c']
    start_urls = ['https://www.ninisite.com/discussion/forum/115/%d9%86%d8%a7%d9%85%d8%b2%d8%af%db%8c/',
    'https://www.ninisite.com/discussion/forum/114/%d8%ae%d8%a7%d8%b7%d8%b1%d8%a7%d8%aa-%d8%a7%d9%93%d8%b4%d9%86%d8%a7%d9%8a%d9%94%db%8c']

    def parse(self, response):
        titles = response.css('.topic_subject::text').extract()
        author = response.css('.last-topic-user a::text').extract()
        link = response.css('.topic--title').xpath('..').xpath('./@href').extract()
        for item in zip(titles, author, link):
            scraped_info = {
                    'titles':item[0],
                    'author':item[1],
                    'link':"https://www.ninisite.com"+item[2]
                    }    
            yield scraped_info

        next_page = response.css('.page-link[title="Next page"]::attr(href)').extract_first()
        if next_page:
            print(next_page)
            yield response.follow(
                next_page,
                callback=self.parse
                )
