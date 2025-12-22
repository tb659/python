""" 函数的使用 """

"""
1.函数核心:封装重复逻辑，实现“定义一次，多次调用”提高代码复用性和可维护性。

2.三大核心要素:
    定义:      def函数名(参数):函数体return返回值;
    参数:      位置参数(必传)、默认参数(可选)、*args(任意位置参数)**kwargS(任意关键字参数);
    返回值:    用return 指定，可返回单个值、多个(元组)，无返回值则隐式返回None。
    
3.变量作用域:
    局部变量:   函数内定义，仅函数内生效;
    全局变量:   函数外定义，全局生效;函数内修改需用 global 声明。
    
4.关键注意:
    先定义后调用，不调用不执行;
    return 会终止函数执行，后面的代码不运行。
   
"""

print("*" * 50)


# 1. 基本函数定义与调用 定义一个简单的函数，无参数无返回值
def hello():
    """
    输出问候语的函数
    该函数不接受任何参数，也不返回任何值
    """
    print("hello world")


# 调用函数
hello()

print("*" * 50)


# 2. 带位置参数的函数
def greet(name):
    """
    向指定的人打招呼

    参数:
        name (str): 要打招呼的人的名字
    """
    print(f"Hello, {name}!")


# 调用带参数的函数
greet("Alice")  # 输出: Hello, Alice!

print("*" * 50)


# 3. 多个位置参数
def introduce(name, age):
    """
    介绍一个人的基本信息

    参数:
        name (str): 人的姓名
        age (int): 人的年龄
    """
    print(f"我是{name}，今年{age}岁")


# 按顺序传入参数
introduce("Bob", 25)  # 输出: 我是Bob，今年25岁

print("*" * 50)


# 4. 带默认参数的函数
def greet_with_title(name, title="先生"):
    """
    带称谓的问候函数

    参数:
        name (str): 姓名
        title (str): 称谓，默认为"先生"
    """
    print(f"您好，{title}{name}！")


# 使用默认参数
greet_with_title("张三")  # 输出: 您好，先生张三！

# 覆盖默认参数
greet_with_title("李四", "女士")  # 输出: 您好，女士李四！

print("*" * 50)


# 5. 带关键字参数的函数
def create_profile(name, age, city):
    """
    创建个人资料

    参数:
        name (str): 姓名
        age (int): 年龄
        city (str): 城市
    """
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")


# 使用关键字参数，可以不按定义顺序传参
create_profile(city="北京", name="王五", age=30)  # 输出: 姓名: 王五, 年龄: 30, 城市: 北京

print("*" * 50)


# 6. 带可变参数的函数
def sum_numbers(*numbers):
    """
    计算任意数量数字的和

    参数:
        *numbers: 可变数量的位置参数，会被打包成元组
    返回:
        int/float: 所有数字的和
    """
    total = 0
    for num in numbers:
        total += num
    return total


# 传入任意数量的参数
result = sum_numbers(1, 2, 3, 4, 5)  # 结果: 15
print(f"总和: {result}")

print("*" * 50)


# 7. 带可变关键字参数的函数
def print_info(**info):
    """
    打印个人信息

    参数:
        **info: 可变数量的关键字参数，会被打包成字典
    """
    print("个人信息:")
    for key, value in info.items():
        print(f"{key}: {value}")


# 传入任意数量的关键字参数
print_info(name="赵六", age=28, job="工程师", city="上海")
"""
# 输出: 
个人信息
name: 赵六
age: 28
job: 工程师
city: 上海
"""

print("*" * 50)


# 8. 混合参数的函数
def complex_function(required_arg, default_arg="default", *args, **kwargs):
    """
    展示各种参数类型的混合使用

    参数:
        required_arg: 必需的位置参数
        default_arg: 带默认值的参数
        *args: 可变位置参数
        **kwargs: 可变关键字参数
    """
    print(f"必需参数: {required_arg}")
    print(f"默认参数: {default_arg}")

    if args:
        print(f"可变位置参数: {args}")

    if kwargs:
        print("可变关键字参数:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")


# 调用复杂参数函数
complex_function(
    "必填项",
    "自定义默认值",
    "额外参数1", "额外参数2",
    name="测试", type="示例"
)
"""
# 输出: 
必需参数: 必填项
默认参数: 自定义默认值
可变位置参数: ('额外参数1', '额外参数2')
可变关键字参数:
  name: 测试
  type: 示例
"""

print("*" * 50)


# 9. 函数的返回值
def calculate_area(length, width):
    """
    计算矩形面积

    参数:
        length (float): 长度
        width (float): 宽度

    返回:
        float: 矩形面积
    """
    area = length * width
    return area


# 获取函数返回值
area_result = calculate_area(5, 3)
print(f"矩形面积: {area_result}")  # 输出: 矩形面积: 15

print("*" * 50)


# 10. 多返回值函数
def get_name_parts(full_name):
    """
    将全名分解为姓和名

    参数:
        full_name (str): 全名

    返回:
        tuple: 包含姓和名的元组
    """
    parts = full_name.split(" ")
    if len(parts) >= 2:
        return parts[0], parts[1]
    else:
        return full_name, ""


# 接收多个返回值
first_name, last_name = get_name_parts("张 三")
print(f"姓: {first_name}, 名: {last_name}")  # 输出: 姓: 张, 名: 三

print("*" * 50)


# 函数变量的使用
# 1. 局部变量是在函数内部定义的变量，只能在函数内部访问
def my_function():
    """
    演示局部变量的使用
    """
    local_var = "我是局部变量"
    print(local_var)


my_function()  # 输出: 我是局部变量
# print(local_var)  # 这行会报错，因为local_var在函数外部无法访问

print("*" * 50)

# 2. 全局变量是在函数外部定义的变量，可以在整个程序中访问。
global_var = "我是全局变量"


def access_global():
    """
    在函数中访问全局变量
    """
    print(global_var)  # 可以直接访问全局变量


access_global()  # 输出: 我是全局变量
print(global_var)  # 在函数外部也可以访问

print("*" * 50)

# 3. 全局变量和局部变量同名的情况  当函数内部定义了与全局变量同名的局部变量时，函数内部优先使用局部变量。
x = "全局变量"


def variable_scope_demo():
    """
    演示变量作用域
    """
    x = "局部变量"  # 这是一个局部变量，与全局变量同名
    print(f"函数内部: {x}")


variable_scope_demo()  # 输出: 函数内部: 局部变量
print(f"函数外部: {x}")

print("*" * 50)

# 4. 使用 global 关键字修改全局变量
# 全局变量
counter = 0


def increment_counter():
    """
    使用global关键字修改全局变量
    """
    global counter  # 声明要修改的是全局变量
    counter += 1
    print(f"计数器当前值: {counter}")


def bad_increment():
    """
    不使用global关键字的错误示例
    """
    # counter += 1  # 这会报错，因为试图修改未声明的局部变量
    pass


increment_counter()  # 输出: 计数器当前值: 1
increment_counter()  # 输出: 计数器当前值: 2
print(f"全局计数器: {counter}")  # 输出: 全局计数器: 2

print("*" * 50)


# 5. 嵌套函数中的变量作用域
def outer_function():
    """
    外层函数
    """
    outer_var = "外层变量"

    def inner_function():
        """
        内层函数
        """
        inner_var = "内层变量"
        print(f"在内层函数中访问外层变量: {outer_var}")
        print(f"内层变量: {inner_var}")

    inner_function()
    # print(inner_var)  # 这会报错，内层变量在外层函数中不可访问


outer_function()
# 输出: 在内层函数中访问外层变量: 外层变量
# 内层变量: 内层变量

print("*" * 50)


# 6. 使用 nonlocal 关键字
def outer_func():
    """
    演示nonlocal关键字的使用
    """
    x = 10

    def inner_func():
        nonlocal x  # 声明x是非局部变量（外层函数的变量）
        x += 5
        print(f"内层函数中的x: {x}")

    print(f"调用内层函数前的x: {x}")
    inner_func()
    print(f"调用内层函数后的x: {x}")


outer_func()
"""
# 输出: 
调用内层函数前的x: 10
内层函数中的x: 15
调用内层函数后的x: 15
"""

print("*" * 50)

# 7. 实际应用示例
# 全局配置变量
APP_NAME = "我的应用程序"
DEBUG_MODE = True
MAX_CONNECTIONS = 100


def configure_app(new_name=None, debug=None):
    """
    配置应用程序设置

    参数:
        new_name (str): 新的应用名称
        debug (bool): 调试模式开关
    """
    global APP_NAME, DEBUG_MODE

    if new_name is not None:
        APP_NAME = new_name

    if debug is not None:
        DEBUG_MODE = debug

    print(f"应用已配置: {APP_NAME}")
    print(f"调试模式: {DEBUG_MODE}")


def get_connection():
    """
    获取连接，演示局部变量使用
    """
    # 局部变量
    connection_id = id(object())
    print(f"创建连接 ID: {connection_id}")
    return connection_id


# 使用全局变量
print(f"初始应用名称: {APP_NAME}")
configure_app("新应用", False)
print(f"更新后应用名称: {APP_NAME}")

# 使用局部变量
conn = get_connection()
# connection_id 在这里无法访问，因为它是一个局部变量
