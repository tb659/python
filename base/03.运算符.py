""" 运算符 """

# 执行加法运算，计算6与4的和
print(6 + 4)  # 加法：两数相加 9
# 执行减法运算，计算6与4的差
print(6 - 4)  # 减法：两数相减 2
# 执行乘法运算，计算6与4的积
print(6 * 4)  # 乘法：两数相乘 24
# 执行除法运算，计算6与4的商
print(6 / 4)  # 除法：两数相除 1.5
# 执行整除运算，计算6与4的整数商
print(6 // 4)  # 整除：两数相除，结果取整 1
# 执行取余运算，计算6与4的余数
print(6 % 4)  # 取余：两数相除，结果取余数 2
# 执行幂运算，计算6的4次方
print(6 ** 4)  # 幂运算：两数相乘，结果取幂 1296

# 尝试执行除零操作以演示异常处理
try:
    # 尝试进行除以零的操作
    print(6 / 0)
# 捕获除零异常
except ZeroDivisionError:
    # 输出错误提示信息
    print("除数不能为0")

# 打印分隔线以便区分不同的代码段
print('-' * 50)

# 对整数和浮点数进行混合运算
# 执行加法运算，计算6与4.0的和
print(6 + 4.0)  # 相加 10.0
# 执行减法运算，计算6与4.0的差
print(6 - 4.0)  # 相减 2.0
# 执行乘法运算，计算6与4.0的积
print(6 * 4.0)  # 相乘 24.0
# 执行除法运算，计算6与4.0的商
print(6 / 4.0)  # 相除 1.5
# 执行整除运算，计算6与4.0的整数商
print(6 // 4.0)  # 整除 1.0
# 执行取余运算，计算6与4.0的余数
print(6 % 4.0)  # 取余 2.0
# 执行幂运算，计算6的4.0次方
print(6 ** 4.0)  # 幂运算 1296.0

# 打印分隔线以便区分不同的代码段
print('-' * 50)

# 演示复合赋值运算符的使用
# 初始化变量count1为10
count1 = 10
# 使用+=运算符将count1增加1
count1 += 1  # count1 = count1 + 1
# 输出count1的值
print(count1)
# 初始化变量count2为10
count2 = 10
# 使用-=运算符将count2减少1
count2 -= 1
# 输出count2的值
print(count2)  # count2 = count2 - 1
# 初始化变量count3为10
count3 = 10
# 使用*=运算符将count3乘以1
count3 *= 1
# 输出count3的值
print(count3)  # count3 = count3 * 1
# 初始化变量count4为10
count4 = 10
# 使用/=运算符将count4除以1
count4 /= 1
# 输出count4的值
print(count4)  # count4 = count4 / 1
# 初始化变量count5为10
count5 = 10
# 使用%=运算符将count5对1取余
count5 %= 1
# 输出count5的值
print(count5)  # count5 = count5 % 1
# 初始化变量count6为10
count6 = 10
# 使用**=运算符计算count6的1次方
count6 **= 1
# 输出count6的值
print(count6)  # count6 = count6 ** 1
# 初始化变量count7为10
count7 = 10
# 使用//=运算符将count7整除以1
count7 //= 1
# 输出count7的值
print(count7)  # count7 = count7 // 1

# 打印分隔线以便区分不同的代码段
print('-' * 50)
