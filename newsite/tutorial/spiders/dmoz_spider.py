import scrapy

from tutorial.items import DmozItem
from scrapy import log
class PriceSpider(scrapy.Spider):
    name = "price"
    allowed_domains = ["aol.com"]

    def __init__(self, category=None, *args, **kwargs):
        super(PriceSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://autos.aol.com/%s-gas-prices/' % category]

    def parse(self, response):
        for sel in response.xpath('//div[@class="clsShow"]/div'):
            item = DmozItem()
            item['price'] = sel.xpath('div[@class="gPrice"]/text()').extract()
            item['address'] = sel.xpath('div[@class="gAddress"]/text()').extract()
            item['name'] = sel.xpath('div[@class="gStatn"]/a/text()').extract()
            log.msg(item['name'])
            yield item