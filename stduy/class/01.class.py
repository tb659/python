""" 类 """

""" 
    1.面向对象核心:   以“对象”为中心，注重“谁来做”，适合复杂、可复用的任务。
    2.类和对象:
        类:   抽象的“设计图”包含属性(特征)和方法(行为)
        对象: 类的“成品”，真实存在，能调用方法、访问属性;
        关系: 先定义类，再创建对象。
    3.类的组成:
        方法:类里的函数(比如 start())，实例方法第一个参数必须是 self ，由对象调用。
        属性:类属性(所有对象共享)和实例属性(每个对象独有)。
    4.构造函数 init:创建对象时自动调用，用于初始化实例属性，简化赋值流程。
    5.关键语法:
        定义类:    class 类名:..(大驼峰命名);
        创建对象:   对象名=类名(参数)(参数传给init);
        调用方法/访问属性:  对象名.方法名()、对象名.属性名。 
"""

# # 定义一个汽车类
# class Car():
#     """汽车类"""
#
#
# pass  # 占位
#   
# # 创建对象（实例化对象）
# car1 = Car()
# print(car1)  # <__main__.Car object at 0x0000020EA5EB0E80> （对象的内存地址）
#
# car2 = Car()
# print(car2)  # <__main__.Car object at 0x0000020EA5EB0F70>


""" 实例方法 """

# class Car:
#     """汽车类"""
#
#     # 实例方法：启动汽车
#     def start(self):
#         print("汽车启动中...")
#         print("self代表当前对象：", self)  # self会自动绑定调用方法的对象
#
#     # 实例方法：行驶
#     def drive(self):
#         print("汽车正在行驶～")
#
#
# # 创建对象
# car1 = Car()
#
# # 调用方法（不用传self参数）
# car1.start()
# car1.drive()

""" 实例方法 """

""" 类属性 """

# class Car:
#     """汽车类"""
#     wheel_count = 4  # 类属性
#
#     def start(self):
#         print("汽车启动中...")
#
# # 1、直接通过类访问类属性
# print(Car.wheel_count)
#
# # 2、创建对象访问类属性
# car1 = Car()
# print(car1.wheel_count)

""" 类属性 """

""" 实例属性 """


class Car:
    """汽车类"""
    wheel_count = 4

    # 创建对象时，会自动调用__init__方法
    def __init__(self, name, color):
        """初始化方法"""
        self.name = name
        self.color = color

    # 程序结束时，会自动调用__del__方法
    def __del__(self):
        print(f"{self.name}被销毁了！")

    def show_info(self):
        # 创建实例属性
        print(f"品牌：{self.name}, 颜色：{self.color}, 轮子个数：{self.wheel_count}")


# 创建对象并设置实例属性
# car1 = Car()
# car1.name = "保时捷"
# car1.color = "黑色"
# car1.show_info()

car1 = Car("保时捷", "黑色")
car1.show_info()

car2 = Car(color="蓝色", name=" Audi")
car2.show_info()

""" 实例属性 """
