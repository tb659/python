""" 正则表达式方法 """

"""
1. 3个核心函数的核心用途：
   • re.search()：全局找第一个匹配，返回 Match 对象（失败返回 None）；
   • re.findall()：全局找所有匹配，返回列表（失败返回空列表）；
   • re.sub()：替换匹配项，返回替换后的新字符串（默认替换所有）。

2. 关键区别：
   • match() vs search()：前者只匹配开头，后者全局找第一个；
   • findall() 返回列表，不用判断是否为 None（空列表不报错）。

3. 实用技巧：
   • 提取信息用 findall()（如所有手机号、邮箱）；
   • 单个匹配用 search()（如找第一个日期）；
   • 验证格式用 match()（如手机号、邮箱格式验证）；
   • 替换/过滤用 sub()（如打码、清理特殊字符）。


"""

import re

# 开头匹配成功
res1 = re.match("th", "this is python")
print(res1.group())  # 输出: th

# 开头不匹配，返回None
res2 = re.match("th", "python is good")
print(res2)  # 输出: None

res3 = re.search("th", "python is good, they are good")
print(res3.group())  # 输出: th

res4 = re.search("abc", "python is good")
print(res4)  # 输出: None

res5 = re.findall("th", "python is good, they are good")
print(res5)  # 输出: ['th', 'th']

res6 = re.findall("abc", "python is good, they are good")
print(res6)  # 输出: []

res7 = re.sub("good", "perfect", "python is good, they are good")
print(res7)  # 输出: python is perfect, they are perfect

res8 = re.sub("good", "perfect", "python is good, they are good", count=1)
print(res8)  # 输出: python is perfect, they are good

res9 = re.sub("a", "*", "123aAa456aA789a")
print(res9)  # 输出: 123*A*a456*A*789*a

res10 = re.sub("a", "*", "123aAa456aA789a", flags=re.I)
print(res10)  # 输出: 123*A*a456*A*789*a
