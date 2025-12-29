""" 闭包示例和使用场景

"""
"""

闭包是指一个函数能够访问并"记住"在其词法作用域外定义的变量。
闭包由两部分组成：
1. 一个嵌套的内部函数
2. 对外部函数作用域中变量的引用

使用场景：
1. 封装私有变量
2. 函数工厂
3. 回调函数和事件处理器
4. 装饰器的基础

1. 闭包：
本质：带“记忆功能”的嵌套函数；
3个条件：函数嵌套、内层用外层变量、外层返回内层函数；
作用：保存状态、数据封装、支撑装饰器。

闭包的外层变量是“被记忆”的，多个闭包实例的变量互不干扰；

"""


# 示例1：基本闭包结构
def outer_function(x):
    """外部函数"""

    def inner_function(y):
        """内部函数，形成闭包"""
        return x + y  # 访问外部函数的变量x

    return inner_function


# 创建闭包实例
add_10 = outer_function(10)
print(add_10(5))  # 输出: 15


# 示例2：封装私有变量
def create_counter():
    """创建计数器，count变量对外部不可直接访问"""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # 输出: 1
print(counter1())  # 输出: 2
print(counter2())  # 输出: 1 (counter2有自己独立的count)
print(counter1())  # 输出: 3


# 示例3：函数工厂
def create_multiplier(factor):
    """创建乘法器函数"""

    def multiplier(number):
        return number * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15


# 示例4：配置函数
def make_prefixer(prefix):
    """创建带前缀的字符串函数"""

    def add_prefix(text):
        return prefix + text

    return add_prefix


# 创建不同前缀的函数
ms = make_prefixer('Ms. ')
mr = make_prefixer('Mr. ')

print(ms('Smith'))  # 输出: Ms. Smith
print(mr('Jones'))  # 输出: Mr. Jones


# 闭包的实用场景：数据持久化
def create_accumulator(initial=0):
    """累加器，保持状态"""
    total = initial

    def accumulator(value):
        nonlocal total
        total += value
        return total

    return accumulator


acc = create_accumulator(10)
print(acc(5))  # 输出: 15
print(acc(-3))  # 输出: 12
print(acc(8))  # 输出: 20
