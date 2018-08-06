# # -*- coding: utf-8 -*-
import json
from testcase.status_code import *
from page.sign import *
from page.ntfgetnew import *
import time


class UserTest(status):
    @classmethod
    def setUpClass(cls):
        pass

    def test_user_001(self):
        '''测试游戏端向商城发起nft资产创建请求，正常case'''
        args_dict = {
            "userId": "6425605781151809538",
            "id": ["e7fbda05223c57d3a3eddc61"],
            "desc": "about desc"
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)

        data = {"args": param["args"], "sign": get_sign}
        time.sleep(80)
        r = post('api/v1/nft/get/new', data)
        print(r.text)
        self.statusCode(r)
        #快速请求会报错，据说有保护，被迫sleep 80秒
        # time.sleep(80)



    # def test_user_002(self):
    #     '''测试游戏端向商城发起nft资产创建请求，desc为空'''
    #     args_dict = {
    #         "userId": "6425605781151809538",
    #         "id": ["e7fbda05223c57d3a3eddc61"],
    #         "desc": ""
    #     }
    #
    #     param = {
    #         "sign": "e17882342f3de28bfdc2cb72105c8743",
    #         "args": json.dumps(args_dict).replace('"', "'")
    #     }
    #
    #
    #     get_sign = api_arguments_sign(param)
    #
    #     data = {"args": param["args"], "sign": get_sign}
    #
    #     r = post('api/v1/nft/get/new', data)
    #     print(r.text)
    #     self.statusCode(r)


