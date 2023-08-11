#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    """
    A simple calculator program that demonstrates basic arithmetic operations.

    This program imports functions to add, subtract, multiply, and divide
    from the calculator_1 module and uses them to perform arithmetic operations
    on two numbers.

    The program calculates the result of adding, subtracting, multiplying, and
    dividing two numbers (a and b) and prints the results.

    Args:
	None

    Returns:
	None
    """
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")

if __name__ == "__main__":
    main()
