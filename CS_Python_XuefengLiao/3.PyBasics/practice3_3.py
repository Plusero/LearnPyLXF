# -*- coding: utf-8 -*-

# 小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
# 并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height = 1.75
# weight = 80.5
height = float(input('Input your height(e.g.:1.75):'))
weight = float(input('Input your weight:(e.g.:65):'))
BMI = weight/(pow(height,2))
if BMI<18.5:
    print('Too light!')
elif BMI<25:
    print('Normal')
elif BMI<28:
    print('Too heavy')
elif BMI<32:
    print('Fat!')
else:
    print('What a fatty!')
