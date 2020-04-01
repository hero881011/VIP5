from class05.example01 import Dog

bDog = Dog('旺财')
wDog = Dog('小白')

# 对象调用实例函数
bDog.eat()
bDog.bark()

# 类调用类函数
Dog.my_type()

print(bDog.my_t)
# 定义了实例变量出来
bDog.my_t = '人'
print(bDog.my_t)
print(wDog.my_t)


