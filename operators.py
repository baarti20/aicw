# Operators in general are used to perform opertaions on values and variables.

# # arithmetic
# a = 20
# b = 2

# print(a + b)  # addition
# print(a - b)  # subtraction
# print(a * b)  # multiplication
# print(a / b)  # division    
# print(a // b)  # floor division

#logical
# AND => condition => true => true
# a = 4
# b = 5
# c = 6
# print(b > a and c > b)

# OR => any condition is true, the output will be true.
# print(b > a or a > c) #true

#assignment
# a += 20 #=== a = a + 20
# a = a + 2
# print(a)

# Input() in Python
# In Python, Using the input() function, we take input from a user, and using the print() function, we display output on the screen.
# Using the input() function, users can give any information to the application in the strings or numbers format.

# num1 = input("Enter a num1 value: ")
# num2 = input("Enter a num2 value: ")    
# print (int(num1) + int(num2))

#if else condition:
# > based on the conditions if we have multiple statements , we can use if else condition.

#syntax:
#if condition:
#     true statement
# else condition:
#     false statement

# login with username and password

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "Frinda" and password == "12345":
#     print("Login successful")
# else:
#     print("Username or password is incorrect")


# Task 1 : Check whether the number is positive, negative or zero
print("1. Check whether the number is positive, negative or zero")
n1 =int (input("Enter a number: "))
if n1 > 0:
     print("The number is positive")
elif n1 < 0:
    print("The number is negative")
else:
    print("The number is zero")
print("-------------------------------------------------------------------------------------------------------")

# Task 2 : Check whether the number is even or odd
print("2. Check whether the number is even or odd")
n2 = int(input("Enter a number:"))
if n2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print("-------------------------------------------------------------------------------------------------------")    

# Task 3 : Check whether the person is eligible to vote or not
print("3. Check whether the person is eligible to vote or not")
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
print("-------------------------------------------------------------------------------------------------------")    


# Task 4 : Find the largest among three numbers
print("4. Find the largest among three numbers")
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:",num3)
print("-------------------------------------------------------------------------------------------------------")


# Task 5 : Ckeck whether the number is divisible by 5 or not
print("5. Check whether the number is divisible by 5 or not")
n5 = int(input("Enter a number:"))
if n5 % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
print("-------------------------------------------------------------------------------------------------------")

#Task 6 : Give grade based on marks
# Rules:
# 90 + : A+
# 80 - 89 : A
# 70 - 79 : B
# below 70 : C
print("6. Give grade based on marks")
marks = int(input("Enter your marks:"))
if marks >= 90:    
    print("Your grade is A+")
elif marks >= 80 and marks <= 89:
    print("Your grade is A")
elif marks >= 70 and marks <= 79:
    print("Your grade is B")
else:   
    print("Your grade is C")
print("-------------------------------------------------------------------------------------------------------")    

#Task 7 : Check whether the year is leap year or not
print("7. Check whether the year is leap year or not")
year = int(input("Enter a year: "))
if (year % 4 == 0):
    print("This is year is a Leap Year")
else:
    print("This is not a Leap Year")
print("-------------------------------------------------------------------------------------------------------")


#Task 8 : Check whether a number is multiple of both 3 and 5
print("8. Check whether a number is multiple of both 3 and 5")
n8 = int(input("Enter a number: "))
if n8 % 3 == 0 and n8 % 5 == 0:
    print("The number is a multiple of 3 and 5")
else:
    print("The number is not a multiple of 3 and 5")
print("-------------------------------------------------------------------------------------------------------")
