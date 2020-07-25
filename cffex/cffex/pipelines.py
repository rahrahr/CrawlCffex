# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.files import FilesPipeline
from scrapy.spiders import Request
from urllib.parse import urlparse
import os


class CffexPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item.get(self.files_urls_field, []), meta=item)

    def file_path(self, request, response=None, info=None):
        name = request.meta['file_url'].split('/')[-1]
        return name
