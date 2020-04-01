##########循环结构#########

######while######

"""
打印一星期每一天要做的事情
星期1~5：上班
星期6，7：玩
"""

# x = int(input("输入星期几："))
# # 定义循环控制条件
# i = 1
# while i <=7 :
#     if i < x:
#         i = i + 1
#         continue
#
#     if 1 <= x <= 5:
#         print('星期%d上班' % i)
#         # break
#     elif 6 <= x <= 7:
#         print('星期%d玩' % i)
#     else:
#         print('您输入有误')
#     # 循环体里面需要改变控制条件
#     i += 1


###### for ######
# for i in range(1,8):
#     if i < x:
#         i += 1
#         print(i)
#
#     if 0<x<6:
#         print('星期%d上班' % i)
#     elif 5<x<8:
#         print('星期%d玩' % i)
#     else:
#         print('您输入有误')
#     # 循环体里面需要改变控制条件
#     i += 1
# s = 0
# for i in range(1,101):
#     s += i
# print(s)

###### 99乘法表 for 正序 ######

# for i in range(1,10):
#     jj = ''
#     for j in range(1,1+i):
#         jj += str(i) + '*' + str(j) + '=' + str(j*i) + '\t'
#     print(jj)
#     i += 1

###### 99乘法表 while 正序 ######
# i = 1
# while i <= 9:
#     j = 1
#     while i >= j:
#         print(str(i) + '*' + str(j) + '=' + str(j*i), end='\t')
#         j += 1
#     i += 1
#     print()

###### 99乘法表 while 倒序 ######
# i = 1
# while i <= 9:
#     j = 9
#     while i <= j:
#         print(str(i) + '*' + str(j) + '=' + str(j*i), end='\t')
#         j -= 1
#     i += 1
#     print()

# 四舍五入保留两位小数
# f1 = 137.39472
# print(round(f1,2))
# print('%.2f' % f1)
#
# f2 = 137.39572
# print(round(f2,2))
# print('%.2f' % f2)

# # 用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？
# while True:
#     usr = input('username:')
#     pwd = input('password:')
#     if len(usr) < 6 or len(usr) > 16:
#         print('请重新输入6-16位的用户名或密码！')
#     elif len(pwd) < 6 or len(pwd) > 16:
#         print('请重新输入6-16位的用户名或密码！')
#     else:
#         print('恭喜，登录成功！')
#         break






