"""
Problem: Target Frequency Percentage
Given an array of integers and a `target` integer, calculate what percentage of the array 
is made up of the target value. 
Return the result as a float between 0.0 and 100.0.
If the array is empty, return 0.0 to avoid division by zero.
You may use Python's built-in methods.

Example:
Input: arr = [5, 2, 5, 5, 8], target = 5
Output: 60.0 (5 appears 3 times out of 5 elements -> 3/5 = 0.6 -> 60.0%)

Input: arr = [1, 2, 3], target = 9
Output: 0.0
"""

def target_percentage(arr: list[int], target: int) -> float:
    # Build your logic here
    if len(arr)==0:
        return 0.0
    return float(arr.count(target)/len(arr))*100

if __name__ == "__main__":
    print(target_percentage([5, 2, 5, 5, 8], 5))  # Expected: 60.0
    print(target_percentage([1, 2, 3], 9))        # Expected: 0.0
    print(target_percentage([], 5))               # Expected: 0.0