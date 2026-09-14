"""
Problem: Next Prime
Given an integer `n`, return the smallest prime number that is strictly greater than `n`.
You must use the O(sqrt(n)) prime checking logic.

Example:
Input: n = 14
Output: 17 (15 is div by 3, 16 is div by 2, 17 is prime)
"""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n: int) -> int:
    # Build your logic here utilizing the helper function
    i = n + 1
    while i > n:
        if is_prime(i):
            return i
        else:
            i+=1


if __name__ == "__main__":
    print(next_prime(14))  # Expected: 17
    print(next_prime(0))   # Expected: 2
    print(next_prime(24))  # Expected: 29