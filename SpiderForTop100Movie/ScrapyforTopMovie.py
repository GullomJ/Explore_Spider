# !usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'libw '

"""
2016-7-31
"""

import urllib2
import re
import string
import os
import sys




class Moviecrary(object):
    __doc__ = " 本类主要用于抓取豆瓣前100的电影名称 "

    def __init__(self):
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self.top_num = 1
        # 添加路径属性，以后拓展为相对路径
        self.pathstr = os.path.abspath(os.path.dirname(sys.argv[0]))
        print ("Ready to work")

    # 获取当前页面
    def get_page(self, cur_page):
        url = self.cur_url
        try:
             pageone = urllib2.urlopen(url.format(page = (cur_page -1)* 25)).read().decode("utf-8")
        except urllib2.URLError, e:
            # It's in __builtin__ module ,return whether the object has an attribute with the given name.
            if hasattr(e, "code"):
                print ("he server couldn't fulfill the request")
            elif hasattr(e, "reason"):
                print ("We failed to reach a server. Please check your url and read the Reason")
        return pageone

    # 对页面进行正则表达
    def get_name(self, page):
        temp_data = []
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', page, re.S)
        if len(movie_items) == 0:
            raise ("movie_items 长度为空")
        # index 是item在数组中的序号， item是数组中的元素， enumerate为内置函数
        for index, item in enumerate(movie_items):
            if item.find("&nbsp") == -1:
                temp_data.append("Top"+str(self.top_num)+" "+item)
                self.top_num += 1
        self.datas.extend(temp_data)

    def start_spider(self):
        while self.page < 4:
            pageone = self.get_page(self.page)
            self.get_name(pageone)
            self.page += 1

    # 保存到本地文件吧 2016-8-1
    def SaveMovieName(self, item):
        __doc__ = " 保存到本地磁盘 "
        if(os.path.exists('./MoviesNameList.txt')):
            try:
            	# 需要续写，否则覆盖全部文本
                with open('/MoviesNameList.txt', 'a') as reader:
                    # 这里应该判断为空
                    # 如果为空直接写入文本，如果不为空，那么先删除再写入文本
                    # reader.write(str.encode(item))
                    # 涉及到unicode转码为str类型
                    reader.writelines(item.encode('utf-8')+'\r\n')
                    reader.flush()
                    reader.close()
            except Exception, e:
                raise ("" + e)
        else:
            raise ("No file find")

def main():
    spider = Moviecrary()
    print spider.__doc__
    spider.start_spider()
    for item in spider.datas:
        spider.SaveMovieName(item)
        # 打印到内存，与本地列表进行对比
        print item
    print "over"
if __name__ == '__main__':
    main()
