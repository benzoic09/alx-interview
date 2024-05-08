#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    if n <= 1:
        return 0
    # Initialize the number of operations
    operations = 0
    # Start with the smallest prime factor
    factor = 2
    while n > 1:
        # Check if the current factor divides n
        if n % factor == 0:
            # Add the current factor to the operations
            operations += factor
            # Divide n by the factor
            n //= factor
        else:
            # If the current factor doesn't divide n, increment it
            factor += 1
    return operations
