
L = ['A', 'B', 'C', 'D', 'E', 'F']
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:-1])

L100 = list(range(100))
print(L100[0:10])  # 前10个数
print(L100[-10:])  # 后10个数
print(L100[10:20])  # 11到20数
print(L100[:10:2]) #前10个数每两个取一个
print(L100[::5]) #所有数每5个取一个
# 复制一个list
L_copy = L[:]
#tuple也是一个list，唯一的区别是tuple不可变
#tuple也可以进行切片操作，操作的结果仍为tuple

#字符串也可以看作一种list
print('ABCDEF'[0:3])




