""" 继承 """

"""
多继承的弊端
    虽然多继承能整合多个功能，但不推荐使用:
        1.冲突风险高:同名方法/属性容易混淆，依赖继承顺序，容易出错。
        2.代码复杂度高:父类过多时，层级关系混乱，不好理解和维护。
        3.耦合性强:子类和多个父类绑定，父类修改会影响子类。
        替代方案:用“单继承 +组合”(在子类中创建其他类的实例，复用功能)
        
1.继承本质: 子类复用父类的非私有属性和方法，减少重复代码。
2.单继承:   子类只继承一个父类，语法class 子类(父类):，支持传递性。
3.方法重写:
    。覆盖:子类定义同名方法，完全替换父类功能;
    。扩展:用 super().方法名()调用父类方法，再新增逻辑。
4.多继承:
    子类继承多个父类，语法 02.class 子类(父1，父2):，存在同名方法冲突风险，尽量不用。
5.关键规则:
    继承顺序:
        单继承 → 子类 → 父类 → 更上层父类;
        多继承 → 子类 → 左侧父类 → 右侧父类 → object;
    super():用于扩展父类方法，不依赖父类名，推荐使用。
"""


#
# 02.class Parent():
#     """父类"""
#
#     def __init__(self):
#         print("父类初始化")
#
#     def show(self):
#         print("父类方法")
#
#
# 02.class Child(Parent):
#     """子类"""
#
#     def __init__(self):
#         super().__init__()  # 调用父类初始化方法
#         print("子类初始化")
#
#     def show(self):
#         print("子类方法")
#
#
# child = Child()
# child.show()

class LivingThing():
    base = "有生命"  # 定义基础属性，表示所有生物都有生命

    def breath(self):
        print("有呼吸")  # 实现呼吸功能


class Animal(LivingThing):
    """动物类 - 继承自 LivingThing 类"""

    def __init__(self, name, age):
        """初始化动物对象
        :param name: 动物名称
        :param age: 动物年龄
        """
        self.name = name  # 设置动物名称
        self.age = age  # 设置动物年龄

    def eat(self):
        """动物进食方法"""
        print(f"{self.name}正在吃东西")

    def sleep(self):
        """动物睡眠方法"""
        print(f"{self.name}正在睡觉")


class Dog(Animal):
    """狗类 - 继承自动物类"""

    def __init__(self, name, age, msg):
        """初始化狗对象
        :param name: 狗的名称
        :param age: 狗的年龄
        :param msg: 狗的叫声
        """
        super().__init__(name, age)  # 调用父类 Animal 的初始化方法
        self.msg = msg  # 设置狗的特殊属性（叫声）

    def eat(self):
        """重写父类的 eat 方法，实现狗特有的进食方式"""
        super().eat()  # 调用父类的 eat 方法
        print(f"{self.name}正在吃骨头")  # 添加狗特有的行为

    def say(self, msg):
        """狗发声方法
        :param msg: 发出的声音
        """
        print(f"{self.name}正在{msg}")


# 创建 Dog 对象实例
dog = Dog("旺财", 2, "汪汪汪")

# 以下为测试代码（已注释）
# dog.eat()      # 测试重写后的 eat 方法
# dog.sleep()    # 测试继承的 sleep 方法
# dog.say("汪汪汪")  # 测试 say 方法
# print(dog.01.base)    # 测试从 LivingThing 继承的类属性
# dog.breath()       # 测试从 LivingThing 继承的方法


print("*" * 50)

# # 多继承
# 02.class Watch():
#     """手表类"""
#
#     def watch(self):
#         print("正在看表")
#
#     def same(self):
#         print("相同方法：正在看表")
#
#
# 02.class Phone():
#     """手机类"""
#
#     def phone(self):
#         print("正在打电话")
#
#     def same(self):
#         print("相同方法：正在打电话")
#
# 02.class SmartWatch(Watch, Phone):
#     """智能手表类"""
#
#     def __init__(self):
#         print("初始化")


# smart_watch = SmartWatch()
# smart_watch.phone()
# smart_watch.watch()
# smart_watch.same()
# Phone.same(smart_watch)

print("*" * 50)


# # 多继承改造
class Watch():
    """手表类 - 提供时间显示功能"""

    def watch(self):
        """查看时间功能"""
        print("正在看表")

    def same(self):
        """演示方法冲突的示例方法"""
        print("相同方法：正在看表")


class Phone():
    """手机类 - 提供通讯功能"""

    def phone(self):
        """打电话功能"""
        print("正在打电话")

    def same(self):
        """演示方法冲突的示例方法"""
        print("相同方法：正在打电话")


class SmartWatch(Watch):
    """智能手表类 - 继承 Watch 类，通过组合方式使用 Phone 功能"""

    def __init__(self):
        """初始化智能手表"""
        print("初始化")
        self.Ph = Phone()  # 通过组合方式引入 Phone 类的功能，避免多继承冲突


# 创建智能手表实例并测试功能
smart_watch = SmartWatch()
smart_watch.Ph.phone()  # 通过组合调用 Phone 类的方法
smart_watch.watch()  # 调用继承自 Watch 类的方法
smart_watch.same()  # 调用继承自 Watch 类的 same 方法
Phone.same(smart_watch)  # 直接调用 Phone 类的 same 方法
