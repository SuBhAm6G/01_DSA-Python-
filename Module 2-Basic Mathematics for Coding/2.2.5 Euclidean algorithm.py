"""
Problem: Coprime Check
Two numbers are considered "coprime" if they share no common divisors other than 1.
(In other words, their GCD is exactly 1).
Write a function `is_coprime(a, b)` that returns True if they are coprime, and False otherwise.
You MUST write out the Euclidean algorithm manually (do not use math.gcd).

Example:
Input: a = 14, b = 15
Output: True (GCD is 1)

Input: a = 14, b = 21
Output: False (GCD is 7)
"""

def is_coprime(a: int, b: int) -> bool:
    # Build your mathematical logic here
    a,b = abs(a), abs(b)
    while b>0:
        a, b = b, a%b
    return True if a == 1 else False

if __name__ == "__main__":
    print(is_coprime(14, 15))  # Expected: True
    print(is_coprime(14, 21))  # Expected: False