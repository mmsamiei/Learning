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

            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                        # once you have gotten the HTML from this page pass it back to this method"
                        )
                # scrapy.Request means that "Hey! scrawl this page! :D"


