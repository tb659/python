""" 字符串 """

str1 = "hello "
str2 = "world"
print(str1 + str2)
print("l" in str1)
print("l" not in str2)
print(str1[0])
print(str1[-1])
# print(str1[10]) # 报错 IndexError: string index out of range

print("*" * 50)

id = "01234567890"
# id[start:end:step]
print(id[1:2])
print(id[:2])
print(id[2:])
print(id[2:4])
print(id[2:8:2])

print("*" * 50)

print(1, "\t", 2)  # \t 制表符
print(3, "\n", 4)  # \n 换行符
print(5, "\r", 6)  # \r 回车符
print(7, "\b", 8)  # \b 退格符
print(9, "\f", 10)  # \f 换页符
print(11, "\v", 12)  # \v 垂直制表符
print(13, "\\", 14)  # \ 斜杠符
print(15, "\a", 16)  # \a 响铃符
print(17, "\u0000", 18)  # \u0000 16进制数
print(19, "\U00000000", 20)  # \U00000000 32进制数
print(21, "\'", 22)  # \' 单引号符`
print(23, "\"", 24)  # \" 双引号符
print(25, "\x00", 26)  # \x00 16进制数
print(r"D:\dev\table")  # r 表示原始字符串，不会对字符串中的特殊字符进行转义
print(f"id是{id}")  # f 表示格式化字符串，可以在字符串中插入变量

print("*" * 50)

num1 = 123
num2 = 1
print(F"0学号是：{num1}")
print(F"1学号是：{num2}")
print(F"2学号是：{num2:3}")  # 3 显示3位
print(F"3学号是：{num2:03}")  # 03 表示不足补0

print("*" * 50)

P = 3.14159
print(f"圆周率是：{P:.2f}")  # .2f 表示保留2位小数 四舍五入
print(f"圆周率是：{P:.10f}")  # .10f 表示保留10位小数 四舍五入

print("*" * 50)

name = "Tom"
print(f"姓名：{name:10}", "默认左对齐")  # 默认左对齐
print(f"姓名：{name:<10}", "左对齐")  # > 左对齐
print(f"姓名：{name:>10}", "右对齐")  # > 右对齐
print(f"姓名：{name:^10}", "居中对齐")  # ^ 居中对齐

print("*" * 50)

print(f"姓名：{name:_<10}", "填充字符")  # _ 填充字符
print(f"姓名：{name:_>10}", "填充字符")  # _ 填充字符
print(f"姓名：{name:_^10}", "填充字符")  # _ 填充字符

print("*" * 50)

# 字符串方法
print("hello world".find("world"), "第一个匹配的位置 返回6")  # 第一个匹配的位置 返回6
print("hello world".rfind("world"), "匹配位置 返回6")  # 匹配位置 返回6
print("hello world".index("world"), "匹配位置 返回6")  # 匹配位置 返回6
print("hello world".rindex("world"), "匹配位置 返回6")  # 匹配位置 返回6
print("hello world".count("l"), "匹配数量 返回3")  # 匹配数量 返回3
print("hello world".startswith("hello"), "判断是否以指定字符串开头 返回True")  # 判断是否以指定字符串开头 返回True
print("hello world".endswith("world"), "判断是否以指定字符串结尾 返回True")  # 判断是否以指定字符串结尾 返回True
print("hello world".replace("hello", "hi"),
      "替换字符串 不改变原字符串 返回新字符串hi world")  # 替换字符串 不改变原字符串 返回新字符串hi world
print("hello world".split(" "), "分割字符串 返回列表['hello', 'world']")  # 分割字符串 返回列表['hello', 'world']
print("hello world".join(["hello", "world"]),
      "连接字符串 返回hellohello worldworld")  # 连接字符串 返回hellohello worldworld js是["hello", "world"].join("hello world")
print("hello world".lower(), "小写 返回hello world")  # 小写 返回hello world
print("hello world".upper(), "大写 返回HELLO WORLD")  # 大写 返回HELLO WORLD
print("hello world".title(), "首字母大写 返回Hello World")  # 首字母大写 返回Hello World
print("hello world".capitalize(), "首字母大写 返回Hello world")  # 首字母大写 返回Hello world
print("hello world".swapcase(), "大小写转换 返回HELLO WORLD")  # 大小写转换 返回HELLO WORLD
print("hello world".strip(), "去除字符串首尾空格 返回hello world")  # 去除字符串首尾空格 返回hello world
print("hello world".lstrip(), "去除字符串左侧空格 返回hello world")  # 去除字符串左侧空格 返回hello world
print("hello world".rstrip(), "去除字符串右侧空格 返回hello world")  # 去除字符串右侧空格 返回hello world
print("hello world".center(20, "*"),
      "居中填充字符 20个字符 返回 ****hello world*****")  # 居中填充字符 20个字符 返回 ****hello world*****
print("hello world".zfill(20), "填充字符 20个字符 返回000000000hello world")  # 填充字符 20个字符 返回000000000hello world
print("*" * 50)
print("hello world".isalpha(), "判断是否只包含字母 返回False")  # 判断是否只包含字母 返回False
print("hello world".isdigit(), "判断是否只包含数字 返回False")  # 判断是否只包含数字 返回False
print("hello world".isalnum(), "判断是否只包含字母数字 返回False")  # 判断是否只包含字母数字 返回False
print("hello world".isidentifier(), "判断是否只包含标识符 返回False")  # 判断是否只包含标识符 返回False
print("hello world".isprintable(), "判断是否只包含可打印字符 返回True")  # 判断是否只包含可打印字符 返回True
print("hello world".isspace(), "判断是否只包含空格 返回False")  # 判断是否只包含空格 返回False
print("hello world".istitle(), "判断是否只包含标题 返回False")  # 判断是否只包含标题 返回False
print("hello world".isupper(), "判断是否只包含大写字母 返回False")  # 判断是否只包含大写字母 返回False
print("hello world".islower(), "判断是否只包含小写字母 返回False")  # 判断是否只包含小写字母 返回False
print("hello world".encode(), "字符串转字节 默认utf-8")  # 编码字符串 默认utf-8 返回b'hello world'
print(type("hello world".encode()))  # 返回<class 'bytes'>
print("hello world".encode().decode(), "字节转字符串 默认utf-8")  # 编码字符串 默认utf-8 返回hello world
print("*" * 50)
print("hello world".expandtabs(), "替换tab字符为空格 默认4个空格")  # 替换tab字符为空格 默认4个空格 返回hello world
print("hello world".partition(" "), "分割字符串 默认空格")  # 分割字符串 默认空格 返回('hello', ' ', 'world')
print("hello world".rpartition(" "), "分割字符串 默认空格")  # 分割字符串 默认空格 返回('hello', ' ', 'world')
print("hello world".partition(" ") == "hello world".rpartition(" "))  # 判断是否相等 返回 True
print("hello world yeah".partition(" "), "分割字符串 默认空格")  # 分割字符串 默认空格 返回('hello', ' ', 'world yeah')
print("hello world yeah".rpartition(" "), "分割字符串 默认空格")  # 分割字符串 默认空格 返回('hello world', ' ', 'yeah')
print("hello world yeah".partition(" ") == "hello world yeah".rpartition(" "))  # 判断是否相等 返回 False
print("hello world yeah".splitlines(), "分割字符串 默认换行符")  # 分割字符串 默认换行符
print("hello world".maketrans("hello", "world"), "创建转换表")  # 创建转换表 返回{104: 119, 101: 111, 108: 108, 111: 100}
print("hello world".translate("hello".maketrans("hello", "world")), "替换字符串")  # 替换字符串
print("hello world".casefold(), "大小写转换")  # 大小写转换 返回hello world
print("hello world".format(), "格式化字符串")  # 格式化字符串 返回hello world
