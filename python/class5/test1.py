# coding=utf-8

globali = 1


# 定义一个类：狗
class Dog:
    # 类变量：种类
    MyType = '狗'

    # 构造函数
    # 为类创建实例对象
    def __init__(self, n):
        # 实例变量：对象名字
        self.name = n
        # n = '1111' # 局部变量
        print('这个一条' + n + '狗')

    def bark(self):
        global globali
        globali = '我是Dog.bark()的全局变量globali'
        print(globali)
        print(self.name + '在叫')
        MyType = '会叫的狗'

    # 类函数：狗摇尾巴
    @classmethod
    def swing(cls):
        print(cls.MyType + '摇尾巴')


# 定义一个黑狗类：继承狗类
class BDog(Dog):
    # 基础函数重载
    def __init__(self, n):
        # 调用父类构造方法的两种形式
        # super().__init__(n)
        Dog.__init__(self, n)
        self.bname = 'BDog黑狗'
        print('BDog实例化')

    def BBark(self):
        print('黑狗')

    def bark(self, s):
        print('子类重写' + s)


class WDog:
    def __init__(self):
        self.wname = '白WDog狗'
        print('WDog实例化')

    def WBark(self):
        print(self.wname + "在叫wwww")


class LittleDog(BDog, WDog):
    def __init__(self):
        BDog.__init__(self, '小奶LLL狗')
        WDog.__init__(self)
        print(self.bname)

    def LBark(self):
        print('LittleDog在LBark')


if __name__ == '__main__':
    wdog = Dog('拉布拉多')

from pprint import pprint
pprint(Dog.mro())
