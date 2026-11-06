#In place filtering

"""
Problem: Segregate Evens (Same-Direction)
Given an array of integers, move all EVEN numbers to the front of the array.
You MUST use the same-direction slow/fast pointer swap technique. 
(Do not use opposite-direction pointers).

Example:
Input: arr = [3, 1, 2, 4, 7, 6]
Output: [2, 4, 6, 3, 7, 1] 
(Note: The exact order of the odds at the back may vary based on swap history, 
but all evens must be safely partitioned at the front).
"""

def move_evens_to_front(arr: list[int]) -> None:
    # Build your O(N) time, O(1) space same-direction swap logic here
    boundary = 0
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[boundary],arr[i]= arr[i],arr[boundary]
            boundary+=1


if __name__ == "__main__":
    arr1 = [3, 1, 2, 4, 7, 6]
    move_evens_to_front(arr1)
    print(arr1)  # Expected prefix: 2, 4, 6