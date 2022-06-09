# print("hello friends")   

# print('hello friend')

# print("this is \\\\ double backslash")

# print("these are /\\/\\/\\/\\/\\ mountains")

# print('he is \t awesome')


# print('\\\" \\\' \\t \\n')

# print(r"he is \t awesome")

# print("\U0001F600")
# print("\U0001F61B")
# print(2*3)
# print(2**3)
# print(2**.5)
# print(round(2**.5, 4))
# a = 3
# print(a)

# print("zahid" + str(123))

# name = input("what is your name:")

# print(name)

# number = int(input("enter number"))

# mother_age = int(input("my mother age is:"))
# father_age = int(input("my father age is:"))
# my_age = int(input("my age is:"))
# print((mother_age + father_age + my_age)/3)
# city = input("in which city are you live?")
# print(f"reverse order {city[::-1]}")
# print("zAhId".count("h"))

# winning_num = 10
# guss_num = int(input("the wininng number is:"))
# if guss_num == winning_num:
#    print("you win !!!")
# elif guss_num < winning_num:
#     print("lower number")
# else:
#    print("upper number")

# sum = 1
# k = 0
#while k <=10:
 #   sum = sum + k
  #  k = k + 1
   # print(sum)

# while_loop
# Num = input("enter the numbers: ")
# sum = 0
# k = 0
# while k < len(Num):
#    sum += int(Num[k])
#    k += 1
# print(sum)

# name = input("enter your name: ")
# temp_var = ""
# k = 0
# while k < len(name):
#    if name[k] not in temp_var:
#        temp_var += name[k]
#        print(f"{name[k]} : {name.count(name[k])}")
#    k +=1

# for_loop
# sum = 0
# for k in range(1,11):
#    sum += k
# print(sum)

# num = input("enter the number: ")
# sum = 0
# for k in range(0, len(num)):
#    sum += int(num[k])
# print(sum)

# Alternate_method
# num = input("enter the number: ")
# sum = 0
# for k in num:
#    sum += int(k)
# print(sum)

# import random
# winning_number = random.randint(0,100) 
# print(winning_number)

# for k in range(1,11,2):
#     print(k)

# for k in range(11,0,-1):
#     print(k)

# for k in "zahid":
#     print(k)

# functions

# def add_two(a,b):
#     return a + b
# print(add_two(3,4))
# print(add_two("zahid"," Riaz"))

# def char(name):
#     return name[0] 
# print(char("zahid"))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(odd_even(8))

# alternative_method
# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"
# print(odd_even(8))

# alternative_method_2
# def odd_even(num):
#     return num%2 == 0
# print(odd_even(9))

# def song():
#     return "happy birthday song"
# print(song())

# def greater_num(a,b):
#     if a>b:
#         return a
#     return b
# bigger = greater_num(3,6)
# print(f"{bigger} is greater")

# any_word = input('palimdrome: ')
# def is_palimdrome(word):
#       return word == any_word[::-1]
# print(is_palimdrome(any_word))

# def my_name(name = "zahid"):
#    print(name)
# my_name()

# def my_name(name = "zahid"):
#    return name
# print(my_name())

# List
# fruits = ['mango','apple','graps']
# fruits.append('banana')
# print(fruits)
# print(fruits[1:-1])

# add --> append , extend, insert
# delete --> pop, remove, del
# few methods --> sort, sorted, clear, copy
# compare --> == , is

# fruits = ['mango','apple','graps','banana','kiwi']
# for fruit in fruits:
#    print(fruit)

# fruit = 0
# while fruit < len(fruits):
#    print(fruits[fruit])
#    fruit += 1

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1])
# print(matrix[1][1])

# for sublist in matrix:
#    for i in sublist:
#       print(i)

# numbers = list(range(1,11))
# print(numbers)
# numbers.pop()
# print(numbers.pop())
# print(numbers)

# def nagitive_number(l):
#    nagitive = []
#    for i in l:
#       nagitive.append(-i)
#    return nagitive
# print(nagitive_number(numbers))

# my_list = [1,2,3,4,5]
# def squre_num(l):
#    square = []
#    for i in l:
#       square.append(i**2)
#    return square
# print(squre_num(my_list))

# my_list = [1,2,3,4,5]
# def reverse_num(l):
#    reverse = []
#    for i in range(len(l)):
#       popped_item = l.pop()
#       reverse.append(popped_item)
#    return reverse
# print(reverse_num(my_list))

# alternate_method_1
# def reverse_num(l):
#    return l[::-1]
# print(reverse_num(my_list))

# alternate_method_2
# def reverse_num(l):
#    l.reverse()
#    return l
# print(reverse_num(my_list))

# new_list = ['abc','tuv','xyz']
# def reverse_elements(l):
#    elements = []
#    for i in l:
#       elements.append(i[::-1])
#    return elements
# print(reverse_elements(new_list))

# list1 = [1,2,3,4,5,6,7,8,9]
# def even_odd(l):
#    even = []
#    odd  = []
#    for i in l:
#       if i%2 == 0:
#          even.append(i)
#       else:
#          odd.append(i)
#    return [even] + [odd]
# print(even_odd(list1))

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# def commen(l1,l2):
#    commen_list = []
#    for i in l1:
#       if i in l2:
#          commen_list.append(i)
#    return commen_list
# print(commen(list1,list2))

# def sublist(l):
#    count = 0
#    for i in l:
#       if type(i) == list:
#          count += 1
#    return count
# mixed = [[2,3],4,6,[7,8]]
# print(sublist(mixed))