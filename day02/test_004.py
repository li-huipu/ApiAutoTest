'''
fixture级别：session、class、module、function（默认）
'''
import pytest

@pytest.fixture(scope='module')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开数据库连接")

@pytest.fixture(scope='module')
def login():
    print("前置：在首次调用login的地方执行前置")
    yield
    print("后置：模块所有用例执行完执行后置")

def test_001():
    print("用例1")

def test_002(login, db):   # 这个用例前执行前置
    print("用例2")

def test_003(db):
    print("用例3")

def test_004(login):     # 这个用例后执行后置
    print("用例4")