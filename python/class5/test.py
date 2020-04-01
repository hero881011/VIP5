# coding = utf-8
from test1 import *

# 创建一个对象
wdog = Dog('小白')
wdog.bark()
print(Dog.MyType)
wdog.swing()
wdog.bark()

bdog = BDog('小黑黑')
bdog.BBark()
bdog.swing()
print(bdog.MyType)  #继承父类属性
print(bdog.name)

# 子类重写
bdog.bark('zzzz')
print(bdog.name)

# 多重继承
bdog = LittleDog()
print(bdog.wname)

ldog = LittleDog()
print(ldog.bname)
