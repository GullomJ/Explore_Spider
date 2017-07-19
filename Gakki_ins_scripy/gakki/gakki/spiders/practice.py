# -*- coding: utf-8 -*-
import scrapy


class PracticeSpider(scrapy.Spider):
    name = 'practice'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/111322']

    def parse(self, response):
        '''

        :param response:
        :return:
        '''
        re_select = response.xpath('//*[@id="post-111322"]/div[1]/h1')

        for key,sel in enumerate(re_select):
            id =key
            pic_url=sel.extract()
            print str(id)+pic_url
