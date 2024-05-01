# This is a simple Python program that performs basic mathematical operations

# Printing "Hello, World!"
print("Hello, World!")

# Addition
print("Addition: ", 5 + 3)  # This will print: Addition: 8

# Subtraction
print("Subtraction: ", 10 - 6)  # This will print: Subtraction: 4

# Multiplication
print("Multiplication: ", 7 * 2)  # This will print: Multiplication: 14

# Division
print("Division: ", 8 / 2)  # This operation divides the first operand by the second operand and returns the quotient. For example, 8 / 2 returns 4.0. Note that division always returns a float in Python 3, even if the division is exact.

# Modulus
print("Modulus: ", 10 % 3)  # This operation divides the first operand by the second operand and returns the remainder. For example, 10 % 3 returns 1, because when 10 is divided by 3, the remainder is 1.

# Exponentiation
print("Exponentiation: ", 2 ** 3)  # This will print: Exponentiation: 8

# To run this program, save it as first_python_program.py and run it using the Python interpreter in your terminal:
# python3 first_python_program.py
# You should see the results of the mathematical operations printed in your terminal.

# Let's write an example of even odd with modulus
# This program takes a number as input from the user and checks if it is even or odd using the modulus operator. If the number is divisible by 2 with no remainder, it is even; otherwise, it is odd. The program then calculates the average of a list of numbers using the sum() and len() functions. The average is calculated by dividing the sum of the numbers by the total number of elements in the list. The result is printed to the console.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Calculate the average of a list of numbers.
numbers = [4, 2, 9, 3]
average = sum(numbers) / len(numbers)
print(f"The average is {average}")


def calculate_speed(distance, time):
    return distance / time

# Calculate the speed of a vehicle given the distance traveled and the time taken.
distance = 100  # km
time = 2  # hours
speed = calculate_speed(distance, time)
print(f"The speed is {speed} km/h")

