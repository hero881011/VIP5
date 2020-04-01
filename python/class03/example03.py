
d1 = {
    'name':'will',
    'age':29,
    'height':173
}
print(d1)

# 获取值
print(d1['name'])
print(d1.get('name'))
print(len(d1))

# 更新
d1['name'] = 'hero'
print(d1)

# 清空
# d1.clear()
# print(d1)

# 删除
d1.pop('name')
print(d1)
# 删除最后一个键值对
tup1 = d1.popitem()
print(tup1)
print(type(tup1))

tup2 = d1.popitem()
print(tup2)
print(type(tup2))










