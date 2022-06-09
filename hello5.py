# OOP Classes

# class Person:
#     def __init__(self, first_name, last_name, age):
#         print('init method // constractor get called')
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('zahid', 'riaz',31)
# p2 = Person('abdul','Hadi',2)

# print(p1.first_name)
# print(p2.first_name)

# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
# p1 = Laptop('dell','gf1',15000)
# p2 = Laptop('hp','gp2',25000)
# print(p1.model_name)
# OOP instance method

# l = [1,2,3]
# l.pop()

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name}  {self.last_name}"
#       def above_18(self):
#           return self.age > 18

# p1 = Person('zahid', 'riaz',31)
# print(p1.full_name()) # similarly l.pop()
# Person.full_name(p1)  # similarly list.append(l,10)
# print(p1.above_18())

# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def discount(self,num):
#         return self.price - (num/100)*self.price

# p1 = Laptop('dell','gf1',15000)
# print(p1.discount(10))

# class variable

# class Circle:
#     def __init__(self, radius, pi):
#         self.radius = radius
#         self.pi = pi
#     def circum(self):
#         return 2*self.pi*self.radius

# c1 = Circle(4, 3.14)
# c2 = Circle(5, 3.14)
# print(c1.circum())

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def circum(self):
#         return 2*Circle.pi*self.radius

# c1 = Circle(4)
# c2 = Circle(5)
# print(c1.circum())

# class Laptop:
#     discount_per = 10
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def discount(self):
#         return self.price - (Laptop.discount_per/100)*self.price

# p1 = Laptop('dell','gf1',15000)
# print(p1.discount())

# class Laptop:
#     discount_per = 10
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def discount(self):
#         return self.price - (self.discount_per/100)*self.price

# p1 = Laptop('dell','gf1',15000)
# p2 = Laptop('apple','macbook',55000)
# p2.discount_per = 50
# print(p2.__dict__)
# print(p2.discount())

# OOP Class Methods

# class Person:
#     count_instance = 0
#     def __init__(self, first_name, last_name, age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     @classmethod   # take class as argument
#     def count_instances(cls):
#         return f"you have created {cls.count_instance} of person class"

#     @staticmethod   # take nothing as argument
#     def hello():   
#         print('hello, static method called')

#     def full_name(self):
#         return f"{self.first_name}  {self.last_name}"
#     def above_18(self):
#         return self.age > 18

# p1 = Person('zahid', 'riaz', 31)
# p2 = Person('amjad', 'hussain', 32)
# print(Person.count_instances()) 

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = price
    
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}")

#     def full_name(self):
#         print(f"{self.brand} {self.model_name}")

# phone1 = Phone('nokia', '1100', 1000)
# print(phone1._price)
# print(phone1.__dict__)

# _name # convention of private name
# __name # name mangling
# __init__ # dunder

# l = [4,3,1,2]
# l.sort() # tim sorting
# print(l)

# Class Inheritance

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = price
    
#     def make_a_call(self, phone_number):
#         return f"calling {phone_number}"

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"

# class Smartphone(Phone):
#     def __init__(self, brand, model_name, price, ram, rear_camera):
#         Phone.__init__(self, brand, model_name, price) 
#         self.ram = ram
#         self.rear_camera = rear_camera
    
#     def full_name(self):
#         print(f"{self.brand} {self.model_name} and price is {self._price}")

# class FlagshipPhone(Smartphone):
#     def __init__(self, brand, model_name, price, ram, rear_camera, front_camera):
#         super().__init__(brand, model_name, price, ram, rear_camera)
#         self.front_camera = front_camera
        
#         def full_name(self):
#             print(f"{self.brand} {self.model_name} and price is {self._price} and {self.front_camera}")

# phone1 = Phone('nokia', '1100', 1000)
# smartphone = Smartphone('oneplus', '5', 30000, '6 gb', '32 MP')
# oneplus = FlagshipPhone('oneplus', '5', 30000, '6 gb', '32 MP', '16 MP')
# print(smartphone.full_name())
# help(Smartphone)
# print(oneplus.full_name())
# help(FlagshipPhone)

# OOP multiple Classes

# class A:
#     def class_a_method(self):
#         return "i\'m just a class A method"
#     def hello(self):
#         return 'hello from class A'

# class B:
#     def class_b_method(self):
#         return "i\'m just a class B method"
#     def hello(self):
#         return 'hello from class B'

# class C(A,B):
#     pass

# instance_c = C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
# print(help(C))
# print(C.__mro__)

