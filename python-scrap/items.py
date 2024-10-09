# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class MovieItemLoader(ItemLoader):
    pass

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Fieldi()

    title=scrapy.Field()
    duration=scrapy.Field()
    original_title=scrapy.Field()

    pass

class VideoCardItem(scrapy.Item):
    nome=scrapy.Field()
    preco=scrapy.Field()
    disponibilidade = scrapy.Field()
    url = scrapy.Field

    pass
