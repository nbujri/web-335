"""
  title: bujri_calculator.py
  author: ngi bujri
  date: april 1 2023
  description: simple calculator app
"""

# return result of add two numbers
def add(a, b):
    return f"{a} + {b} is {a + b}"

# return result of subtracting two numbers
def subtract(a, b):
    return f"{a} - {b} is {a - b}"

# return result of dividing two numbers
def divide(a, b):
    return f"{a} / {b} is {a / b}"

# return result of multiplying two numbers
def multiply(a, b):
    return f"{a} * {b} is {a * b}"

# print results
print(add(4, 4))
print(subtract(10, 6))
print(divide(8, 2))
print(multiply(10, 2))