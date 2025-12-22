'''
Author: tb659
Date: 2021-08-14 12:17:34
LastEditors: tb659
LastEditTime: 2021-08-14 14:46:58
Description:
FilePath: \python\日期时间.py
'''
# -*- coding: UTF-8 -*-

from datetime import timedelta
from datetime import time as time_datetime
from datetime import date
from datetime import datetime
import datetime
import time
import calendar


"""
    时间元组（年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时）
        一周的第几日: 0-6
        一年的第几日: 1-366
        夏令时: -1, 0, 1
"""

"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""


# （1）当前时间戳
# 1538271871.226226
time.time()


# （2）时间戳 → 时间元组，默认为当前时间
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=4, tm_sec=1, tm_wday=6, tm_yday=246, tm_isdst=0)
time.localtime()
time.localtime(1538271871.226226)


# （3）时间戳 → 可视化时间
# time.ctime(时间戳)，默认为当前时间
time.ctime(1538271871.226226)


# （4）时间元组 → 时间戳
# 1538271871
time.mktime((2018, 9, 30, 9, 44, 31, 6, 273, 0))


# （5）时间元组 → 可视化时间
# time.asctime(时间元组)，默认为当前时间
time.asctime()
time.asctime((2018, 9, 30, 9, 44, 31, 6, 273, 0))
time.asctime(time.localtime(1538271871.226226))


# （6）时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# （7）可视化时间（定制） → 时间元祖
# time.strptime(时间字符串，时间格式)
print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S'))


i = datetime.datetime.now()
print("当前的日期和时间是 %s" % i)
print("ISO格式的日期和时间是 %s" % i.isoformat())
print("当前的年份是 %s" % i.year)
print("当前的月份是 %s" % i.month)
print("当前的日期是  %s" % i.day)
print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print("当前小时是 %s" % i.hour)
print("当前分钟是 %s" % i.minute)
print("当前秒是  %s" % i.second)


#!/usr/bin/python
# -*- coding: UTF-8 -*-


# ------------------1、获得当前时间-------------#

# 得到当前时间戳
print(time.time())

# 时间戳转换为时间元组
print(time.localtime(time.time()))
print(time.gmtime(time.time()))

# 将时间元组格式化输出成字符串时间
print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
print(time.strftime("%Y-%m-%d", time.gmtime(time.time())))

# 不带参数默认输出当前时间
print(time.strftime("%Y-%m-%d"))

# 通过datetime模块来实现
print(datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.today().strftime("%Y-%m-%d"))

# ------------------2、获取时间差，计算执行时间-------------#

# time 模块获取时间戳
start = time.time()
time.sleep(1)
print(time.time() - start)

# datetime模块
start = datetime.now()
time.sleep(1)
print((datetime.now() - start).seconds)

# 计算昨天的日期
print(datetime.now() - timedelta(days=1))

# 时间元组转化为时间戳
print(time.mktime(time.localtime()))  # localtime获取时间元组
print(time.mktime(time.gmtime()))  # gmtime获取时间元组，格林威治时间
print(time.mktime(datetime.now().timetuple()))  # datetime里获取时间元组

# 将时间字符串转换为时间元组
print(time.strptime("2019-07-14 11:23:33", "%Y-%m-%d %H:%M:%S"))

# 表示时间的两种方式：
# 1. 时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的
# 2. 时间元组 即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同

# ------------------3、time时间模块-------------#
# time.clock方法
# 这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间
# 戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
# （实际上是以WIN32 上QueryPerformanceCounter()
# 为基础，它比毫秒表示更为精确）

start = time.clock()
time.sleep(1)
print(time.clock() - start)

# 返回本地时间元组
print(time.localtime())
print(time.localtime(time.time()))

# 从时间元组按照格式进行格式化输出字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 从时间元组转换为时间戳
print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))
print(time.mktime(datetime.now().timetuple()))

# ------------------4、datetime时间模块-------------#
# 1.datetime.date: 是指年月日构成的日期(相当于日历)
# 2.datetime.time: 是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)
# 3.datetime.datetime: 上面两个合在一起，既包含时间又包含日期
# 4.datetime.timedelta: 时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)
# 可以得到一个新的时间点(datetime)。比如今天的上午3点加上5个小时得到今天的上午8点。同理，两个时间点相减会得到一个时间间隔。
# 获取当天日期
print(date.today())

# 构造函数构造日期
print(date(2018, 1, 1))

# 格式化日期输出
print(date.today().strftime("%Y%m%d"))

# 日期转换成时间元组，其中时分秒都是0
print(date.today().timetuple())

# 按照时间戳转换为日期
print(date.fromtimestamp(time.time()))

# datetime中的time模块，构造时间
t = time_datetime(8, 11, 11)
print(t)

# 格式化时间
print(t.strftime("%H-%M-%S"))

# 新建一个datetime对象，日期为今天，既可以直接调用datetime.datetime.today()，
# 也可以直接向datetime.datetime()传值，如下：
print(datetime.today())
print(datetime.now())
print(datetime(2014, 8, 15, 8, 12, 34, 790945))

# datetime.datetime.now([tz]) 当不指定时区时，和datetime.datetime.today()是一样的结果
# 格式化时间
print(datetime.now().strftime("%H-%M-%S"))

# 返回时间元组
print(datetime.now().timetuple())
print(time.mktime(datetime.now().timetuple()))

# 数据替换
d1 = datetime(2014, 8, 15, 8, 12, 34, 790945)
print(d1.replace(year=2000))

# ------------------5、timedelta-------------#
print(datetime.today())
print(datetime.today() - timedelta(days=1))
