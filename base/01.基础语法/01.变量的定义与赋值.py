""" 变量的定义与赋值 """

# 定义变量
# 变量名 = 变量值

# 直接赋值
phone1 = 13888888888
print(phone1)

# 把一个变量赋给另一个变量
phone2 = phone1
print(phone2)

# 把一个表达式赋给变量
num = 3 * 4
print(num)

# 动态变量
count = 1
count = 2.5
count = "hello world"
# 变量可以被反复赋值,并且可以是不同的类型,后面的值会覆盖前面的值(因为代码是从上到下的顺序逐行执行的)
print(count)

# 序列赋值 解构赋值
a, b, c = 1, 2, 3
print(a, b, c)

# 数据类型
type0 = """
    多行字符串
    多行字符串
"""
type1 = "Tom"
type2 = 18
type3 = 18.5
type4 = 2 + 3j
type5 = True
type6 = ["Tom", 18, 18.5, True]
type7 = (1, 2, 3)
type8 = {1, 2, 3}
type9 = {"name": "Tom", "age": 18, "height": 180}
type10 = None

print(type(type1), "\n", type(type2), "\n", type(type3), "\n", type(type4), "\n", type(type5), "\n", type(type6), "\n",
      type(type7), "\n", type(type8), "\n", type(type9), "\n", type(type10))
print(type1, "\n", type2, "\n", type3, "\n", type4, "\n", type5, "\n", type6, "\n", type7, "\n", type8, "\n", type9, "\n", type10)
