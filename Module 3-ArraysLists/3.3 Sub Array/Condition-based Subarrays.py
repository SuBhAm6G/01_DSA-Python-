"""
Problem: Shortest Subarray with Target Sum or Greater (Brute Force)
Given an array of positive integers and a `target`, find the length of the 
SHORTEST contiguous subarray whose sum is GREATER THAN OR EQUAL TO the target.
If no such subarray exists, return 0.

Example:
Input: arr = [2, 3, 1, 2, 4, 3], target = 7
Output: 2
Explanation: The subarray [4, 3] has a sum of 7 and is the shortest (length 2).
"""

def shortest_subarray_gte_target(arr: list[int], target: int) -> int:
    # Build your O(N^2) running-state logic here
    if not arr:
        return 0
    shortest_len = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            shortest_len = min(shortest_len or float("inf"), j - i + 1) if current_sum >= target else shortest_len
    return shortest_len
    

if __name__ == "__main__":
    print(shortest_subarray_gte_target([2, 3, 1, 2, 4, 3], 7))  # Expected: 2
    print(shortest_subarray_gte_target([1, 4, 4], 4))           # Expected: 1
    print(shortest_subarray_gte_target([1, 1, 1, 1], 10))       # Expected: 0