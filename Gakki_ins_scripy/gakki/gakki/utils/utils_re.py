#! usr/bin/env python2.7
# coding:utf-8

import re

class Util_re(object):

    __doc__ = '正则匹配'


    def __init__(self):
        pass

    def search(self, question=None):

        '''
        
        :param question:
        :return:
        '''
        if question and isinstance(question, str):

            pattern = re.compile(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}\s\d{2}:\d{2}')
            match = pattern.search(question)
            if match:
                return True
            else:
                return False
        else:
            return False
