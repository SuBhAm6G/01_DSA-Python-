"""
Problem: Valid Drone Path
A drone logs its flight path as a string of directional characters ('N', 'S', 'E', 'W').
However, the log is corrupted with sensor static (hyphens '-', dots '.', and spaces).
A flight path is considered a "Return-to-Base" path if the sequence of valid directional 
characters reads the exact same forwards and backwards.

Write an O(1) space function to determine if a corrupted log is a Return-to-Base path.

Example:
Input: log = "N- E.. . E, -N"
Output: True (Valid characters form "NEEN")

Input: log = "S - W - N"
Output: False (Valid characters form "SWN")
"""

def is_return_to_base(log: str) -> bool:
    # Build your O(N) time, O(1) space skipping-pointer logic here
    left = 0
    right = len(log)-1
    while left<right:
        while left<right and not log[left].isalnum():
            left+=1
        while left<right and not log[right].isalnum():
            right-=1
        if log[left].lower()!=log[right].lower():
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    print(is_return_to_base("N- E.. . E, -N")) # Expected: True
    print(is_return_to_base("S - W - N"))      # Expected: False
    print(is_return_to_base("   .  -  "))     # Expected: True (Empty valid string)