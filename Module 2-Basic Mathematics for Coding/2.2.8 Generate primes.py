"""
Problem: Primes Ending in Target Digit
Given an inclusive upper bound `n` and a single-digit integer `target` (0-9), 
return a list of all prime numbers up to `n` that end with the `target` digit.
Use the O(N sqrt N) generation method.

Example:
Input: n = 30, target = 3
Output: [3, 13, 23]
"""

def is_prime(n: int) -> bool:
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def primes_ending_in_digit(n: int, target: int) -> list[int]:
    # Build your generation and filtering logic here
    res = []
    for i in range(2, n+1):
        if is_prime(i) and i%10 == target:
            res.append(i)
    return res

if __name__ == "__main__":
    print(primes_ending_in_digit(30, 3))  # Expected: [3, 13, 23]
    print(primes_ending_in_digit(50, 7))  # Expected: [7, 17, 37, 47]