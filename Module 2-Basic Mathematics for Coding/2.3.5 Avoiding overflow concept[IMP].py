"""
Problem: Modulo Power
Calculate (base^power) % MOD. 
Do NOT use Python's built-in `pow()` function. You must write a `for` loop 
that multiplies the base `power` times, preventing overflow at every step.

Example:
Input: base = 2, power = 10, mod = 1000
Output: 24 (Because 2^10 = 1024, and 1024 % 1000 = 24)
"""

def power_modulo(base: int, power: int, mod: int) -> int:
    # Build your iterative, overflow-safe logic here
    res = 1
    for i in range(power):
        res = (res*base)%mod
    return res%mod
if __name__ == "__main__":
    print(power_modulo(2, 10, 1000))       # Expected: 24
    print(power_modulo(5, 3, 10**9 + 7))   # Expected: 125