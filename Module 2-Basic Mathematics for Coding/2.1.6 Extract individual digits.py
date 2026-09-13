"""
Problem: Replace Even Digits
Given an integer `n`, return a list of its digits in left-to-right order.
However, every even digit must be replaced by 0 in the final list.
You must use mathematical extraction (no string casting).

Example:
Input: n = 258
Extraction: 8 -> 5 -> 2
Transformation: 8 (even -> 0), 5 (odd -> 5), 2 (even -> 0)
Final left-to-right Output: [0, 5, 0]
"""

def replace_even_digits(n: int) -> list[int]:
    # Build your mathematical logic here
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        dgt = n % 10
        digits.append(0 if dgt%2 == 0 else dgt)
        n = n//10
    digits.reverse()
    return digits

if __name__ == "__main__":
    print(replace_even_digits(258))    # Expected: [0, 5, 0]
    print(replace_even_digits(135))    # Expected: [1, 3, 5]
    print(replace_even_digits(0))      # Expected: [0]