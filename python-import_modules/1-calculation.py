#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("Addition: {} + {} = {}".format(a, b, add(a, b)))
print("Subtraction: {} - {} = {}".format(a, b, sub(a, b)))
print("Multiplication: {} * {} = {}".format(a, b, mul(a, b)))
print("Division: {} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    pass
