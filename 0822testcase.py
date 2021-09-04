import time
from unittest import TestCase


class High(type):
    def __new__(cls, name, class_from, class_data, *args, **kwargs):
        case_site = super().__new__(cls, name, class_from, class_data)
        print(class_data['test_case'])
        for k, v in enumerate(class_data['test_case']):
            # print(k)
            setattr(case_site, 'test_{}'.format(k), lambda x: x)
        return case_site


class_name = 'site2'
data = {"class_name": class_name, "class_time": time.time(), "test_case": [11, 22, 33, 44, 55, 66]}

data2 = {"cases": [11, 22, 33, 44, 55], "test_case1": lambda x: x, "test02": lambda x: x}
site = High(class_name, (TestCase,), data)
site2 = type("site2", (TestCase,), data2)
# print(site.class_time)

if __name__ == '__main__':
    import unittest
    import unittestreport

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(site)
    unittestreport.TestRunner(suite).run()
