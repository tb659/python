""" 模块 """

"""
模块使用要点总结
    1、import语句：导入整个模块，使用时需要模块前缀
    2、from...import语句：导入模块中的特定项目，可直接使用
    3、别名导入：使用as关键字简化模块名或避免冲突
    4、相对导入vs绝对导入：相对导入使用.和..，绝对导入使用完整模块路径
    5、动态导入：使用importlib模块在运行时动态导入
    6、模块缓存：Python会缓存已导入的模块，避免重复导入开销
    7、包结构：使用目录和__init__.py文件组织模块
    8、模块搜索路径：Python按照sys.path中的路径顺序搜索模块
    9、自定义模块：创建.py文件即可作为模块使用
    10、内置模块：充分利用Python丰富的标准库
    通过以上示例，您可以掌握Python中模块的各种使用方式和最佳实践。

包使用要点总结
    1、包的本质:包含init_.py 文件的文件夹，用于组织多个相关模块，避免命名冲突
    2、包的创建:新建包 → 放入相关模块。
    3、种常用导入方式:
        import 包名.模块名     层级清晰，无冲突，适合复杂项目:from 包名 
        import 模块名         简化书写，不用带包名
        from 包名 import *    批量导入，需在_init_.py 中配置_a11
    4、关键文件:_init_.py 用于标识包、控制导入范围、执行初始化。
    5、实用场景:项目代码较多时，用包按功能分类(比如“用户模块包”“订单模块包”)，让代码结构更清晰，便于维护。
"""

""" Python模块使用详解 """

# 1. 导入整个模块
import math


def import_module_example():
    """
    使用import语句导入整个模块
    使用时需要加上模块名作为前缀
    """
    # 使用math模块中的函数和常量
    result = math.sqrt(16)  # 计算平方根
    print(f"math.sqrt(16) = {result}")  # 打印结果 4.0

    pi_value = math.pi  # 获取圆周率
    print(f"math.pi = {pi_value}")  # 打印结果 3.141592653589793

    sine_value = math.sin(math.pi / 2)  # 计算正弦值
    print(f"math.sin(π/2) = {sine_value}")  # 打印结果 1.0


# 2. 导入模块并设置别名
import datetime as dt


def import_alias_example():
    """
    使用as关键字为模块设置别名
    可以简化模块名或避免命名冲突
    """
    # 使用别名dt代替datetime
    now = dt.datetime.now()
    print(f"当前时间: {now}")  # 打印当前时间  2025-12-21 20:23:09.974819

    today = dt.date.today()
    print(f"今天日期: {today}")  # 打印当前日期  2025-12-21


# 3. 从模块中导入特定函数或变量
from random import randint, choice


def import_specific_items_example():
    """
    使用from...import语句导入模块中的特定项目
    可以直接使用导入的项目，无需模块前缀
    """
    # 直接使用导入的函数
    random_number = randint(1, 100)  # 生成1到100之间的随机整数
    print(f"随机数: {random_number}")

    fruits = ['苹果', '香蕉', '橙子', '葡萄']
    random_fruit = choice(fruits)  # 从列表中随机选择一个元素
    print(f"随机水果: {random_fruit}")


# 4. 导入模块中的所有内容（不推荐）
from statistics import *


def import_all_example():
    """
    使用*导入模块中的所有公共项目
    注意：这种方式可能导致命名冲突，一般不推荐使用
    """
    data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

    mean_val = mean(data)  # 计算平均值
    median_val = median(data)  # 计算中位数
    mode_val = mode(data)  # 计算众数

    print(f"数据: {data}")  # 打印数据 [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    print(f"平均值: {mean_val}")  # 打印平均值 5
    print(f"中位数: {median_val}")  # 打印中位数 5.0
    print(f"众数: {mode_val}")  # 打印众数 5


# 5. 条件导入
def conditional_import_example():
    """
    根据条件动态导入模块
    """
    try:
        # 尝试导入可能不存在的模块
        import numpy as np
        print("numpy模块已导入")
        array = np.array([1, 2, 3, 4, 5])
        print(f"numpy数组: {array}")
    except ImportError:
        print("numpy模块未安装，使用内置列表替代")
        array = [1, 2, 3, 4, 5]
        print(f"普通列表: {array}")


# 6. 相对导入和绝对导入
# 假设我们有一个包结构:
# my_package/
#   __init__.py
#   module1.py
#   subpackage/
#     __init__.py
#     module2.py

# 在subpackage/module2.py中:
# from ..module1 import something  # 相对导入
# from my_package.module1 import something  # 绝对导入

# 7. 动态导入模块
import importlib


def dynamic_import_example():
    """
    使用importlib动态导入模块
    """
    # 动态导入math模块
    math_module = importlib.import_module('math')
    result = math_module.sqrt(25)
    print(f"动态导入math模块计算sqrt(25) = {result}")

    # 根据字符串动态导入模块
    module_name = 'random'
    random_module = importlib.import_module(module_name)
    random_int = random_module.randint(1, 10)
    print(f"动态导入{module_name}模块生成随机数: {random_int}")


# 8. 模块属性查看
def module_inspection_example():
    """
    查看模块的属性和方法
    """
    import sys

    print("sys模块的部分属性:")
    print(f"Python版本: {sys.version}")
    print(f"平台: {sys.platform}")
    print(f"路径: {sys.path[:3]}...")  # 只显示前3个路径

    # 查看模块的所有属性
    print("\nmath模块的部分函数:")
    # 获取math模块中所有不以下划线开头的属性和方法名
    math_functions = [attr for attr in dir(math) if not attr.startswith('_')]
    print(math_functions[:10])  # 显示前10个函数


# 9. 创建和使用自定义模块
# 创建一个名为my_utils.py的文件:
"""
# 16.my_utils.py
def greet(name):
    '''问候函数'''
    return f"你好, {name}!"

def calculate_circle_area(radius):
    '''计算圆的面积'''
    import math
    return math.pi * radius ** 2

PI = 3.14159

# 私有函数（以下划线开头）
def _internal_function():
    return "这是私有函数"

# 在模块中执行的代码（模块被导入时会执行）
print("my_utils模块已被导入")
"""


# 使用自定义模块
def custom_module_example():
    """
    演示如何创建和使用自定义模块
    注意：需要在同一目录下创建my_utils.py文件
    """
    try:
        import my_utils

        greeting = my_utils.greet("张三")
        print(greeting)

        area = my_utils.calculate_circle_area(5)
        print(f"半径为5的圆面积: {area:.2f}")

        print(f"PI常量: {my_utils.PI}")

    except ImportError:
        print("未找到my_utils模块，请确保在同一目录下创建该模块")


# 10. 包的使用
# 创建包结构:
# my_package/
#   __init__.py
#   calculator.py
#   formatter.py

"""
# my_package/__init__.py
# 包的初始化文件
print("my_package包正在初始化")

# 可以在这里定义包级别的变量或函数
VERSION = "1.0.0"

def package_info():
    return f"MyPackage version {VERSION}"
"""

"""
# my_package/calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""

"""
# my_package/formatter.py
def format_name(first, last):
    return f"{last.upper()}, {first.capitalize()}"
"""

#  1、引入包 包内所有模块的导出根据__init__来控制
# from my_package import *

# print(f"格式化姓名: {format_name("ke", "le")}") # 1、__init__中， __all__rugo定义，且不导出format_name 这里获取不到会报错

#  2、引入包里的模块 模块内部的导出根据__all__来控制


# print(f"13 × 4 = {multiply(13, 4)}")  # multiply 这里获取不到会报错


# 使用包
def package_example():
    """
    演示包的使用方法
    """
    try:
        # 导入包中的模块
        import my_package.calculator as calc
        import my_package.formatter as fmt

        # 使用包中的函数
        sum_result = calc.add(10, 5)
        print(f"10 + 5 = {sum_result}")

        product_result = calc.multiply(3, 4)
        print(f"3 × 4 = {product_result}")

        formatted_name = fmt.format_name("san", "zhang")
        print(f"格式化姓名: {formatted_name}")

        # 如果__init__.py中有定义，可以直接访问包级别内容
        # print(my_package.VERSION)
        # print(my_package.package_info())

    except ImportError:
        print("未找到my_package包，请先创建包结构")


# 11. 模块缓存机制
def module_cache_example():
    """
    演示Python的模块缓存机制
    """
    import sys

    print("已导入的模块:")
    # 获取已导入的模块名称列表
    loaded_modules = list(sys.modules.keys())
    # 筛选出以'sys'或'math'开头的模块名称
    python_modules = [mod for mod in loaded_modules if mod.startswith('sys') or mod.startswith('math')]
    # 打印这些模块名称
    print(python_modules)

    # 再次导入不会重新执行模块代码
    print("再次导入math模块（无额外输出）")


# 12. reload重新加载模块
def reload_module_example():
    """
    演示如何重新加载模块（开发时有用）
    """
    import importlib

    try:
        import my_package
        print("首次导入my_utils模块")

        # 修改my_utils.py文件后，重新加载模块
        importlib.reload(my_package)
        print("重新加载my_utils模块")

    except ImportError:
        print("未找到my_utils模块")


# 13. 模块搜索路径
def module_search_path_example():
    """
    查看和修改模块搜索路径
    """
    import sys

    print("模块搜索路径:")
    for i, path in enumerate(sys.path[:5]):  # 显示前5个路径
        print(f"{i + 1}. {path}")

    # 可以添加自定义路径
    # sys.path.append('/path/to/my/modules')
    # 或者在环境变量PYTHONPATH中设置


# 14. 内置模块使用示例
def builtin_modules_example():
    """
    演示常用内置模块的使用
    """
    # os模块 - 操作系统接口
    import os
    print(f"当前工作目录: {os.getcwd()}")
    print(f"操作系统: {os.name}")

    # json模块 - JSON处理
    import json
    data = {"name": "张三", "age": 25, "city": "北京"}
    # 将字典序列化为JSON格式字符串，ensure_ascii=False允许非ASCII字符正常显示
    json_string = json.dumps(data, ensure_ascii=False)
    print(f"JSON序列化: {json_string}")

    # re模块 - 正则表达式
    import re
    text = "我的电话号码是13812345678"
    phone_pattern = r'1[3-9]\d{9}'
    match = re.search(phone_pattern, text)
    if match:
        print(f"找到电话号码: {match.group()}")

    # time模块 - 时间处理
    import time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"当前时间: {current_time}")


# 15. 模块文档和帮助
def module_documentation_example():
    """
    查看模块文档和帮助信息
    """
    import math

    # 查看模块文档字符串
    print("math模块文档:")
    print(math.__doc__[:100] + "...")  # 只显示前100个字符

    # 查看函数文档
    print(f"\nsqrt函数文档: {math.sqrt.__doc__}")

    # 使用help函数查看详细帮助（在交互式环境中使用）
    # help(math)
    # help(math.sqrt)


# 主程序演示各种模块使用方式
def main():
    """
    主函数，演示各种模块使用方式
    """
    print("=== Python模块使用演示 ===\n")

    print("1. 导入整个模块:")
    import_module_example()

    print("\n2. 模块别名:")
    import_alias_example()

    print("\n3. 导入特定项目:")
    import_specific_items_example()

    print("\n4. 导入所有项目:")
    import_all_example()

    print("\n5. 条件导入:")
    conditional_import_example()

    print("\n7. 动态导入:")
    dynamic_import_example()

    print("\n8. 模块检查:")
    module_inspection_example()

    print("\n9. 内置模块:")
    custom_module_example()

    print("\n10. 使用包:")
    package_example()

    print("\n13. 模块搜索路径:")
    module_search_path_example()

    print("\n14. 内置模块使用示例:")
    builtin_modules_example()


# 程序入口
if __name__ == "__main__":
    main()
