
import requests


query = input('输入搜索内容')
# url = f'https://www.baidu.com/s?wd={query}'
url = f'https://www.sogou.com/web?query={query}'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
res = requests.get(url, headers)  # 请求头处理反爬
print(res)
# print(res.text)  # 网页源代码

with open('search.html', 'w') as f:
    f.write(res.text)

res.close()
