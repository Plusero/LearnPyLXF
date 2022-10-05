#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)#把上面n-1个的整体从a移到b
        move(1,a,b,c)#a上剩下那个最大的从a移动到c
        move(n-1,b,a,c)#把n-1个整体从b移到c
        # 不要考虑单个如何移动，具体移动交给递归函数，只要把握整体，将n-1看成整体移动就ok了
move(4,'A','B','C')

