"""
Problem: Maximum Wealth
You are given an array of integers representing the daily bank account balances of a single customer.
Return the highest balance recorded. 
You must process this using a manual loop (do not use the built-in max() function).

Example:
Input: balances = [-50, -10, -5, -120]
Output: -5

Input: balances = [0, 50, 120, 80]
Output: 120
"""

def find_max_wealth(balances: list[int]) -> int:
    # Build your tracking logic here
    h=float('-inf')
    for num in balances:
        if num>h:
            h = num
    return h if h>float('-inf') else None

if __name__ == "__main__":
    print(find_max_wealth([-50, -10, -5, -120])) # Expected: -5
    print(find_max_wealth([0, 50, 120, 80]))     # Expected: 120
    print(find_max_wealth([]))                   # Expected: None or error handling