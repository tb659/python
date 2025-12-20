""" 变量的定义与赋值 """

# 定义变量
# 变量名 = 变量值

# 直接赋值 - 将手机号码赋值给变量phone1
phone1 = 13888888888
# 打印变量phone1的值
print(phone1)

# 把一个变量赋给另一个变量 - 将phone1的值赋给phone2
phone2 = phone1
# 打印变量phone2的值
print(phone2)

# 把一个表达式赋给变量 - 计算3*4的结果赋值给num
num = 3 * 4
# 打印变量num的值
print(num)

# 动态变量
# 给count变量赋整数值1
count = 1
# 重新赋值为浮点数2.5，覆盖之前的值
count = 2.5
# 再次重新赋值为字符串，覆盖之前的值
count = "hello world"
# 变量可以被反复赋值,并且可以是不同的类型,后面的值会覆盖前面的值(因为代码是从上到下的顺序逐行执行的)
# 打印最终的count值
print(count)

# 序列赋值 解构赋值 - 同时给多个变量赋值
a, b, c = 1, 2, 3
# 打印a, b, c三个变量的值
print(a, b, c)

# 数据类型示例
# 字符串类型 - 多行字符串
type0 = """
    多行字符串
    多行字符串
"""
# 字符串类型
type1 = "Tom"
# 整数类型
type2 = 18
# 浮点数类型
type3 = 18.5
# 复数类型
type4 = 2 + 3j
# 布尔类型
type5 = True
# 列表类型 - 可以存储不同类型的数据
type6 = ["Tom", 18, 18.5, True]
# 元组类型 - 不可变序列
type7 = (1, 2, 3)
# 集合类型 - 不重复元素的无序集合
type8 = {1, 2, 3}
# 字典类型 - 键值对的集合
type9 = {"name": "Tom", "age": 18, "height": 180}
# 空值类型
type10 = None

# 打印各个变量的数据类型
print(type(type1), "\n", type(type2), "\n", type(type3), "\n", type(type4), "\n", type(type5), "\n", type(type6), "\n",
      type(type7), "\n", type(type8), "\n", type(type9), "\n", type(type10))
# 打印各个变量的值
print(type1, "\n", type2, "\n", type3, "\n", type4, "\n", type5, "\n", type6, "\n", type7, "\n", type8, "\n", type9,
      "\n", type10)
