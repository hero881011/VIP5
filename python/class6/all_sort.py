# coding=utf-8
import time, sys
from class6.def_sort import *

# 修改堆栈大小
sys.setrecursionlimit(100000)

# list1=[443,166,567,890,995,445,111,490,852,234,354,256]
list1 = [i for i in range(5000, 0, -1)]

##########################################################################
###### 基于函数的调用 ######
# 冒泡排序
t1 = time.time()
bubble_sort(list1)
t2 = time.time()
print("函数的冒泡效率")
print(t2 - t1)
# print(list1)

# 选择排序
t1 = time.time()
select_sort(list1)
t2 = time.time()
print("函数的选择效率")
print(t2 - t1)
# print(list1)

# 快速排序
t1 = time.time()
quick_sort(list1, 0, len(list1) - 1)
t2 = time.time()
print("函数的快排效率")
print(t2 - t1)
# print(list1)

# 二分排序
t1 = time.time()
list2 = erfen(list1)
t2 = time.time()
print("函数的二分排序效率")
print(t2 - t1)
# print(list2)

##########################################################################
###### 基于类的调用 ######
from class6. class_sort import *

# 冒泡排序
msort = Sort()  # 实例化
t1 = time.time()  # 调用实例函数
msort.bubble_sort(list1)
t2 = time.time()
print("类的冒泡效率")
print(t2 - t1)
# print(list1)

# 选择排序
xsort = Sort()
t1 = time.time()
xsort.select_sort(list1)
t2 = time.time()
print("类的选择效率")
print(t2 - t1)
# print(list1)

# 快速排序
qsort = Sort()
t1 = time.time()
qsort.quick_sort(list1, 0, len(list1) - 1)
t2 = time.time()
print("类的快排效率")
print(t2 - t1)
# print(list1)

# 二分排序
ersort = Sort()
t1 = time.time()
list1 = ersort.erfen(list1)
t2 = time.time()
print('类的二分排效率')
print(t2 - t1)
# print(list1)
