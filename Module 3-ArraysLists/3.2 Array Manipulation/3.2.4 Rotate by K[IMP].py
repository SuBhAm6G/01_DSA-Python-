"""
Problem: Optimize Right Rotation
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
You must do this IN-PLACE in O(1) extra space. Do NOT use Python slicing.
Hint: You should write a small helper function to handle the reversing of sub-segments.

Example:
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
"""

def rotate_by_k(nums: list[int], k: int) -> None:
    # Build your O(N) time, O(1) space 3-step reverse logic here
    nums.reverse()
    left = 0
    right = k%len(nums) - 1
    while(left<right):
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
    left = k%len(nums)
    right = len(nums) - 1
    while(left<right):
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1 

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate_by_k(nums1, 3)
    print(nums1)  # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    nums2 = [-1, -100, 3, 99]
    rotate_by_k(nums2, 2)
    print(nums2)  # Expected: [3, 99, -1, -100]
    
    nums3 = [1, 2]
    rotate_by_k(nums3, 5)
    print(nums3)  # Expected: [2, 1]