"""
Problem: Threshold Filter
Given an array of daily sales numbers and a target `threshold`, 
return a new array containing only the sales numbers that met or exceeded the threshold.

Example:
Input: sales = [150, 80, 200, 90, 300], threshold = 100
Output: [150, 200, 300]
"""

def filter_sales(sales: list[int], threshold: int) -> list[int]:
    # Build your traversal and filtering logic here
    res = []
    for num in sales:
        if num>threshold:
            res.append(num)
    return res

if __name__ == "__main__":
    print(filter_sales([150, 80, 200, 90, 300], 100)) # Expected: [150, 200, 300]
    print(filter_sales([50, 20], 100))                # Expected: []