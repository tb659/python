""" 注释与输出print和输入input """

from time import sleep

print("hello world")  # 输出hello world

'''
块注释
'''

"""
块注释
"""

print(1, sep=" ", end="\n")
print(123, 456, sep="*", end="\n")

# 输出正在加载中...... \r 回车符会将光标移动到行首，但不会清除原有内容
for i in range(1, 101):
    print(f"\r正在加载中{i}%", end="")
    sleep(0.03)

print('-' * 50)


# 参数详解:   _prompt:提示信息，会显示在控制台，告诉用户该输入什么(比如“请输入年龄:”)，可省略(省略后控制台只显示光标，不提示)。
# input(__prompt=None)

name = input("请输入你的名字:")
print("hello, %s" % name)
print(f"hello, {name}")

age = input("请输入你的年龄:")
print("age:", age, type(age))  # 返回的是str类型

age = int(input("请输入你的年龄:"))
print("age:", age, type(age))  # 返回的是int类型

score = float(input("请输入你的分数:"))
print("score:", score, type(score)) # 返回的是float类型
