def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


__all__ = ["add"]

#  不导出 multiply  在代码中通过 from my_package.calculator import * 引入时，multiply 会被忽略
