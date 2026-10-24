"""
Problem: The Duplicate ID
You are given an array of user IDs of size N + 1. 
Every ID is an integer in the range [1, N]. 
There is exactly one repeating ID, but it may appear multiple times.
Find and return the repeating ID in O(N) time and O(1) space. 
(You are allowed to modify the array).

Example:
Input: ids = [3, 1, 3, 4, 2]
Output: 3
"""

def get_duplicate_id(ids: list[int]) -> int:
    # Build your O(1) space Negative Marking logic here
    for num in ids:
        val = abs(num)
        if(ids[val - 1]) < 0:
            return val
        else:
            ids[val - 1]*=-1
    

if __name__ == "__main__":
    print(get_duplicate_id([3, 1, 3, 4, 2]))  # Expected: 3
    print(get_duplicate_id([1, 4, 2, 2, 5]))  # Expected: 2
    print(get_duplicate_id([2, 2, 2]))        # Expected: 2