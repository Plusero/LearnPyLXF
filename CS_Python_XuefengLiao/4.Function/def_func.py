def my_abs(x):
    """[summary]

    Args:
        x ([type]): [description]

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-1))
print(my_abs(-5))
# print(my_abs('a'))
# for i in range(-5,6):
#     print(i)
#     print(my_abs(i))
