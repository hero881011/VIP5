# coding=utf-8

#################### class03 ####################
# # 99乘法表正序：
# for i in range(1,10):
#     row = ''
#     for j in range(1,1+i):
#         row += str(i) + '*' + str(j) + '=' + str(j*i) + '\t'
#     print(row)
#     i += 1

# # 99乘法表倒叙：
# for i in range(1,10):
#     row = ''
#     for j in range(1,11-i):
#         row += str(10-i) + '*' + str(j) + '=' + str(j*(10-i)) + '\t'
#     print(row)
#     i += 1

# 99乘法去掉对角线
# for i in range(1,10):
#     row = ''
#     for j in range(0,9):
#         j += 1
#         if i == j or i + j == 10:
#             row += ' ' + '\t'
#             continue
#
#         row += str(i*j) + '\t'
#
#     print(row)
#     i += 1

######
# 1. 关于print的%
#   %d|f|s  (整数|小数|字符串)
#   %3d     (规定输出占位3位，不足会在左边不空格，-3，就是在右边补，超过会按实际位输出)
#   %8.2f   (总位数为8位，包括小数点，小数点为两位)
#   %3s     (和整数是一样的)
# 2. 是用if语句的注意事项
#    判断变量是否为空指针None
######
# 四舍五入保留两位小数   <<round在100.00001保留3位会出现100.0的问题>>
# f = 123456.23456789
# f = 100.00000
# print(round(f,3))
# print('%-8.3f' % f)
# print('%-8.2s' % str(f))
# print('%8.2d' % f)
# print('%d' % f)
# print('%s' % str(f))
# print('%s%2.2f' % (str(f),f))


# dict1 = {'key1': 11, 'key2': "66'''\';;;", 'Roy': "男\'''"}
# print(dict1.keys())
# print(type(dict1.keys()))
# print(dict1.values())
# print(type(dict1.values()))

# 键的遍历，类似于把所有键看作一个列表
# for key in dict1.keys():
#     print(key + ':' + str(dict1[key]))
#     dict1[key] = str(dict1[key]) + '666'
# print(dict1)

# 值的遍历，一般不怎么用
# for value in dict1.values():
#     print(value)

# 键值对的遍历1
# for item in dict1.items():
#     print(item)
# print(type(item))
# 键值对的遍历2
# for key,value in dict1.items():
#     print(key + ':' + str(value))
#     print(type(key + ':' + str(value)))  # <class 'str'>


# import json
# s = '/**/jQuery110201270640987324041_1581588266985({"status":"0","t":"1581604043468","set_cache_time":"","data":[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.1.1.1","origipquery":"1.1.1.1","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"1.1.1.1","tplt":"ip","resourceid":"6006","fetchkey":"1.1.1.1","appinfo":"","role_id":0,"disp_type":0}]})'
# # 处理为标准json
# s = s[s.find('{'):s.rfind('}')+1]   # 字符串截取
# print(s)
# json_res = json.loads(s)  # 字符串转换为json格式
# print(json_res)
# print(json_res['data'][0]['location'])

#################### class04 ####################
# 关于print格式化输出的使用方式
# string = "hello"
#
# # %s打印时结果是hello
# print("string=%s" % string)  # output: string=hello
#
# # %2s意思是字符串长度为2，当原字符串的长度超过2时，按原长度打印，所以%2s的打印结果还是hello
# print("string=%2s" % string)  # output: string=hello
#
# # %7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串左侧补空格，
# # 所以%7s的打印结果是  hello
# print("string=%7s" % string)  # output: string=  hello
#
# # %-7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串右侧补空格，
# # 所以%-7s!的打印结果是  hello  !
# print("string=%-7s!" % string)  # output: string=hello  !
#
# # %.2s意思是截取字符串的前2个字符，所以%.2s的打印结果是he
# print("string=%.2s" % string)  # output: string=he
#
# # %.7s意思是截取字符串的前7个字符，当原字符串长度小于是字符串本身，7时，即
# # 所以%.7s的打印结果是hello
# print("string=%.7s" % string)  # output: string=hello
#
# # %a.bs这种格式是上面两种格式的综合，首先根据小数点后面的数b截取字符串，
# # 当截取的字符串长度小于a时，还需要在其左侧补空格
# print("string=%7.2s" % string)  # output: string=     he
# print("string=%2.7s" % string)  # output: string=hello
# print("string=%10.7s" % string)  # output: string=     hello
#
# # 还可以用%*.*s来表示精度，两个*的值分别在后面小括号的前两位数值指定
# print("string=%*.*s" % (7, 2, string))  # output: string=     he
#
#
# num = 14
# # %d打印时结果是14
# print("num=%d" % num)  # output: num=14
#
# # %1d意思是打印结果为1位整数，当整数的位数超过1位时，按整数原值打印，所以%1d的打印结果还是14
# print("num=%1d" % num)  # output: num=14
#
# # %3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格，所以%3d的打印结果是 14
# print("num=%3d" % num)  # output: num= 14
#
# # %-3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数右侧补空格，所以%3d的打印结果是14_
# print("num=%-3d" % num)  # output: num=14_
#
# # %05d意思是打印结果为5位整数，当整数的位数不够5位时，在整数左侧补0，所以%05d的打印结果是00014
# print("num=%05d" % num)  # output: num=00014
#
# # %.3d小数点后面的3意思是打印结果为3位整数，
# # 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果是014
# print("num=%.3d" % num)  # output: num=014
#
# # %.0003d小数点后面的0003和3一样，都表示3，意思是打印结果为3位整数，
# # 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果还是014
# print("num=%.0003d" % num)  # output: num=014
#
# # %5.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，再在左侧补空格，
# # 规则就是补0优先，最终的长度选数值较大的那个，所以%5.3d的打印结果还是  014
# print("num=%5.3d" % num)  # output: num=  014
#
# # %05.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，
# # 由于是05，再在左侧补0，最终的长度选数值较大的那个，所以%05.3d的打印结果还是00014
# print("num=%05.3d" % num)  # output: num=00014
#
# # 还可以用%*.*d来表示精度，两个*的值分别在后面小括号的前两位数值指定
# # 如下，不过这种方式4就失去补0的功能，只能补空格，只有小数点后面的3才能补0
# print("num=%*.*d" % (4, 3, num))  # output: num= 014
#
#
# import math
# # %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度
#
# # 只是%f时表示原值，默认是小数点后6位数
# print("PI=%f" % math.pi)  # output: PI=3.141593
#
# # 只是%9f时，表示打印长度9位数，小数点也占一位，不够左侧补空格
# print("PI=%9f" % math.pi)  # output: PI=_3.141593
#
# # 只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0
# print("PI=%03.f" % math.pi)  # output: PI=003
#
# # %6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格
# print("PI=%6.3f" % math.pi)  # output: PI=_3.142
#
# # %-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格
# print("PI=%-6.3f" % math.pi)  # output: PI=3.142_
#
# # 还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定
# # 如下，不过这种方式6就失去补0的功能，只能补空格
# print("PI=%*.*f" % (6, 3, math.pi))  # output: PI=_3.142

# list1=[263,642,489,537,216,852,173,724,317,525,752,715,178,274]
### 冒泡排序 ###
# # 最外层循环控制不计较的轮次
# for i in range(len(list1)-1):
#     # 内存循环，每一轮的比较，找出本轮的最大值
#     for j in range(len(list1)-1-i):
#         # 如果当前元素比后一个元素大，就交换
#         if list1[j] > list1[j+1]:
#             # 交换
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(list1)

### 选择排序 ###
# for i in range(len(list1)):
#     # 记录最大的下标，最开始认为是第一个是最大的
#     max = 0
#     # 内存循环，每一轮的比较，找出本轮的最大的下标
#     for j in range(len(list1)-i):
#         if list1[max] < list1[j]:
#             max = j
#     list1[max],list1[len(list1)-i-1] = list1[len(list1)-i-1],list1[max]
# print(list1)

# 如何拼成2020-3-1
# year,mon,day = 2020,3,1
# alls = str(year) + '-' + "%02d" % mon + '-' + "%02d" % day
# print(alls)

# 杨辉三角        ?????????????????
# 杨辉的格式化输出
# 	假设每一个数字占4位输出
# 	底边长：(yh+1)*4位数
# 	第一个数开始输出的位置：(yh+1-1)*4/2位
# 	每一行输出都比前一行往前：4/2位

# yh = 8
# # 定义两个列表，一个存上一行数据，一个存下一行数据
# arr1 = []
# arr2 = []
# for i in range(yh+1):
#     arr1.append(0)
#     arr2.append(0)
#
# # 一次方和二次方的系数我们是知道的
# arr1[0] = 1
# # 前面输出yh*2位
# print("%*.*s" % (yh * 2, 1, ''), end='')
# print("%4d" % arr1[0])
# arr1[1] = 1
# print("%*.*s" % ((yh-1) * 2, 0, ''), end='')
# print("%4d%4d" % (arr1[0],arr1[1]))
# # print(arr1)
# # 通过上一个次方的系数得到下一个次方的系数
# for i in range(2,yh+1):
#
#     # 得到当前次方的系数
#     for j in range(i+1):
#         if j == 0 or j == i:
#             arr2[j] = 1
#         else:
#             arr2[j] = arr1[j-1] + arr1[j]
#
#     # print(arr2)
#     print("%*.*s" % ((yh - i) * 2,0,''),end='')
#     #更新arr1为上一轮得到的系数列表
#     for j in range(i+1):
#         print("%4d" % arr2[j],end='')
#         arr1[j] = arr2[j]
#
#     print()

#################### class05 ####################
# test1.py
class Dog:
    MyType = '狗类'

    def __init__(self, n):
        self.name = n
        print('创建了一条叫' + self.name + '的狗')

    def bark(self):
        global gbark
        gbark = 'bark全局变量gbark'
        print(gbark)
        print(self.name + '在吠ing')

    # 类函数：狗摇尾巴
    @classmethod
    def swing(cls):
        print(cls.MyType + '摇尾巴')


# 定义一个黑狗类，继承狗类
class BDog(Dog):

    def __init__(self, n):
        self.bname = '大黑'
        print('BDog实例化')

        # 调用父类构造函数的两种方式：
        # super().__init__(self,n)
        Dog.__init__(self, n)

    def BBark(self):
        print(self.bname + '在叫')

    def bark(self):
        print('bark子类重写')


class WDog:

    def __init__(self):
        self.wname = '白白'
        print('WDog实例化')

    def WBark(self):
        print(self.wname + '在叫')


class LittleDog(BDog, WDog):

    def __init__(self, n):
        print('little_dog')
        BDog.__init__(self, n)
        WDog.__init__(self)

    def LBark(self):
        print('小狗叫')


if __name__ == '__main__':
    mydog = Dog('我的狗')

####################  ####################



####################  ####################



####################  ####################



####################  ####################



