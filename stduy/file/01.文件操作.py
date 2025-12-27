""" 文件操作 """

"""
    模式      功能描述          是否创建新文件                     注意事项
    r        只读(默认)        否(文件不存在报错)                 只能读，不能写 
    w        只写             是(文件不存在创建，存在则覆盖内容)     只能写，不能读
    a        追加             是(文件不存在创建，存在则写在末尾)     只能写，不能读
    r+       读写             否(文件不存在报错)                  可同时读写，不覆盖原有内容
    w+       读写             是(文件不存在创建，存在则覆盖)        可同时读写
    a+       读写             是(文件不存在创建，存在则追加)        可同时读写，写在末尾

    关键:
        二进制文件操作需加 b模式(如rb、wb等)。

1、FileNotFoundError:        文件不存在(检查路径是否正确，或用w/a模式创建)。
2、io.Unsupportedoperation:  读写权限不匹配(比如 r模式下尝试写,改模式为r+)。
3、UnicodeDecodeError:       编码不匹配I指定正确的 encoding,如utf-8)。


1.文件操作流程:
    打开(open()/with)  一  读写(read()/write())  一  关闭(自动/close())。
2.关键参数:
    访问模式:     r只读、 w只写(覆盖)、 a追加、 rb/wb二进制读写;
    encoding:   文本文件用utf-8，二进制文件不用加。
3.读取方法:
    read(n):        读指定字符/字节，适合小文件;
    readline():     逐行读,适合大文件;
    readlines():    读所有行(列表),适合小文件。
4.写入方法:     write()(文本写字符串，二进制写字节串)。
5.文件指针:     tell()(返回指针所在位置)、seak(offset, where)(偏移量，位置0:开头 1:当前位置 2:末尾)
6.推荐用法:     用with语句自动关闭文件，避免资源泄露。

"""
# 使用基础方法打开文件并立即关闭
file = open("text.txt", mode="r", encoding="utf-8")
file.close()

print("*" * 50)

# 使用with语句自动管理文件资源
with open("text.txt", "r", encoding="utf-8") as file:
    # 打印文件对象的属性信息
    print("file.name =>", file.name)  # 文件名
    print("file.encoding =>", file.encoding)  # 文件编码
    print("file.mode =>", file.mode)  # 文件访问模式
    print("file.closed =>", file.closed)  # 文件是否已关闭

    # 读取前4个字符
    print(file.read(4))

    # 将文件指针重置到开头
    file.seek(0)
    # 读取全部内容
    print(file.read())

    # 将文件指针重置到开头
    file.seek(0)
    # 读取第一行
    line1 = file.readline()
    # 读取第二行
    line2 = file.readline()
    print("第一行 =>", line1)
    print("第二行 =>", line2)

    # 将文件指针重置到开头
    file.seek(0)
    # 读取所有行到列表
    lines = file.readlines()
    print(lines)

    # 将文件指针重置到开头
    file.seek(0)
    # 逐行遍历文件
    for line in file:
        print(line)

print("*" * 50)

# 使用w模式创建/覆盖文件并写入内容
with open("text1.txt", "w", encoding="utf-8") as file:
    file.write("hello world\n")

# 使用a模式追加内容到文件
with open("text2.txt", "a", encoding="utf-8") as file:
    file.write("hello world\n")

print("*" * 50)

# 使用a+模式进行追加和读取操作
with open("text3.txt", "a+", encoding="utf-8") as file:
    # 写入内容（此时文件指针在文件末尾）
    file.write("hello world\n")
    # 将文件指针重置到开头（偏移量1，位置0表示开头）
    file.seek(1, 0)
    # 读取文件内容
    print(file.read())

print("*" * 50)

# 以二进制读取模式打开图片文件
with open("img.jpg", "rb") as img:
    # 读取图片的二进制数据
    b = img.read()

# 以二进制写入模式创建图片备份
with open("img_bak.jpg", "wb") as img:
    # 将二进制数据写入新文件
    img.write(b)
    # 打印当前文件指针位置
    print(img.tell())

# 提示图片备份完成
