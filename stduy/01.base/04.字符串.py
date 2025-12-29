""" 字符串 """

# 定义两个字符串变量
str1 = "hello "
str2 = "world"
# 字符串拼接
print(str1 + str2)
# 判断字符是否在字符串中
print("l" in str1)
# 判断字符是否不在字符串中
print("l" not in str2)
# 正向索引取字符
print(str1[0])
# 反向索引取字符
print(str1[-1])
# ) # 报错 IndexError: string index out of range
# print(str1[10]

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 定义字符串id用于演示切片操作
# 定义字符串id
id = "01234567890"
# 字符串切片语法说明
# id[start:end:step]
# 切片操作示例
# 切片，从索引1到2（不包括2），输出"1"
print(id[1:2])
# 切片，从开头到索引2（不包括2），输出"01"
print(id[:2])
# 切片，从索引2到末尾，输出"234567890"
print(id[2:])
# 切片，从索引2到4（不包括4），输出"23"
print(id[2:4])
# 切片，从索引2到8（不包括8），步长为2，输出"246"
print(id[2:8:2])
# 切片，整个字符串，步长为2，输出"024680"
print(id[::2])
# 切片，整个字符串倒序，步长为2，输出"08642"
print(id[::-2])

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 转义字符演示
# \t 制表符
print(1, "\t", 2)
# \n 换行符
print(3, "\n", 4)
# \r 回车符
print(5, "\r", 6)
# \b 退格符
print(7, "\b", 8)
# \f 换页符
print(9, "\f", 10)
# \v 垂直制表符
print(11, "\v", 12)
# \ 斜杠符
print(13, "\\", 14)
# \a 响铃符
print(15, "\a", 16)
# \u0000 16进制数
print(17, "\u0000", 18)
# \U00000000 32进制数
print(19, "\U00000000", 20)
# \' 单引号符`
print(21, "\'", 22)
# \" 双引号符
print(23, "\"", 24)
# \x00 16进制数
print(25, "\x00", 26)
# 原始字符串
# r 表示原始字符串，不会对字符串中的特殊字符进行转义
print(r"D:\dev\table")
# 格式化字符串
# f 表示格式化字符串，可以在字符串中插入变量
print(f"id是{id}")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 数字变量定义
# 定义整数num1
num1 = 123
# 定义整数num2
num2 = 1
# 格式化数字输出
# 格式化字符串，输出"0学号是：123"
print(F"0学号是：{num1}")
# 格式化字符串，输出"1学号是：1"
print(F"1学号是：{num2}")
# 3 显示3位，输出"2学号是：  1"
print(F"2学号是：{num2:3}")
# 03 表示不足补0，输出"3学号是：001"
print(F"3学号是：{num2:03}")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 浮点数格式化演示
# 定义浮点数P
P = 3.14159
# .2f 表示保留2位小数 四舍五入，输出"圆周率是：3.14"
print(f"圆周率是：{P:.2f}")
# .10f 表示保留10位小数 四舍五入，输出"圆周率是：3.1415900000"
print(f"圆周率是：{P:.10f}")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 字符串对齐格式化演示
# 定义字符串name
name = "Tom"
# 默认左对齐，输出"姓名：Tom        默认左对齐"
print(f"姓名：{name:10}", "默认左对齐")
# > 左对齐，输出"姓名：Tom        左对齐"
print(f"姓名：{name:<10}", "左对齐")
# > 右对齐，输出"姓名：       Tom 右对齐"
print(f"姓名：{name:>10}", "右对齐")
# ^ 居中对齐，输出"姓名：   Tom    居中对齐"
print(f"姓名：{name:^10}", "居中对齐")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 使用自定义字符填充字符串
# _ 填充字符，输出"姓名：Tom_______ 填充字符"
print(f"姓名：{name:_<10}", "填充字符")
# _ 填充字符，输出"姓名：_______Tom 填充字符"
print(f"姓名：{name:_>10}", "填充字符")
# _ 填充字符，输出"姓名：___Tom____ 填充字符"
print(f"姓名：{name:_^10}", "填充字符")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 字符串方法演示
# 第一个匹配的位置 返回6
print("hello world".find("world"), "第一个匹配的位置 返回6")
# 匹配位置 返回6
print("hello world".rfind("world"), "匹配位置 返回6")
# 匹配位置 返回6
print("hello world".index("world"), "匹配位置 返回6")
# 匹配位置 返回6
print("hello world".rindex("world"), "匹配位置 返回6")
# 匹配数量 返回3
print("hello world".count("l"), "匹配数量 返回3")
# 判断是否以指定字符串开头 返回True
print("hello world".startswith("hello"), "判断是否以指定字符串开头 返回True")
# 判断是否以指定字符串结尾 返回True
print("hello world".endswith("world"), "判断是否以指定字符串结尾 返回True")
print("hello world".replace("hello", "hi"),
      # 替换字符串 不改变原字符串 返回新字符串hi world
      "替换字符串 不改变原字符串 返回新字符串hi world")
# 分割字符串 返回列表['hello', 'world']
print("hello world".split(" "), "分割字符串 返回列表['hello', 'world']")
print("hello world".join(["hello", "world"]),
      # 连接字符串 返回hellohello worldworld js是["hello", "world"].join("hello world")
      "连接字符串 返回hellohello worldworld")
# 小写 返回hello world
print("HELLO WORLD".lower(), "小写 返回hello world")
# 大写 返回HELLO WORLD
print("hello world".upper(), "大写 返回HELLO WORLD")
# 首字母大写 返回Hello World
print("hello world".title(), "首字母大写 返回Hello World")
# 首字母大写 返回Hello world
print("hello world".capitalize(), "首字母大写 返回Hello world")
# 大小写转换 返回HELLO WORLD
print("hello world".swapcase(), "大小写转换 返回HELLO WORLD")
# 大小写转换 返回hello world
print("HELLO WORLD".swapcase(), "大小写转换 返回hello world")
# 去除字符串首尾空白 返回hello world
print(" \t    hello world   \n ".strip(), "去除字符串首尾空白 返回hello world")
# 去除指定字符串 返回heo word
print("hello world".strip("l"), "去除指定字符串 返回heo word")
# 去除字符串左侧空白 返回hello world
print("hello world".lstrip(), "去除字符串左侧空白 返回hello world")
# 去除字符串右侧空白 返回hello world
print("hello world".rstrip(), "去除字符串右侧空白 返回hello world")
print("hello world".center(20, "*"),
      # 居中填充字符 20个字符 返回 ****hello world*****
      "居中填充字符 20个字符 返回 ****hello world*****")
# 填充字符 20个字符 返回000000000hello world
print("hello world".zfill(20), "填充字符 20个字符 返回000000000hello world")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 字符串判断方法演示
# 判断是否只包含字母 返回False
print("hello world".isalpha(), "判断是否只包含字母 返回False")
# 判断是否只包含数字 返回False
print("hello world".isdigit(), "判断是否只包含数字 返回False")
# 判断是否只包含字母数字 返回False
print("hello world".isalnum(), "判断是否只包含字母数字 返回False")
# 判断是否只包含标识符 返回False
print("hello world".isidentifier(), "判断是否只包含标识符 返回False")
# 判断是否只包含可打印字符 返回True
print("hello world".isprintable(), "判断是否只包含可打印字符 返回True")
# 判断是否只包含空格 返回False
print("hello world".isspace(), "判断是否只包含空格 返回False")
# 判断是否只包含标题 返回False
print("hello world".istitle(), "判断是否只包含标题 返回False")
# 判断是否只包含大写字母 返回False
print("hello world".isupper(), "判断是否只包含大写字母 返回False")
# 判断是否只包含小写字母 返回False
print("hello world".islower(), "判断是否只包含小写字母 返回False")

# 字符串编码解码演示
# 将中文字符串编码为字节
b = "你好世界".encode()
# 编码字符串 默认utf-8 返回b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'
print(b, "编码字符串转字节 默认utf-8")
# 返回<02.class 'bytes'>
print(type(b))
# 将字节解码为字符串
txt = b.decode()
# 编码字符串 默认utf-8 返回你好世界
print(txt.decode(), "解码字节转字符串 默认utf-8")

# 分隔线
# 输出50个*作为分隔线
print("*" * 50)

# 其他字符串方法演示
# 替换tab字符为空格 默认4个空格 返回hello world
print("hello world".expandtabs(), "替换tab字符为空格 默认4个空格")
# 分割字符串 默认空格 返回('hello', ' ', 'world')
print("hello world".partition(" "), "分割字符串 默认空格")
# 分割字符串 默认空格 返回('hello', ' ', 'world')
print("hello world".rpartition(" "), "分割字符串 默认空格")
# 判断是否相等 返回 True
print("hello world".partition(" ") == "hello world".rpartition(" "))
# 分割字符串 默认空格 返回('hello', ' ', 'world yeah')
print("hello world yeah".partition(" "), "分割字符串 默认空格")
# 分割字符串 默认空格 返回('hello world', ' ', 'yeah')
print("hello world yeah".rpartition(" "), "分割字符串 默认空格")
# 判断是否相等 返回 False
print("hello world yeah".partition(" ") == "hello world yeah".rpartition(" "))
# 分割字符串 默认换行符
print("hello world yeah".splitlines(), "分割字符串 默认换行符")
# 创建转换表 返回{104: 119, 101: 111, 108: 108, 111: 100}
print("hello world".maketrans("hello", "world"), "创建转换表")
# 替换字符串
print("hello world".translate("hello".maketrans("hello", "world")), "替换字符串")
# 小写转换 返回hello world
print("hello WORLD".casefold(), "小写转换")
# 格式化字符串 返回hello world
print("hello world".format(), "格式化字符串")
