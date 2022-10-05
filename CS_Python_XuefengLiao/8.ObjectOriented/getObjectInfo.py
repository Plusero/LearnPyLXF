import types
print(type(123))
print(type('int'))
print(type(None))
print(type(abs))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))
print('ABC'.__len__())


class Dog(object):
    def __init__(self):
        pass

    def __len__(self):
        return 100


dog = Dog()
len(dog)

print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x**2


obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))
