"""
Problem: Breakpoint Index
Given an array of integers, check if it is sorted in non-decreasing (ascending) order.
If it is NOT sorted, return the index of the FIRST element that is strictly smaller 
than the element immediately before it.
If it IS perfectly sorted (or empty, or size 1), return -1.

Example:
Input: arr = [10, 20, 30, 25, 40]
Output: 3 (Because 25 is smaller than 30, and 25 is located at index 3)

Input: arr = [5, 5, 5]
Output: -1 (Sorted)
"""

def find_sort_breakpoint(arr: list[int]) -> int:
    # Build your O(N) time and O(1) space logic here
    if (len(arr)<2):
        return -1
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return i+1
    return -1

if __name__ == "__main__":
    print(find_sort_breakpoint([10, 20, 30, 25, 40]))  # Expected: 3
    print(find_sort_breakpoint([5, 5, 5]))             # Expected: -1
    print(find_sort_breakpoint([9, 4, 3]))             # Expected: 1
    print(find_sort_breakpoint([100]))                 # Expected: -1