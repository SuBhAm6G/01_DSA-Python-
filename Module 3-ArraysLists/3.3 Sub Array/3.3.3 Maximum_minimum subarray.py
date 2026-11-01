"""
Problem: Minimum Subarray Sum (Brute Force)
Given an array of integers, find the contiguous subarray that has the SMALLEST sum,
and return that sum. Use the O(N^2) running-state technique.

Example:
Input: arr = [3, -4, 2, -3, 5]
Output: -5
Explanation: The subarray [-4, 2, -3] has the smallest sum (-5).
"""

def min_subarray_sum(arr: list[int]) -> int | float:
    # Build your O(N^2) nested loop logic here
    if not arr:
        return float('inf')
    global_min=float('inf')
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i,len(arr)):
            current_sum+=arr[j]
            if current_sum<global_min:
                global_min=current_sum
    return global_min

if __name__ == "__main__":
    print(min_subarray_sum([3, -4, 2, -3, 5]))  # Expected: -5
    print(min_subarray_sum([10, 20, 30]))       # Expected: 10
    print(min_subarray_sum([]))                 # Expected: inf (or float('inf'))