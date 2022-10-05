def trim(s):
    if not isinstance(s, str):
        raise TypeError('bad operand type')
    for i in range(len(s)):
        if s[i] != " ":
            s_tmp = s[:i-1:-1]
            break
    for i in range(len(s_tmp)):
        if s_tmp[i] != " ":
            s_tmp2 = s_tmp[:i-1:-1]
            break
    return s_tmp2
print(trim('  good man  '))
#以上是+0的最初答案，一个非常面向过程的解法
#下面我们来试试面向对象的解法
def trim_ByWhile(s):
    if not isinstance(s, str):
        raise TypeError('bad operand type')
    while(s[:1]==' '):
        s = s[1:]
    while(s[-1:]==' '):
        s = s[:-1] #注意，这里的-1仅仅是一个位置标识，表示倒数第一个数，并不影响切片的顺序
    return s
print(trim_ByWhile('  Good Man  '))
