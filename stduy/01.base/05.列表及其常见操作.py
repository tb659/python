""" 列表及其常见操作 """

"""
本质
    有序的、可修改的、数据容器
核心操作
    访问：索引（取单个） 切片（取部分）
    修改：列表[索引] = 新值
    嵌套：列表[外层索引][内层索引]
常用方法
    添加：append()（加一个）、extend()（加多个）、insert()（指定位置添加）
    查找：index()（索引找）、count()（统计次数）、in/not in判断是否存在
    删除：remove()（删除第一个匹配到的值）
    排序：sort()（升序降序）、reverse()（反转）
"""

# 创建一个包含5个字母的列表
letter = ['a', 'b', 'c', 'd', 'e']
# 打印列表的数据类型
print("打印列表的数据类型", type(letter))  # <02.class 'list'>
# 通过正索引访问第一个元素
print("通过正索引访问第一个元素", letter[0])  # a
# 通过负索引访问最后一个元素
print("通过负索引访问最后一个元素", letter[-1])  # e
# 使用切片获取前两个元素
print("使用切片获取前两个元素", letter[0:2])  # ['a', 'b']
# 省略起始索引的切片
print("省略起始索引的切片", letter[:2])  # ['a', 'b']
# 省略结束索引的切片
print("省略结束索引的切片", letter[2:])  # ['c', 'd', 'e']
# 步长为2的切片
print("步长为2的切片", letter[::2])  # ['a', 'c', 'e']
# 反转列表的切片
print("反转列表的切片", letter[::-1])  # ['e', 'd', 'c', 'b', 'a']
# 指定起始、结束和步长的切片
print("指定起始", letter[1:4:2])  # ['b', 'd']
# 列表连接操作
print("列表连接操作", letter + ['f', 'g'])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 列表重复操作
print("列表重复操作", letter * 3)  # ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
# 在列表末尾添加元素
letter.append('f')
# 打印添加元素后的列表
print("打印添加元素后的列表", letter)  # ['a', 'b', 'c', 'd', 'e', 'f']
# 在指定位置插入元素
letter.insert(0, 'z')
# 打印插入元素后的列表
print("打印插入元素后的列表", letter)  # ['z', 'a', 'b', 'c', 'd', 'e', 'f']
# 弹出并返回列表最后一个元素
print("弹出并返回列表最后一个元素", letter.pop())  # f
# 打印弹出元素后的列表
print("打印弹出元素后的列表", letter)  # ['z', 'a', 'b', 'c', 'd', 'e']
# 弹出并返回指定位置的元素
print("弹出并返回指定位置的元素", letter.pop(0))  # z
# 移除列表中第一个匹配的元素
letter.remove('a')
# 打印移除元素后的列表
print("打印移除元素后的列表", letter)  # ['b', 'c', 'd', 'e']
# 反转列表顺序
letter.reverse()
# 打印反转后的列表
print("打印反转后的列表", letter)  # ['e', 'd', 'c', 'b']
# 对列表进行排序
letter.sort()
# 打印排序后的列表
print("打印排序后的列表", letter)  # ['b', 'c', 'd', 'e']
# 使用sorted函数返回排序后的新列表
print("使用sorted函数返回排序后的新列表", sorted(letter))  # ['b', 'c', 'd', 'e']
# 查找元素在列表中的索引位置
print("查找元素在列表中的索引位置", letter.index('c'))  # 1
# 判断元素是否存在于列表中
print("判断元素是否存在于列表中", 'c' in letter)  # True
# 判断元素是否不存在于列表中
print("判断元素是否不存在于列表中", 'x' not in letter)  # True
# 获取列表长度
print("获取列表长度", len(letter))  # 4
# 统计元素在列表中出现的次数
print("统计元素在列表中出现的次数", letter.count('a'))  # 0
# 清空列表所有元素
letter.clear()
# 打印清空后的列表
print("打印清空后的列表", letter)  # []
# 复制列表
print("复制列表", ['a', 'b', 'c'].copy())  # ['a', 'b', 'c']
# 扩展列表，添加多个元素
letter.extend(['f', 'g'])
# 打印扩展后的列表
print("打印扩展后的列表", letter)  # ['f', 'g']
# 查找元素在列表中的索引位置
print("查找元素在列表中的索引位置", letter.index('g'))  # 1
# 创建嵌套列表
letter = ['a', 'b', 'c', ['d', 'e']]
# 打印嵌套列表
print("打印嵌套列表", letter)
# 连接两个列表
print("连接两个列表", [1] + [2])
