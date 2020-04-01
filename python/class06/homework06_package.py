import time, sys
from class06.homework06 import *

list2 = [i for i in range(6666, 0, -1)]
# print('原始列表list2：' + str(list2))


# 修改堆栈大小
sys.setrecursionlimit(100000)

###### 排序算法调用 ######
# 冒泡排序
t1 = time.time()
bubble_sort(list2)
t2 = time.time()
print("冒泡效率：排倒叙%.d个使用时间为：%.6f秒" % (len(list2), (t2 - t1)))
# print(list2)

# 选择排序
t1 = time.time()
select_sort(list2)
t2 = time.time()
print("选择效率：排倒叙%.d个使用时间为：%.6f秒" % (len(list2), (t2 - t1)))
# print(list2)

# 快速排序
t1 = time.time()
quick_sort(list2, 0, len(list2) - 1)
t2 = time.time()
print("快排效率：排倒叙%.d个使用时间为：%.6f秒" % (len(list2), (t2 - t1)))
# print(list2)

# 二分排序
t1 = time.time()
list2 = erfen(list2)
t2 = time.time()
print("二分效率：排倒叙%.d个使用时间为：%.6f秒" % (len(list2), (t2 - t1)))
# print(list2)
