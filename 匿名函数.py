#匿名函数的应用
li=[[1,2],[3,33],[3,4553,6]]
li.sort(key=lambda x: x[0])
print(li)
#过滤数据
# filter()
#
# # 处理数据
# map()
#
# #识别数据类型，执行
# eval()
#执行python代码
data = """
def login():
    print('1111111111')"""
exec(data)

#聚合函数
title=['a','b','c']
value=[1,2,3,4]
data=zip(title,value)
print(dict(data))

