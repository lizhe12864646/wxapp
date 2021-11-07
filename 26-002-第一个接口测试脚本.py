# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术


import requests

# 首页
url_index = 'http://127.0.0.1:12356/'
# response_index = requests.get(url_index)
# print(f'Response内容：{response_index.json()}')


# 登录
url_login = 'http://127.0.0.1:12356/login'
payload = {'username':'admin','password':'admin'}
response_login = requests.post(url_login, json=payload)
print(f'Response内容：{response_login.json()}')


# 选择装备
url_select = 'http://127.0.0.1:12356/selectEq'
payload = {'equipmentid':'200'}
# response_select = requests.post(url_select, json=payload)
# print(f'Response内容：{response_select.json()}')


# 杀敌
url_kill = 'http://127.0.0.1:12356/kill'
payload = {'equipmentid':'200','enemyid':'20'}
# response_kill = requests.post(url_kill, json=payload)
# print(f'Response内容：{response_kill.json()}')