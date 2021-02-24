'''
读取数据的文件
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取工程路径
    :return:  E:\ApiAutoTest\zonghe\
    '''
    file_path = os.path.realpath(__file__)
    # print("当前文件路径:",file_path)
    dir_path = os.path.dirname(file_path)
    # print("当前文件所在的目录:", dir_path)
    dir_path = os.path.dirname(dir_path)
    # print("再上一级目录:", dir_path)
    # 最后拼一个\
    return dir_path + "\\"


def read_ini(file_path, key):
    '''
    读取配置文件
    :param file_path: 配置文件的路径
    :param key: 配置文件中的key，比如url
    :return: 返回key对应的value
    '''
    # python内置的模块configparser
    config = configparser.ConfigParser()
    file_path = get_project_path() + file_path
    config.read(file_path)
    # "env" 对应 ini文件中的 [env]
    value = config.get("env", key)
    return value


def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding='utf-8') as f:
        # 读文件
        file_content = f.read()
        # 用yaml中的load方法，将文件内容转成yaml格式的。
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content # 列表嵌套字典


# 测试代码，用完可删除
if __name__ == '__main__':
    v = read_ini(r"test_env\env.ini", "url")
    print(v)
    v = read_ini(r"test_env\env.ini", "db_info")
    print(v)
    content = read_yaml("test_data/register_fail.yaml")
    print(content)
