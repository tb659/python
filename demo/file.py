'''
Author: tb659
Date: 2021-08-14 15:03:35
LastEditors: tb659
LastEditTime: 2021-08-14 18:34:25
Description:  
FilePath: \python\demo\file.py
'''

# -*- coding: UTF-8 -*-
import os
import time


# 打开一个文件
fo = open('foo.txt', 'w')
fo.write('www.runoob.com!\nVery good site!\n')

# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open(file='foo.txt', mode='r', encoding='utf-8')
print(fo)
print(fo.tell)
str = fo.read()
print('读取的字符串是 : ', str)
# 关闭打开的文件
fo.close()

time.sleep(2)
os.remove('foo.txt')
time.sleep(2)
os.mkdir('newdir')
time.sleep(2)
# rmdir()方法删除目录，目录名称以参数传递。
# 在删除这个目录之前，它的所有内容应该先被清除。
os.rmdir('newdir')
