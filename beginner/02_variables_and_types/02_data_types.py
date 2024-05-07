# 02_data_types.py

# Different types of data that Python can handle
integer = 10
floating_point = 20.5
complex_number = 3+5j
string = "Hello, Python learner!"
boolean = True
none_type = None

# Python's numeric, sequence, mapping, set, boolean, and None data types
numeric = 123
sequence = [1, 2, 3]
mapping = {"name": "John", "age": 20}
set_type = {1, 2, 3}
boolean = False
none_type = None

# Truthy and falsy values
truthy = bool(1)  # True
falsy = bool(0)  # False

# Boolean and comparison operators
is_equal = 5 == 5  # True
is_not_equal = 5 != 5  # False

# Data type conversion
integer_to_string = str(100)  # '100'
string_to_integer = int("100")  # 100

# String formatting methods
formatted_string = "Hello, {}".format("John")  # "Hello, John"

# Type annotations in Python
def greet(name: str) -> str:
    return "Hello, " + name

# Mutable vs immutable types
mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)

# 'is' vs '==' operators
list1 = list2 = [1, 2, 3]
print(list1 is list2)  # True
print(list1 == list2)  # True

# Binary and bitwise operations
binary_and = 5 & 3  # 1
binary_or = 5 | 3  # 7

# Handling of Unicode and byte data by Python
unicode_char = "\u0030"  # '0'
byte_data = b"Hello"

# Dynamic Typing in Python
dynamic_var = "Hello"
dynamic_var = 123

# Duck Typing in Python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def quack_it(obj):
    print(obj.quack())

duck = Duck()
person = Person()

quack_it(duck)  # "Quack!"
quack_it(person)  # "I'm quacking like a duck!"