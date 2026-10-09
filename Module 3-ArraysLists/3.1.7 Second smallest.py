"""
Problem: Second Lowest Temperature
Given an array of daily temperatures, find the strictly second lowest unique temperature.
If there is no valid second lowest (e.g., empty array, only 1 element, or all identical), return None.

Example:
Input: temps = [72, 75, 70, 72, 79]
Output: 72 (70 is lowest, 72 is second lowest. The duplicate 72 is ignored).

Input: temps = [40, 40, 40]
Output: None
"""

def get_second_lowest(temps: list[int]) -> int | None:
    # Build your dual-tracking logic here
    if len(temps)<2:
        return None
    smallest = float('inf')
    second = float('inf')
    for num in temps:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num
    return second if second < float('inf') else None
if __name__ == "__main__":
    print(get_second_lowest([72, 75, 70, 72, 79]))  # Expected: 72
    print(get_second_lowest([40, 40, 40]))          # Expected: None
    print(get_second_lowest([10]))                  # Expected: None