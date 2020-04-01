# -*- coding: UTF-8 -*-

# 关于print格式化输出的使用方式
string = "hello"

# %s打印时结果是hello
print("string=%s" % string)  # output: string=hello

# %2s意思是字符串长度为2，当原字符串的长度超过2时，按原长度打印，所以%2s的打印结果还是hello
print("string=%2s" % string)  # output: string=hello

# %7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串左侧补空格，
# 所以%7s的打印结果是  hello
print("string=%7s" % string)  # output: string=  hello

# %-7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串右侧补空格，
# 所以%-7s的打印结果是  hello
print("string=%-7s!" % string)  # output: string=hello  !

# %.2s意思是截取字符串的前2个字符，所以%.2s的打印结果是he
print("string=%.2s" % string)  # output: string=he

# %.7s意思是截取字符串的前7个字符，当原字符串长度小于7时，即是字符串本身，
# 所以%.7s的打印结果是hello
print("string=%.7s" % string)  # output: string=hello

# %a.bs这种格式是上面两种格式的综合，首先根据小数点后面的数b截取字符串，
# 当截取的字符串长度小于a时，还需要在其左侧补空格
print("string=%7.2s" % string)  # output: string=     he
print("string=%2.7s" % string)  # output: string=hello
print("string=%10.7s" % string)  # output: string=     hello

# 还可以用%*.*s来表示精度，两个*的值分别在后面小括号的前两位数值指定
print("string=%*.*s" % (7, 2, string))  # output: string=     he

num = 14

# %d打印时结果是14
print("num=%d" % num)  # output: num=14

# %1d意思是打印结果为1位整数，当整数的位数超过1位时，按整数原值打印，所以%1d的打印结果还是14
print("num=%1d" % num)  # output: num=14

# %3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格，所以%3d的打印结果是 14
print("num=%3d" % num)  # output: num= 14

# %-3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数右侧补空格，所以%3d的打印结果是14_
print("num=%-3d" % num)  # output: num=14_

# %05d意思是打印结果为5位整数，当整数的位数不够5位时，在整数左侧补0，所以%05d的打印结果是00014
print("num=%05d" % num)  # output: num=00014

# %.3d小数点后面的3意思是打印结果为3位整数，
# 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果是014
print("num=%.3d" % num)  # output: num=014

# %.0003d小数点后面的0003和3一样，都表示3，意思是打印结果为3位整数，
# 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果还是014
print("num=%.0003d" % num)  # output: num=014

# %5.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，再在左侧补空格，
# 规则就是补0优先，最终的长度选数值较大的那个，所以%5.3d的打印结果还是  014
print("num=%5.3d" % num)  # output: num=  014

# %05.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，
# 由于是05，再在左侧补0，最终的长度选数值较大的那个，所以%05.3d的打印结果还是00014
print("num=%05.3d" % num)  # output: num=00014

# 还可以用%*.*d来表示精度，两个*的值分别在后面小括号的前两位数值指定
# 如下，不过这种方式4就失去补0的功能，只能补空格，只有小数点后面的3才能补0
print("num=%*.*d" % (4, 3, num))  # output: num= 014

import math

# %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度

# 只是%f时表示原值，默认是小数点后5位数
print("PI=%f" % math.pi)  # output: PI=3.141593

# 只是%9f时，表示打印长度9位数，小数点也占一位，不够左侧补空格
print("PI=%9f" % math.pi)  # output: PI=_3.141593

# 只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0
print("PI=%03.f" % math.pi)  # output: PI=003

# %6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格
print("PI=%6.3f" % math.pi)  # output: PI=_3.142

# %-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格
print("PI=%-6.3f" % math.pi)  # output: PI=3.142_

# 还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定
# 如下，不过这种方式6就失去补0的功能，只能补空格
print("PI=%*.*f" % (6, 3, math.pi))  # output: PI=_3.142

### 冒泡排序 ###
list1 = [159, 593, 333, 995, 445, 111, 490, 795]

# 最外层循环控制不计较的轮次
for i in range(len(list1) - 1):
    # 内存循环，每一轮的比较，找出本轮的最大值
    for j in range(len(list1) - 1 - i):
        # 如果当前元素比后一个元素大，就交换
        if list1[j] > list1[j + 1]:
            j = j + 1
            # 交换
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)

### 选择排序 ###
list1 = [159, 593, 333, 995, 445, 111, 490, 795]

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
print(list1)

year = 2019
mon = 12
day = 11
# 如何拼成2019-12-05
alls = str(year) + '-' + "%02d" % mon + '-' + "%02d" % day
print(alls)

# 杨辉三角
# 杨辉的格式化输出
# 	假设每一个数字占4位输出
# 	底边长：(yh+1)*4位数
# 	第一个数开始输出的位置：(yh+1-1)*4/2位
# 	每一行输出都比前一行往前：4/2位

yh = 8
# 定义两个列表，一个存上一行数据，一个存下一行数据
arr1 = []
arr2 = []
for i in range(yh + 1):
    arr1.append(0)
    arr2.append(0)

# 一次方和二次方的系数我们是知道的
arr1[0] = 1
# 前面输出yh*2位
print("%*.*s" % (yh * 2, 1, ' '), end='')
print("%4d" % arr1[0])
arr1[1] = 1
print("%*.*s" % ((yh - 1) * 2, 0, ''), end='')
print("%4d%4d" % (arr1[0], arr1[1]))
# print(arr1)
# 通过上一个次方的系数得到下一个次方的系数
for i in range(2, yh + 1):

    # 得到当前次方的系数
    for j in range(i + 1):
        if j == 0 or j == i:
            arr2[j] = 1
        else:
            arr2[j] = arr1[j - 1] + arr1[j]

    # print(arr2)
    print("%*.*s" % ((yh - i) * 2, 0, ''), end='')
    # 更新arr1为上一轮得到的系数列表
    for j in range(i + 1):
        print("%4d" % arr2[j], end='')
        arr1[j] = arr2[j]

    print()
