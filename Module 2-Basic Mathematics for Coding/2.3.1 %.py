"""
Problem: Circular Printer
You have an array of characters representing a circular printing wheel.
Given a starting index `start` and an integer `steps` (which can be massive), 
return the character the wheel lands on after moving `steps` positions to the right.

Example:
Input: wheel = ['A', 'B', 'C', 'D'], start = 1, steps = 6
Path: B (start) -> C (+1) -> D (+2) -> A (+3) -> B (+4) -> C (+5) -> D (+6)
Output: 'D'
"""

def circular_printer(wheel: list[str], start: int, steps: int) -> str:
    # Build your O(1) time complexity logic here
    return wheel[(start + steps) % len(wheel)]

if __name__ == "__main__":
    print(circular_printer(['A', 'B', 'C', 'D'], 1, 6))    # Expected: 'D'
    print(circular_printer(['X', 'Y', 'Z'], 0, 100))       # Expected: 'Y'
    print(circular_printer(['M', 'N'], 1, 1))              # Expected: 'M'