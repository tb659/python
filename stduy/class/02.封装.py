""" 定义银行账户类 """

"""
1.封装本质:     隐藏内部细节，对外提供简洁接口，“隐藏复杂，暴露简单”
2.私有成员:     属性/方法名前加双下划线()，只能在类内部访问，外部直接访问报错。
3.操作私有成员:  通过类中定义的公开方法(接口)，可添加验证逻辑，保证数据安全。
4.封装意义:     数据安全、隐藏逻辑、便于维护、代码清晰。
5.关键语法:
        定义私有属性:     self.   属性名=值;
        定义公开接口:     def方法名(self，参数):...     (内部访问 self. 属性名);
        使用封装类:      创建对象 → 调用公开方法(不用管内部细节)
"""

# 需求:定义银行账户类，把“账户名”“余额”这些属性和“查询余额”方法打包在类里
# class BankAccount:
#     """银行账户类"""
#
#     def __init__(self, name, balance):
#         """初始化方法"""
#         self.name = name  # 账户名
#         self.balance = balance  # 余额
#         print("账户创建成功！")
#
#     def check_balance(self):
#         """查询余额"""
#         print("账户查询成功！")
#         print("%s的账户余额为：￥%d元" % (self.name, self.balance))
#         print(f"{self.name}的账户余额为：￥{self.balance}元")
#
#
# account = BankAccount("张三", 1000)
# account.check_balance()

print("*" * 50)

# 需求:定义银行账户类，把“账户名”“余额”这些属性和“查询余额”方法打包在类里, 不能直接修改余额
# class BankAccount:
#     """银行账户类"""
#
#     def __init__(self, name, balance):
#         """初始化方法"""
#         self.name = name  # 账户名 公开属性 允许外部访问
#         self.__balance = balance  # 余额 私有属性 禁止外部访问
#         print("账户创建成功！")
#
#     def check_balance(self):
#         """查询余额"""
#         print("账户查询成功！")
#         print(f"{self.name}的账户余额为：￥{self.__balance}元")
#
#
# account = BankAccount("张三", 1000)
# # account.balance = 2000
# account.check_balance()
# # print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

print("*" * 50)


# 实现存款、取款功能(操作私有余额)
class BankAccount:
    """银行账户类"""

    def __init__(self, name, balance):
        """初始化方法"""
        self.name = name  # 账户名 公开属性 允许外部访问
        self.__balance = balance  # 余额 私有属性 禁止外部访问
        print("账户创建成功！")

    def deposit(self, amount):
        """存款"""

        if not isinstance(amount, (int, float)):
            print("请输入正确的存款金额")
        elif amount <= 0:
            print("存款失败，存款金额必须大于0")
        else:
            self.__balance += amount
            print(f"存款成功！存款金额为：￥{amount}元")
            self.check_balance()

    def withdraw(self, amount):
        """取款"""
        if not isinstance(amount, (int, float)):
            print("请输入正确的取款金额")
        elif amount > self.__balance:
            print("取款失败，余额不足！")
        elif amount <= 0:
            print("取款失败，取款金额必须大于0")
        else:
            self.__balance -= amount
            print(f"取款成功！取款金额为：￥{amount}元")
            self.check_balance()

    def check_balance(self):
        """查询余额"""
        print("账户查询成功！")
        print(f"{self.name}的账户余额为：￥{self.__balance}元")


account = BankAccount("张三", 1000)
account.check_balance()
print("*" * 10)
account.deposit("200")
print("*" * 10)
account.deposit(-500)
print("*" * 10)
account.deposit(500)
print("*" * 10)
account.withdraw(-200)
print("*" * 10)
account.withdraw(11200)
print("*" * 10)
account.withdraw(200)

print("*" * 50, account._BankAccount__balance)  # 强制访问私有属性 不推荐
