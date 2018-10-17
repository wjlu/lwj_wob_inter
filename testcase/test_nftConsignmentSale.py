# # -*- coding: utf-8 -*-

import json
from page.sign import *
from page.ntfgetnew import *
from testcase.status_code import *
import psycopg2


class UserTest(status):
    @classmethod
    def setUp(self):
        conn = psycopg2.connect(dbname="wob_test", user="wob", password="WWpigxo1101", host="47.75.105.222",
                                port="5432")
        print('connect successful!')
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM public.commodity where status =1 ")

        cursor.execute("UPDATE public.commodity SET status =0  where price ='1.56782000'  ")
        conn.commit()
        conn.close()
        print('db reset done')




    def test_user_001(self):
        '''测试用于游戏端向商城发起nft资产挂售请求，正常case'''
        #self.dbreset()
        args_dict = {
            "userId": "6425591600348397569",
            "id": ["e7fbda05223c57d3a3eddc68"],
            "desc": "des",
            "price":"1.56782",
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/consignment', data)
        print('case1')
        print(r.text)
        self.statusCode(r)
        print('测试用于游戏端向商城发起nft资产挂售请求，正常case')

    def test_user_002(self):
        '''测试用于游戏端向商城发起nft资产挂售请求，正常case，描述为空'''

        args_dict = {
            "userId": "6425591600348397569",
            "id": ["e7fbda05223c57d3a3eddc68"],
            "desc": "",
            "price":"1.56782",
            'tsId': str(self.get_itemId())
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print('case2')

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/consignment', data)
        self.statusCode(r)
        print('测试用于游戏端向商城发起nft资产挂售请求，正常case，描述为空')
        #self.log('测试用于游戏端向商城发起nft资产挂售请求，正常case，描述为空')



