"""
Problem: Aligning Orbits
Three planets orbit a star. They take `p1`, `p2`, and `p3` days to complete one orbit, respectively.
If they are perfectly aligned today, how many days will it take for all three to align again?
You must solve this using Python's built-in math module.

Example:
Input: p1 = 4, p2 = 5, p3 = 6
Output: 60 (60 is the smallest number divisible by 4, 5, and 6)
"""
import math

def days_until_alignment(p1: int, p2: int, p3: int) -> int:
    # Build your logic here
    return math.lcm(p1,p2,p3)

if __name__ == "__main__":
    print(days_until_alignment(4, 5, 6))      # Expected: 60
    print(days_until_alignment(10, 15, 20))   # Expected: 60