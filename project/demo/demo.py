'''
Author: tb659
Date: 2021-08-14 18:30:03
LastEditors: tb659
LastEditTime: 2021-08-15 04:16:19
Description: demo
FilePath: \python\demo\demo.py
'''

from urllib.request import urlopen 

url = 'http://www.baidu.com'
res = urlopen(url)
with open("mybaidu.html", mode='w', encoding='utf-8') as f:
  f.write(res.read().decode('utf-8'))

