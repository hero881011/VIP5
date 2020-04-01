# 1. 求|x| + |y|的值

# while True:
#     try:
#         x = int(input('请输入x的值:'))
#         y = int(input('请输入y的值:'))
#         if x >= 0 and y >= 0:
#             print('|x| + |y|的值为：' + str(x + y))
#         elif x < 0 and y >= 0:
#             print('|x| + |y|的值为：' + str(-x + y))
#         elif x < 0 and y < 0:
#             print('|x| + |y|的值为：' + str(-x - y))
#         else:
#             print('|x| + |y|的值为：' + str(x - y))
#         break
#
#     except Exception as e:
#         print("请输入正确的整数！！！")

# 2. 练习题1：
# 设x=3,y=4
# z满足x的平方+y的三次方
# 打印z的值
# x = 3
# y = 4
# z = x ** 2 + y ** 3
# print(z)


# 课外作业：
# 你老婆对你说：“老公，晚上回来买一个西瓜，如果看到西红柿，就买两个。”
# 请用程序打印你从下班，到家的全过程


try:
    tomato = int(input('有没有看见2个西红柿：'))
    if tomato == 1:
        print('买2个西红柿，看看有没有西瓜')

        watermelon = int(input('有没有西瓜？：'))
        if watermelon == 0:
            print('就买2个西红柿回家')
        else:
            print('买1个西瓜，2个西红柿回家')

    else:
        watermelon = int(input('有没有西瓜？：'))
        if watermelon == 1:
            print('买1个西瓜回家')
        elif watermelon == 0:
            print('没有西瓜，没有西红柿，回家跪搓衣板')

except Exception as e:
    print("请输入正确的整数！！！")
