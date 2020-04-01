a = []
i = 20
while i > 0:
    a.append(i)
    i -= 1
print('a=' + str(a))

# 冒泡排序for方法
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print('冒泡排序for方法: ' + str(a))
#
# # 冒泡排序while方法
i = 0
while i < len(a):
    j = 0
    while j < (len(a) - i - 1):
        j += 1
        if a[j] > a[j - 1]:
            continue
        a[j], a[j - 1] = a[j - 1], a[j]
    i += 1
print('冒泡排序while方法: ' + str(a))
#
# 选择排序for方法
for i in range(len(a) - 1):
    base = 0
    for j in range(1, len(a) - i):
        if a[base] < a[j]:
            base = j

    a[base], a[len(a) - i - 1] = a[len(a) - i - 1], a[base]
print('选择排序for方法: ' + str(a))

# 选择排序while方法
i = 0
while i < len(a):
    j = 0
    base = 0
    while j < len(a) - i - 1:
        j += 1
        if a[base] < a[j]:
            base = j
    a[base], a[len(a) - i - 1] = a[len(a) - i - 1], a[base]
    i += 1
print('选择排序while方法: ' + str(a))

# # 杨辉三角 while方法
# # 杨辉三角的次方
yh = 10

# 定义两个列表，用来存上一个杨辉的系数，和推算下一个杨辉系数
arr1 = [1]
arr2 = [1]
print('%*s' % (2 * yh, ''), end='')
print('%4d' % 1)

i = 1
# 一个一个次方往下推
while i < yh:
    # 下一个系数都要比上一个系数多一个元素
    arr2.append(1)
    # 通过上一个次方的系数，推下一个次方
    j = 0
    while j <= i:
        # 两边两个元素都是1
        if j == 0 or j == i:
            arr2[j] = 1
        else:
            # 中间的元素等于它肩膀上两个元素之和
            arr2[j] = arr1[j - 1] + arr1[j]

        j += 1
    print('%*s' % (2 * (yh - i), ''), end='')

    for d in arr2:
        print('%4d' % d, end='')

    print()

    i += 1
    arr1 = arr2.copy()
