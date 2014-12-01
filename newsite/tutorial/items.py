# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    price = scrapy.Field()
    address = scrapy.Field()
    miles = scrapy.Field()
    name = scrapy.Field()
