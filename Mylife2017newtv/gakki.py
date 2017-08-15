#! usr/bin/env python
# ! -*- coding:utf-8 -*-

'__author__ = atsukon_lee'

import urllib
import urllib2
import re


class gakkisp(object):
    # 获取网址
    __doc__ = "爬取评论"

    def geturl(self):
        u = "https://movie.douban.com/subject/26816519/discussion/614421639/"
        page = urllib.urlopen(u)

        if page is not None:
            return page.read().decode('utf-8')
        else:
            raise Exception("page is None")

    def getpicture(self, page):
        list = re.findall(r'<p class="">(.*?)</p>', page, re.S)
        timelist = re.findall(r'<span class="">(.*?)</span>', page, re.S)
        authorlist = re.findall(r'<a href="https://www.douban.com/people/  class"  ">(.*?)</a>', page, re.S)
        if len(list) == 0 or len(timelist) == 0:
            raise Exception("长度为0")
        else:
            return list, timelist


    def show(self, list, timelist):
        print
        u"我Gakki新剧的评论:"
        n = 0
        while (n < len(list) and n < len(timelist)):
            print
            u"评论内容：" + list[n] + u"时间：" + timelist[n]
            # print u"评论内容: {0}"+u" 时间：{1}".format(list[n],timelist[n])
            n = n + 1


gakki = gakkisp()
page = gakki.geturl()
list, timelist = gakki.getpicture(page)
gakki.show(list, timelist)
