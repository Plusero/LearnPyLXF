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

# this can be in generator form
N = [i for i in range(1, 366)]
# of course, with NumPy, this can be more efficient generating a sequence

print(len(N))
for i in range(1, 366):
    numerator = 1
    for x in range(1, i+1):  # remember to format your code!
        numerator = numerator*(366-x)  # this is not elegant!
        numerator *= 366 - x  # this is elegant!
        # one possible solution is, use reduce() method in functools package,
        # multiply the whole list
    P.append(1-(numerator)/(pow(365, i)))  # format your code!
    P.append(1 - numerator / 365 ** i)  # no need to call pow(), just use **
    print(P[i-1])

plt.plot(N, P, marker='.')  # no need to specify kwargs
plt.plot(N, P, 'o.--')
plt.show()


def same_birth(n):
    numerator = 1
    for x in range(1, n+1):
        numerator = numerator*(366-x)
        numerator *= 366 - x
    return 1-(numerator)/(pow(365, n))
