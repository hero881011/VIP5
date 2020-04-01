# 全局变量
global_val = '地球人'


class People:
    """
    人类，可以创造出千千万万个人
    """

    # 类变量
    people_type = '中国人'

    def __init__(self, name):
        """
        构造函数
        """
        # 实例变量
        self.name = name
        print('创造了一个：' + self.name + '人类')

    def eat(self):
        # 新增全局变量
        global food
        food = '面包'
        # print('新增全局变量:' + food)
        print(self.name + '在吃' + food)

    # 类函数
    @classmethod
    def money(cls):
        print(cls.people_type + '喜欢钱')


class Male(People):
    male_type = '男人类'

    def __init__(self, m):
        self.mname = m
        print('Male实例化')
        # print(self.mname)

        # 调用父类构造函数
        # super().__init__(self, m)
        # 多重继承需显示条用父类构造函数
        People.__init__(self, m)

    @classmethod
    def car(cls):
        print(cls.male_type + '喜欢豪车')

    # 子类重写
    def eat(self):
        food1 = '汉堡（子类重写）'
        print(self.name + '在吃' + food1)


class Female():
    female_type = '女人类'

    def __init__(self, f):
        self.fname = f
        print('Female实例化')
        # print(self.fname)

        # # 调用父类构造函数
        # People.__init__(self, f)

    @classmethod
    def bao(cls):
        cls.female_type1 = '富家女'
        print(cls.female_type1 + '喜欢包')

    def drink(self):
        xicha = '喜茶'
        print(self.fname + '喜欢喝' + xicha)


class Little(Male, Female):
    little_type = '儿童类'

    def __init__(self, l):
        self.lname = '祖国的花朵'
        # print(self.lname + '在成长')

        # 调用男人类、女人类
        Male.__init__(self, l)
        Female.__init__(self, l)

    def study(self):
        print(self.lname + 'good good study')

    def drink(self):
        xingbake = '星巴克'
        print(self.lname + '喜欢喝' + xingbake)
