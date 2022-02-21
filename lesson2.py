def my_func(a, b, /):
    return a * b


def grav_force(m, *, g=9.8):
    return m * g


print(grav_force(10, g=10))

p = ('asd', 4)


# print(my_func('asd', 5))
# print(my_func('asd', 5))

def square(n):
    return n * n


def map_f(lst):
    res = []
    for i in lst:
        res.append(square(i))
    return res


# print(map_f([1, 2, 3]))
map_iterator = map(lambda x: x ** 2, list(range(3)))

print(map_iterator)
# print(map_iterator.__next__())
# print(map_iterator.__next__())
# print(map_iterator.__next__())
# next(map_iterator)
# print(map_iterator.__next__())
print(list(map_iterator))

# map_iterator_2 = map(lambda x,y:x*y, (1,2,3), (4, 5, 6))
# print(list(map_iterator_2))

lst = ['asd', 'aaaaa', 'yyyyyy']
print(list(map(len, lst)))

dirty_list = ['a', 1, [1, 2, 3], ('b', 'c'), False]
filtered_obj = filter(lambda x: type(x) == int, dirty_list)
print(filtered_obj)
print(list(filtered_obj))

# v = False
# print(type(v))
# print(isinstance(v, int))
# print(type(v) == int)


'''generators'''
import sys

range_limit = 10000
lst = [i for i in list(range(range_limit))]
gen = (i for i in list(range(range_limit)))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))


# for i in gen:
#     print(i)


def my_gen(limit):
    k = 0
    while k < limit:
        k += 1
        if k % 2 == 1:
            yield k


my_gen_res = my_gen(4)
# print(my_gen_res.__next__())
# print(my_gen_res.__next__())
# print(my_gen_res.__next__())
# print(type(my_gen_res))

# print(my_gen_res.__next__())
# print(my_gen_res.__next__())
# print(my_gen_res.__next__())
# print(my_gen_res.__next__())
# print(my_gen_res.__next__())


'''input/output'''
'''modes
r - readonly
w - writeonly
r+ - read and write
w+ - read and write
x - create
a - append
'''

# file = open('test.txt', 'r')
# file.write('this is first line \n')
# file.write('this is second line \n')
# file.close()


# file = open('test.txt', 'r')
# lines = file.readline()
# print([i for i in lines])
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# with open('test.txt', 'r') as f:
#     print(f.readline())

'''function scopes'''
a = []


def myFunc():
    # global a
    a = [1, 2]
    print(a)


myFunc()
print(a)


#
# def outer_function(msg):
#     message = msg
#     def inner_function():
#         print(message)
#     return inner_function


# inner_func = outer_function('hello world')
# inner_func()
# print(type(inner_func))

# def display_info():
#     print('info')
#
# def outer_function(func):
#     def inner_function():
#         print('before run')
#         func()
#     return inner_function


def timer(func):
    import time
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('this function run take {} sec'.format(end - start))

    return wrapper


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# @my_logger
# def square(x):
#     import time
#     time.sleep(2)
#     return x ** 2


@my_timer
@my_logger
def my_sum(a, b):
    return a + b


print(my_sum(4, 6))

'''recursion'''


def factorial(n):
    res = n
    for i in range(1, n):
        res *= i
    return res


def factorial_rec(n):
    if n < 0:
        raise TypeError()
    if n == 1:
        return n
    return n * factorial_rec(n - 1)


from functools import lru_cache


# @lru_cache


# print(factorial(8))
# print(fibonacci_numbers(40))
# print(2 **40)

def my_timer_with_arg(format='s'):
    def my_timer_wrapper(orig_func):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            if format == 'ms':
                print('{} ran in: {} ms'.format(orig_func.__name__, t2 * 1000))
            else:
                print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result

        return wrapper

    return my_timer_wrapper


@my_timer_with_arg
def fibonacci_numbers_wrapper(n):
    return fibonacci_numbers(n)


@my_timer_with_arg
def my_upper(n):
    return n.upper()


def fibonacci_numbers(n):
    if n < 2:
        return 1
    return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)


print('=' * 100)
fibonacci_numbers_wrapper('34')
my_upper(134)


