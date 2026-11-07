"""
Problem: Validate Clickstream
Given a `target` sequence of event codes and a massive `stream` of logged events, 
verify if the `target` events occurred in the exact chronological order within the `stream`.

Example:
Input: target = "abc", stream = "ahbgdc"
Output: True (Because 'a', 'b', and 'c' appear in that exact order)

Input: target = "axc", stream = "ahbgdc"
Output: False ('x' is missing)
"""

def is_valid_clickstream(target: str, stream: str) -> bool:
    # Build your O(M) time, O(1) space two-pointer matching logic here
    t,s=0,0
    while t<len(target) and s<len(stream):
        if target[t]==stream[s]:
            t+=1
        s+=1
    return t==len(target)

if __name__ == "__main__":
    print(is_valid_clickstream("abc", "ahbgdc")) # Expected: True
    print(is_valid_clickstream("axc", "ahbgdc")) # Expected: False
    print(is_valid_clickstream("acb", "ahbgdc")) # Expected: False (Out of order)