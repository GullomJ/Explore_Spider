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
        self.excel_name, self.excel_column_name = self.get_input_from_client()
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
                        print 'image-{id} download complete'.format(id=x)
        else:
            print '图片地址列表没有获取到'

    def get_picurl_from_source(self):
        try:
            with open(self.excel_name) as imagecv:
                reader = csv.DictReader(imagecv)
                list_pic = [row.get(self.excel_column_name) for row in reader]
                return list_pic
        except Exception as e:
            raise e.message

    def get_excel_path(self):
        try:
            local_path = sorted(sys.path[2], reverse=True)[1] + '\\spiderforwinter\\{excelname}'.format(
                excelname=self.excel_name)
            assert os._exists(local_path) == True
        except AssertionError as e:
            raise 'Excel 不存在' + e.message
        except Exception as e:
            raise e.message
        else:
            return local_path

    def get_input_from_client(self):
        try:
            excel_name = raw_input('请输入Excel:')
            excel_column_name = raw_input('请输入Excel_column_name:')

            assert excel_name is not None, excel_column_name is not None

            return excel_name, excel_column_name
        except AssertionError as e:
            raise '请按照规则输入'
        except Exception as e:
            raise '异常信息:' + e.message


if __name__ == '__main__':
    GetImage().get_pic()
