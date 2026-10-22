"""
Problem: QuickSort Partition Step
Given an array of integers and a `pivot_value`, rearrange the array IN-PLACE 
so that all elements strictly LESS than `pivot_value` appear on the left, 
and all elements GREATER THAN OR EQUAL to `pivot_value` appear on the right.
The relative order of the elements does NOT need to be preserved.
You must use the Two-Pointer Swap technique (O(N) time, O(1) space).

Example:
Input: arr = [9, 2, 7, 3, 6, 1, 8], pivot_value = 5
Output: [1, 2, 3, 7, 6, 9, 8] 
(Note: Any valid partitioned layout is acceptable, such as [3, 2, 1, 9, 6, 7, 8])
"""

def partition_by_pivot(arr: list[int], pivot_value: int) -> None:
    # Build your O(1) space two-pointer swap logic here
    if not arr:
        return
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left]<pivot_value:
            left+=1
        elif arr[right]>=pivot_value:
            right-=1
        else:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    

if __name__ == "__main__":
    arr1 = [9, 2, 7, 3, 6, 1, 8]
    partition_by_pivot(arr1, 5)
    print(arr1)  # Expected: Left side < 5, Right side >= 5

    arr2 = [10, 10, 5, 2, 1]
    partition_by_pivot(arr2, 6)
    print(arr2)  # Expected: Left side < 6, Right side >= 6