"""
Problem: Conditional Sum
Given an array of integers, calculate and return the sum of ONLY the positive numbers.
(Ignore zeros and negative numbers).
You must write the traversal manually (do not use sum() with list comprehensions).

Example:
Input: arr = [15, -4, 10, -2, 0, 5]
Output: 30 (15 + 10 + 5)
"""

def sum_positive_numbers(arr: list[int]) -> int:
    # Build your conditional summing logic here
    total = 0
    for num in arr:
        total += num if num>0 else 0
    return total

if __name__ == "__main__":
    print(sum_positive_numbers([15, -4, 10, -2, 0, 5]))  # Expected: 30
    print(sum_positive_numbers([-5, -10]))               # Expected: 0
    print(sum_positive_numbers([]))                      # Expected: 0