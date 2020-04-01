# coding=utf-8
import requests,time,json

# print(time.time())

# 发包
res = requests.post('http://112.74.191.10:80/inter/HTTP/auth')  # 拿到token
print(res.text)
jsonres = json.loads(res.text)
# jsonres = eval(res.text)
print(jsonres['token'])

# eval函数的作用：把一个字符串按python语法，得到它执行后的结果
# jsonres = eval(res.text)
# print(jsonres)

# 构造函数
params = {'username':'Will',
          'password':'123456'
          }

# 发包
res = requests.post('http://112.74.191.10:80/inter/HTTP/login',data=params,headers={'token':jsonres['token']})
# print(res.content.decode('utf-8'))
print(res.text)





