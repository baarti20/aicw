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


#task 1:
#Write a Python function to make calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division) based on user input. The function should take two numbers and an operator as parameters and return the result of the operation.
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


# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Output
print("Result:", calculator(num1, num2, op))

print("-----------------------------------------------------------------------------------")

#task 2
# Write a Python function to check if a number is even or odd :
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(number, "is", check_even_odd(number))
print("-----------------------------------------------------------------------------------")    
