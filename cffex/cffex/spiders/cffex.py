# -*- coding: utf-8 -*-
import scrapy
from cffex.items import CffexItem
import datetime
class CffexSpider(scrapy.Spider):
    name = 'cffex'
    start_urls = ['http://www.cffex.com.cn/lssjxz/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', 'encoding': 'unicode'
    }
    endYear = datetime.datetime.now().year 
    endMonth = datetime.datetime.now().month

    def parse(self, response):
        item = CffexItem()
        def f(x): return '0' + str(x) if x < 10 else str(x)

        start_urls = ['http://www.cffex.com.cn/sj/historysj/2010' +
                      f(i) + '/zip/2010' + f(i) + '.zip' for i in range(4, 13)]

        for year in range(2011, self.endYear + 1):
            start_urls += ['http://www.cffex.com.cn/sj/historysj/' + str(year) +
                           f(i) + '/zip/' + str(year) + f(i) + '.zip' for i in range(1, 13)]

        for url in start_urls:
            item['file_url'] = url
            yield item
            if url.split('/')[-1] == '{}{}.zip'.format(self.endYear,self.endMonth):
                break
