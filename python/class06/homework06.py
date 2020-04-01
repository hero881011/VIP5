########### 快速排序 递归 ###########
def quick_sort(height, l, h):
    left = l
    right = h
    base = height[h]

    while l < h:
        # 从左往右找比基准大的
        while l < h:
            if height[l] > base:
                height[l], height[h] = height[h], height[l]
                h -= 1
                break
            else:
                l += 1
        while l < h:
            if height[h] < base:
                height[l], height[h] = height[h], height[l]
                l += 1
                break
            else:
                h -= 1

    if l - 1 <= left:
        pass
    else:
        quick_sort(height, left, l - 1)

    if h + 1 >= right:
        pass
    else:
        quick_sort(height, h + 1, right)


########### 快速排序 循环 ###########
def erfen(list1):
    if len(list1) < 2:
        return list1
    else:
        middle = list1[(len(list1) // 2)]
        list1.remove(middle)
        left, right = [], []

        for i in list1:
            if i < middle:
                left.append(i)
            else:
                right.append(i)
        list1 = left + [middle] + right
        return list1


########### 冒泡排序 for方法 ###########
def bubble_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


########### 选择排序 while方法 ###########
def select_sort(list1):
    i = 0
    while i < len(list1):
        j = 0
        base = 0
        while j < len(list1) - i - 1:
            j += 1
            if list1[base] < list1[j]:
                base = j
        list1[base], list1[len(list1) - i - 1] = list1[len(list1) - i - 1], list1[base]
        i += 1


if __name__ == '__main__':
    list1 = [i for i in range(20, 0, -1)]
    print('原始列表：' + str(list1))

    quick_sort(list1, 0, len(list1) - 1)
    print('快速排序：' + str(list1))

    erfen(list1)
    print('二分排序: ' + str(list1))

    bubble_sort(list1)
    print('冒泡排序for方法: ' + str(list1))

    select_sort(list1)
    print('选择排序while方法: ' + str(list1))
