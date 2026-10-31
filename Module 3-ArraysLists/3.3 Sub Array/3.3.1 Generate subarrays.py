"""
Problem: Same-End Subarrays
Given an array of integers, count how many subarrays start and end with the EXACT same number.
(Note: A single-element subarray trivially starts and ends with the same number).

Example:
Input: arr = [1, 2, 1]
Valid Subarrays:
- [1] (starts/ends with 1)
- [2] (starts/ends with 2)
- [1] (starts/ends with 1)
- [1, 2, 1] (starts/ends with 1)
Output: 4
"""

def count_same_end_subarrays(arr: list[int]) -> int:
    # Build your O(N^2) boundary evaluation logic here
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]==arr[j]:
                count+=1
    return count


if __name__ == "__main__":
    print(count_same_end_subarrays([1, 2, 1]))       # Expected: 4
    print(count_same_end_subarrays([3, 3, 3]))       # Expected: 6
    print(count_same_end_subarrays([5, 4, 3, 2, 1])) # Expected: 5