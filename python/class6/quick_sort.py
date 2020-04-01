# coding=utf-8

list1 = [346, 546, 47, 457, 327, 577, 356, 789, 332]


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
        while l < h:
            if list1[h] < base:
                # 把基准小的交换到基准位置
                list1[l], list1[h] = list1[h], list1[l]
                # h往左移一位
                l = l + 1
                break
            else:
                # 如果比基准大，就继续往左找
                h = h - 1

    # 递归出口
    # 左边出口是left == l
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


quick_sort(list1, 0, len(list1) - 1)
print(list1)
