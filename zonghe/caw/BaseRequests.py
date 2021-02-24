'''
1. get、post方法做一下异常处理
2. 打印日志
3. 保持会话，使用session发送请求
'''

import requests


class BaseRequests:
    # 在构造方法中创建一个session。
    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            print(f"发送get请求，url：{url}，请求参数：{kwargs}成功。")
            return r
        except Exception as e:
            print(f"发送get请求，url：{url}，请求参数：{kwargs}异常，异常信息为：{e}")

    def post(self, url, **kwargs):
        try:
            r = self.session.post(url, **kwargs)
            # 格式化输出，如下两个效果一样
            print(f"发送post请求，url：{url}，请求参数：{kwargs}成功。")
            # print("发送post请求，url：%s，请求参数：%s成功。"%url%kwargs)
            return r
        except Exception as e:
            print(f"发送post请求，url：{url}，请求参数：{kwargs}异常，异常信息为：{e}")


# 测试代码，用完可以删除
if __name__ == '__main__':
    r = BaseRequests().get("http://192.168.1.64:8089/futureloan/mvc/api/member/list")
    print(r.text)
    r = BaseRequests().post("http://192.168.1.64:8089/futureloan/mvc/api/member/login",
                            data={"mobilephone": "", "pwd": "123123"})
    print(r.text)
