# 全局变量
g_val = '全局变量'

class Dog:
    """
    狗类，可以创建千千万万只狗
    """

    # 类变量
    my_t = '狗'

    def __init__(self, name):
        """
        构造函数
        """
        # 实例变量
        self.name = name
        print(name)

    def bark(self):
        """
        实例函数
        self：代表了实例本身，是python面向对象的机制，不需要传入
        :return:
        """
        name1 = '小白'
        print(name1)
        print('狗叫')

    @classmethod
    def my_type(cls):
        """
        类函数
        cls：类本身，是python面向对象的机制，不需要传入
        :return:
        """
        print(cls.__doc__)

    def eat(self):
        global g_val
        print(self.name)
        print(g_val)

class WhileDog(Dog):
    """
    子类
    """
    my_t = '白狗'

    def __init__(self):
        """
        构造函数
        """
        # 显示调用父类的构造函数
        super().__init__('小白')

    def eat(self):
        print('只吃有肉的骨头')

    def swing(self):
        print('摇尾巴')





