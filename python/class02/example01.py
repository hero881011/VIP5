

"""
    短路原则：
    and：False and 任何值都是False
    or：True or 任何值都是True
"""


# xx = None
#
# if (xx == None) and (len(xx) == 3):
#     print(xx)


x = int(input())

def fun(x):
    if x == 1:
        print('星期一')
        return

    if x == 2:
        print('星期二')
        return

    if x == 3:
        print('星期三要去打篮球啦！！！')






