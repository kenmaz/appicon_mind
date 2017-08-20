# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CrawlerItem(scrapy.Item):
    image_urls = Field()
    images = Field()
    app_name = Field()
    app_url = Field()
    genre_name = Field()
    descriptions = Field()
