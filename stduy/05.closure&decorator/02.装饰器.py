""" 装饰器 """

"""
2. 装饰器：
    本质：接收函数、返回新函数的闭包；
    核心价值：不修改原函数，给函数添加额外功能；
    关键语法：
        基础装饰器：def 装饰器(func): def wrapper(*args, **kwargs): 新功能 + func(*args, **kwargs) return wrapper；
        语法糖：@装饰器名（放在原函数上）；
        多个装饰器：从内到外执行。
3. 避坑指南：
装饰带参数的函数时，内层函数必须用 *args 和 **kwargs，否则会报错；
多个装饰器的执行顺序：离函数越近，越先执行。

"""

# 定义闭包装饰器
def login_decorator(func):
    def wrapper():
        print("正在验证登录...")
        print("登录成功！")
        func()

    return wrapper


# 原始函数
def send_msg():
    print("发送消息给冰冰：勤奋打工人")


def transfer_money():
    print("转账给冰冰~")


# 手动应用闭包装饰器
send_msg = login_decorator(send_msg)
transfer_money = login_decorator(transfer_money)

# 调用
send_msg()
transfer_money()

print("****************************************************************************")


# 定义装饰器（和上面一样）
def login_decorator(func):
    def wrapper():
        print("正在验证登录...")
        print("登录成功！")
        func()

    return wrapper


# 用@语法糖装饰原函数（不用手动调用装饰器）
@login_decorator  # 等价于 send_msg = login_decorator(send_msg)
def send_msg():
    print("发送消息给冰冰：勤奋打工人")


@login_decorator  # 等价于 transfer_money = login_decorator(transfer_money)
def transfer_money():
    print("转账给冰冰~")


# 直接调用原函数名（实际调用的是装饰后的新函数）
send_msg()
transfer_money()
# 输出和之前一样，代码更简洁！


print("***********************************************************************")


# 定义一个装饰器，能够处理带有参数的函数
def login_decorator(func):
    # 定义包装函数，使用 *args 和 **kwargs 接收任意参数
    def wrapper(*args, **kwargs):
        # 在调用原函数前执行的操作
        print("正在验证登录...")
        print("登录成功！")
        # 调用原始函数并传递参数，同时返回其结果
        return func(*args, **kwargs)

    # 返回包装后的函数
    return wrapper


# 使用装饰器装饰 send_msg 函数，该函数接收一个参数 msg
@login_decorator
def send_msg(msg):
    # 打印传入的消息
    print(msg)


# 使用装饰器装饰 transfer_money 函数，该函数接收一个参数 money
@login_decorator
def transfer_money(money):
    # 打印转账信息，包含转账金额
    print("转账给冰冰~", money)


# 调用被装饰的 send_msg 函数，实际会先执行装饰器中的代码
send_msg("发送消息给冰冰：勤奋打工人")
# 调用被装饰的 transfer_money 函数，实际会先执行装饰器中的代码
transfer_money(500)

