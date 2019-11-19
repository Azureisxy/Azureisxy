# -*- coding:utf-8 -*-
"""
1、模块名： 小写字母，单词之间用_分割  如：logging
2、包名: 小写字母，单词之间用_分割 如：logging
3、类名：单词首字母大写 如：python class LogRecord(object):
4、普通变量：小写字母，单词之间用_分割  如：exc_info
5、实例变量：以_开头，小写字母，单词之间用_分割
    如:_exc_info，以一个下划线开头的标识符(_xxx)，不能访问的类属性，但可通过类提供的接口进行访问，
    不会被语句 “from module import *” 语句加载
6、私有实例变量：以__开头（2个下划线），小写字母，单词之间用_分割  如:__private_var ，外部访问会报错
7、专有变量：开头，结尾，一般为python的自有变量，不要以这种方式命名  如:doc ，是系统定义的，具有特殊意义的标识符
8、普通函数：小写字母，单词之间用_分割： 如:get_name()
9、私有函数： 以__开头（2个下划线），小写字母，单词之间用分割 如:__get_name() ，外部访问会报错
"""

import os
import xlrd
import xlwt

def azure(fromPath,toPath):
    file_names = os.listdir(fromPath)
    for file_name in file_names:
        if os.path.isfile(file_name):
            continue
        workbook = xlrd.open_workbook(fromPath)
        sheet_names = workbook.sheet_names()

        for sheet_name in sheet_names:
            worksheet = workbook.sheet_by_name(sheet_name)

