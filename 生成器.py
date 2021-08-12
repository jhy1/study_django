'''
可迭代对象
1.迭代器（如何将可迭代对象转成迭代器）
2.掌握使用next进行操作
3.生成器
    1.生成器的定义
        生成器表达式
        生成器函数
    2.生成器的迭代操作
    3.和生成器内部的数据交换
        send可以往生成器发送数据
'''
# 生成器表达式
li=(i for i in range(10))
#使用next生成数据
# print(next(li))

# 生成器函数 只能在函数中用

def  login():
    # print('iiiiiiii')
    for i in range(100):
        s = yield i
        print('zzzzzzzzz'+s)
lg = login()

next(lg)

print(lg.send('yyyyy'))