"""
Problem: Find the Missing Number
Given a list containing (N - 1) distinct numbers taken from the range 1 to N, 
find the one missing number.
You must solve this in O(N) time and O(1) space. (Do not sort the array).

Example:
Input: arr = [1, 2, 4, 5, 6], N = 6
Output: 3
"""

def find_missing_number(arr: list[int], n: int) -> int:
    # Build your O(1) space logic here
    if n <= 0:
        return 0
    total = n*((n+1)/2)
    missing = 0
    for x in arr:
        total -= x
    return int(total)

if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5, 6], 6))  # Expected: 3
    print(find_missing_number([2, 3, 1, 5], 5))     # Expected: 4