""" 运算符 """

print(6 + 4)  # 加法：两数相加 9
print(6 - 4)  # 减法：两数相减 2
print(6 * 4)  # 乘法：两数相乘 24
print(6 / 4)  # 除法：两数相除 1.5
print(6 // 4)  # 整除：两数相除，结果取整 1
print(6 % 4)  # 取余：两数相除，结果取余数 2
print(6 ** 4)  # 幂运算：两数相乘，结果取幂 1296

try:
    print(6 / 0)
except ZeroDivisionError:
    print("除数不能为0")

print('-' * 50)

print(6 + 4.0)  # 相加 10.0
print(6 - 4.0)  # 相减 2.0
print(6 * 4.0)  # 相乘 24.0
print(6 / 4.0)  # 相除 1.5
print(6 // 4.0)  # 整除 1.0
print(6 % 4.0)  # 取余 2.0
print(6 ** 4.0)  # 幂运算 1296.0

print('-' * 50)

count1 = 10
count1 += 1  # count1 = count1 + 1
print(count1)
count2 = 10
count2 -= 1
print(count2)  # count2 = count2 - 1
count3 = 10
count3 *= 1
print(count3)  # count3 = count3 * 1
count4 = 10
count4 /= 1
print(count4)  # count4 = count4 / 1
count5 = 10
count5 %= 1
print(count5)  # count5 = count5 % 1
count6 = 10
count6 **= 1
print(count6)  # count6 = count6 ** 1
count7 = 10
count7 //= 1
print(count7)  # count7 = count7 // 1

print('-' * 50)
