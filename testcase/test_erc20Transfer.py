# # -*- coding: utf-8 -*-
import json
from page.sign import *
from page.ntfgetnew import *
from testcase.status_code import *

class UserTest(status):
    @classmethod
    def setUpClass(cls):
        pass


    def test_user_001(self):
        '''用于游戏端向商城发起erc20资产转移请求，正常case'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": 0.001,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)


        data = {"args": param["args"], "sign": get_sign}
        print('case1')

        r = post('api/v1/erc20/transfer', data)
        print(r.text)
        self.statusCode(r)



    def test_user_002(self):
        '''异常case，用于游戏端向商城发起erc20资产转移请求，没有对应资产'''

        args_dict = {
            "userId": "6425925273086066694",
            "amount": 1,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)

        data = {"args": param["args"], "sign": get_sign}
        print('case2')
        r = post('api/v1/erc20/transfer', data)
        print(r.text)
        self.ne_no_statusCode(r)
        self.assertEqual(r.json()['message'],"The user have no wbt asset")


    def test_user_003(self):
        '''异常case，用于游戏端向商城发起erc20资产转移请求，对应资产为负数'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": -1,

            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print('case3')
        data = {"args": param["args"], "sign": get_sign}
        r = post('api/v1/erc20/transfer', data)
        print(r.text)
        self.statusCode_400error(r)
        self.assertTrue(r.json()['message'] , 'the amount in args body must greater than zero')


    def test_user_004(self):
        '''异常case，用于游戏端向商城发起erc20资产转移请求，转移数目超过用户数量'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": 999999999,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print('case4')
        data = {"args": param["args"], "sign": get_sign}
        r = post('api/v1/erc20/transfer', data)
        print(r.text)
        self.ne_no_statusCode(r)
        self.assertTrue('The user at most transfer' in r.json()['message'])

