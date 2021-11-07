# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术


import requests
import uuid

requests.adapters.DEFAULT_RETRIES = 5

# s=requests.session()
# s.keep_alive=False    keep_alive默认为True，代表长连接，设置为False代表短连接，使用完就断开连接。
# s.get('https://httpbin.org/ip')

# 1、GET请求
# r = requests.get('https://httpbin.org/ip')
# print(r.text)
# print(r.content)
# print(r.json())

# 2、发送GET请求，带参数
# 等同于直接访问https://httpbin.org/get?name=mikezhou&age=18
# r = requests.get('https://httpbin.org/get', params={'name': 'mikezhou','age':18})
# print(r.url)
# print(r.text)

# 3、定制请求头
# header = {'user-agent': 'my-app/0.0.1','token':str(uuid.uuid1())}
# r = requests.get('https://httpbin.org/get', headers=header)
# print(r.text)

# 4、发送get请求， 加proxy
proxies = {'http': 'http://127.0.0.1:8080',
           'https': 'http://127.0.0.1:8080'}
# r=requests.get('https://httpbin.org/get', proxies=proxies)
# print(r.text)

# 5、发送get请求，加鉴权 -- Basic Auth
# from requests.auth import HTTPBasicAuth
# r = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'password'))
# print(r.text)


# 6、发送POST请求
# 通常，你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。
# 要实现这个，只需简单地传递一个字典给 data 参数, 数据字典在发出请求时会自动编码为表单形式
# content-type: application/x-www-form-urlencoded
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data = payload)
# print(r.text)

# 7、如果你想要发送的数据并非编码为表单形式的。
# 如果你传递一个 string 而不是一个 dict。
import json
# payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
print(r.text)

# content-type: application/json
# 8、你还可以使用 json 参数直接传递，然后它就会被自动编码，下述和上述代码等价
r = requests.post('http://httpbin.org/post', json=payload)
print(r.text)



# 发送PUT请求
# r = requests.put('https://httpbin.org/put', data={'name': 'mikezhou'})
# print(r.text)
#
# 发送 DELETE 请求
# r = requests.delete('https://httpbin.org/anything', data={'name': 'mikezhou'})
# print(r.text)


# 获取接口返回值
# r = requests.post('https://httpbin.org/anything', data={'hello': 'mikezhou'})

# 返回文本型response
# print(r.text)
# 获取二进制返回值
# print(r.content)

# 返回JSON串
# print(r.json())

# 获取请求返回码
# print(r.status_code)

# # 获取response的headers
# print(r.headers)
#
# # 获取response的cookie
# print(r.cookies.get_dict())


# 6.Requests 保存 Session

# 初始化一个session对象
s = requests.Session()
r1=s.get('http://localhost/login')
cookie=r1.cookies.get_dict()
s.post('http://localhost/user',cookies=cookie)

# httpbin这个网站允许我们通过如下方式设置，在set后写你需要的值即可
# s.get('https://httpbin.org/cookies/set/name/mikezhou')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)

