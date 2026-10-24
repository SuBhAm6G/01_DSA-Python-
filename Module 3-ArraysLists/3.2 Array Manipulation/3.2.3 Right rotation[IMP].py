"""
Problem: Right Rotate by 1
Write the logic to rotate an array to the RIGHT by exactly 1 position IN-PLACE.
You must use a manual loop. Do not use `.insert()` or `.pop()`.

Example:
Input: arr = [10, 20, 30, 40, 50]
Output: [50, 10, 20, 30, 40]
"""

def right_rotate_by_one(arr: list[int]) -> None:
    # Build your O(N) time, O(1) space right-rotation logic here
    if len(arr)<2:
        return
    last = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0]= last

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    right_rotate_by_one(arr1)
    print(arr1)  # Expected: [50, 10, 20, 30, 40]
    
    arr2 = [7]
    right_rotate_by_one(arr2)
    print(arr2)  # Expected: [7]