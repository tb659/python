
import requests


url = 'https://fanyi.baidu.com/sug'
key = input('请输入翻译单词')
data = {
    "kw": key
}
res = requests.post(url, data)
print(res.json())

res.close()
