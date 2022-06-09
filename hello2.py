# Tuples:

# mixed = (1,2,3,4.0,"Hadi")
# for i in mixed:
#     print(i)

# i = 0
# while i <= len(mixed):
#     print(mixed[i])
#     i = i + 1

# nums = (1,)
# words = ('word',)
# fruits = 'banana','apple',"pear"
# print(type(fruits))

# friends = ('zahid',['sohaib','qaiser'])
# friends[1].pop(1)
# friends[1].append("faizan")
# print(friends)

# mixed = (1,2,3,4.0)
# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))

# def func(int1,int2):
#     add = int1 + int2
#     multi = int1 * int2
#     return add, multi
# # print(func(2,3))
# add, multi = func(2,3)
# print(add)
# print(multi)

# num_tuple = tuple(range(1,11))
# num_list = list(range(1,11))
# print(num_tuple)
# print(num_list)

# list_tuple = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(list_tuple)
# tuple_str = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(tuple_str)
# print(type(tuple_str))

# Dictionaries:

# user = dict(name = 'zahid',age = 31)
# print(user) # output --> {'name': 'zahid', 'age': 31}
# print(user['name'])

# user1 = ['zahid', 31, ['coco','kimi no na wa'], ['awakening','fairy tale']]

# user_info1 = {}
# user_info1['name'] = 'zahid'
# user_info1['age'] = 31
# print(user_info1)

# user_info = {
#     'name' : 'zahid',
#     'age' : 31,
#     'fav_mov' : ['coco','kimi no na wa'],
#     'fav_tune' : ['awakening','fairy tale']
# }
# print(user_info['age'])

# if 'name' in user_info(): # keys
#     print('present')
# else:
#     print('not present')

# if 'zahid' in user_info.values(): # values
#     print('present')
# else:
#     print('not present')

# for i in user_info: #keys
#     print(i)

# for i in user_info.values(): # values
#     print(i)

# for i in user_info:
#     print(user_info[i]) # values

# print(user_info.values())
# print(type(user_info.values()))

# print(user_info.keys())
# print(type(user_info.keys()))

# print(user_info.items())
# print(type(user_info.items()))

# for i, j in user_info.items():
#     print(f"key is: {i}, value is: {j}")

# user_info = {
#     'name' : 'zahid',
#     'age' : 31,
#     'fav_mov' : ['coco','kimi no na wa'],
#     'fav_tune' : ['awakening','fairy tale']
# }

# user_info['fav_song'] = ['song1','song2']
# print(user_info)

# user_info.pop('fav_tune')
# print(user_info)

# user_info.popitem() # random remove 
# print(user_info)
# popped_item = user_info.popitem()
# print(popped_item)

# user_info = {
#     'name' : 'zahid',
#     'age' : 31,
#     'fav_mov' : ['coco','kimi no na wa'],
#     'fav_tune' : ['awakening','fairy tale']
# }
 
# more_info = {'name':'zahid riaz','state':'Multan','hobby':['reading','coding']}
# user_info.update(more_info)
# print(user_info)

# my_dict = dict.fromkeys(['name','age','height'],'unknown')
# print(my_dict)

# my_dict = dict.fromkeys('abc','unknown')
# print(my_dict)    

# my_dict = dict.fromkeys(range(1,5),'unknown')
# print(my_dict)

# new_dict = {'name': 'zahid', 'age': '31', 'height': '6.7'}
# print(new_dict['names'])

# print(new_dict.get('names')) # get use to access keys

# if new_dict.get('name'): # instead of (if 'name' in new_dict:)
#     print("present")
# else:
#     print('not present')

# new_dict.clear()
# print(new_dict)

# new_dict1 = new_dict.copy() # not equal to (new_dict1 = new_dict)
# print(new_dict1)

# def cube_finder(n):
#     cube_dict = {}
#     for i in range(1,n+1):
#         cube_dict[i] = i**3
#     return cube_dict
# print(cube_finder(5))

# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count
# print(word_counter('zahidriaz'))

# name = input('what is your name: ')
# age = int(input('what is your age: '))
# city = input('what is your home town: ')
# fav_colors = input('what are your favorite colors: ').split(',')
# fav_fruites = input('what is your favorite fruites: ').split(',')
# my_dict = {}
# my_dict['name'] = name
# my_dict['age'] = age
# my_dict['city'] = city
# my_dict['fav_colors'] = fav_colors
# my_dict['fav_fruites'] = fav_fruites
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

# Set

# s = {1,2,3,4}
# print(s)
# l = [1,1,2,2,2,3,3,4,5,6,6,6,7,7,8]
# s1 = set(l)
# print(s1)

# s.add(5)
# s.remove(4)
# s.discard(6)
# print(s)

# s2 = s.copy()
# print(s2)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1 | s2) # union
# print(s1 & s2) # intersation

