# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : test_battal.py


import unittest
import requests

class TestBattal(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://127.0.0.1:12356/'

    def test_index(self):
        '''测试访问首页'''
        response = requests.get(TestBattal.url)
        self.assertEqual(response.status_code, 200, '请求返回非200')
        self.assertEqual(response.json().get('Code'),'0','接口返回状态码不正确!')

    def test_login(self):
        '''测试登录'''
        payload = {'username': 'admin', 'password': 'admin'}
        response = requests.post(TestBattal.url+'login',json=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertEqual(response.json().get('Code'), '0', '接口返回状态码不正确!')
        self.assertTrue(len(response.json().get('Data'))>0)

    def test_select(self):
        '''测试选择装备'''
        payload = {'equipmentid':'300'}
        response = requests.post(TestBattal.url+'selectEq',json=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('equipmentid', response.text, '响应不包含equipmentid')

    def test_kill(self):
        '''测试杀敌'''
        payload = {'equipmentid': '300', 'enemyid': '20'}
        response = requests.post(TestBattal.url+'kill',json=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('你赢了', str(response.json()), '响应不包含指定字符串')

if __name__ == '__main__':
    unittest.main()