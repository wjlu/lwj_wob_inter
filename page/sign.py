# # -*- coding: utf-8 -*-
from hashlib import md5
def api_arguments_sign(args, appsecret = "$2b$10$1ZbzRhmxxPZAtwzb/2zFc..lvkByyQiJFrxITmaV0tRQXAHuWSoN2"):
    """
    接口参数签名验证
    appsecret使用默认值
    """

    del args["sign"]
    pairs = sorted(args.items(), key=lambda e: e[0].lower())
    print("排序后的 (k、v pair) 列表",pairs)
    text = str()
    for key, value in pairs:
        text = text + "{}={}".format(key, value)
    print("排序后的字符串",text)
    text = "{0}{1}{0}".format(appsecret, text)
    text = text.encode("utf-8")
    sign = md5(text).hexdigest().lower()
    return sign
