import requests, json, traceback

# 会话管理
session = requests.session()

# 获取token
result = session.post('http://testingedu.com.cn:8081/inter/HTTP/auth')
print(result.text)


# 键值对格式的参数，在python里面需要用字典传
# 如果是json字符串，就直接传json=字符串
params = {
    'username': 'hero',
    'password': '123456'
}

# result.headers对应response header
# 对应request headers
print(result.request.headers)
# result.status_code对应status code

jsonres = json.loads(result.text)
session.headers['token'] = jsonres['token']

result = session.post('http://testingedu.com.cn:8081/inter/HTTP/login', data=params)
# text对应response
print(result.text)

# try:
#     expectres = '{"status":200,"msg":"恭喜您，登录成功"}'   # 校验字符串全部一样
#     expectres = json.loads(expectres)
#     for key in expectres.keys():
#         if expectres[key] != jsonres[key]:
#             print('FAIL')
#             break
#
# except Exception as e:
#     print('FAIL')
#     print(traceback.format_exc())

jsonres = json.loads(result.text)

try:
    if jsonres['userid'] == '46':
        print('PASS')
    else:
        print('FAIL')
except Exception as e:
    print('FAIL')
    print(traceback.format_exc())

# 退出
result = session.post('http://testingedu.com.cn:8081/inter/HTTP/logout')
print(result.text)

