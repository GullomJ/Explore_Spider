#! usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# bfdf1be0-4e9d-4d24-ad66-f04a395d36f2
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class GakkiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id = Field()
    pic_url = Field()
    filepath = Field()
    filename = Field()
    content_type = Field()
    proxy = Field()
    memo = Field()
    memo1 = Field()
    memo2 = Field()
