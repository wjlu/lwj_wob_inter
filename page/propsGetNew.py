#-*-coding:utf-8-*-

import  requests
import  os



def getHeaders():
	'''获取请求头信息'''
	headers={
        "Content-Type": "application/json",
        "App-Id": "wob071913289742227",
        "appsecret": "$2b$10$1ZbzRhmxxPZAtwzb/2zFc..lvkByyQiJFrxITmaV0tRQXAHuWSoN2"\
        }
	return headers

def post(api,data):
	'''
	对post请求进行二次封装
	:parameter api:请求ip地址+api
	:parameter data:请求参数
	'''
	r=requests.post(url='http://47.75.105.222/'+api,json=data,timeout=6,headers=getHeaders())
	return r