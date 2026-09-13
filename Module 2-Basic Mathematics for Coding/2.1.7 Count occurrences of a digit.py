"""
Problem: Digit Frequency Difference
Given an integer `n` and two single-digit integers `a` and `b`, 
return the absolute difference between the number of times `a` appears in `n` 
and the number of times `b` appears in `n`.
You must do this in a single mathematical pass (one while loop).
No strings allowed.

Example:
Input: n = 112231, a = 1, b = 2
Occurrences of 1: 3
Occurrences of 2: 2
Difference: abs(3 - 2) = 1
"""

def digit_frequency_difference(n: int, a: int, b: int) -> int:
    # Build your one-pass mathematical logic here
    n = abs(n)
    c1 = 0
    c2 = 0
    if n==0:
        c1+=1 if a == 0 else 0
        c2+=1 if b == 0 else 0
        return abs(c1 - c2)
    while n > 0:
        c1+=1 if n%10 == a else 0
        c2+=1 if n%10 == b else 0
        n = n//10
    return abs(c1 - c2)

if __name__ == "__main__":
    print(digit_frequency_difference(112231, 1, 2))  # Expected: 1
    print(digit_frequency_difference(-9998, 9, 8))   # Expected: 2 (3 nines, 1 eight)
    print(digit_frequency_difference(0, 0, 5))       # Expected: 1 (1 zero, 0 fives)