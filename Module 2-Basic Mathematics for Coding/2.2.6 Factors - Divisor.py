"""
Problem: Kth Factor of N
Given two positive integers `n` and `k`, find all factors of `n`, 
sort them in ascending order, and return the `k`-th factor (1-indexed). 
If `n` has fewer than `k` factors, return -1.

You must solve this in O(sqrt(n) + F log F) time where F is the number of factors.

Example: n = 12, k = 3
Factors of 12: [1, 2, 3, 4, 6, 12]
The 3rd factor is 3. Output: 3
"""

def kth_factor(n: int, k: int) -> int:
    # Build your optimized logic here
    factors = []
    i = 1
    while i*i <= n:
        if n%i == 0:
            factors.append(i)
        if i*i != n:
            factors.append(n//i)
        i+=1
    return sorted(factors)[k-1] if k-1 < len(factors) else -1

if __name__ == "__main__":
    print(kth_factor(12, 3))   # Expected: 3
    print(kth_factor(4, 4))    # Expected: -1 (factors are 1, 2, 4)