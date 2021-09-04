import unittest
# from unittestreport import TestRunner
from concurrent.futures.thread import ThreadPoolExecutor

suite = unittest.defaultTestLoader.discover('F:\Tencentstudy\\0628study\\testcase')
suite_list = []
for item in suite:
    for sui_cls in item:
        suite_list.append(sui_cls)

# print(suite_list)

# TestRunner(suite).run()


def execute_suite(suite:unittest.TestSuite):
    # print(suite)
    # res = unittest.TextTestRunner().run(suite)
    # print(res)
    result = unittest.TestResult()
    res = suite.run(result)
    res =dict(
        fail=len(res.failures),
        error=len(res.errors),
        skip=len(res.skipped),
        all_test=res.testsRun
    )
    return res

    print(res)


with ThreadPoolExecutor(max_workers=2) as pool:
    result=pool.map(execute_suite, suite_list)
    res={'fail': 0, 'error': 0, 'skip': 0, 'all_test': 0}
    for item in list(result):
        res['fail']+=item['fail']
        res['error'] += item['error']
        res['skip'] += item['skip']
        res['all_test'] += item['all_test']
    print(res)
