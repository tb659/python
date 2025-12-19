""" 注释与输出函数 """
from time import sleep

print("hello world")  # 输出hello world

'''
块注释
'''

"""
块注释
"""

print(123, 456, sep="*", end="\n")

# 输出正在加载中...... \r 回车符会将光标移动到行首，但不会清除原有内容
for i in range(1, 101):
    print(f"\r正在加载中{i}%", end="")
    sleep(0.03)
