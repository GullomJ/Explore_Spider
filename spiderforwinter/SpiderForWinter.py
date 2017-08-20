# !usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Aisuko'
# date:2017-08-16

import urllib2
import os
import sys
import csv


class GetImage(object):
    # doc：后面加的是检索号
    __doc__ = '1102f8a5-db49-4d90-935e-93291a251a80'

    # __init__:初始化对象
    def __init__(self):
        """

        """
        self.excel_name, self.excel_column_name = self.get_input_from_client()
        self.image_list = self.get_picurl_from_source()

    def get_pic(self):
        """

        :return:
        """
        if self.image_list:
            for x, imng_url in enumerate(self.image_list):
                try:
                    page = urllib2.urlopen(imng_url)
                    print 'Get picture successed'
                except Exception as e:
                    print e.message
                else:
                    data = page.read()
                    print 'Load picture successed, download picture right now, please wait...'
                    with open('img/{num}.jpeg'.format(num=x), 'wb') as f:
                        f.write(data)
                        print 'image-{id} download complete'.format(id=x)
        else:
            print 'Picture list is None'

    def get_picurl_from_source(self):
        """

        :return: 返回图片
        """
        try:
            with open(self.excel_name) as imagecv:
                reader = csv.DictReader(imagecv)
                list_pic = [row.get(self.excel_column_name) for row in reader]
                return list_pic
        except Exception as e:
            raise MyException(message=e.message).re_message

    def get_excel_path(self, excel_name):
        try:
            local_path = sys.path.__getitem__(2) + '\\spiderforwinter\\{excelname}'.format(
                excelname=excel_name)
            assert os.path.exists(local_path)
        except AssertionError as e:
            raise MyException(message=e.message).re_message
        except Exception as e:
            raise MyException(message=e.message).re_message
        else:
            return local_path

    def get_input_from_client(self):
        try:
            excel_name = raw_input('Please input csv name:')
            excel_column_name = raw_input('Please input Excel_column_name:')

            assert excel_name is not None, excel_column_name is not None
            path = self.get_excel_path(excel_name=excel_name)
            assert path
            return excel_name, excel_column_name
        except AssertionError as e:
            raise MyException(message='Please enter the correct information or check excel name. ').re_message
        except Exception as e:
            raise MyException(message=e.message).re_message


class MyException(BaseException):
    def __init__(self, message=None):
        self.message = message if message else 'System Error'

    @property
    def re_message(self):
        return self.message


if __name__ == '__main__':
    GetImage().get_pic()
    # 656开始
    # OriginalURL

    # MyException().re_message
