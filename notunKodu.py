
# _________________chap-01_________________
# import os
# print("Hello World")
# print(os.listdir())
# print("hello python")


# __________________chap02: var__________________
# a = "Ali "
# b = ''' Ali
# Neaz'''
# c = 415
# d = 42.25
# print(a, b, c, d)

# e = True
# f = False
# print(e, f)
# g = None
# print(type(g))

# h = type(a)
# print(h)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


# _____________________chap 3_____________________
# a = 34
# b = "Ali Neaz"
# print(a)
# print(b)
# c = "Ali's"
# print(c)
# d = ''' Ali's'''
# print(d)
# e = "Shakil"
# f = len(e)
# print(f)

# # slice
# name = "Ali neaz"
# print(name)
# print(type(name))
# greeting = "Good Morinin"
# c = greeting + " " + name
# print(c)


# # print(name[0:3])
# # print(name[::2])
# print(name[10])  # string index is out of range
# likes = 45
# # print(likes)
# likes = 10
# # print(likes)
# likes = 15
# print(likes, likes, likes)

# a = 45
# b = 25
# c = 78
# print(a, b, c)

# name = "Ali Neaz"
# # print(name[-1])

# print(name[::2])
# story = "Once upon a time there was a stupid little brat name Ali Neaz"
# print(len(story))
# print(story.capitalize())
# print(story.lower())
# print(story.find("Ali"))
# print(story.replace("Ali", "Neaz"))
# story2 = "Once upon a time there \' lived a tortoise name \\ hablu and he was not very happy"
# print(story2)


# letter
# letter = ''' Dear <|Name|>,
# You are selected! Greeting from ABC coding house,
# Have a great day ahed.
# data: <|Date|>
# '''

# name = input("Enter Your name :")
# date = input("Enter date :")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)

# print(letter)
# myList = []
# for i in range(5):
#     digit = int(input("enter a number: "))
#     myList.append(digit)

# myList.sort()
# sumL = sum(myList)
# print(sumL)

# _________________________chap five _________________________


# myDict = {
#     "name": "Ali Neaz",
#     "address": {
#         "vill": "jamgora",
#         "thana": "Ashulia",
#         "dist": "Dhaka"
#     },
#     "marks": [1, 2, 3, 4],
#     "age": "23",
#     "status": "single"

# }
# print(myDict)
# print(myDict.keys())
# print(myDict.values())
# print(myDict["name"])
# print(type(myDict))
# myDict['marks'] = [5, 6, 7, 8, 9]
# print(myDict["marks"])

# dictinay methods
# myDict = {
#     "fast": "IN a Quick Manner",
#     "neaz": "A Coder",
#     "marks": [1, 2, 3],
#     "age": 24,
#     "status": True,
#     "address": {  # nested dictionay
#         "vill": "kandail",
#         "thana": "ashulia",
#         "upozila": "savar",
#         "district": "Dhaka"
#     }
# }

# print(list(myDict.values()))
# print(list(myDict.keys()))

# upDate = {
#     "value": None,
#     "status": False
# }
# myDict.update(upDate)
# print(myDict)


# also get function to get something
# which won't print any type of errors

# sets
# a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5}
# a.add(10)
# a.add((11, 12, 13, 14))
# print(a)
# a.pop()
# print(a)
# myDict = {
#     "pakha": "fan",
#     "bakso": "box",
#     "lekha": "write",
#     "ekta": "a"
# }
# print(myDict.keys())
# b = input("Enter: ")

# print(myDict.get(b))
# num = int(input("enter number: "))
# s = set()
# for i in range(1, num+1):
#     s.add(i*num)
# # s.sort()
# print(s)


# a = None
# if a is None:
#     print("Yes")


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# num4 = int(input("Enter a number: "))

# if num1 > num2:
#     f1 = num1
# else:
#     f1 = num2
# if num3 > num4:
#     f2 = num3
# else:
#     f2 = num4

# if f1 > f2:
#     print(" is greatest", f1)
# else:
#     print("Num", f2)


# post = input("enter a post: ")
# if "ali" in post or "Ali" in post:
#     print("They are talking")
# else:
#     print("They ain't")


# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# fruits = ['brinjal', 'banana', 'apple', 'guava', 'pineapple', "mango", "grape"]

# for i in fruits:
#     print(i)


# chap seven problems
# num = int(input("Enter number: \n"))
# for i in range(1, 11):
#     print(f"{num}X{num*i}")

# num = int(input("Enter a number: \n"))

# print(f"table of {num} is : ")
# i = 1
# while i <= 10:
#     print(i*num)
#     i += 1

# prime = True
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break

# if prime:
#     print("this number is prime")
# else:
#     print("this numbe is not prime")


# print(12 % 5)
# num = int(input("Enter the number: "))

# # sum = (num*(num+1))/2
# # print(int(sum))
# sum = 0

# for i in range(1, num+1):
#     # sum = sum+i
#     sum += i

# print(sum)


# num = int(input("enter a number "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# # print(factorial)
# print(f"The factorial of this numbe is {factorial}")

# n = 3
# for i in range(3):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))

# n = 4  # take input
# for i in range(4):
#     print("*"*(i+1))

# n = 4
# for i in range(4):
#     print("*"*(i+1))


# n = 3
# for i in range(3):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))


# n = 4
# for i in range(4):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))

# n = 4
# for i in range(4):
#     print("*"*(2*i+1))

# chap eight
# def func(msg):
#     print(msg)

# import pandas as pd
# 10
# func("Hello world")


# def sum(a, b):
#     sum = a+b
#     return sum


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))


# print(sum(a, b))

# def defaultValue(name="Ali Neaz"):
#     print(name)


# # name = "Shamim"
# defaultValue()


# oops
# class Number:
#     def sum(self):
#         return self.a+self.b


# num = Number()
# num.a = 12
# num.b = 45
# sum = num.sum()
# print(sum)


# pd.DataFrame()

# import pandas as pd
# pd.DataFrame()
# class RailwayForm:
#     formType = "Railway Form"

#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")


# harrysApplication = RailwayForm()
# harrysApplication.name = "Harry"
# harrysApplication.train = "Rajdhani Express"
# harrysApplication.printData()


# class Remote():
#     pass


# class Player():
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass

#     def moveTop(self):
#         pass


# remote1 = Remote()
# player1 = Player()
# if (remote1.isLeftPressed()):
#     player1.moveLeft()


# class Employee:
#     comapny = "Google"
#     salary = 1240


# harry = Employee()
# rajni = Employee()
# harry.salary = 300
# rajni.salar = 400

# # print(harry.comapny)
# # print(rajni.comapny)
# Employee.comapny = "Youtube"
# print(harry.comapny)
# print(rajni.comapny)
# print(harry.salary)
# print(rajni.salary)


# class Employee:
#     company = "google"
#     salary = 100


# harry = Employee()
# rajni = Employee()

# harry.salary = 500

# print(rajni.salary)
# print(harry.salary)


# class Employee:
#     company = "Google"

#     def getSalary(self):
#         print(
#             f"Salary for this employee: {self.company} is salary { self.salary} ")


# harry = Employee()
# harry.salary = 5200
# harry.getSalary()


# class Emp:
#     company = "google"

#     def getSalary(self, signature):
#         print(
#             f"Salary for this employee working in {self.company} is{self.salary} \n{signature} ")

#     @staticmethod
#     def greet():
#         print("good Morning")

#     @staticmethod
#     def time():
#         print("The time is worng bro")


# harry = Emp()
# harry.salary = 555465
# harry.getSalary("Thanks")
# harry.greet()
# harry.time()


# class Emp:
#     company = "google"

#     def __init__(self, name, salary, subunit):
#         self.name = name
#         self.salary = salary
#         self.subunit = subunit
#         print("constructor created")

#     def getDetails(self):
#         print(f"{self.name} {self.salary} {self.subunit}")

#     @staticmethod
#     def greet():
#         print("Hello World")

#     @staticmethod
#     def time():
#         print("Hello time")


# harry = Emp("Harry", 561, "You tube")

# harry.getDetails()
# harry.greet()
# harry.time()


# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"{self.company} ")
#         print(f"{self.name} and {self.product} ")


# harry = Programmer("Harry", "skype")
# ali = Programmer("Ali", "github")
# harry.getInfo()
# ali.getInfo()


# class Calculator:
#     def __init__(self, num):
#         self.num = num

#     def sq(self):
#         print(f"value {self.num**2} ")

#     def sqR(self):
#         print(f"{self.num**0.5} ")

#     def cube(self):
#         print(f"{self.num**3} ")


# cal = Calculator(25)
# cal.sq()
# cal.sqR()
# cal.cube()


# class Sample:
#     a = "Harry"


# obj = Sample()
# obj.a = "Ali"
# print(Sample.a)
# print(obj.a)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # l2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # l3 = (1,2,3,4,5,6,7,8,9)

# i = 0
# while i < len(l1):
#     print(l1[i])
#     # print(l2[i])
#     # print(l3[i])
#     i += 1

# def sum(a, b):
#     sum = a+b
#     return sum


# print(sum(5, 20))
# print(sum(5, 251))
# print(sum(5, 2))
# print(sum(5, 1850))
# print(sum(5, 264))
# print(sum(5, 264))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)


# a = factorial(5)
# print(a)

# def sum(n):
#     sum = n*(n+1)/2
#     return sum


# a = sum(100)
# print(int(a))


# import os
# print(os.listdir())

# print('''Twinkel, twinkel, little star,
# How I wonder what you are!
# Up above the world so high,
# like a diamond in the sky.
# ''')
# from chapter six
# a = 1
# if a > 3:
#     print("The value of a is greater than 3")
# elif a < 3:
#     print("the value is less than 3")
# elif a < 3:
#     print("the value is less than 3")
# else:
# print("the value is null")
# b = False
# if b:
#     print("The statement is true")
# else:
#     print("the statement is false")

# n = 1
# for i in range(1, 11):
#     print(i*n)
#     n += 1


# age = int(input("Enter your age: \n"))
# if age >= 18 and age <= 60:
#     print("Your are okay to work here")
# elif age < 18:
#     print("You are under aged")
# else:
#     print("You are over aged")

# a = True
# if a is True:
#     print("Yes")
# else:
#     print("No way")
# l1 = [2, 3, 4]
# print(15 in l1)


# a = 6
# if a == 7:
#     print("TYes")
# elif a > 56:
#     print("no and yes")
# else:
#     print("I am optional")

# l1 = []
# for i in range(1, 10):
#     num = input("Enter a num or str: \n")
#     l1.append(num)

# print(l1)


# num1 = int(input("Enter num1: \n"))
# num2 = int(input("Enter num2: \n"))
# num3 = int(input("Enter num3: \n"))
# num4 = int(input("Enter num4: \n"))

# if num1 > num2:
#     f1 = num1
# else:
#     f1 = num2
# if num3 > num4:
#     f2 = num3
# else:
#     f2 = num4
# if f1 > f2:
#     print(f" {f1} is greatest of them all ")
# else:
#     print(f" {f2} is greatest of them all ")


# subject = []
# for i in range(1, 4):
#     num = int(input("Enter numbers \n"))
#     subject.append(num)

# if subject[0] < 33 or subject[1] < 33 or subject[2] < 33:
#     print("You faild cz one subject is less than 33 ")
# elif (subject[0]+subject[1]+subject[2])/3 < 40:
#     print("you failed cz your average is less than 40")
# else:
#     print("You passed and your marks is: ")
#     print(f"bangla: {subject[0]} ")
#     print(f"english: {subject[1]} ")
#     print(f"math: {subject[2]} ")


# text = input("Enter some text: \n")
# if "you are gay" in text:
#     print("They are talking about you my boy or gal")
# else:
#     print("They are not talking about you bad boy")


# spam = False
# if "make a lot of money" in text:
#     spam = True
# elif "buy now" in text:
#     spam = True
# elif "subscribe now" in text:
#     spam = True
# else:
#     spam = False


# if spam:
#     print("This text is spam")
# else:
#     print("This text is noton spam")


# mark = int(input("enter the marks: \n"))


# if mark > 100 or mark < 0:
#     print("You input is wrong")
# elif mark <= 100 and mark >= 90:
#     print("Excelent!")
# elif mark < 90 and mark >= 80:
#     print("Excelent A+!")
# elif mark < 80 and mark >= 70:
#     print(" B")
# elif mark < 70 and mark >= 60:
#     print("C")
# elif mark < 60 and mark >= 50:
#     print("D")
# elif mark < 50 and mark >= 40:
#     print("E")
# else:
#     print("Failed")
# chap:6 completed


# _________________chap :7_________________
# i = 0
# while i <= 10:
#     print("yes", str(i))
#     i += 1


# i = 2
# while i <= 50:
#     print(i)
#     i += 2


# fruites = ["banana", "komola", "amm", "jam", "kathal"]
# i = 0
# while i < len(fruites):
#     print(fruites[i])
#     i += 1
# print("***********done***********")
# for i in fruites:
#     print(i)

# for i in range(1, 8, 1):
#     print(i)
#     continue
# for i in range(1, 8, 2):
#     print(i)
#     break


# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print("This is inside else of for loop ")
# for i in range(10):
#     print(i)
#     # if i == 5:
#     #     continue
# else:
#     print("This is inside else of for loop ")


# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# i = 4


# def run(player):
#     pass


# def ouch(player):
#     pass


# if i > 0:
#     pass
# while i > 6:
#     pass
# print("Ali is a good boy ")


# num = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(f"{num}X{i}= {num*i}")


# l1 = ["Harry", "Sohan", "Sachin", "Rahul"]


# for names in l1:
#     print(names)


# num = int(input("Enter a number: "))

# prime = True
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break
# if prime:
#     print("This is a prime number")
# else:
#     print("not a prime number ")


# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# print(factorial)


# n = 4
# for i in range(n):
#     print("*"*(i+1))


# n = 4
# for i in range(n):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" ")


# _____________________chap:8_____________________

# def Percent(marks):
#     sum = 0
#     for i in range(len(marks)):
#         sum = sum+marks[i]
#         i += 1
#     percentage = (sum/len(marks))
#     return percentage


# marks1 = [90, 54, 78, 95, 68, 47, 15]
# marks2 = [90, 90, 90, 90, 90, 90, 90, 80, 10]
# percentage1 = Percent(marks1)
# percentage2 = Percent(marks2)
# # marks2 = [51, 54, 78, 95, 45, 15, 15]
# # percentage2 = Percent(marks2)
# print(percentage1)
# print(percentage2)


# ei problem ta niye pore vabte hobene
# def Percent(marks):
#     sum = 0
#     for i in range(len(marks)):
#         sum = sum(marks[i])
#         i += 1
#     percentage = (sum/len(marks))
#     return percentage


# student = Percent([80, 85, 95, 90, 98, 78, 45])
# print(student)


# def Greet(name):
#     print("Good Day sir,", name)


# def Sum(a, b):
#     return a+b


# def Name(a, b):
#     print(f"sum={a+b} ")


# Greet("Ali Neaz")
# s = Sum(12, 45)
# n = Name(12, 45)
# print(s)


# def greet(name="Plz write your name"):
#     return f"Hello! {name}"


# print(greet("Ali Neaz"))


# def Factorial(n="Plz enter a number"):
#     product = 1
#     for i in range(n):
#         product = product*(i+1)
#     return product


# f = Factorial(5)
# print(f)


# def Factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*Factorial_recursive(n-1)


# num = int(input("Enter a number "))
# g = Factorial_recursive(num)
# print(g)


# def __maximum__(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c


# num = __maximum__(20, 30, 40)
# print(num)


# def __maximum__(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c


# value = __maximum__(50, 20, 100)
# print(value)

# def fah(cel):
#     fah = (cel*(9/5))+32
#     return fah


# f = fah(38)
# print(f)


# print("Hello one ", end="")
# print("Hello one ", end="")
# print("Hello one ", end="")
# print("Hello one")


# def sumation(n):
#     su
#     sumAll = n+sumation(n-1)
#     return sumAll


# s = sumation(100)
# print(s)


# n = 5
# for i in range(5):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))


f = open("sample.txt", "w")
value = f.write("Hello dear")
f.close()

# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
