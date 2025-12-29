""" 多态 """

"""
1.多态本质:     同一方法名，不同对象有不同实现，调用时产生不同结果。
2.两种实现方式:
    鸭子类型(推荐):   不用继承，只要对象有同名方法，就能调用;
    继承 +方泜重写:   子类继承父类，重写同名方法，适合有层级关系的场景。
3.核心接口:     多态依赖“统一方法名”作为接口，调用者通过接口操作对象，不用关心对象类型。
4.关键优势:     统一接口、便于扩展、提高可读性。
5.Python 特色:
    鸭子类型让多态更灵活，不用像其他语言(如Java)那样依赖抽象类或接口，零基础更容易上手。
"""


# 支付类 鸭子类型
class WechatPay():
    """微信支付"""

    def pay(self, money):  # 定义pay方法，实现微信支付功能
        print(f"微信支付￥{money}元")  # 打印微信支付信息


class Alipay():
    """支付宝"""

    def pay(self, money):  # 定义pay方法，实现支付宝支付功能
        print(f"支付宝支付￥{money}元")  # 打印支付宝支付信息


def pay(obj, money):  # 定义通用支付函数
    """支付"""  # 函数说明
    obj.pay(money)  # 调用传入对象的pay方法


pay(WechatPay(), 10)  # 创建微信支付对象并支付10元
pay(Alipay(), 20)  # 创建支付宝对象并支付20元

print("*" * 50)  # 打印分隔线


class Animal():
    """动物"""

    def say(self):  # 定义动物叫声方法
        print("叫叫叫")  # 打印默认叫声


class Dog(Animal):  # Dog类继承Animal类
    """狗"""

    def say(self):  # 重写父类的say方法
        print("汪汪汪")  # 打印狗的叫声


class Cat(Animal):  # Cat类继承Animal类
    """猫"""

    def say(self):  # 重写父类的say方法
        print("喵喵喵")  # 打印猫的叫声


def animal_say(animal):  # 定义动物叫声函数
    animal.say()  # 调用动物对象的say方法


animal_say(Dog())  # 调用狗的叫声方法
animal_say(Cat())  # 调用猫的叫声方法

print("*" * 50)  # 打印分隔线


class Red():
    """红色"""

    def eat(self):  # 定义eat方法
        print("红色的")  # 打印颜色信息


class Blue():
    """蓝色"""

    def eat(self):  # 定义eat方法
        print("蓝色的")  # 打印颜色信息


class Fruit():
    """水果"""

    def has_color(self, color):  # 定义颜色方法
        color.eat()  # 调用传入颜色对象的eat方法


Fruit().has_color(Red())  # 创建水果对象并传入红色对象
Fruit().has_color(Blue())  # 创建水果对象并传入蓝色对象
