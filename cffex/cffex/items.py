# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CffexItem(scrapy.Item):
    file_url = scrapy.Field()
    file = scrapy.Field()
