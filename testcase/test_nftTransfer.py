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
        '''测试用于游戏端向商城发起nft资产转移请求，正常case'''

        args_dict = {
            "userId": "6425591600348397569",
            "id": ["e7fbda05223c57d3a3eddc68"],
            "desc": "des",
            "price":"1",
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/transfer', data)
        print(r.text)
        self.statusCode(r)

    def test_user_002(self):
        '''测试用于游戏端向商城发起nft资产挂售请求，正常case，描述为空'''

        args_dict = {
            "userId": "6425591600348397569",
            "id": ["e7fbda05223c57d3a3eddc68"],
            "desc": "",
            "price":"1.11",
            'tsId': str(self.get_itemId())

        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/transfer', data)
        print(r.text)
        self.statusCode(r)



