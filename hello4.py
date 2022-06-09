# Decorators

# def square(a):
#     return a**2
# s = square
# print(s(7))
# print(s)
# print(square)
# print(s.__name__)

# def square(a):
#     return a**2
# l = [1,2,3,4]
# print(list(map(square,l)))

# print(list(map(lambda  a: a**2, l)))

# def my_map(func,l):
#     new_l = []
#     for i in l:
#         new_l.append(func(i))
#     return new_l
# print(my_map(square,l))

# def outer_func():
#     def inner_func():
#         print("inside inner function")
#     return inner_func()
# var = outer_func()

# def outer_func1(msg):
#     def inner_func1():
#         print(f"message is: {msg}")
#     return inner_func1
# var = outer_func1('hello')
# var()

# def to_pow(x):
#     def calc_pow(n):
#         return n**x
#     return calc_pow
# cube = to_pow(3)
# print(cube(5))

# def decorator_func(any_func):
#     def wrapper_fun():
#         print('this is awesome function')
#         any_func()
#     return wrapper_fun

# @decorator_func # this is shortcut
# def func1():
#     print('this is function 1')
# func1()

# def func2():
#     print('this is function 2')

# var = decorator_func(func2)
# var()

# def decorator_func(any_func):
#     def wrapper_fun(*args, **kwargs):
#         print('this is awesome function')
#         any_func(*args, **kwargs)
#     return wrapper_fun

# @decorator_func # this is shortcut
# def func(a):
#     print(f'this is function with argument {a}')
# func(7)

# def decorator_func(any_func):
#     def wrapper_fun(*args, **kwargs):
#         print('this is awesome function')
#         return any_func(*args, **kwargs)
#     return wrapper_fun

# @decorator_func # this is shortcut
# def func3(a,b):
#     return a + b
# print(func3(2,3))

# import time
# t1 = time.time()
# from functools import wraps
# def print_func_data(function):
#     @wraps(function)
#     def wrapper_func(*args, **kwargs):
#         print(f"you are calling {function.__name__} function")
#         print(f"{function.__doc__}")
#         return function(*args, **kwargs)
#     return wrapper_func

# @print_func_data
# def add(a,b):
#     ''' this take two numbers as arguments and return their sum'''
#     return a + b
# print(add(3,4))
# t2 = time.time()
# print(f"this function took {t2-t1} seconds")

# Generator

# l = [1,2,3] # iterable

# for i in l:
#     print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))

# for i in map(lambda a: a**2, l): #iterators
#     print(i)

# def nums(n):
#     for i in range(1,n+1):
#         print(i)
# nums(10)

# def nums(n):
#     for i in range(1,n+1):
#         yield(i)  # generator function

# for x in nums(10):
#     print(x)

# number = nums(10)
# for x in number:
#     print(x)

# for x in number:
#     print(x)

# def generator_func(n):
#     for i in range(0,n):
#         if i%2 == 0:
#              yield(i)
# for num in generator_func(10):
#     print(num)

# def generator_func(n):
#     for i in range(0,n,2):
#          yield(i)
# for num in generator_func(10):
#     print(num)

# generator comprehension

# square = [i**2 for i in range(1,11)]
# print(square)

# square = (i**2 for i in range(1,11)) # for generator
# for num in square:
#     print(num)





