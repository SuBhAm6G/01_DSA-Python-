"""
Problem: 
Given an integer `n`, determine if it is a palindrome. 
If it IS a palindrome, return the number itself. 
If it is NOT a palindrome, return the sum of the number and its reversed version.
You must NOT convert the number to a string at any point.

Examples:
- Input: 121 -> Output: 121 (It is a palindrome)
- Input: 123 -> Output: 444 (Not a palindrome, so 123 + 321 = 444)
- Input: -45 -> Output: -99 (Negatives are not palindromes, so -45 + (-54) = -99)
"""

def process_palindrome_or_sum(n: int) -> int:
    # Build your mathematical logic here
    org = n
    is_neg = n < 0
    n = abs(n)
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n = n // 10
    if rev == org:
        return org
    else:
        return org + (-rev) if is_neg else org + rev

    

if __name__ == "__main__":
    print(process_palindrome_or_sum(121))   # Expected: 121
    print(process_palindrome_or_sum(123))   # Expected: 444
    print(process_palindrome_or_sum(-45))   # Expected: -99