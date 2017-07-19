#! usr/bin/env python2.7
# coding:utf-8
# bfdf1be0-4e9d-4d24-ad66-f04a395d36f2
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','practice'])
execute(['scrapy','crawl','ins'])
