class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')
# run() of subclass overlays the run() of superclass.


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


dog1 = Dog()
dog1.run()
cat1 = Cat()
cat1.run()

a = list()
b = Animal()
c = Dog()

isinstance(a, list)
isinstance(b, Animal)
print(isinstance(c, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())


class Timer(object):
    def run(self):
        print('Start...')


run_twice(Timer())
# Python is a dynamic language
# It looks like a duck, it walks like a duck, then it is a duck
