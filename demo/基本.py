'''
Author: tb659
Date: 2021-08-14 12:17:34
LastEditors: tb659
LastEditTime: 2021-08-14 15:13:33
Description:
FilePath: \python\基本.py
'''
# coding=utf-8

import datetime
import random
import math
import time
import calendar

a = 1
b = 2
print(a + b)

print('你好')

list = ["a", "b", "c"]
print(list)
for item in list:
    print(item)


if False:
    print(1)
elif 1 + 1 >= 2 and 1 == 1 or 1 == 2:
    print(2)
else:
    print(3)


item_one = 'item_one'
item_two = 'item_two'
item_three = 'item_three'
total = item_one + \
    item_two + \
    item_three
total.capitalize()
print(total)


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)


word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word)
print(sentence)
print(paragraph)


# 第一个注释
print("Hello, Python!")  # 第二个注释


aa = 1
aa = 222222
print(aa)
str1 = '123456789'
print(str1[2])
print(str1[2:])
print(str1[12:])
print(str1[:4])
print(str1[:14])
print(str1[2:15])


list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表


tuple = ('runoob', 786, 2.23, 'john', 70.2)
list = ['runoob', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值


print(random.random())
print(math.floor(3.3))
print(math.ceil(3.3))
print(dir(math))

'''
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 
'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 
'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 
'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 
'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
'''


print(dir(time))
'''
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 
'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 
'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 
'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']
'''

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
print(time.time())

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)


i = datetime.datetime.now()
print("当前的日期和时间是 %s" % i)
print("ISO格式的日期和时间是 %s" % i.isoformat())
print("当前的年份是 %s" % i.year)
print("当前的月份是 %s" % i.month)
print("当前的日期是  %s" % i.day)
print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print("当前小时是 %s" % i.hour)
print("当前分钟是 %s" % i.minute)
print ("当前秒是  %s" % i.second)
