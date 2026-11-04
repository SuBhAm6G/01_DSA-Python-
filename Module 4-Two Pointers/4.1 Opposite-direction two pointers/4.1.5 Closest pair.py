"""
Problem: Temperature Calibration
Given a SORTED array of component temperatures, find the pair of temperatures 
whose sum is closest to the `target` optimal operating limit. 
Return the pair as a tuple. (If there are multiple pairs with the exact same 
closest difference, returning the first one found is acceptable).
You must solve this in O(N) time and O(1) space.

Example:
Input: temps = [10, 22, 28, 29, 30, 40], target = 54
Output: (22, 30)
Explanation: 
22 + 30 = 52 (difference of 2). 
28 + 29 = 57 (difference of 3).
(22, 30) is the closest pair to 54.
"""

def get_closest_temps(temps: list[int], target: int) -> tuple[int, int] | None:
    # Build your O(1) space opposite-direction two-pointer logic here
    left = 0
    right = len(temps) -1
    best_difference = float('inf')
    best_pair = None
    while left < right:
        current_sum = temps[left]+temps[right]
        difference = abs(target - current_sum)
        if difference == 0:
            return (temps[left],temps[right])
        elif difference < best_difference:
            best_difference = difference
            best_pair = (temps[left], temps[right])
        elif current_sum<target:
            left +=1
        else:
            right -=1
    return best_pair

if __name__ == "__main__":
    print(get_closest_temps([10, 22, 28, 29, 30, 40], 54)) # Expected: (22, 30)
    print(get_closest_temps([1, 4, 5, 7, 10], 13))         # Expected: (4, 10) or (5, 7) based on exact tie-break logic