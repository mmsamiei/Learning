import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2017']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield{
                    'name':brickset.css(NAME_SELECTOR)[-1].extract(),
                    'pieces':brickset.xpath(PIECES_SELECTOR).extract_first(),
                    'image':brickset.css(IMAGE_SELECTOR).extract_first()
            }



