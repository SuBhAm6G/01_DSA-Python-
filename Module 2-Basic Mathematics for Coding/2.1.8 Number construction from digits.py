"""
Problem: Build Non-Zero Integer
Given a list of digits (0 through 9) in left-to-right order, 
construct and return the resulting integer, but IGNORE any '0' digits.
You must build the number mathematically. No strings allowed.

Example:
Input: digits = [1, 0, 4, 0, 5]
Output: 145 (Because the zeros are ignored: 1 -> 4 -> 5)

Input: digits = [0, 0, 7]
Output: 7
"""

def build_non_zero_integer(digits: list[int]) -> int:
    # Build your mathematical logic here
    res = 0
    for x in digits:
        if x == 0:
            pass
        else:
            res = res*10 + x
    return res

if __name__ == "__main__":
    print(build_non_zero_integer([1, 0, 4, 0, 5]))  # Expected: 145
    print(build_non_zero_integer([0, 0, 7]))        # Expected: 7
    print(build_non_zero_integer([0, 0, 0]))        # Expected: 0