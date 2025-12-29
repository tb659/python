""" 异常处理 """

""" Python异常处理详解 """

"""
异常处理最佳实践总结
    1、具体化异常处理：尽可能捕获具体的异常类型，而不是使用通用的Exception
    2、合理使用else子句：在没有异常时执行正常流程代码
    3、善用finally子句：用于清理资源，确保重要代码总是被执行
    4、自定义异常：为应用程序定义有意义的自定义异常类
    5、异常链：使用raise ... from ...保留原始异常信息
    6、日志记录：使用logging模块记录异常信息以便调试
    7、避免忽略异常：不要使用空的except块忽略异常
    8、资源管理：使用with语句或上下文管理器自动管理资源
    通过以上示例，您可以掌握Python中异常处理的各种技巧和最佳实践。

"""


# 1. 基本的try-except结构
def basic_exception_handling():
    """
    最基本的异常处理结构
    try块中放可能出错的代码
    except块中处理特定类型的异常
    raise语句用于主动抛出一个异常
    assert语句用于调试，在生产环境中可以通过-O选项禁用
    """
    try:
        # 可能出现异常的代码
        number = int(input("请输入一个数字: "))
        result = 10 / number
        print(f"10除以{number}的结果是: {result}")
    except ValueError:
        # 处理ValueError异常（如输入非数字字符）
        print("输入错误：请输入一个有效的数字！")
    except ZeroDivisionError:
        # 处理ZeroDivisionError异常（除零错误）
        print("数学错误：不能除以零！")


# 2. 捕获多种异常
def multiple_exceptions():
    """
    同时处理多种类型的异常
    """
    try:
        numbers = [1, 2, 3]
        index = int(input("请输入索引值: "))
        result = 10 / numbers[index]
        print(f"结果: {result}")
    except (ValueError, IndexError, ZeroDivisionError) as e:
        # 同时捕获多种异常，并获取异常对象
        print(f"发生错误: {type(e).__name__}: {e}")


# 3. 捕获所有异常
def catch_all_exceptions():
    """
    使用通用Exception捕获所有类型的异常
    注意：通常不推荐这样做，应该具体问题具体处理
    """
    try:
        # 一些可能出错的操作
        data = input("输入一些数据: ")
        result = eval(data)  # 注意：eval存在安全风险，仅作演示
        print(f"计算结果: {result}")
    except Exception as e:
        # 捕获所有异常
        print(f"发生了未预期的错误: {type(e).__name__}: {e}")


# 4. 使用else子句
def try_else_example():
    """
    else子句在没有异常时执行
    """
    try:
        number = int(input("请输入一个正整数: "))
        if number <= 0:
            # raise语句用于主动抛出一个异常
            # 当程序执行到这里时，会立即抛出ValueError异常
            # 异常信息为"数字必须大于0"
            # 这会让程序跳转到匹配的except块进行处理
            raise ValueError("数字必须大于0")
    except ValueError as e:
        print(f"输入错误: {e}")
    else:
        # 只有在try块中没有异常时才会执行
        print(f"输入正确，您输入的数字是: {number}")
        result = number ** 2
        print(f"{number}的平方是: {result}")


# 5. 使用finally子句
def try_finally_example():
    """
    finally子句无论是否有异常都会执行
    常用于清理资源，如关闭文件、网络连接等
    """
    file_handle = None
    try:
        # 尝试打开文件
        file_handle = open("test.txt", "r")
        content = file_handle.read()
        print("文件内容:", content)
    except FileNotFoundError:
        print("错误：找不到指定的文件")
    except IOError:
        print("错误：读取文件时出现问题")
    finally:
        # 无论是否出现异常，都会执行这里的代码
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("文件已关闭")


# 6. 自定义异常
class CustomError(Exception):
    """
    自定义异常类
    继承自Exception基类
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def custom_exception_example():
    """
    演示如何抛出自定义异常
    """
    try:
        age = int(input("请输入您的年龄: "))
        if age < 0:
            # 抛出自定义异常
            raise CustomError("年龄不能为负数")
        elif age > 150:
            raise CustomError("年龄不能超过150岁")
        else:
            print(f"您的年龄是: {age}")
    except CustomError as e:
        # 处理自定义异常
        print(f"自定义错误: {e.message}")
    except ValueError:
        print("输入错误：请输入一个有效的数字")


# 7. 常见异常场景及处理

def common_exception_scenarios():
    """
    演示常见的异常场景
    """

    # 场景1: 类型转换错误
    try:
        value = int("abc")  # ValueError
    except ValueError as e:
        print(f"类型转换错误: {e}")

    # 场景2: 列表索引越界
    try:
        my_list = [1, 2, 3]
        item = my_list[10]  # IndexError
    except IndexError as e:
        print(f"索引错误: {e}")

    # 场景3: 字典键不存在
    try:
        my_dict = {"name": "张三", "age": 25}
        value = my_dict["height"]  # KeyError
    except KeyError as e:
        print(f"键错误: 字典中不存在键 {e}")

    # 场景4: 文件未找到
    try:
        with open("nonexistent.txt", "r") as f:  # FileNotFoundError
            content = f.read()
    except FileNotFoundError as e:
        print(f"文件错误: {e}")

    # 场景5: 数学运算错误
    try:
        import math
        result = math.sqrt(-1)  # ValueError
    except ValueError as e:
        print(f"数学运算错误: {e}")


# 8. 异常链和重新抛出异常
def exception_chaining():
    """
    演示异常链和重新抛出异常
    """
    try:
        try:
            result = 10 / 0  # 引发ZeroDivisionError
        except ZeroDivisionError as e:
            # 记录日志或做一些处理后再重新抛出
            print("内部处理了除零错误")
            # 重新抛出异常，保留原始异常信息
            raise ValueError("转换为值错误") from e
    except ValueError as e:
        print(f"捕获到值错误: {e}")
        if e.__cause__:  # 检查是否有原因异常
            print(f"原因是: {type(e.__cause__).__name__}: {e.__cause__}")


# 9. 断言异常
def assertion_example():
    """
    演示断言的使用
    assert语句用于调试，在生产环境中可以通过-O选项禁用
    """
    try:
        age = int(input("请输入年龄: "))
        # 使用断言检查条件
        assert age >= 0, "年龄不能为负数"
        assert age <= 150, "年龄不能超过150岁"
        print(f"有效年龄: {age}")
    except AssertionError as e:
        print(f"断言失败: {e}")
    except ValueError:
        print("输入错误：请输入一个有效的数字")


# 10. 上下文管理器与异常处理
class MyContextManager:
    """
    自定义上下文管理器示例
    实现__enter__和__exit__方法
    """

    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文")
        if exc_type:
            print(f"捕获到异常: {exc_type.__name__}: {exc_value}")
        # 返回True表示异常已被处理，不会继续传播
        return False


def context_manager_example():
    """
    演示上下文管理器与异常处理
    """
    try:
        with MyContextManager() as cm:
            print("在上下文中执行代码")
            # 故意引发异常
            result = 10 / 0
    except ZeroDivisionError:
        print("捕获到除零错误")


# 11. 日志记录异常
import logging

# 配置日志
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def logging_exception_example():
    """
    演示如何使用日志记录异常
    """
    try:
        # 模拟一些可能出错的操作
        data = [1, 2, 3]
        index = int(input("请输入索引: "))
        value = data[index] / 0  # 会引发两个异常
    except (IndexError, ZeroDivisionError) as e:
        # 记录异常到日志
        logging.exception("发生了一个异常")  # 自动记录堆栈跟踪
        print(f"处理异常: {type(e).__name__}: {e}")


# 12. 完整的异常处理示例
def complete_exception_handling():
    """
    综合展示异常处理的最佳实践
    """
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            # 获取用户输入
            user_input = input("请输入一个数字（尝试次数 {}/{}）: ".format(attempts + 1, max_attempts))

            # 转换为数字并进行计算
            number = float(user_input)
            if number < 0:
                raise ValueError("数字不能为负数")

            result = 100 / number
            print(f"100除以{number}等于{result:.2f}")
            break  # 成功则跳出循环

        except ValueError as e:
            attempts += 1
            print(f"输入错误 ({attempts}/{max_attempts}): {e}")
            if attempts >= max_attempts:
                print("已达最大尝试次数，程序退出")
        except ZeroDivisionError:
            attempts += 1
            print(f"数学错误 ({attempts}/{max_attempts}): 不能除以零")
            if attempts >= max_attempts:
                print("已达最大尝试次数，程序退出")
        except Exception as e:
            # 捕获其他未预期的异常
            print(f"未知错误: {type(e).__name__}: {e}")
            break  # 遇到未知错误直接退出


# 主程序演示各种异常处理方式
def main():
    """
    主函数，演示各种异常处理方式
    """
    print("=== Python异常处理演示 ===\n")

    # 演示基本异常处理
    # print("1. 基本异常处理:")
    # basic_exception_handling()
    #
    # print("\n2. 多种异常处理:")
    # multiple_exceptions()
    #
    # print("\n3. 捕获所有异常:")
    # catch_all_exceptions()

    # print("\n4. 使用else子句:")
    # try_else_example()
    #
    # print("\n5. 使用finally子句:")
    # try_finally_example()
    #
    # print("\n6. 自定义异常:")
    # custom_exception_example()
    #
    # print("\n7. 常见异常场景及处理:")
    # common_exception_scenarios()
    #
    # print("\n8. 异常链和重新抛出异常:")
    # exception_chaining()
    #
    # print("\n9. 断言异常演示:")
    # assertion_example()
    #
    # print("\n10. 上下文管理器与异常处理:")
    # context_manager_example()
    #
    # print("\n11. 日志记录异常:")
    # logging_exception_example()

    print("\n12. 完整的异常处理示例:")
    complete_exception_handling()


# 程序入口
if __name__ == "__main__":
    main()
