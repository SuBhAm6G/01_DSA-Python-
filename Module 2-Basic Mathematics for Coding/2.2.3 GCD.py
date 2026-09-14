"""
Problem: Array GCD
Given a list of positive integers, find the Greatest Common Divisor of the ENTIRE array.
The GCD of an array is the largest number that divides every single element in the array perfectly.
You must solve this in O(N log(min_value)) time using Python's built-in functions.

Example:
Input: arr = [24, 36, 48]
Output: 12 (12 divides 24, 36, and 48)

Input: arr = [33, 44, 55, 66]
Output: 11
"""
import math

def array_gcd(arr: list[int]) -> int:
    # Build your logic here
    return math.gcd(*arr) #*arr is called unpacking

if __name__ == "__main__":
    print(array_gcd([24, 36, 48]))      # Expected: 12
    print(array_gcd([33, 44, 55, 66]))  # Expected: 11
    print(array_gcd([7, 13, 21]))       # Expected: 1