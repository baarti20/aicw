# what is Function?
# A function is a block of code that runs only when it is called.

# why use function?

# 1. Avoid repetition code
# 2. Makes program clean & organised.
# 3. easy to debug and reuse

#syntax
# def function_name():
#     #code to execute

#example:
# def greet():
#     print("hello students")

# greet() #calling the function

# greet() #calling the function
# -------------------------------------------------------------------------------------
# function with parameters:
# used to pass values

# def greet (name="student"):
#     print(f"hello {name}")

# greet()
# greet("shreyarth")
# greet("AICW")

# TASK 1: Calculator
def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

print("---- Calculator ----")
calc_n1 = float(input("Enter first number: "))
calc_n2 = float(input("Enter second number: "))
calc_op = input("Enter operator (+, -, *, /): ")
print("Result:", calculator(calc_n1, calc_n2, calc_op))
print("-------------------------------------------------------------------------------------------------------")

# TASK 2: Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("\n---- Even or Odd ----")
even_odd_num = int(input("Enter a number: "))
print(even_odd_num, "is", check_even_odd(even_odd_num))
print("-------------------------------------------------------------------------------------------------------")    


# TASK 3: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n---- Factorial ----")
fact_num = int(input("Enter a number: "))
print("Factorial is:", factorial(fact_num))
print("-------------------------------------------------------------------------------------------------------")


# TASK 4: Maximum of Three Numbers
def find_maximum(a, b, c):
    return max(a, b, c)

print("\n---- Maximum of 3 Numbers ----")
max_a = int(input("Enter first number: "))
max_b = int(input("Enter second number: "))
max_c = int(input("Enter third number: "))
print("Maximum is:", find_maximum(max_a, max_b, max_c))
print("-------------------------------------------------------------------------------------------------------")

# TASK 5: Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print("\n---- Palindrome Check ----")
palindrome_text = input("Enter a string: ")
if is_palindrome(palindrome_text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
print("-------------------------------------------------------------------------------------------------------")


# TASK 6: Area of Circle
def area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative"
    pi = 3.14159
    return pi * radius * radius

print("\n---- Area of Circle ----")
circle_radius = float(input("Enter radius: "))
print("Area is:", area_of_circle(circle_radius))
print("-------------------------------------------------------------------------------------------------------")
