"""
Problem: Check for Divisible Subarray (Brute Force Math Check)
Given an array of integers and an integer `k`, generate the prefix modulo array.
Then, verify if the number `0` appears anywhere in the prefix modulo array.
(If a prefix modulo is 0, it means the subarray starting from the VERY BEGINNING 
up to that point is perfectly divisible by k).
Return True if a 0 exists, otherwise False.

Example:
Input: arr = [4, 2, 9], k = 3
running sums = [4, 6, 15]
prefix mods = [4%3, 6%3, 15%3] = [1, 0, 0]
Output: True (Because 0 exists in the prefix mods)
"""

def has_divisible_prefix(arr: list[int], k: int) -> bool:
    # Build your mathematical prefix modulo logic here
    if k == 0 or len(arr)==0:
        return False
    prefix_mods = []
    running_sum = 0
    for x in arr:
        running_sum += x
        if running_sum%k == 0:
            return True
    return False

if __name__ == "__main__":
    print(has_divisible_prefix([4, 2, 9], 3))  # Expected: True
    print(has_divisible_prefix([1, 2, 1], 5))  # Expected: False
    print(has_divisible_prefix([7, 13], 10))   # Expected: True (7+13 = 20, 20%10 = 0)