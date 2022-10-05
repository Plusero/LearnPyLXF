try:
    print('trying...')
    r = 10/2
    print('results', r)

except ZeroDivisionError as e:
    print('except:', e)

finally:
    print('finally...')
print('END')
print('\n********************************')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error!')
finally:
    print('finally...')
print('END')

print('********************************')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


main()

print('********************************')
# err.py:


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()
