# 迭代器是可迭代对象，可迭代对象不一定是迭代器
# iter可将可迭代对象转成迭代器


li=iter([11,22,33,44])
print(li.__length_hint__())
print(li.__setstate__(2))
print(li.__next__())
print(next(li))