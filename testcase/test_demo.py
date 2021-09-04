import time
import unittest

# from ddt import ddt
from unittestreport import ddt, list_data


@ddt
class Testdemo1(unittest.TestCase):
    data = [
        {'title': 'Testdemo1测试用例1', 'data': 11},
        {'title': 'Testdemo1测试用例2', 'data': 22},
        {'title': 'Testdemo1测试用例3', 'data': 33},
    ]

    @list_data(data)
    def test_demo001(self, item):
        time.sleep(0.5)
        print("执行用例{}".format(item))


@ddt
class Testdemo2(unittest.TestCase):
    data = [
        {'title': 'Testdemo2测试用例1', 'data': 11},
        {'title': 'Testdemo2测试用例2', 'data': 22},
        {'title': 'Testdemo2测试用例3', 'data': 33},
    ]

    @list_data(data)
    def test_demo002(self, item):
        time.sleep(0.5)
        print("执行用例{}".format(item))
