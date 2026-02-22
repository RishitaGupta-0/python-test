# Simple Hello World program
print("Hello, World!")

# Simple calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Using the functions
num1 = 10
num2 = 5

print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")

# Simple list operations
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")