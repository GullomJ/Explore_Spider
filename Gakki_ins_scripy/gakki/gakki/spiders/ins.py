#! usr/bin/env python2.7
# -*- coding: utf-8 -*-

# __author__ = 'Gakki的男友 Aisuko'
import json
import os

from datetime import datetime
import scrapy
from urlparse import urlparse
import random
from gakki.items import GakkiItem as FileItem


class InsSpider(scrapy.Spider):
    name = 'ins'
    allowed_domains = ['www.instagram.com/gakkiilove']
    start_urls = ['http://www.instagram.com/gakkiilove/']

    def __init__(self):
        '''
        初始化函数
        '''
        pass

    def parse(self, response):
        '''
        bfdf1be0-4e9d-4d24-ad66-f04a395d36f2
        获取ins pic 2017-07-19 22:03
        表达式----[ //div[@class="mine"]: 选择所有包含 class="mine" 属性的 div 标签元素 ]
        :param response:
        :return:
        '''
        try:
            res = response.xpath('//script/text()').re(r'window._sharedData = \s*(.*);$')[0].encode("utf-8")
            data = json.loads(res)
            u = data["entry_data"]["ProfilePage"][0]["user"]
            for n in u["media"]["nodes"]:
                title = ""
                if "caption" in n:
                    title = n["caption"]
                filename = u'我老婆' + datetime.now().strftime('%y%m%d%H%M%S') + str(random.randint(0, 1000))
                thumb = "%s/img/%s" % (1, filename)
                storage = ""
                if n["is_video"]:
                    storage = "%s/vod/%s" % (1, filename)
                    url = "https://www.instagram.com/p/%s/?taken-by=%s&__a=1" % (n["code"], u["username"])
                    req = scrapy.Request(url, callback=self.get_instagram_video)
                    if req:
                        req.meta["filename"] = filename + ".mp4"
                        req.meta["proxy"] = True
                        req.meta["storage"] = storage
                        # TODO 保存到本地
                        yield req
                    else:
                        # TODO 需要发请求
                        pass
                item = FileItem()
                item["pic_url"] = [n["display_src"]]
                item["filepath"] = thumb
                item["filename"] = filename + ".jpg"
                item["content_type"] = "image/jpeg"
                item["proxy"] = True
                print item
        except Exception as e:
            print e.message
        else:
            pass
        finally:
            print 'Spider Complete'

    def get_instagram_video(self, response):
        '''
        bfdf1be0-4e9d-4d24-ad66-f04a395d36f2
        获取ins video 2017-07-19 22:03
        待调试
        :param response:
        :return:
        '''
        try:
            data = json.loads(response.body)
            item = FileItem()
            item["file_urls"] = [data["media"]["video_url"]]
            item["filepath"] = response.meta["storage"]
            item["filename"] = response.meta["filename"]
            item["content_type"] = "video/mpeg4"
            item["proxy"] = True
            yield item
        except Exception as e:
            pass
        else:
            pass
        finally:
            pass
