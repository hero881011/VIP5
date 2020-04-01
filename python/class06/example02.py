'''
###########传值与传地址#########
def func(b):
    """

    :param b:
    :return:
    """
    # python产地直必须的容器变量（list，dict）
    # 如果对容器变量本身修改，则会把容器变量看做一个变量，也就是传值
    # 只有对容器里的变量修改，才视为容器，才是传地址

    # 形参：函数所接收的参数
    b[1] = 22
    print(id(b))


list1 = [1, 2, 3, 4]
# 实参，实际传递的参数
func(list1)
print(id(list1))
'''


# 选择排序for方法
# def select_sort(a):
#     for i in range(len(a) - 1):
#         base = 0
#         for j in range(1, len(a) - i):
#             if a[base] < a[j]:
#                 base = j
#
#         a[base], a[len(a) - i - 1] = a[len(a) - i - 1], a[base]
#     print('选择排序for方法: ' + str(a))
#
#
# h = [3, 5, 7, 7, 2, 6, 7, 8, 5, 3, 5]
# select_sort(h)
# print(h)


###############函数的返回值###############

def add_x_y(x, y):
    """
    实现x+y=z的功能
    :return:
    :param x: 参数1
    :param y: 参数2
    :return: x+y的值
    """

    z = x + y
    # 返回值
    # 返回一个变量，或者一个元组（return 1，3,5,7）
    # return z, 3, 4  # 返回多个值，返回的是元组
    return z


if __name__ == "__main__":  # 执行模块时执行的代码，导入调用时不会执行
    a = add_x_y(1, 4)
    print(a)

