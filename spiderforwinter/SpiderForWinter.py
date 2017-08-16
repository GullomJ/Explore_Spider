# !usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Aisuko'
# date:2017-08-16

import urllib
import urllib2
import os
import sys
import csv


class GetImage(object):
    __doc__ = '1102f8a5-db49-4d90-935e-93291a251a80'

    def __init__(self):
        self.image_list = self.get_picurl_from_source()

    def get_pic(self):
        '''
        基于python2
        :return:
        '''
        if self.image_list:
            for x, imng_url in enumerate(self.image_list):

                try:
                    page = urllib2.urlopen(imng_url)
                except Exception as e:
                    print e.message
                else:
                    data = page.read()
                    with open('img/{num}.jpeg'.format(num=x), 'wb') as f:
                        f.write(data)
        else:
            print '图片地址列表没有获取到'

    def get_picurl_from_source(self):
        with open('images.csv') as imagecv:
            reader = csv.DictReader(imagecv)
            list_pic = [row.get('OriginalURL') for row in reader]
            return list_pic


if __name__ == '__main__':
    GetImage().get_pic()
