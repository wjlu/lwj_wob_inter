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
        '''测试游戏端向商城发起nft资产创建请求，正常case'''
        args_dict = \
            {
            "userId": "6425605781151809538",
            "items": [
                {
                    "name": "profd3",
                    "desc": "the desc about prop1",
                    "price": "12.22334",
                    "itemId": str(self.get_itemId()),
                    "amount": 1
                },
                {
                    "name": "profd4",
                    "desc": "the desc about prop2",
                    "price": "10.900",
                    "itemId":str(self.get_itemId()),
                    "amount": 100
                }
            ],
            "sign": "92d1880ca61cf5717633d10cf8d89cf8"
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)


        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.statusCode(r)

    def test_user_002(self):
        '''测试游戏端向商城发起nft资产创建请求，资产项只有一个'''
        args_dict = \
            {
                "userId": "6425605781151809538",
                "items": [
                    {
                            "name": "profd3",
                            "desc": "the desc about prop1",
                            "price": "12.22334455",
                            "itemId": str(self.get_itemId()),
                            "amount": 1
                    }
                ],
                    "sign": "92d1880ca61cf5717633d10cf8d89cf8"
            }

        param = {
                "sign": "e17882342f3de28bfdc2cb72105c8743",
                "args": json.dumps(args_dict).replace('"', "'")
            }

        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.statusCode(r)

    def test_user_003(self):
        '''异常case，测试游戏端向商城发起nft资产创建请求，amount数量为负数'''
        args_dict = \
            {
                "userId": "6425605781151809538",
                "items": [
                    {
                            "name": "profd3",
                            "desc": "the desc about prop1",
                            "price": "12.22334",
                            "itemId": str(self.get_itemId()),
                            "amount": -1
                    }
                ],
                    "sign": "92d1880ca61cf5717633d10cf8d89cf8"
            }

        param = {
                "sign": "e17882342f3de28bfdc2cb72105c8743",
                "args": json.dumps(args_dict).replace('"', "'")
            }

        get_sign = api_arguments_sign(param)


        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.ne_statusCode(r)

    def test_user_004(self):
        '''异常case，测试游戏端向商城发起nft资产创建请求，"price"，"amount"数量字段校验需要做非零校验'''
        args_dict = \
            {
                "userId": "6425605781151809538",
                "items": [
                    {
                            "name": "profd3",
                            "desc": "the desc about prop1",
                            "price": "",
                            "itemId": str(self.get_itemId()),
                            "amount": 0
                    }
                ],
                    "sign": "92d1880ca61cf5717633d10cf8d89cf8"
            }

        param = {
                "sign": "e17882342f3de28bfdc2cb72105c8743",
                "args": json.dumps(args_dict).replace('"', "'")
            }

        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.ne_statusCode(r)

    def test_user_005(self):
        '''正常case，测试游戏端向商城发起nft资产创建请求，描述为空'''
        args_dict = \
            {
                "userId": "6425605781151809538",
                "items": [
                    {
                            "name": "profd3",
                            "desc": "",
                            "price": "1.11111111",
                            "itemId": str(self.get_itemId()),
                            "amount": 1
                    }
                ],
                    "sign": "92d1880ca61cf5717633d10cf8d89cf8"
            }

        param = {
                "sign": "e17882342f3de28bfdc2cb72105c8743",
                "args": json.dumps(args_dict).replace('"', "'")
            }

        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.statusCode(r)

    def test_user_006(self):
        '''极限case，测试游戏端向商城发起nft资产创建请求，items有10项'''
        args_dict = \
            {
                "userId": "6425605781151809538",
                "items": [
                    {
                            "name": "profd1",
                            "desc": "1",
                            "price": "1.11111111",
                            "itemId": str(self.get_itemId()),
                            "amount": 1
                    },
                    {
                        "name": "profd2",
                        "desc": "2",
                        "price": "1.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 2
                    },
                    {
                        "name": "profd3",
                        "desc": "3",
                        "price": "3.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 3
                    },
                    {
                        "name": "profd4",
                        "desc": "4",
                        "price": "4.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 4
                    },
                    {
                        "name": "profd5",
                        "desc": "5",
                        "price": "1.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 5
                    },
                    {
                        "name": "profd6",
                        "desc": "6",
                        "price": "1.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 6
                    },
                    {
                        "name": "profd7",
                        "desc": "7",
                        "price": "7.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 7
                    },
                    {
                        "name": "profd8",
                        "desc": "8",
                        "price": "8.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 8
                    },
                    {
                        "name": "profd9",
                        "desc": "9",
                        "price": "9.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 9
                    },
                    {
                        "name": "profd10",
                        "desc": "10",
                        "price": "10.11111111",
                        "itemId": str(self.get_itemId()),
                        "amount": 10
                    }

                ],
                    "sign": "92d1880ca61cf5717633d10cf8d89cf8"
            }

        param = {
                "sign": "e17882342f3de28bfdc2cb72105c8743",
                "args": json.dumps(args_dict).replace('"', "'")
            }

        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/props/get/new', data)
        print(r.text)
        self.statusCode(r)


