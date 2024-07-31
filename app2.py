def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test the functions
print(add(10, 5))         # Expected output: 15
print(subtract(10, 5))    # Expected output: 5
print(multiply(10, 5))    # Expected output: 50
print(divide(10, 5))      # Expected output: 2
print(divide(10, 0))      # Expected output: Error: Division by zero
