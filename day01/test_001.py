'''
pytest命名约束：
1、文件用test_开头
2、类用Test开头
3、函数或方法用test_开头
'''


def test_register_001():
    print("注册成功的脚本")
    assert "" in ""
    assert "" == ""


def test_register_002():
    print("手机号码格式不正确")


def test_register_003():
    print("密码不足5位")

# 使用requests+pytest实现金融项目注册、登录接口的自动化脚本。
