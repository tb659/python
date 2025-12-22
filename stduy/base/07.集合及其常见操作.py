""" 集合及其常见操作 """

"""
本质
    唯一的、无序的、可修改的、数据容器
特性
    自动去重，无索引
常用方法
    添加：add()（加一个）、update()（加多个）
    删除：discard()（删除的值 不报错）、remove()（删除的值 报错）、clear()（清空）

"""

# 创建一个集合
letter = {'a', 'b', 'c', 'd', 'e'}
# 打印集合的类型
print("打印集合的类型", type(letter))  # <class 'set'>
# 打印集合内容
print("打印集合内容", letter)  # {'c', 'd', 'a', 'b', 'e'}
# 向集合中添加元素'f'
letter.add('f')
# 打印添加元素后的集合
print("打印添加元素后的集合", letter)  # {'c', 'd', 'a', 'b', 'e', 'f'}
# 从集合中移除元素'a'
letter.remove('a')
# 打印移除元素后的集合
print("打印移除元素后的集合", letter)  # {'d', 'b', 'c', 'e', 'f'}
# 清空集合
letter.clear()
# 打印清空后的集合
print("打印清空后的集合", letter)  # set()
# 分隔线
print("*" * 50)
# 重新创建集合
letter = {'a', 'b', 'c', 'd', 'e'}
# 打印集合的副本
print("打印集合的副本", letter.copy())
# 打印两个集合的并集
print("打印两个集合的并集", letter.union({'a', 'b', 'b', 'c', 'c', 'd', 'e', 'e', 'f'}))
# 打印两个集合的交集
print("打印两个集合的交集", letter.intersection({'c', 'd', 'e'}))
# 打印两个集合的差集
print("打印两个集合的差集", letter.difference({'a', 'd', 'e'}))
# 打印两个集合的对称差集
print("打印两个集合的对称差集", letter.symmetric_difference({'b', 'c', 'e'}))
# 判断是否为子集
print("判断是否为子集", letter.issubset({'c', 'd', 'e'}))
# 判断是否为超集
print("判断是否为超集", letter.issuperset({'d', 'e'}))
# 判断是否不相交
print("判断是否不相交", letter.isdisjoint({'a', 'b', 'c', 'd', 'e'}))
# 更新集合
letter.update({'a', 'b', 'c', 'd', 'e', 'f'})
print(letter)
# 丢弃元素'a'
letter.discard('a')
print(letter)
