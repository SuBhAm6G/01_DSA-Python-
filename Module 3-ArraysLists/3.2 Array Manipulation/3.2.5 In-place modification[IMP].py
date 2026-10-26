"""
Problem: Running Suffix Sum In-Place
Given an array of integers, modify the array IN-PLACE so that each element 
becomes the sum of all elements strictly to its RIGHT. 
The last element should always become 0.

Example:
Input: arr = [10, 4, 8, 3]
Output: [15, 11, 3, 0]
Explanation: 
- Index 0: 4 + 8 + 3 = 15
- Index 1: 8 + 3 = 11
- Index 2: 3
- Index 3: 0 (nothing on the right)
"""

def suffix_sum_inplace(arr: list[int]) -> None:
    # Build your O(N) time, O(1) space right-to-left logic here
    sum=0
    for i in range(len(arr)-1,-1,-1):
        x = arr[i]
        arr[i]=sum
        sum+=x


if __name__ == "__main__":
    arr1 = [10, 4, 8, 3]
    suffix_sum_inplace(arr1)
    print(arr1)  # Expected: [15, 11, 3, 0]
    
    arr2 = [5]
    suffix_sum_inplace(arr2)
    print(arr2)  # Expected: [0]