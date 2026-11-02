"""
Problem: Symmetric Array Check
Given an array of integers, determine if the array reads the same forwards and backwards.
You must use O(1) space two-pointer logic. Do not use array slicing (arr[::-1]).

Example:
Input: arr = [1, 2, 3, 2, 1]
Output: True

Input: arr = [1, 2, 3, 4]
Output: False
"""

def is_symmetric_array(arr: list[int]) -> bool:
    # Build your O(1) space two-pointer logic here
    if len(arr)<2:
        return True
    l,r=0,len(arr)-1
    while l<r:
        if arr[l]!=arr[r]:
            return False
        l+=1
        r-=1
    return True

if __name__ == "__main__":
    print(is_symmetric_array([1, 2, 3, 2, 1]))  # Expected: True
    print(is_symmetric_array([1, 2, 3, 4]))     # Expected: False