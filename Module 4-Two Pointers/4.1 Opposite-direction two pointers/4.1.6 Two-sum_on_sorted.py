"""
Problem: Book Budget
You have a SORTED array of book prices and a specific `budget`.
Find if there are EXACTLY two distinct books you can buy that use up the entire budget perfectly.
Return True if such a pair exists, otherwise False.
You must solve this in O(N) time and O(1) space.

Example:
Input: prices = [5, 10, 15, 20, 25], budget = 35
Output: True (Because 15 + 20 = 35)

Input: prices = [5, 10, 15], budget = 30
Output: False
"""

def can_spend_budget(prices: list[int], budget: int) -> bool:
    # Build your O(1) space Opposite-Direction Two Pointers logic here
    left, right = 0, len(prices)-1
    while left<right:
        total = prices[left] + prices[right]
        if total == budget:
            return True
        elif total < budget:
            left +=1
        else:
            right -=1
    return False


if __name__ == "__main__":
    print(can_spend_budget([5, 10, 15, 20, 25], 35)) # Expected: True
    print(can_spend_budget([5, 10, 15], 30))         # Expected: False
    print(can_spend_budget([10, 10], 20))            # Expected: True