""" 流程控制-条件语句 """

"""
        运算符     含义
        >         大于
        <         小于
        >=        大于等于
        <=        小于等于
        ==        等于
        !=        不等于
        and       逻辑与，两边都为真时才为真
        or        逻辑或，两边都为假时才为假
        not       逻辑非，将真转为假，将假转为真
"""

# 示例代码
a = 10
b = 20

# 大于
if a > 5:
    print("a大于5")

# 小于
if b < 30:
    print("b小于30")

# 大于等于
if a >= 10:
    print("a大于等于10")

# 小于等于
if b <= 20:
    print("b小于等于20")

# 等于
if a == 10:
    print("a等于10")

# 不等于
if a != b:
    print("a不等于b")

# and逻辑运算符
if a > 5 and b < 30:
    print("a大于5且b小于30")

# or逻辑运算符
if a > 15 or b < 30:
    print("a大于15或b小于30")

# not逻辑运算符
if not (a > b):
    print("a不大于b")

num = 10
if num > 5:
    print("num大于5")
elif num < 5:
    print("num小于5")
else:
    print("num等于5")

# 三元运算符
result = "大于8" if num > 8 else "小于8"
print(result)