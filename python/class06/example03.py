########### 递归 facs ###########

def facs(n):
    if n == 1:
        return 1
    else:
        return n * facs(n - 1)


print(facs(4))


########### 快速排序 ###########
def quick_sort(height, l , h):
    left = l
    right = h
    base = height[h]

    # 如果l<h，说明比较没有完成，
    while l < h:
        # 第一步：从左往右找比基准大的
        while l < h:
            # 如果找到就交换
            if height[l] > base:
                height[l], height[h] = height[h], height[l]
                # 然后h往左移一位
                h -= 1
                break
            else:
                l += 1

        # 第二步：从右往左找比基准小的
        while l < h:
            # 如果找到就交换
            if height[h] < base:
                height[l], height[h] = height[h], height[l]
                # 然后l往右移一位
                l += 1
                break
            else:
                h -= 1

    # 对分出来的两部分进行递归排序
    # 递归出口
    # 左边出口是left == l 、 l - 1 <= left
    # if left == l:
    if l - 1 <= left:
        pass
    else:
        quick_sort(height, left, l - 1)

    # 右边出口是h == right 、 h + 1 >= right
    # if right == h:
    if h + 1 >= right:
        pass
    else:
        quick_sort(height, h + 1, right)


if __name__ == '__main__':
    h = [346, 546, 47, 457, 327, 577, 356, 789, 332]
    quick_sort(h, 0, len(h) - 1)
    print(h)


