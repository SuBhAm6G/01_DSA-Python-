"""
Problem: Reverse Sub-segment
Given an array and two indices `start` and `end`, reverse ONLY the elements 
within that index range (inclusive) IN-PLACE.

Example:
Input: arr = [10, 20, 30, 40, 50, 60], start = 1, end = 4
Output: [10, 50, 40, 30, 20, 60]
(Only the sub-segment [20, 30, 40, 50] is reversed)
"""

def reverse_sub_segment(arr: list[int], start: int, end: int) -> None:
    # Build your O(1) space two-pointer logic here
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50, 60]
    reverse_sub_segment(arr1, 1, 4)
    print(arr1)  # Expected: [10, 50, 40, 30, 20, 60]