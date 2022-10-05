def quadratic(a, b, c):
    import math
    for i in [a,b,c]:
        if not isinstance(i,(int, float)):
            raise TypeError('bad operand type')
    if (b**2-4*a*c)<0:
        print('无解')
        return None
    else:    
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2

print(quadratic(1, 5, 6))
print(quadratic(1,1,1))
# print(quadratic('a','b','c'))
