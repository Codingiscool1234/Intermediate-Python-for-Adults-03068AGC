#Dictionaries
'''
Content
1.Creating and accesing dictionaries
2.common operations (add,remove , update)
3.Dictionary Comprehensions
'''

# #1
# student={"name":"Alex",
#          "age":25,
#          "grade":"A"
#          }
# empty_dict={}

# #accessing values
# print(f"Name: {student["name"]}")
# print(f"Age: {student.get("age")}")

# #modify dictionary values
# student["age"]=26
# student['course']="Python" #adding a new key-value pair
# del student['grade'] #remove key-value pair
# print(f"Updated Student: {student}")

# #Dictionary methods
# print(f"Keys : {student.keys()}") 
# print(f"Values : {student.values()}")
# print(f"Items : {student.items()}")

# #loop through the dictionary
# for key,value in student.items():
#     print(f"{key}:{value}")

# #Dictionary comprension
# squares_dictionary={x: x**2 for x in range(1,6)} #not recommended to use at this point
# print(squares_dictionary)


#Advanced Function Features
''''
Default and keyword arguments
variable length arguments
'''

# def greet(name):
#     return f"Hello, {name}"

# print(greet("Ali"))

# #Default arguements/parameter
# def greet_with_title(name,title='Mr./Ms.'):
#     return f"Hello, {title} {name}"

# print(greet_with_title("Abbas"))

# #keyword arguments
# def describe_person(name,age,job):
#     return f"{name} is {age} and works as {job}"

# print(describe_person(age=30,job="Engineer",name="Charlie"))


# #vairblae-length arguments
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1,2,3,4,5,6,3,2))

# #lambda with map
# number=[1,2,3,4]
# doubled=list(map(lambda x:x*2,number)) #anonymous function , which does not have a name
# print(doubled)

#Modules
''''
importing built-in modules (math) from python
create and use custom modules
'''

#using builting modules
from math import sqrt
print(f"Square root of 16: {sqrt(16)}")
# print(f"Pi: {math.pi}")

from random import randint
print(f"Random number : {randint(1,10)}") #random int between 1 and 10

#custome modules

import utils

number1=int(input("Enter number 1"))
number2=int(input("Enter number 2"))
print(f"Add : {utils.add(number1,number2)}")
print(f"Subtract : {utils.subtract(number2,number1)}")


