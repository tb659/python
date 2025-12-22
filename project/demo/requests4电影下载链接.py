
import requests
import time
import re
import csv

url = 'https://www.dytt89.com'
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

res = requests.get(url=url)
res.encoding = "gbk"
# print(res.text)

print("--" * 20)

# 主页源代码匹配
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
# 二级链接匹配
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

# 子链接
chidl_href_List = []

res1 = obj1.finditer(res.text)
for item1 in res1:
    res2 = obj2.finditer(item1.group('ul').strip())
    for item2 in res2:
        chidl_href_List.append(url + item2.group('href'))

print(chidl_href_List)

# 子页面源代码匹配电影名称和下载链接
obj3 = re.compile(
    r'《(?P<movie_name>.*?)》.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S
)

f = open('电影下载.csv', mode='w')

for child_href in chidl_href_List:
    # 获取子页面源代码
    res = requests.get(child_href)
    res.encoding = "gbk"
    # 匹配电影名称和下载链接
    res3 = obj3.search(res.text)
    movie_name = res3.group('movie_name')
    download = res3.group('download')
    # 写入本地
    csv.writer(f).writerow([movie_name, download])

f.close()
res.close()

print('finished!!!')
