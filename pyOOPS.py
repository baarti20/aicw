#What is Object Oriented Programming?
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. It allows for the creation of reusable code and promotes modularity, making it easier to manage and maintain complex software systems.  

# Key Concepts of OOP:
# 1. Class: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
# Creating an object of the Student class
student1 = Student("Aarti", 20) 
print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("-------------------------------------------------------------------------------------------------------")


# 2. Object: An instance of a class. It is a specific realization of the class with actual values for the attributes defined in the class.  
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
# Creating an object of the Student class
student1 = Student("Aarti", 20) 
print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("-------------------------------------------------------------------------------------------------------")


# 3. Inheritance: A mechanism where a new class (called a child or subclass) can inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and allows for the creation of a hierarchical relationship between classes.  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Inherit attributes from Person
        self.student_id = student_id  # Additional attribute for Student
# Creating an object of the Student class
student1 = Student("Aarti", 20, "S12345")   
print("Student Name:", student1.name)  # Inherited from Person
print("Student Age:", student1.age)    # Inherited from Person
print("Student ID:", student1.student_id)  # Specific to Student
print("-------------------------------------------------------------------------------------------------------")    


# 4. Encapsulation: The bundling of data (attributes) and methods that operate on the data into a single unit (class). It also restricts direct access to some of the object's components, which can prevent accidental modification of data.   
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    def get_name(self):
        return self.__name  # Getter method for name
    def get_age(self):
        return self.__age   # Getter method for age 
# Creating an object of the Student class
student1 = Student("Aarti", 20)     
print("Student Name:", student1.get_name())  # Accessing private attribute via getter   
print("Student Age:", student1.get_age())    # Accessing private attribute via getter   
print("-------------------------------------------------------------------------------------------------------")


# 5. Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface. It allows for methods to be used on objects of different classes, even if they implement those methods differently.
class Animal:
    def speak(self):
        pass  # Abstract method 
class Dog(Animal):
    def speak(self):
        return "Woof!"  # Dog's implementation of speak method
class Cat(Animal):
    def speak(self):
        return "Meow!"  # Cat's implementation of speak method 
# Creating objects of Dog and Cat classes
dog = Dog()     
cat = Cat()  # Creating objects of Dog and Cat classes  
print("Dog says:", dog.speak())  # Output: Dog says: Woof!
print("Cat says:", cat.speak())  # Output: Cat says: Meow!   
print("-------------------------------------------------------------------------------------------------------")


# 6. Constructors:  (__init__ method)
# A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.    
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Creating an object of the Student class
student1 = Student("Aarti", 20) 
print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("-------------------------------------------------------------------------------------------------------")


# 7. Methods: Functions defined within a class that operate on the attributes of the class. They can perform operations on the data and provide functionality to the objects created from the class.
class Student:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
    def display_info(self):  
        print(f"Name: {self.name}, Age: {self.age}")
# Creating an object of the Student class
student1 = Student("Aarti", 20) 
student1.display_info()  # Output: Name: Aarti, Age: 20
print("-------------------------------------------------------------------------------------------------------")    

#task 1: Create a class "Car" with constructor to initialize brand and method "drive" to print "Driving a {brand} car.".
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"Driving a {self.brand} car.")

# Creating an object of the Car class
my_car = Car("Toyota")
my_car.drive()  # Output: Driving a Toyota car.
print("-------------------------------------------------------------------------------------------------------")

# Task 2: Create a class "Employee" with constructor to initialize first_name , last_name, age, role, salary and method "work" to print "{first_name} {last_name} is working as a {role} , with salary {salary}.".
class Employee:
    def __init__(self, first_name, last_name, age, role, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role
        self.salary = salary

    def work(self):
        print(f"{self.first_name} {self.last_name} is working as a {self.role}, with salary ${self.salary}.")

# Creating an object of the Employee class
employee1 = Employee("John", "Doe", 30, "Software Engineer", 80000)
employee1.work()  # Output: John Doe is working as a Software Engineer, with salary $80000.
print("-------------------------------------------------------------------------------------------------------")
