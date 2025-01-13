#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1.
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1).

# Read the input number from the command line arguments.
# Convert the input string to an integer and calculate its factorial.
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation.
print(f)

