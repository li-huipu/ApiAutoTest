'''
Cookie 用来识别用户
'''

import  requests

# 没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上cookie信息
head  = {
"Cookie": 'BAGSESSIONID=febfdd4e-8154-44d9-ad60-1fa30a7b75cd; JSESSIONID=79108DBF36459FEB863022018DB90297; __asc=21c0338117747dac507c1c1f387; __auc=21c0338117747dac507c1c1f387; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611818256; _ga=GA1.2.866168421.1611818259; _gid=GA1.2.241486894.1611818259; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818266'
}
r = requests.get(url, headers=head)
print(r.text)
assert  "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：
1. cookie会失效，失效后需要重新获取
2. 登录后的每个接口，需要带着cookie
'''