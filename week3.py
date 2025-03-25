#error Handling try-except
# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

# try:
#     age=int(input("Enter your age"))
#     if age<0:
#         raise ValueError("Age cannot be negative")
#     elif age>120:
#         raise ValueError("Age should be less then 120")
# except ValueError as e:
#     print(f"Error : {e}")

# try:
#     age=int(input("Enter age"))
# except ValueError:
#     print("Please enter a valid integer")
# except ValueError as e:
#     print(e)
# else:
#     print(f"Your age is {age}")

# try:
#     #some code
#     file=open("example.txt",'r')
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()

#OOP - Object Oriented Programming
#Every class have two things
#1-Attributes
#2-functions

# class Dog:
#     #constructor
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def bark(self):
#         return "Woof!"

# my_dog=Dog("Buddy","Golden Retriever")
# print(my_dog.name)
# print(my_dog.bark())

# dog2=Dog("ABC","German Shefered")
# print(dog2.name)
# print(dog2.bark())

class BankAccount:
    def __init__(self,balance=0):
        if balance<0:
            raise ValueError("Balance cannot be negative")
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Desposited succesfully")
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("Wthdrawn amount")
    
    def check_balance(self):
        return self.balance
    



try:
    account=BankAccount(-10)
    account.withdraw(150)
    account.deposit(100)
    print(account.check_balance())
except ValueError:
    print("There is an error")