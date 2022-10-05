#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = input('Please input your age:')
age = int(age)
if age > 18:
    print('Your age is %s' % age)
    print('Adult')
elif age > 12:
    print('Your age is %s' % age)
    print('Teenager')
else:
    print('Your age is %s' % age)
    print('Kid')
        
