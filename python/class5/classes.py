# -*- coding: UTF-8 -*-

# 全局变量，在整个库文件里面有效
ii = 11
def test():
    print('导入成功')

class Dog:
    """
    实例类：狗
    """

    # 类变量
    t = '狗类'

    # 构造函数（又称为基础函数）
    def __init__(self, n):
        # 在Python里面，实例是用self表示的，必须写
        # 对象在创建成功之后，这个self就代表了这个对象
        # 这个self参数是不用传的，因为它代表了创建出来的对象

        # 我们使用self.xxx，定义实例变量
        self.name = n
        print('构造一条狗：' + str(n))

        self.__ttt = '私有变量__ttt'
        # print('私有变量__ttt:' + self.__ttt)

    # 实例函数：狗叫
    def bark(self):
        # global ii  # 引用全局变量
        # 局部变量，它只在这个过程里面生效
        i = 0
        print(self.name + self.__ttt + '在叫')
        print(i)
        print(ii)

    # 私有函数
    def __test(self):
        print('私有变量__ttt:' + self.__ttt)

    # 类函数：摇尾巴
    @classmethod
    def swing(cls):
        # cls代表了这个类，必须写，不用传
        print('这是' + cls.t + '的类方法')
        print(cls.t)

# 中华田园犬，继承Dog类
class ChinaDog(Dog):
    """
    继承Dog的子类
    """

    t = '田园犬'

    def __init__(self,):
        # 子类构造函数调用父类构造函数
        # super()代表父类
        self.name1 = '1'
        print(self.name1)
        # super().__init__(n)

    # 子类特有的函数
    def Cbark(self):
        print('这是田园犬')

    # # 重写父类函数
    # def bark(self):
    #     print(self.name + '在叫')

class Cdog(Dog,ChinaDog):

    def __init__(self):
        ChinaDog.__init__(self)
        Dog.__init__(self,'小黑')

    def test(self):
        print('test')
