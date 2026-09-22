"""
Problem: Filter Above Average
Given an array of integers, calculate the average (mean) of the array. 
Return a new array containing ONLY the elements that are strictly greater than the calculated average.

Example:
Input: arr = [10, 20, 30, 40, 50]
Average = (150 / 5) = 30
Output: [40, 50]
"""

def get_above_average(arr: list[int]) -> list[int]:
    # Build your averaging and filtering logic here
    if not arr:
        return []
    avg = sum(arr)/len(arr)
    return [n for n in arr if n>avg]

if __name__ == "__main__":
    print(get_above_average([10, 20, 30, 40, 50]))  # Expected: [40, 50]
    print(get_above_average([5, 5, 5]))             # Expected: []
    print(get_above_average([]))                    # Expected: []