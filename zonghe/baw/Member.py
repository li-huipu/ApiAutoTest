'''
金融项目用户管理模块的接口
member 是模块名
list 是接口名
http://192.168.1.64:8089/futureloan/mvc/api/member/list
'''


def register(baserequest, url, data):
    '''
    :param baserequest:  是BaseRequests的实例
    :param url: 环境url
    :param data: 注册数据
    :return: 响应
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequest.post(url, data=data)
    return r


def list(baserequest, url):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequest.post(url)
    return r


def login(baserequest, url, data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequest.post(url, data=data)
    return r
