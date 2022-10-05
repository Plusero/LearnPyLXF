#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_power(x, n=2):
    """[summary]

    Args:
        x ([type]): [description]
        n ([type]): [default value is 2]

    Returns:
        [type]: [description]
    """
    p = 1
    while n > 0:
        n = n-1
        p = p*x
    return p


def enroll(name, gender, age=6, city='Shenzhen'):
    """[summary]

    Args:
        name ([type]): [description]
        gender ([type]): [description]
        age (int, optional): [description]. Defaults to 6.
        city (str, optional): [description]. Defaults to 'Shenzhen'.
    """
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(my_power(5, 3))
print(my_power(2, 3))
print(my_power(6))

enroll('Anne', 'Female')

L1 = ['Bruce', 'Lira', 'Jack']
print(L1)
add_end(L1)
print(L1)

print(calc(1, 2, 3, 4))

print(person('Coke', 20))
print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 18, **extra))


def person_a(name, age, *, city='Shenzhen', job):
    print(name, age, city, job)


print(person_a('Bruce', 20, job='EE Engineer'))
