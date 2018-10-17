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
        '''正常case，玩家在游戏内花费wbt资产'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": 0.1,
            "targetUserId":'222',
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)


        data = {"args": param["args"], "sign": get_sign}
        print('case1')

        r = post('/api/v1/erc20/expend', data)
        print(r.text)
        self.statusCode(r)



    def test_user_002(self):
        '''正常case，玩家在游戏内花费wbt资产，没有对应targetUserId，为空则表示是直接消耗(由系统吃掉)'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": 0.1,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)


        data = {"args": param["args"], "sign": get_sign}
        print('case2')

        r = post('/api/v1/erc20/expend', data)
        print(r.text)
        self.statusCode(r)

    def test_user_003(self):
        '''异常case，玩家在游戏内花费wbt资产，大于所持有的资产数目'''

        args_dict = {
            "userId": "6425605781151809538",
            "amount": 9999999999,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        data = {"args": param["args"], "sign": get_sign}
        print('case3')
        r = post('/api/v1/erc20/expend', data)
        print(r.text)
        self.ne_no_statusCode(r)
        self.assertTrue('The user at most spend' in r.json()["message"])


    def test_user_004(self):
        '''异常case，玩家在游戏内花费wbt资产为负数'''

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
        data = {"args": param["args"], "sign": get_sign}
        print('case4')
        r = post('/api/v1/erc20/expend', data)
        print(r.text)
        self.tatusCode_400error(r)
        self.assertEqual(r.json()['message'],'the amount in args body must greater than zero')

    def test_user_005(self):
        '''异常case，没有该玩家'''

        args_dict = {
            "userId": "64256057811518095381",
            "amount": 1,
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        data = {"args": param["args"], "sign": get_sign}
        print('case4')
        r = post('/api/v1/erc20/expend', data)
        print(r.text)
        self.ne_no_statusCode(r)
        print(r.json()['message'])
        self.assertEqual(r.json()["message"],"invalid user id")

