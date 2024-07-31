from app2 import add, divide, multiply, subtract


def operate(func, a, b):
    return func(a, b)

# Test the higher-order function with different operations
print(operate(add, 10, 5))         # Expected output: 15
print(operate(subtract, 10, 5))    # Expected output: 5
print(operate(multiply, 10, 5))    # Expected output: 50
print(operate(divide, 10, 5))      # Expected output: 2

