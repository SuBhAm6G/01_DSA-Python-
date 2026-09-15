"""
Problem: Leap Year Checker
A year is considered a leap year if it follows these mathematical rules:
1. It is divisible by 4.
2. HOWEVER, if it is also divisible by 100, it is NOT a leap year...
3. UNLESS it is also divisible by 400.

Write a single-pass O(1) time function to return True if the year is a leap year.

Example:
Input: year = 2024 
Output: True

Input: year = 1900 
Output: False (Divisible by 100 but not 400)

Input: year = 2000 
Output: True (Divisible by 400)
"""

def is_leap_year(year: int) -> bool:
    # Build your O(1) conditional logic here
    if year % 100 == 0:
        return True if year%400 == 0 else False
    elif year % 4 == 0:
        return True
    return False

if __name__ == "__main__":
    print(is_leap_year(2024))  # Expected: True
    print(is_leap_year(1900))  # Expected: False
    print(is_leap_year(2000))  # Expected: True