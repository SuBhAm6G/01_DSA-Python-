"""
Problem: Count Primes (Strictly Less Than N)
Given an integer `n`, return the total number of prime numbers that are STRICTLY LESS than `n`.
You must use the Sieve of Eratosthenes to achieve optimal time complexity.

Example:
Input: n = 10
Output: 4 (The primes strictly less than 10 are 2, 3, 5, 7)

Input: n = 2
Output: 0
"""

def count_primes_less_than(n: int) -> int:
    # Build your sieve logic here
    if n<=2:
        return 0
    is_prime = (n+1) * [True]
    is_prime[0]=is_prime[1]=False
    p = 2
    while p*p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p+=1
    return is_prime[:-1].count(True)

if __name__ == "__main__":
    print(count_primes_less_than(10))  # Expected: 4
    print(count_primes_less_than(2))   # Expected: 0
    print(count_primes_less_than(30))  # Expected: 10