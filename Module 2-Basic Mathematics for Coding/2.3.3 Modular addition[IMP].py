"""
Problem: Large Array Sum Modulo
Given an array of very large integers, calculate their total sum. 
Since the sum can be enormous, return the result modulo (10^9 + 7).
You must apply modular addition step-by-step in your loop.

Example:
Input: arr = [10**9, 10**9, 10**9]
Modulo = 10**9 + 7
Output: 999999979
"""

def sum_modulo(arr: list[int]) -> int:
    MOD = 10**9 + 7
    # Build your step-by-step modular addition logic here
    res = 0
    for x in arr:
        res = (res + (x % MOD)) % MOD
    return res

if __name__ == "__main__":
    print(sum_modulo([10**9, 10**9, 10**9]))  # Expected: 999999979
    print(sum_modulo([5, 5, 5]))              # Expected: 15