""" 学员管理系统 """

"""
代码逻辑详解
    1. 数据结构设计
        使用全局列表 students 存储所有学员信息
        每个学员用字典表示，包含 id、name、tel 三个字段
    2. 函数设计
        show_menu(): 显示系统菜单
        add_student(): 添加新学员
        delete_student(): 删除学员
        modify_student(): 修改学员信息
        search_student(): 查询学员
        show_all_students(): 显示所有学员
        main(): 主程序控制循环
    3. 核心功能实现
        添加: 使用 append() 方法将新学员添加到列表末尾
        删除: 使用 remove() 方法从列表中移除指定学员
        修改: 在列表中找到目标学员并更新其属性
        查询: 遍历列表查找匹配的学员
        显示所有: 遍历列表并打印每个学员的信息
    4. 用户交互
        使用 input() 获取用户输入
        使用 strip() 去除输入的首尾空格
        使用 while True 实现无限循环，直到用户选择退出
        这个系统展示了Python中函数调用、数据存储、循环控制等核心概念的实际应用，是一个非常适合初学者学习和实践的项目。

"""

""" 学员管理系统 v1.0 """

# 全局变量：存储所有学员信息的列表
students = [
    {'id': '1', 'name': '张三', 'tel': '13812345678'},
    {'id': '2', 'name': '李四', 'tel': '13987654321'},
    {'id': '3', 'name': '王五', 'tel': '13711223344'}
]


def show_menu():
    """
    显示系统菜单

    该函数负责打印出系统的主菜单，用户可以根据菜单选择相应的功能
    """
    print("=" * 30)
    print("     学员管理系统  v1.0")
    print("=" * 30)
    print("1. 添加学员")
    print("2. 删除学员")
    print("3. 修改学员")
    print("4. 查询学员")
    print("5. 显示所有学员")
    print("6. 退出系统")
    print("=" * 30)


def add_student():
    """
    添加新学员的功能

    该函数会提示用户输入新的学员信息，并将这些信息添加到全局的students列表中
    """
    print("=== 添加学员 ===")

    # 获取用户输入的新学员信息
    name = input("请输入学员姓名: ").strip()
    id_num = input("请输入学号: ").strip()
    tel = input("请输入手机号: ").strip()

    # 创建新的学员字典
    new_student = {
        'id': id_num,
        'name': name,
        'tel': tel
    }

    # 将新学员添加到列表中
    students.append(new_student)
    print(f"添加成功！已添加学员: {name}")


def delete_student():
    """
    删除学员的功能

    该函数会根据用户输入的姓名查找并删除对应的学员信息
    """
    print("=== 删除学员 ===")

    # 获取要删除的学员姓名
    name = input("请输入要删除的学员姓名: ").strip()

    # 查找并删除学员
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print(f"删除成功！已删除学员: {name}")
            return

    # 如果没有找到匹配的学员
    print(f"错误：未找到姓名【{name}】的学员！")


def modify_student():
    """
    修改学员信息的功能

    该函数会根据用户输入的姓名查找学员，并允许修改其学号和手机号
    """
    print("=== 修改学员 ===")

    # 获取要修改的学员姓名
    name = input("请输入要修改的学员姓名: ").strip()

    # 查找学员
    for student in students:
        if student['name'] == name:
            # 获取新的学号和手机号
            new_id = input("请输入新的学号: ").strip()
            new_tel = input("请输入新的手机号: ").strip()

            # 更新学员信息
            student['id'] = new_id
            student['tel'] = new_tel

            print(f"修改成功！更新后信息: {student}")
            return

    # 如果没有找到匹配的学员
    print(f"错误：未找到姓名【{name}】的学员！")


def search_student():
    """
    查询学员信息的功能

    该函数会根据用户输入的姓名查找并显示对应的学员信息
    """
    print("=== 查询学员 ===")

    # 获取要查询的学员姓名
    name = input("请输入要查询的学员姓名: ").strip()

    # 查找并显示学员信息
    for student in students:
        if student['name'] == name:
            print(f"找到学员: {student}")
            return

    # 如果没有找到匹配的学员
    print(f"错误：未找到姓名【{name}】的学员！")


def show_all_students():
    """
    显示所有学员信息的功能

    该函数会遍历全局的students列表，并打印出所有学员的信息
    """
    print("=== 显示所有学员 ===")

    # 如果没有学员
    if not students:
        print("暂无学员信息！")
        return

    # 遍历并显示所有学员
    for student in students:
        print(f"学员信息: {student}")


def main():
    """
    主程序函数

    该函数是整个系统的入口点，负责控制程序的主循环
    """
    while True:
        # 显示菜单
        show_menu()

        # 获取用户选择的功能序号
        choice = input("请输入功能序号（1-6）: ").strip()

        # 根据用户选择执行相应功能
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            print("感谢使用学员管理系统，再见！")
            break  # 退出循环，结束程序
        else:
            print("无效输入，请输入1-6之间的数字！")


# 程序入口点
if __name__ == "__main__":
    main()
