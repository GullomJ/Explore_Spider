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
        # 获取csv文件名称，列名
        self.excel_name, self.excel_column_name = self.get_input_from_client()
        # 获取图片的url listS
        self.image_list = self.get_picurl_from_source()

    def get_pic(self):
        """

        :return:
        """
        if self.image_list:
            # 循环获取图片的URL
            for x, imng_url in enumerate(self.image_list):
                try:
                    page = urllib2.urlopen(imng_url)
                    print 'Get picture successed'
                except Exception as e:
                    print e.message
                else:
                    # 读取带有图片的网页
                    data = page.read()
                    print 'Load picture successed, download picture right now, please wait...'
                    # 把图片保存到本地
                    with open('img/{num}.jpeg'.format(num=x), 'wb') as f:
                        f.write(data)
                        print 'image-{id} download complete'.format(id=x)
        else:
            print 'Picture list is None'

    def get_picurl_from_source(self):
        """
        从csv文件中读取图片的url地址
        :return: 返回图片
        """
        try:
            # 打开csv文件
            with open(self.excel_name) as imagecv:
                # 读取为对象
                reader = csv.DictReader(imagecv)
                # 循环获取图片URL为list集合
                list_pic = [row.get(self.excel_column_name) for row in reader]
                return list_pic
        except Exception as e:
            raise MyException(message=e.message).re_message

    def get_excel_path(self, excel_name):
        try:
            # 检查csv文件的路径
            local_path = sys.path.__getitem__(2) + '\\spiderforwinter\\{excelname}'.format(
                excelname=excel_name)
            # 断言路径不能为None,否则程序终止
            assert os.path.exists(local_path)
        except AssertionError as e:
            raise MyException(message=e.message).re_message
        except Exception as e:
            raise MyException(message=e.message).re_message
        else:
            return local_path

    def get_input_from_client(self):
        """
        在控制台与用户交互，并获取csv文件的名称和需要使用的列名
        :return:
        """
        try:
            # 获取控制台输入的csv_name和csv文件的列表
            excel_name = raw_input('Please input csv name:')
            excel_column_name = raw_input('Please input Excel_column_name:')
            # 断言 变量都不为空
            assert excel_name is not None, excel_column_name is not None
            # 对csv文件的存在路径进行检查
            path = self.get_excel_path(excel_name=excel_name)
            # 断言路径存在
            assert path
            # 返回csv文件名称和列名称
            return excel_name, excel_column_name
        except AssertionError as e:
            # try方法中的断言异常被捕获，这里是出口
            raise MyException(message='Please enter the correct information or check excel name. ').re_message
        # 捕获所有异常，这么做不明知
        except Exception as e:
            #
            raise MyException(message=e.message).re_message


class MyException(BaseException):
    __doc__ = '自定义异常类型，对程序的异常进行处理'

    def __init__(self, message=None):
        """
        类初始化函数，初始化类的message属性，对其进行赋值
        :param message:需要打印的异常信息
        """
        self.message = message if message else 'System Error'

    @property
    def re_message(self):
        """
        使用@property装饰器，指定re_message函数为类的特性
        :return:
        """
        return self.message


# 程序入口，实例化GetImage对象，并调用对象的获取图片方法
if __name__ == '__main__':
    GetImage().get_pic()
    # 656开始
    # OriginalURL

    # MyException().re_message
