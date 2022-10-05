height = 1.75
weight = 80.5
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