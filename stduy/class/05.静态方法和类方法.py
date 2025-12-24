""" 静态方法和类方法 """

"""
对比维度        静态方法( @staticmethod )   类方法( @classmethod )             实例方法

第一个参数      无(不用 self/cls)           cls(代表类)                        self(代表实例)
装饰器         需要 @staticmethod          需要 @classmethod                 不需要
访问属性       只能访问属性(不推荐)           只能访问类属性(通过c1s)              能访问实例属性(通过 self)
调用方式       类名.方法名()(推荐)           类名.方法名()(推荐)对象.方法名(0)      对象.方法名()(必须创建对象)
核心用途       对象.方法名()                操作类属性、工厂方法                  操作实例属性、实例相关功能


要操作实例属性→用实例方法(self);

要操作类属性→用类方法(cls);

啥属性都不操作一用静态方法(无self /cls)。



1.静态方法:类里的独立工具函数，无se1f/c1s，不依赖类/实例，直接用类名调用，适合通用工具功能。
2.类方法:绑定类的方法，第一个参数是c1s，可访问/修改类属性，适合类级别的操作。
3.调用优先级:
    静态方法、类方法:优先用类名.方法名();
    实例方法:必须用 对象.方法名()。
4.关键区别:
    静态方法和类、实例都无关;
    类方法只和类有关，和实例无关，
    实例方法只和实例有关，和类无关。


"""


class GeometryTools:
    """几何工具类 - 提供几何计算相关的静态方法"""

    @staticmethod  # 静态方法装饰器
    def cicle_area(r):  # 定义静态方法，计算圆面积
        """计算圆面积"""
        return 3.14 * r ** 2  # 返回圆面积公式 π * r^2


print(GeometryTools.cicle_area(5))  # 使用类名直接调用静态方法，计算半径为5的圆面积

geometryTools = GeometryTools()  # 创建GeometryTools类的实例对象


# print(geometryTools.cicle_area(2))  #  不推荐 - 虽然可以通过实例调用静态方法，但不推荐这样做

class People:
    """人类 - 演示类方法的使用"""

    sleep_time = 8  # 类属性，定义默认睡眠时间为8小时

    @classmethod  # 类方法装饰器
    def get_sleep_time(cls):  # 定义类方法，获取睡眠时间
        return f"睡觉需要{cls.sleep_time}小时"  # 返回类属性sleep_time的值

    @classmethod  # 类方法装饰器
    def update_sleep_time(cls, sleep_time):  # 定义类方法，更新睡眠时间
        if sleep_time < 6:  # 检查睡眠时间是否小于6小时
            # raise ValueError("睡眠时间不能小于0")
            return f"睡眠时间不能小于6"  # 返回错误信息
        else:  # 如果睡眠时间合理
            # People.sleep_time = sleep_time
            cls.sleep_time = sleep_time  # 更新类属性sleep_time的值
            return f"更新睡眠时间为{sleep_time}小时"  # 返回成功信息


print(People.get_sleep_time())  # 调用类方法获取当前睡眠时间
print(People.update_sleep_time(5))  # 调用类方法尝试更新睡眠时间为5小时（会返回错误信息）
print(People.update_sleep_time(10))  # 调用类方法更新睡眠时间为10小时
print(People.update_sleep_time(12))  # 调用类方法更新睡眠时间为12小时
