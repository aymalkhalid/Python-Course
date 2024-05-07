# 01_variables.py

# Declaration and assignment of variables
# A variable in Python is created the moment you first assign a value to it.
message = "Hello, Python learner!"
print(message)  # Output: Hello, Python learner!

# Rules and best practices for naming variables in Python
# Variable names should be descriptive, without being too long or too short.
# They should be in lowercase, with words separated by underscores.
# They should not start with a number or contain any special characters, except for the underscore.
student_name = "John Doe"
student_age = 20
print(student_name, student_age)  # Output: John Doe 20

# Assigning values to multiple variables at once
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)  # Output: Orange Banana Cherry

# Local, nonlocal, and global variables
# A variable declared inside a function is local to that function and can't be accessed outside of it.
def myfunc():
    local_var = "I'm local!"
    print(local_var)  # Output: I'm local!

myfunc()

# A global variable can be accessed from anywhere in the code, both inside and outside of functions.
global_var = "I'm global!"

def print_global():
    print(global_var)  # Output: I'm global!

print_global()

# Constants in Python
# Python doesn't have built-in constant types, but it's a common practice to create a constant by using an all-uppercase variable name.
PI = 3.14159
print(PI)  # Output: 3.14159