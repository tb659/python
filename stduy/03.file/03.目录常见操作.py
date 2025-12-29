""""""

"""

1.所有操作需先导入 os模块(import os)
2.文件操作:
    重命名/移动:
        os.rename(源路径,目标路径)(同磁盘可用);。
    删除文件:
        os.remove(文件路径)(只能删文件，谨慎!)。
3.目录操作:
    创建目录:
        os.mkdir(目录路径)(不能已存在);。
    删除目录:
        os.rmdir(目录路径)(只能删空目录，谨慎!);。
    查看当前目录:
        os.getcwd()(返回绝对路径);。
    查看目录内容:
    os.listdir(目录路径)(返回文件/目录列表)。
4.路径检验(避免报错):
    路径是否存在:
        os.path.exists(路径);。
    是否为文件:
        os.path.isfile(路径);。
    是否为目录:
        os.path.isdir(路径)。
5.关键提醒:删除操作不可逆，建议先判断路径存在性再操作。




1、重命名
    os.rename(sourcePath, targetPath)
        源路径：     文件/目录的原始路径(相对路径或绝对路径)
        目标路径：   修改后的新路径(如果只改名字，路径不变;如果移动，改路径即可)


2、删除
    os.remove(targetPath)

    文件必须存在,否则报错 FilNotFoundError;
    只能删除文件，不能删除目录(删目录用 os.rmdir()，后面讲);
    删除后无法恢复(除非有备份)，谨慎操作!


3、创建文件夹
    os.mkdir(targetPath)
    
    目录不能已存在,否则报错 FileExistsError(文件已存在);
    父目录必须存在(比如要创建E:\a\b，必须先有E:\a目录，否则报错)。
    
    
4.删除文件夹
    os.rmdir(targetPath)
    
    目录必须存在,否则报错 FileNotFoundError;
    目录必须为空(没有文件、没有子目录)，否则报错WinError 145(目录不是空的);
    删除后无法恢复，谨慎操作!
    
    
5、查看当前目录
    os.getcwd()    
    

6、查看目录内容
    os.listdir()


7、检测路径是否存在
    os.path.exists()

8、检测是否是目录
    os.path.isdir()
    
9、检测是否是文件
    os.path.isfile()
    
    os.makedirs()           支持创建嵌套目录
    os.removedirs()         支持删除嵌套目录
    
    os.path.join()          路径拼接使用
    os.path.split()         路径分割使用
    os.path.splitext()      文件名和扩展名分割使用
    os.path.dirname()       获取目录名使用
    os.path.basename()      获取基础名使用
    os.path.getsize()       获取文件大小使用
"""

import os

# 示例1:重命名当前目录的文件(只改名字，不改路径)#把"image[备份].png"改成"image2.png"
os.rename("image[备份].png", "image2.png")

# 示例2:移动文件到同一磁盘的其他目录(改路径，名字不变)#把当前目录的"image2.png"移动到D盘tools目录
os.rename("image2.png", "D:/tools/image2.png")

# 示例3:重命名目录(和文件操作一致)#把当前目录的"old_dir"改成"new_dir"
os.rename("old_dir", "new_dir")

print("****************************************************************************")

# 删除文件
os.remove("image2.png")

print("****************************************************************************")

# 示例1:在当前目录创建"bingbing"文件夹
os.mkdir("bingbing")

# 示例2:在指定磁盘创建目录(绝对路径)
os.mkdir(r"E:\bingbing")

print("****************************************************************************")

# 示例1:删除当前目录的"bingbing"空目录
os.rmdir("bingbing")

# 示例2:删除指定磁盘的空目录(绝对路径)
os.rmdir(r"E:\bingbing")

print("****************************************************************************")

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)  # 输出示例:D:\PythonStudy\PythonBase

print("****************************************************************************")

# 示例1:查看当前目录的所有内容
current_files = os.listdir()
print("当前目录内容:", current_files)  # 输出示例:['test.txt'，'bingbing','main.py']

# 示例2:查看指定目录的内容(绝对路径)
tools_files = os.listdir(r"D:\tools")
print("D盘tools目录内容:", tools_files)

print("****************************************************************************")

# 示例1:检验文件是否存在(相对路径)
print(os.path.exists("test.txt"))  # 输出:True(存在)
print(os.path.exists("image.png"))  # 输出:False (不存在)

# 示例2:检验目录是否存在(绝对路径)
print(os.path.exists(r"D:\tools"))  # 输出:True (存在)
print(os.path.exists(r"D:\test_dir"))  # 输出:False (不存在)

print("****************************************************************************")

# 示例1:相对路径检验
print(os.path.isdir("bingbing"))  # 输出:True(是目录)
print(os.path.isdir("test.txt"))  # 输出:False(是文件，不是目录)
# 示例2:绝对路径检验
print(os.path.isdir(r"D:\tools"))  # 输出:True(是目录)

print("****************************************************************************")

# 示例1:相对路径检验
print(os.path.isfile("test.txt"))  # 输出:True(是文件)
print(os.path.isfile("bingbing"))  # 输出:False(是目录，不是文件)
# 示例2:绝对路径检验
print(os.path.isfile(r"D:\tools"))  # 输出:False(是目录，不是文件)

print("****************************************************************************")

# 示例:安全删除文件
file_path = "test.txt"
if os.path.isfile(file_path):  # 先判断是文件且存在
    os.remove(file_path)
    print(f"文件{file_path}删除成功!")
else:
    print(f"文件{file_path}不存在，无需删除~")

# 示例:安全创建目录
dir_path = "new_dir"
if not os.path.exists(dir_path):  # 先判断不存在
    os.mkdir(dir_path)
    print(f"目录{dir_path}创建成功!")
else:
    print(f"目录{dir_path}已存在，无需创建~")
