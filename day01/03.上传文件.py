import requests

# 接口路径
url = "http://www.httpbin.org/post"
# 本地存在的文件
file = "d:/test.png"
# rb二进制只读的方式打开
with open(file, mode='rb') as f:
    # {'name': file-tuple}
    # file-tuple: ('filename', fileobj, 'content_type')
    cs = {"filename": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)

# 租车系统上传图片
url = "http://192.168.150.70:8089/carRental/file/uploadFile.action"
file = "d:/test.png"
with open(file, mode='rb') as f:
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    # {"code":0,"msg":"","count":null,"data":{"src":"2021-01-28/202101281413251577831.png_temp"}}
    # 获取图片的路径
    uploadPath = r.json()['data']['src']

# 添加车，使用刚上传的图片
url = "http://192.168.150.70:8089/carRental/car/addCar.action"
cs = {
    "carnumber": "陕A123459", "cartype": "比亚迪", "color": "白色",
    "carimg": uploadPath, "description": "2020年新车",
    "price": 200000, "rentprice": 1000, "deposit": 500, "isrenting": 0
}
head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
r = requests.post(url, data=cs, headers=head)
print(r.text)
