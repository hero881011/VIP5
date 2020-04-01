from class05.homework05 import *

print('==========创建一个对象==========')
person = People('男和女')
man = Male('小哥哥')
woman = Female('小姐姐')
little = Little('小妹妹')

print('==========继承父类属性：==========')
print(man.people_type)
print(little.people_type)

print('==========对象调用实例函数==========')
person.eat()
man.eat()
woman.drink()

print('==========类调用类函数==========')
People.money()
Male.car()
Female.bao()

print('==========子类重写==========')
man.eat()
print(man.mname)
little.drink()
print(little.lname)

print('==========类变量==========')
print('人类类变量:' + person.people_type)
# 定义新的类变量
person.people_type = '上海人'
print('定义新的类变量:' + person.people_type)
man.male_type = '上海男人'
print('男人类类变量：' + man.male_type)
woman.female_type = '上海女人'
print('女人类类变量：' + woman.female_type)

print('==========多重继承==========')
little1 = Little('小男孩')
print(little1.name)
little2 = Little('小女孩')
print(little2.mname)
little3 = Little('小屁孩')
print(little3.lname)

print('====================')
