"""
Problem: Minimum Absolute Value
Given an array of integers (which can be positive, negative, or zero), 
find and return the original integer that has the smallest ABSOLUTE value.
If there is a tie (e.g., -3 and 3), return the one that appeared first in the array.
You must process this using a manual loop (do not just use min() with a lambda).

Example:
Input: arr = [10, -5, -2, 4, 2]
Output: -2 (Absolute value is 2, which is the smallest. -2 appears before 2).
"""

def min_absolute_value(arr: list[int]) -> int:
    # Build your tracking logic here
    m = float('inf')
    for n in arr:
        if abs(n)<abs(m):
            m = n
    return m

if __name__ == "__main__":
    print(min_absolute_value([10, -5, -2, 4, 2]))  # Expected: -2
    print(min_absolute_value([-100, 50, 100]))     # Expected: 50
    print(min_absolute_value([0, -1, 1]))          # Expected: 0