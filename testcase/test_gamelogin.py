# # -*- coding: utf-8 -*-

import json
from page.sign import *
from page.ntfgetnew import *
from testcase.status_code import *

class UserTest(status):
    @classmethod
    def setUpClass(cls): #类方法，不管多少case只执行一次
        pass


    def test_user_001(self):
        '''正常case,用于游戏端向商城发起登录请求'''

        args_dict = {
            "email": "844916536@qq.com",
            "password": "030618aaa",
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/game/login', data)
        print(r.text)
        self.gamelogin_statusCode(r)

    def test_user_002(self):
        '''正常case,用于游戏端向商城发起登录请求,用户名错误'''

        args_dict = {
            "email": "3@qq.com",
            "password": "030618aaa",
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/game/login', data)
        self.gamelogin_err_statusCode(r)
        self.assertEqual(r.json()['message'],"username error or user is diabled")

    def test_user_003(self):
        '''正常case,用于游戏端向商城发起登录请求,密码错误'''

        args_dict = {
            "email": "333@qq.com",
            "password": "030618",
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/game/login', data)
        print(r.text)
        self.gamelogin_err_statusCode(r)
        self.assertEqual(r.json()['message'],"password error")


    def test_user_004(self):
        '''异常case,用于游戏端向商城发起登录请求,用户名密码为空'''

        args_dict = {
            "email": "",
            "password": "",
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/game/login', data)
        print(r.text)
        self.statusCode_400error(r)
        self.assertEqual(r.json()['message'],"email and password are required")


