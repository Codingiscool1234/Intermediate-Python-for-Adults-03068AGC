#Basic data types

number=42  #integer
decimal=35.5 #float
name="Python"  #string
is_active=True #boolean

#type checking

# print(type(number)) #parathesis
# print(type(decimal))
# print(type(name))
# print(type(is_active))

#control structures - decision making
#conditional statments
age=25

# if age<18:
#     print("minor")
# elif age==18:
#     print("You are young")
# else:
#     print("You are an adult")

#comparision operators we have
#< , > , == , <= , >= , !=


#loops , for , while

# for i in range(1,6):
#     print("Hello")

#while loop
# count=0
# while count<=5:
#     print(count)
#     count=count+1 #count+=1


#functions

# def greet(name):
#     print("Hello "+name)  #concatenation is joining strings together using + operator

# greet("Asim") #parameter
# greet("Ali")
# greet("Sarah")


#Write a python program that takes a number and calculates the square of it

# def get_square(number):
#     print(number**2)

# while True:
#     number=int(input("Enter a number to get square or 0 to exit"))
#     if number==0:
#         break
#     get_square(number)

#list
numbers=[1,2,3,4,5,6]
#fruits=["banana","mango","cherry","grapes"]
mix_list=[1,"Sarah",True,3.14]

#accessing elements in list
# print(numbers[4])
# print(fruits)
#negative indexing
# print(numbers[-2])

#changing element in list
# print(numbers)
# numbers[3]=23
# print(numbers)

# numbers.append(7) #add 7 to the end
# print(numbers)

# brand_new_list=[]

# for i in range(5):
#     num=int(input("Enter number"))
#     brand_new_list.append(num)

# print(brand_new_list)

# #list methods
# fruits=["apple","banana","cherry"]

# #adding elements
# fruits.append("date") #add to the last
# fruits.insert(1,"apricot")
# print(fruits)

# #remove elements
# fruits.remove("banana")
# print(fruits)

# print(fruits)

#sort() , reverse() 

squares=[i**2 for i in range(10)]

# squares=[]
# for i in range(10):
#     squares.append(i**2)

print(squares)