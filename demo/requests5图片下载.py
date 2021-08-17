
import requests
from requests import exceptions
import random
import time
import re
from bs4 import BeautifulSoup

url = 'http://www.jj20.com/bz/nxxz/nxmt'

# 保存到列表
dataList = []
page = 1
_url = '/list_57_'

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}


def getDataList(count, times):
    global url
    global subUrl
    global dataList
    global page

    for index in range(count):
        subUrl = _url + str(page + index) + '.html'

        mainResp = requests.get(url=url + subUrl)
        mainResp.encoding = "gbk"
        # print(mainResp.text)
        # f = open('美图.html', mode='w')
        # f.write(mainResp.text)
        # f.close()

        # 获取主页面图片信息
        mainMatch = re.compile(
            r'target="_blank"><img.*?<a href="/bz/nxxz/nxmt(?P<id>.*?).html">(?P<dirName>.*?)</a>[(](?P<count>.*?)[张)]', re.S
        )
        # 子页面图片匹配
        # imgSrcSearch = re.compile(
        #     r'<div class="info_pic">.*?<img src="(?P<imgSrc>.*?)"', re.S
        # )
        mainRes = mainMatch.finditer(mainResp.text)
        for item1 in mainRes:

            item = {}
            item['srcList'] = []
            # 拿到子页面链接http://www.jj20.com/bz/nxxz/nxmt/318147.html
            childHref = url + item1.group('id') + '.html'
            item['childHref'] = childHref
            # 拿到文件夹名称
            item['dirName'] = item1.group('dirName')
            # 拿到图片数量
            item['count'] = item1.group('count')
            # print(item)
            # 拿到子页面源代码
            try:
                childResp = requests.get(childHref, headers=headers)
                childResp.encoding = "gbk"
            except exceptions.HTTPError as e:
                print('http请求错误' + str(e.message))
                break
            else:
                if childResp.status_code == 200:
                    # print(childResp.text)

                    # 方法1
                    # imgUrl = imgSrcSearch.search(childResp.text)
                    # item['imgSrc'] = imgUrl.group('imgSrc')

                    # 方法二
                    childPage = BeautifulSoup(childResp.text, 'html.parser')
                    print(item['dirName'])
                    # print(childPage)
                    item['imgSrc'] = childPage.find(
                        'div', class_="info_pic").find('img').get("src")

                    # 遍历拿到子页面所有图片
                    for subItemIndex in range(int(item['count'])):
                        src = item['imgSrc']
                        # 拿到不同的imgUrl
                        src = src[:-10] + str(subItemIndex + 1) + src[-9:]
                        item['srcList'].append(src)

                        # 下载图片
                        imgResp = requests.get(src)
                        # 图片名称
                        imgName = src.split('/')[-1]

                        with open('images/' + item['dirName'] + imgName, mode='wb') as f:
                            f.write(imgResp.content)
                        
                        print('下载成功：' + item['dirName'] + imgName)
                        time.sleep(times)
                        
                    # 间隔时间
                    time.sleep(times)
                else:
                    print('请求错误：' + str(childResp.status_code) +
                          ', ' + str(childResp.reason))
                    break
            dataList.append(item)
            childResp.close()
        # 间隔时间
        time.sleep(times)
    print(dataList)

    # 存储到本地数据
    with open('图片数据.txt', mode='w', encoding="utf-8") as f:
        f.write(str(dataList))

    mainResp.close()


getDataList(1, 1)
print("*" * 30)
print('finished!!!')
