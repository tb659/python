""" 正则表达式 """

"""
核心总结
    1.正则表达式:描述字符串模式的规则，用于匹配、验证、提取字符串。
    2.核心流程:导入 re 模块，定义规则(pattern)，执行匹配，提取结果。
    3.必记规则:
        单个字符:   .(任意)    \d(数字)    \w(单词字符)    [a-z](小写字母);
        数量限定:   *(0+次)    +(1+次)    ?(0-1次)       {m,n}(m-n次);
        位置限定:   ^(开头)    $(结尾);
        分组:      ()(分组)   |(多选一)    \num(引用分组)。
    4.关键提醒:匹配失败返回None，需先判断再调用group();带\的规则加r前缀避免转义。

"""

import re

pattern = r"h\w+"  # 匹配h开头的字符串
string1 = "hello"
string2 = "world"

result1 = re.match(pattern, string1)
if result1:
    print("string1 匹配成功", result1.group())
else:
    print("string1 匹配失败", result1)

result2 = re.match(pattern, string2)
if result2:
    print("string2 匹配成功", result2.group())
else:
    print("string2 匹配失败", result2)

print("*" * 50)

print(".", re.match(".", "hello"))

print("[abc]", re.match(r"[abc]", "hello"))
