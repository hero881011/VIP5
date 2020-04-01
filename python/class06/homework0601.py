# 面向对象封装：

# 作业：前
# class Rev:
#
#     def __init__(self):
#
#         self.s = input('输入字符串：')
#         print('输入了字符串：' + self.s)
#
#     # 实现字符串反转
#     def fz(self):
#         s1 = self.s[::-1]
#         print('字符串反转为：' + s1)
#
#     # 判断反转后字符串是否和原来字符串一模一样（不传入参数，返回True or False）
#     def isequal(self):
#         s2 = self.s[::-1]
#
#         if self.s == s2:
#             # print('反转后与原字符串一样')
#             return True
#         else:
#             # print('反转后与原字符串不一样')
#             return False
#
#     # 返回字符串相反的两部分
#     def equal_return(self):
#         s3 = self.s[::-1]
#
#         if self.s == '' or self.s is None:
#             print(self.s)
#
#         elif self.s == s3:
#             middle = len(s3) // 2
#
#             if len(self.s) % 2 == 1:
#                 a = self.s[0:middle + 1]
#                 b = self.s[middle:len(self.s)]
#                 return a, b
#
#             elif len(self.s) % 2 == 0:
#                 a = self.s[0:middle]
#                 b = self.s[middle:len(self.s)]
#                 return a, b
#         else:
#             return False
#
# if __name__ == '__main__':
#     r = Rev()
#     r.fz()
#     r.isequal()
#     print(r.equal_return())


# 作业：后

class strC:

    def __init__(self, s):
        self.s = s

    def revers_str(self):

        if self.s is None or not isinstance(self.s, str):
            return None

        else:
            return self.s[::-1]

    def is_revers(self):

        if self.s is None or not isinstance(self.s, str):
            return False

        else:
            if self.s == self.s[::-1]:
                return True
            else:
                return False

    def get_revers(self):

        flg = self.is_revers()

        if flg:
            l = len(self.s)

            if l % 2 == 1:
                return self.s[0:l // 2 + 1], self.s[l // 2:]
            else:
                return self.s[0:l // 2], self.s[1 // 2:]


if __name__ == '__main__':
    ss = strC('zxcvcxz')
    print(ss.revers_str())
    print(ss.is_revers())
    print(ss.get_revers())
