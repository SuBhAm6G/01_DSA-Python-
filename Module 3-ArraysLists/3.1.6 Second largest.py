"""
Problem: Silver Medalist
Given an array of athlete scores, return the strictly second highest unique score. 
If there is no valid second highest score (e.g., the array is empty, has only 1 element, 
or all elements are identical), return -1.

Example:
Input: scores = [50, 40, 50, 30]
Output: 40

Input: scores = [100, 100, 100]
Output: -1
"""

def get_silver_medalist(scores: list[int]) -> int:
    # Build your dual-tracking logic here
    if (len(scores) < 2):
        return -1
    largest = float('-inf')
    second = float('-inf')
    for n in scores:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n!=largest:
            second = n
    return second if second > float('-inf') else -1

if __name__ == "__main__":
    print(get_silver_medalist([50, 40, 50, 30]))  # Expected: 40
    print(get_silver_medalist([100, 100, 100]))   # Expected: -1
    print(get_silver_medalist([10]))              # Expected: -1