"""
Problem: Insert into Sorted Array
Given a SORTED array of integers and a `target` value, insert the `target` 
into the array such that the array remains sorted. 
You must do this by finding the correct index, appending a dummy value 
to extend the array, and MANUALLY shifting the elements.
Do NOT use `arr.insert()` or `arr.sort()`.

Example:
Input: arr = [10, 20, 30, 40], target = 25
Output: [10, 20, 25, 30, 40]
"""

def insert_sorted(arr: list[int], target: int) -> None:
    # Build your O(N) manual insertion logic here
    arr.append(0)
    idx = len(arr) - 2
    while idx >= 0 and arr[idx]>target:
        arr[idx+1]=arr[idx]
        idx-=1
    arr[idx+1]=target

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40]
    insert_sorted(arr1, 25)
    print(arr1)  # Expected: [10, 20, 25, 30, 40]
    
    arr2 = [5, 15]
    insert_sorted(arr2, 3)
    print(arr2)  # Expected: [3, 5, 15]
    
    arr3 = [1, 2]
    insert_sorted(arr3, 99)
    print(arr3)  # Expected: [1, 2, 99]