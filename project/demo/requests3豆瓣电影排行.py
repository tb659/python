
import requests
from requests import exceptions
import time


url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
dataList = []


def getList(size, times):
    # 声明引用的是全局变量
    global dataList
    for index in range(times):
        params["limit"] = size
        params["start"] = size * index
        print(params)

        try:
            res = requests.get(url=url, params=params, headers=headers)
        except exceptions.HTTPError as e:
            print('http请求错误:' + str(e.message))
            break
        else:
            if res.status_code == 200:
                print(res.text)
                if len(res.json()) and index == 0:
                    dataList = res.json()
                # 非第一次请求处理数据合并
                elif len(res.json()):
                    dataList.extend(res.json())
                else:
                    break
                # 间隔3秒
                time.sleep(10)
            else:
                print('请求错误：' + str(res.status_code)+', ' + str(res.reason))
                break

    print(dataList)
    # 如果列表有数据存储下来
    if len(dataList):
        with open("豆瓣剧情电影排行榜.json", mode="w", encoding="utf-8") as f:
            f.write(str(dataList))
    print("finished")


getList(20, 50)
