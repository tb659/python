""" 注释与输出print和输入input """

from time import sleep

# 打印hello world
print("hello world")  # 输出hello world

'''
块注释
'''

"""
块注释
"""

# 打印数字1，使用默认分隔符和行尾符号
print(1, sep=" ", end="\n")
# 打印两个数字，使用*作为分隔符
print(123, 456, sep="*", end="\n")

# 输出正在加载中...... \r 回车符会将光标移动到行首，但不会清除原有内容
for i in range(1, 101):
    print(f"\r正在加载中{i}%", end="")
    sleep(0.03)

# 打印分隔线
print('-' * 50)

# 参数详解:   _prompt:提示信息，会显示在控制台，告诉用户该输入什么(比如"请输入年龄:")，可省略(省略后控制台只显示光标，不提示)。
# input(__prompt=None)

# 获取用户姓名
name = input("请输入你的名字:")
print("hello, %s" % name)
print(f"hello, {name}")

# 获取用户年龄(字符串形式)
age = input("请输入你的年龄:")
print("age:", age, type(age))  # 返回的是str类型

# 获取用户年龄(整数形式)
age = int(input("请输入你的年龄:"))
print("age:", age, type(age))  # 返回的是int类型

# 获取用户分数
score = float(input("请输入你的分数:"))
print("score:", score, type(score))  # 返回的是float类型
