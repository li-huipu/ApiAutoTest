'''
测试前置和后置
    模块级和函数级
    名字不能写错，pytest根据名字来识别是前置和后置
'''

def setup_module():
    print("前置，模块中所有用例前执行一次")

def teardown_module():
    print("后置，模块中所有用例后执行一次")
    
def setup_function():
    print("前置，每个用例前执行一次")

def teardown_function():
    print("后置，每个用例后执行一次")

def test_001():
    print("用例1")
def test_002():
    print("用例2")
def test_003():
    print("用例3")