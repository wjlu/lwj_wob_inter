# # -*- coding: utf-8 -*-

import unittest
import random


class status(unittest.TestCase):
    def statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json()['code'], 1)
        self.assertEqual(r.json()['http_status_code'], 201)


    def ne_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        self.assertEqual(r.json()['http_status_code'], 200)

    def ne_no_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], -1)
        self.assertEqual(r.json()['http_status_code'], 200)



    def gamelogin_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 1)
        self.assertEqual(r.json()['http_status_code'], 200)

    def gamelogin_err_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], -1)
        self.assertEqual(r.json()['http_status_code'], 200)

    def gamelogin_allerr_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''

        self.assertEqual(r.json()['code'], -1)
        self.assertEqual(r.json()['http_status_code'], 400)

    def get_itemId(self):
        return random.randint(10, 1000000)