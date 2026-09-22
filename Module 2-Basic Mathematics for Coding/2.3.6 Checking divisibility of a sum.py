"""
Problem: Check if Total Weight is Divisible
You are given an array of massive cargo weights and a limit `k`.
Return True if the total weight of all cargo can be evenly divided by `k`.
You must prevent the integer from growing large during calculation.

Example:
Input: weights = [10**9, 10**9, 10**9], k = 3
Output: True (Because 3 * 10^9 is perfectly divisible by 3)
"""

def check_cargo_divisibility(weights: list[int], k: int) -> bool:
    # Build your overflow-safe logic here
    if len(weights) == 0:
        return 0
    running_modulo = 0
    for x in weights:
        running_modulo = (running_modulo + x)%k
    return running_modulo == 0

if __name__ == "__main__":
    print(check_cargo_divisibility([10**9, 10**9, 10**9], 3))  # Expected: True
    print(check_cargo_divisibility([15, 20, 11], 5))           # Expected: False
