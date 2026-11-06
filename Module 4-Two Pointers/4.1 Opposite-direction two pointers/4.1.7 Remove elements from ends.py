"""
Problem: Trim Sensor Outliers
Given an array of sensor readings, remove all zero-value readings (0) 
from BOTH ends of the array. 
Do NOT remove any 0s that are trapped in the middle of valid readings.

Example:
Input: readings = [0, 0, 4, 0, 5, 0]
Output: [4, 0, 5]

Input: readings = [0, 0, 0]
Output: []
"""

def trim_sensor_zeros(readings: list[int]) -> list[int]:
    # Build your opposite-direction trimming logic here
    left = 0
    right = len(readings)-1
    while left<=right and readings[left]==0:
        left+=1
    while right>=left and readings[right]==0:
        right -=1
    return readings[left:right+1]

if __name__ == "__main__":
    print(trim_sensor_zeros([0, 0, 4, 0, 5, 0]))  # Expected: [4, 0, 5]
    print(trim_sensor_zeros([0, 0, 0]))           # Expected: []
    print(trim_sensor_zeros([1, 2, 3]))           # Expected: [1, 2, 3]