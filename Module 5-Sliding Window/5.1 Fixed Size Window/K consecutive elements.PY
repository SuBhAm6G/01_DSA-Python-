"""
Problem: Rolling Server Load
Given an array of integer server CPU loads and a window size `k`, 
return the MAXIMUM average CPU load over any contiguous `k` minutes.
You must solve this in strictly O(N) time (no slicing in loops).

Example:
Input: loads = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
Explanation: The maximum sum for a window of size 4 is 51 (from [12, -5, -6, 50]).
The average is 51 / 4 = 12.75.
"""

def max_average_load(loads: list[int], k: int) -> float:
    # Build your O(N) sliding window logic here
    if len(loads)<k or k<=0:
        return float('-inf')
    current_sum=sum(loads[:k])
    max_sum=current_sum
    for i in range(k,len(loads)):
        current_sum+=loads[i]-loads[i-k]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum/k

if __name__ == "__main__":
    print(max_average_load([1, 12, -5, -6, 50, 3], 4))  # Expected: 12.75
    print(max_average_load([5, 5], 1))                  # Expected: 5.0