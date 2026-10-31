"""
Problem: Sort 0s, 1s, and 2s
Given an array containing only 0s, 1s, and 2s, sort them IN-PLACE so that objects 
of the same color are adjacent, with the colors in the order 0, 1, and 2.
You must use a single-pass O(N) time algorithm in O(1) space.
Do not use Python's built-in `.sort()`.

Example:
Input: arr = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
"""

def sort_012(arr: list[int]) -> None:
    # Build your 3-way partition logic here
    start,mid = 0,0
    end = len(arr) - 1
    while mid<=end:
        if arr[mid]==0:
            arr[mid],arr[start] = arr[start],arr[mid]
            mid+=1
            start+=1
        elif arr[mid]==2:
            arr[mid],arr[end]=arr[end],arr[mid]
            end-=1
        else:
            mid+=1 

if __name__ == "__main__":
    arr1 = [2, 0, 2, 1, 1, 0]
    sort_012(arr1)
    print(arr1)  # Expected: [0, 0, 1, 1, 2, 2]
    
    arr2 = [2, 0, 1]
    sort_012(arr2)
    print(arr2)  # Expected: [0, 1, 2]