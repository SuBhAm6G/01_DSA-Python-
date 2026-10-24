"""
Problem: Move Target Values
You are given an array of integers and a `target` value. 
Move all instances of the `target` value to the END of the array while maintaining 
the relative order of all other elements.
You must modify the array IN-PLACE with O(1) extra space.

Example:
Input: arr = [4, 2, 4, 1, 3], target = 4
Output: [2, 1, 3, 4, 4]

Input: arr = [7, 7, 7], target = 7
Output: [7, 7, 7]
"""

def move_target_to_end(arr: list[int], target: int) -> None:
    # Build your O(1) space two-pointer logic here
    if not arr:
        return 0
    insert_idx=0
    for i in range(0,len(arr)):
        if arr[i]!=target:
            arr[insert_idx]=arr[i]
            insert_idx+=1
    
    for i in range(insert_idx,len(arr)):
        arr[i]=target
    

if __name__ == "__main__":
    arr1 = [4, 2, 4, 1, 3]
    move_target_to_end(arr1, 4)
    print(arr1)  # Expected: [2, 1, 3, 4, 4]

    arr2 = [7, 7, 7]
    move_target_to_end(arr2, 7)
    print(arr2)  # Expected: [7, 7, 7]