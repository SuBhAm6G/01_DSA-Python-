"""
Problem: First Duplicate
Given an array of integers, find and return the FIRST duplicate number you encounter 
while traversing from left to right. 
If no duplicates exist, return -1.

Example:
Input: arr = [10, 5, 2, 5, 10]
Output: 5 (Even though 10 repeats, 5 is the first duplicate detected when moving left-to-right).
"""

def first_duplicate(arr: list[int]) -> int:
    # Build your O(N) time and O(N) space logic here using a set
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

if __name__ == "__main__":
    print(first_duplicate([10, 5, 2, 5, 10]))  # Expected: 5
    print(first_duplicate([1, 2, 3, 4]))       # Expected: -1
    print(first_duplicate([7, 7, 7, 7]))       # Expected: 7