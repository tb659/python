'''
Author: tb659
Date: 2021-08-17 23:41:18
LastEditors: tb659
LastEditTime: 2021-08-17 23:55:27
Description: 
FilePath: \python\demo\test.py
'''

data = '[{"a": "1"}, {"b": "2"}]'
data1 = data[:-1] + ", " + data[1:]
print(data1)

print('-' * 50)
src = 'http://img.jj20.com/up/allimg/1114/022421113R9/210224113R9-1-1200.jpg'
s1 = src[:-10]
for i in range(5):
    print(src[:-10] + str(i + 1) + '.jpg')


a = []
a.append(1)
print(a)

a = 'http://img.jj20.com/up/allimg/1114/022421113R9/210224113R9-1-1200.jpg'
b = a.split('http://img.jj20.com/up/allimg/')
print(b)

item = {}
item['imgSrc'] = 'http://img.jj20.com/up/allimg/1114/022421113R9/210224113R9-1-1200.jpg'
print(item['imgSrc'].split('/')[-1])