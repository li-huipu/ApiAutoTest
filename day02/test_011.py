'''
mark标记：
    跳过用例：1、这个版本有缺陷，导致用例执行失败，缺陷修改周期比较长，自动化通过率有一定的要求，
             为了不影响通过率，可以将失败的用例跳过，待缺陷解决后，再执行。
             2、某个功能在最新的版本V1R2实现的，V1R2之前的版本不支持。
    执行某一部分用例：界面、接口、功能、冒烟，脚本规模逐步增大，只想执行冒烟测试的用例，或者
             只执行接口的用例，怎么办？自定义标记
            smoke 冒烟用例
            func  功能用例
            api  接口用例
'''

import pytest

Version = "V1R2"

@pytest.mark.smoke
def test_001():
    print("用例1")


@pytest.mark.skip("跳过的原因：由于XXXX缺陷导致失败，该缺陷近期不解决")
def test_002():
    print("用例2")


# skipif 第一个参数是一个表达式，结果为true时，跳过，false时执行
@pytest.mark.skipif(Version != "V1R2", reason="非V1R2版本不支持")
def test_003():
    print("用例3")

@pytest.mark.func  # 类里所有用例都具有这个标记
class TestMark:
    def test_004(self):
        print("用例4")

    @pytest.mark.smoke   # 既有smoke标记，又有func标记
    def test_005(self):
        print("用例5")

    def test_006(self):
        print("用例6")

    def test_007(self):
        print("用例7")
