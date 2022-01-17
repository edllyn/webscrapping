import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/list/ls095964455/']

    def parse(self, response):
        for series in response.css('.mode-detail'):
            yield{
                'titulo': series.css('.lister-item-header a::text').get(),
                'ano': response.css('.text-muted.unbold ::text').get(),
                'nota': response.css('.ipl-rating-star.small .ipl-rating-star__rating ::text').get()
            }
