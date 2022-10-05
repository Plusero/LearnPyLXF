#!/usr/bin/python
# -*- coding:utf-8 -*-
# This program shows the probability that at least two students
# were born on the same day in a class as the number of students
# increases from 1 to 365


import matplotlib.pyplot as plt

N = []
P = []
product = 1
for i in range(1, 366):
    N.append(i)
print(len(N))
for i in range(1, 366):
    numerator = 1
    for x in range(1, i+1):
        numerator = numerator*(366-x)
    P.append(1-(numerator)/(pow(365, i)))
    print(P[i-1])
plt.plot(N, P, marker='.')
plt.show()
