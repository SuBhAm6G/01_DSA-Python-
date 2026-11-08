"""
Problem: Sorted Squares (Disguised Two-Pointer)
Given an integer array `nums` sorted in non-decreasing order, return a NEW array 
containing the squares of each number, also sorted in non-decreasing order.

Constraint: You must solve this in exactly O(N) time. 
(Squaring them normally and calling .sort() takes O(N log N) time, which fails the constraint).

Hint: The largest squares are at the extreme left or extreme right. 
Use opposite-direction pointers to pick the largest square and fill your result array 
from RIGHT to LEFT (from the last index down to the first).

Example:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: 
Left pointer at -4 (square is 16). Right pointer at 10 (square is 100).
100 is larger, so 100 goes into the last slot of the result array. Right pointer moves inward.
"""

def sorted_squares(nums: list[int]) -> list[int]:
    # Build your O(N) time opposite-direction logic here
    l,r=0,len(nums)-1
    idx=r
    res=[0]*len(nums)
    while l<=r:
        if nums[l]**2>nums[r]**2:
            res[idx]=nums[l]**2
            l+=1
        else:
            res[idx]=nums[r]**2
            r-=1
        idx-=1
    return res
if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))  # Expected: [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))  # Expected: [4, 9, 9, 49, 121]