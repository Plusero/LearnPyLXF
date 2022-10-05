X = [x*x for x in range(1,11) ]
print(X)
Y = [y*y for y in range(1,11) if y%2 ==0]
str1 = [m+n for m in 'ABC' for n in 'XYZ']

d = {'x':'A','y':'B','z':'C'}
str2 = [k+'='+v for k,v in d.items()]

L = ['Hello','World','Tesla','TI','ADI']
L_lower=[s.lower() for s in L]
print(L_lower)


