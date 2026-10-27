"""
Problem: Delete by Value
Given an array and a `target` value, find the FIRST occurrence of the `target` 
and delete it MANUALLY by shifting elements. Shrink the array length.
If the target does not exist, do nothing. 
Do NOT use `arr.remove(target)`.

Example:
Input: arr = [10, 20, 30, 20, 40], target = 20
Output: [10, 30, 20, 40]
"""

def delete_first_occurrence(arr: list[int], target: int) -> None:
    # Build your O(N) manual deletion logic here
    try:
        idx = arr.index(target)
    except:
        return
    for i in range(idx,len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()

if __name__ == "__main__":
    arr1 = [10, 20, 30, 20, 40]
    delete_first_occurrence(arr1, 20)
    print(arr1)  # Expected: [10, 30, 20, 40]
    
    arr2 = [5, 15]
    delete_first_occurrence(arr2, 99)
    print(arr2)  # Expected: [5, 15]