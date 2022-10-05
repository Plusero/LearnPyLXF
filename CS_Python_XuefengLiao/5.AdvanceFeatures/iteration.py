#!/usr/bin/python
# -*- coding: utf-8 -*-
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key in d:
    print(key)
# 注意，dict的储存不是按照list的方式顺序排列，所以迭代出的结果可能不一样

print(enumerate(['A', 'B', 'C']))
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
