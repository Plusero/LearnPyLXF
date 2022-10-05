#!/usr/bin/python
# -*- coding:utf-8 -*-
#The first line tells system to use the tool--python to interpret this program
#The second line designate utf-8 as the encoding method
import matplotlib.pyplot as plt
import random
import time

try:
    Oscilloscope = list(range(200))
    xAxis = list(range(200))
    ADC_Random = list(range(200))
    for x in range(len(xAxis)):
        xAxis[x] = x
        Oscilloscope[x] = 0
    while(1):
        for index in range(200):
            Oscilloscope[index] = random.uniform(-5,5)
            print("0 ADC = %lf" % (Oscilloscope[index]))
            print("%lf" % (index))
        flag = input('Please input the gain you want:(1、10 or 0.1):')
        if flag == '1':
            Oscilloscope = [i-2.5 for i in Oscilloscope]
        elif flag == '10':
            Oscilloscope = [i*0.1-2.5 for i in Oscilloscope]
        else:
            Oscilloscope = [i*10-2.5 for i in Oscilloscope]
        plt.title('Oscilloscope')
        plt.ylabel('Voltage')
        plt.plot(xAxis, Oscilloscope)
        plt.show()
except:
    print("\r\nProgram end     ")
    exit()

