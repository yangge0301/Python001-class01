import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem
class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        n = 0
        maoyan_elements = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for element in maoyan_elements:
            if n < 10:
                item = MaoyanItem()
                x = element.xpath('./div[1]/span[1]/text()').extract()[0]
                y = element.xpath('./div[2]/text()').extract()[1].replace(" ", "").replace("\n", "")
                z = element.xpath('./div[4]/text()').extract()[1].replace(" ", "").replace("\n", "")
                item['film_name'] = x
                item['film_type'] = y
                item['film_date'] = z
                n = n+1
                yield item
