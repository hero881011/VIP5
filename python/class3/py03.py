# coding=utf-8

# 99乘法表 for表达式
for x in range(1, 10):
    row = ''
    for y in range(1, 1 + x):
        row += str(y) + "*" + str(x) + "=" + str(x * y) + "\t"

    print(row)
    x += 1

# 去掉对角线
for i in range(1, 10):
    row = ''
    for j in range(0, 9):
        j += 1
        if i == j:
            row += ' ' + '\t'
            continue
        if i + j == 10:
            row += ' ' + '\t'
            continue

        row += str(i * j) + '\t'

    print(row)
    i += 1

####################################
# 1. 关于print的%
#   %d|f|s  (整数|小数|字符串)
#   %3d     (规定输出占位3位，不足会在左边不空格，-3，就是在右边补，超过会按实际位输出)
#   %8.2f   (总位数为8位，包括小数点，小数点为两位)
#   %3s      (和整数是一样的)
# 2. 是用if语句的注意事项
#    判断变量是否为空指针None
####################################

# 四舍五入保留两位小数
print('# 四舍五入保留两位小数')
f = 100.00000
print(round(f, 3))
# f='%.2f' % f
print('%7.2s' % str(f))
print('%s%2.2f' % (str(f), f))

dict1 = {'key1': 11, 'key2': 30, 'Roy': "男\'''"}
print(dict1.keys())
print(type(dict1.keys()))
print(dict1.values())

# 键的遍历，类似于把所有键看作一个列表
for key in dict1.keys():
    print(key + ':' + str(dict1[key]))
    dict1[key] = str(dict1[key]) + 'sss'
print(dict1)

# 值的遍历，一般不怎么用
for value in dict1.values():
    print(value)

# 键值对的遍历1
for item in dict1.items():
    print(item)
    print(type(item))
# 键值对的遍历2
for key, value in dict1.items():
    print(key + ':' + str(value))

import json

s = '/**/jQuery110201270640987324041_1581588266985(\
{"status":"0","t":"1581604043468","set_cache_time":"",\
"data":[{"location":"澳大利亚","titlecont":"IP地址查询",\
"origip":"1.1.1.1","origipquery":"1.1.1.1","showlamp":"1",\
"showLikeShare":1,"shareImage":1,"ExtendedLocation":"",\
"OriginQuery":"1.1.1.1","tplt":"ip","resourceid":"6006",\
"fetchkey":"1.1.1.1","appinfo":"","role_id":0,"disp_type":0}]})'

# 处理为标准json
s = s[s.find('{'):s.rfind('}') + 1]  # 字符串截取
print(s)
jsonres = json.loads(s)  # 字符串转换为json格式
print(jsonres)
print(jsonres['data'][0]['location'])
