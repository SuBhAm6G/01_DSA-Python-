"""
Problem: Merge Sorted Arrays (In-Place Variant)
You are given two sorted integer arrays `nums1` and `nums2`.
`nums1` has a length of `m + n`, where the first `m` elements are the real values, 
and the last `n` elements are just padding (set to 0) to hold `nums2`.
`nums2` has a length of `n`.

Merge `nums2` into `nums1` IN-PLACE so that `nums1` becomes a single sorted array.

HINT: If you start pointers at index 0, you will overwrite unread data in nums1. 
Where should your pointers start to safely overwrite the padding first?
"""

def merge_in_place(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Build your O(M+N) time, O(1) space logic here
    p1,p2 = m-1, n-1
    x=m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]>=nums2[p2]:
            nums1[x]=nums1[p1]
            p1-=1
            x-=1
        else:
            nums1[x]=nums2[p2]
            p2-=1
            x-=1
    while p2 >= 0:
        nums1[x] = nums2[p2]
        p2-=1
        x-=1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge_in_place(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]
    
    nums3 = [0]
    merge_in_place(nums3, 0, [1], 1)
    print(nums3)  # Expected: [1]