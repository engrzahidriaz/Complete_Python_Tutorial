# list Comprehension 
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# square2 = [i**2 for i in range(1,11)]
# print(square2)

# print([-i for i in range(1,11)])

# names = ['zahid','shahid','Hadi']
# print([name[0] for name in names])

# my_list = ['abc','tuv','xuz']
# print([i[::-1] for i in my_list])

# new_list = [1,2,3,4,5,6,7,8,9]
# print([i for i in new_list if i%2 == 0])

# input_list = [1,2,3.0,4.5,'zahid','Hadi']
# print([i for i in input_list if type(i) == int or type(i) == float]) 

# nums = [1,2,3,4,5,6,7,8,9]
# print([i*2 if (i%2 == 0) else -i for i in nums])

# print([[i for i in range(1,4)] for j in range(3)])

# Dictionary Comprehension
# print({a:a**2 for a in range(1,11)})

# print({f"squar of {a} is" :a**2 for a in range(1,11)})

# string = "zahid riaz"
# print({i:string.count(i) for i in string})

# print({i:('even' if i%2 == 0 else 'odd') for i in range(1,11)})

# Sets Comprehension
# print({k**2 for k in range(1,11)})

# flexible functions

# def total(*args):
#     print(args)
# total(1,2,3,4,5)

# def total(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(total(1,2,3,4,5))

# def multiply(num, *args):
#     print(num)
#     print(args)
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi
# print(multiply(2,3,4))

# def multiplay(*args):
#     print(args)
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi
# num = [2,3,4]
# print(multiplay(*num))

# def power(num, *args):
#     if args: 
#         return [i**3 for i in args]
#     else:
#         return "you did\'t pass any args"
# nums = [1,2,3]
# print(power(2, *nums))

# kwargs (keyward arguments)
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func(first_name = 'zahid', last_name = 'riaz')

# def func(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
# func(first_name = 'zahid', last_name = 'riaz')

# def func(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
# d = {'name':'zahid','age':'31'}
# func(**d)

# def func(name, *args, new_name = "zahid", **kwargs):
#     print(name)
#     print(args)
#     print(new_name)
#     print(kwargs)
# func('Hadi',1,2,3,a=1,b=2)

# lambda expressions

# def add(a,b):
#     return a + b

# add1 = lambda a,b : a+b
# print(add(2,3))

# print(add)
# print(add1)

# even = lambda a : a%2 == 0
# print(even(4))

# last_char = lambda s : s[-1]
# print(last_char('zahid'))

# func = lambda l : True if len(l) > 5 else False
# print(func('zahidriaz'))

# func = lambda l : len(l) > 5
# print(func('zahidriaz'))

# Built=in functions

# names = ['zahid','Hadi','riaz']
# pos = 0
# for i in names:
#     print(f"{pos} ---> {i}")
#     pos += 1

# for pos,i in enumerate(names):
#     print(f"{pos} ---> {i}")

# l = ['zahid','riaz','Hadi','akbar']
# def find_pos(l,target):
#     for pos,i in enumerate(l):
#         if i == target:
#             return pos
#     return -1
# print(find_pos(l,'Hadi'))

# map functions

# numbers = [1,2,3,4]
# def square(a):
#     return a**2
# print([square(1),square(2),square(3),square(4)])

# print(list(map(square,numbers)))

# print(list(map(lambda a: a**2 ,numbers)))

# print([i**2 for i in numbers])

# numbers = [1,2,3,4]
# def square(a):
#     return a**2
# new_numbers = []
# for i in numbers:
#     new_numbers.append(square(i))
# print(new_numbers)

# filter functions

# def even(a):
    # return a%2 == 0
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(tuple(filter(even,numbers)))

# print(tuple(filter(lambda a: a%2==0, numbers)))

# print([i for i in numbers if i%2 ==0])

# iterator vs iterable

# numbers = [1,2,3,4,5]    # iterable
# print([i**2 for i in numbers]) # iterator
# print(map(lambda a: a**2, numbers)) # iterator

# number_inter = iter(numbers)
# print(next(number_inter))
# print(next(number_inter))
# print(next(number_inter))
# print(next(number_inter))

# zip functions

# user_id = ['user1','user2','user3']
# name = ['zahid', 'riaz','Hadi']
# print(list(zip(user_id,name)))

# print(dict(zip(user_id,name)))
# print(tuple(zip(user_id,name)))

# l = [(1,0),(3,4),(5,2),(7,8),(9,5)]
# print(list(zip(*l)))
# l1,l2 = list(zip(*l))
# print(l1)
# print(l2)

# l1 = [1,3,5,7,9]
# l2 = [0,4,2,8,5]
# new_list = []
# for i in zip(l1,l2):
#     new_list.append(max(i))
# print(new_list)

# def func(l1,l2):
#     avg = []
#     for i in zip(l1,l2):
#         avg.append(sum(i)/len(i))
#     return avg
# print(func([1,2,3],[4,5,6])) 

# def func(*args):
#     avg = []
#     for i in zip(*args):
#         avg.append(sum(i)/len(i))
#     return avg
# print(func([1,2,3],[4,5,6],[7,8,9])) 

# average = lambda *args: [max(i)/len(i) for i in zip(*args)]
# print(average([1,2,3],[4,5,6],[7,8,9])) 

# any and all function

# print(all([True,True,True])) # ---> True
# print(all([True,False,True])) # ---> False

# numbers1 = [2,4,6,8] # all even
# print(all([i%2 ==0 for i in numbers1]))

# numbers2 = [2,3,6,7] # any even
# print(any([i%2 ==0 for i in numbers2]))

# def my_sum(*args):
#     if all([(type(i) == int or type(i) == float) for i in args]):
#         total = 0
#         for i in args:
#             total += i
#         return total
#     else:
#         return "worng input"
# print(my_sum(1,2,3,4.5,'zahid',[1,3,5])) # ---> wrong
# print(my_sum(1,2,3,4,6)) # ---> sum

# min and max functions

# my_list = [1,2,3,4,5]
# print(max(my_list))
# print(min(my_list))

# names = ['zahid','riaz','AbdulHadi']
# def maximun(item):
#     return len(item)
# print(max(names, key = maximun))

# print(max(names, key = lambda i: len(i)))

# Sort functions
# fruits1 = ['grapes','mango','apple']
# fruits1.sort()
# print(fruits1)

# fruits2 = ('grapes','mango','apple')
# print(sorted(fruits2))

# fruits3 = {'grapes','mango','apple'}
# print(sorted(fruits3))

# cars = [
#     {'model':'tyota','price':'25000'},
#     {'model':'honda','price':'20000'},
#     {'model':'syzuki','price':'30000'}
# ]
# print(sorted(cars, key = lambda i: i['price']))
# print(sorted(cars, key = lambda i: i['price'], reverse = True))

# print(sum.__doc__)
# print(help(sum))