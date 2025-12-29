""" 字典及其常见操作 """

"""
本质
   有序的、可修改的、键值对 数据容器 键唯一 值任意

常用方法
    查找：get(key)（安全不报错） dict[key] 找不到报错
    增改：dict[key] = value  键存在即修改 键不存在则增加 update({key: value})
    删除：pop(key)（删除指定键值对）、clear()（清空）
    遍历：keys()（取所有键）、values()（取所有值）、items()（取所有键值对）
"""

data = {
    'name': 'Tom',
    'age': 18,
    'height': 180
}
# 打印字典data的类型
print("打印字典data的类型", type(data))  # <02.class 'dict'>
# 打印整个字典data
print("打印整个字典data", data)  # {'name': 'Tom', 'age': 18, 'height': 180}
# 通过键'name'访问对应的值
print("通过键'name'访问对应的值", data['name'])  # Tom
# 使用get方法获取键'name'对应的值
print("使用get方法获取键'name'对应的值", data.get('name'))  # Tom
# 获取字典所有的键
print("获取字典所有的键", data.keys())  # dict_keys(['name', 'age', 'height'])
# 获取字典所有的值
print("获取字典所有的值", data.values())  # dict_values(['Tom', 18, 180])
# 获取字典所有的键值对
print("获取字典所有的键值对", data.items())  # dict_items([('name', 'Tom'), ('age', 18), ('height', 180)])
# 修改键'name'对应的值为'Jerry'
data['name'] = 'Jerry'
# 打印修改后的字典
print("打印修改后的字典", data)  # {'name': 'Jerry', 'age': 18, 'height': 180}
# 使用update方法更新字典内容
data.update({'name': 'Tom', 'age': 18, 'height': 180})
# 打印更新后的字典
print("打印更新后的字典", data)  # {'name': 'Tom', 'age': 18, 'height': 180}
# 创建并打印字典的一个副本
print("创建并打印字典的一个副本", data.copy())  # {'name': 'Tom', 'age': 18, 'height': 180}
# 打印原字典
print("打印原字典", data)  # {'name': 'Tom', 'age': 18, 'height': 180}
# 删除键'name'及其对应的值
data.pop('name')
# 打印删除元素后的字典
print("打印删除元素后的字典", data)  # {'age': 18, 'height': 180}
# 删除字典中最后一对键值对
data.popitem()
# 打印删除元素后的字典
print("打印删除元素后的字典", data)  # {'age': 18}
# 清空字典中的所有元素
data.clear()
# 打印清空后的字典
print("打印清空后的字典", data)  # {}
# 打印字典中键值对的数量
print("打印字典中键值对的数量", len(data))  # 0
