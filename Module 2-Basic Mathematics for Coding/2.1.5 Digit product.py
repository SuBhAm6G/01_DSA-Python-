"""
Problem: Subtract the Product and Sum of Digits of an Integer
Given an integer `n`, return the difference between the product of its digits and the sum of its digits.
Assume `n` is a positive integer greater than 0. 
**You must calculate both in a single pass (one while loop).**
No strings allowed.

Example:
Input: n = 234
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""
def prod(n: int) -> int:
    if n == 0:
        return 0
    res = 1
    while(n > 0):
        res *= n % 10
        n = n//10
    return res

def sum(n: int) -> int:
    if n == 0:
        return 0
    res = 0
    while(n > 0):
        res += n % 10
        n = n//10
    return res
def subtract_product_and_sum(n: int) -> int:
    # Build your one-pass mathematical logic here
    return prod(n) - sum(n)


if __name__ == "__main__":
    print(subtract_product_and_sum(234))   # Expected: 15
    print(subtract_product_and_sum(4421))  # Expected: 21 (32 - 11)