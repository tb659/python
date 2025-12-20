""" 复合数据结构 """

"""
核心总结
    类型选择
        单个数据：           数字用int/float，文字用str，判断用bool，无数据用None
        多个数据：           需要修改用list，固定不变用tuple，去重对比用set，键值对用dict
    通用技巧
        in判断存在，len()计算长度，del删除，sum()/max()/min()处理数值
    类型转换
        用对用函数方法，str()（万能转文字）、int()/float()（文字转数字）、set()（去重）
    关键区别
        可修改vs不可修改：      list/set/dict可修改，str/tuple不可修改
        有序vs无序：           str/list/tuple/dict有序，set无序
        唯一vs去重：           dict 键唯一、set 元素唯一、其他类型（除None）可重复
"""

"""
    数据类型            通俗易懂            核心特点
    列表（list）        可修改的有序数据筐    有序、可增删改、元素可重复
    元组（tuple）       不可修改的有序数据筐  有序、不可修改、元素可重复
    集合（set）         自动去重的无序数据筐  无序、元素唯一、支持集合运算
    字典（dict）        键值对映射表         有序、键唯一、可增删改
"""

# 通用操作
"""
    操作              作用
    in / not in      判断元素是否存在
    len()            统计元素个数
    del              删除元素/变量
    sum()            求和（只针对数值）
    max()            求最大值   
    min()            求最小值
    
    age in dict 判断的事key值
    sum()、max()、min() 只对数值类型有效，字符串用max()、min() 是按照ASCII码排序
"""

# 类型转换
"""
    转换方法            作用
    int()              转为整数
    float()            转为小数
    bool()             转为布尔值
    str()              转为字符串
    eval()             执行字符串表达式，并返回表达式的值
    list()             转为列表
    tuple()            转为元组
    set()              转为集合（自动去重）
    dict()             转为字典

"""

