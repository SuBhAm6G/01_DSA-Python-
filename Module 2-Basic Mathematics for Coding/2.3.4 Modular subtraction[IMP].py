"""
Problem: Remaining Suffix Sum
You are given the `total_sum` of a massive array and the `prefix_sum` of the first half. 
Both values have ALREADY been modulo'd by (10^9 + 7). 
Calculate the sum of the remaining suffix modulo (10^9 + 7).

Example:
MOD = 10
total_sum = 2   (Original sum was 12, but 12 % 10 = 2)
prefix_sum = 8  (Original prefix was 8, 8 % 10 = 8)
Expected Suffix: The original suffix was (12 - 8) = 4. 
Output: 4
"""

def get_suffix_sum(total_sum: int, prefix_sum: int) -> int:
    MOD = 10**9 + 7
    # Build your strictly safe modular subtraction logic here
    return ((total_sum%MOD) - (prefix_sum)%MOD + MOD) % MOD

if __name__ == "__main__":
    print(get_suffix_sum(2, 8))             # Expected: 4 (using MOD = 10 for this conceptual test)
    # Note: For the actual function, assume MOD = 10**9 + 7