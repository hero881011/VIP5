# coding=utf-8


def select_sort(list1):
    for i in range(len(list1)):
        # 记录最大的下标，最开始认为是第一个是最大的
        max = 0
        # 内存循环，每一轮的比较，找出本轮的最大是的下标
        for j in range(1, len(list1) - i):
            # 如果最大的元素比后一个元素小，就将最大的元素下标，变成后一个元素的下标
            if list1[max] < list1[j]:
                max = j

        # 一轮比较完交换
        list1[max], list1[len(list1) - i - 1] = list1[len(list1) - i - 1], list1[max]


def bubble_sort(list1):
    for i in range(len(list1) - 1):
        # 内存循环，每一轮的比较，找出本轮的最大值
        for j in range(len(list1) - 1 - i):
            # 如果当前元素比后一个元素大，就交换
            if list1[j] > list1[j + 1]:
                # 交换
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


def quick_sort(list1, left, high):
    l = left
    h = high
    base = list1[h]
    # 实现第一轮比较
    while l < h:

        # 从左往右找比基准大的
        while l < h:
            if list1[l] > base:
                # 把基准大的交换到基准位置
                list1[l], list1[h] = list1[h], list1[l]
                # h往左移一位
                h = h - 1
                break
            else:
                # 如果比基准小，就继续往右找
                l = l + 1

        # 从右往左找比基准小的
        while l > h:
            if list1[l] < base:
                # 把基准小的交换到基准位置
                list1[l], list1[h] = list1[h], list1[l]
                # h往左移一位
                l = l + 1
                break
            else:
                # 如果比基准大，就继续往左找
                h = h - 1

        # 递归出口
        # 左边出口是lief == 1
        if left == l:
            pass
        else:
            # 使用递归，对左边剩下元素排序
            quick_sort(list1, left, l - 1)

        # 右边出口是h == high
        if h == high:
            pass
        else:
            # 使用递归，对右边剩下元素排序
            quick_sort(list1, h + 1, high)


def erfen(list):
    # 如果数组长度小于2直接返回该数组
    if len(list) < 2:
        return list
    else:
        # 使用地板除选取中间数作为比较基准
        middle = list[len(list) // 2]
        # 定义基准值左右两个数列
        left, right = [], []
        # 从原始数组中移除中间数
        list.remove(middle)
        for i in list:
            # 大于基准值放右边
            if i >= middle:
                right.append(i)
            else:
                # 小于基准值放左边
                left.append(i)
        # 使用迭代进行比较
        list = erfen(left) + [middle] + erfen(right)
        return list
