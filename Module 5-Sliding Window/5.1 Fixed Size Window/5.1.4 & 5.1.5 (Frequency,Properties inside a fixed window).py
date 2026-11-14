"""
Problem: Maximum Vowels in a Window
Given a string `s` and an integer `k`, return the MAXIMUM number of vowel letters 
('a', 'e', 'i', 'o', 'u') in any contiguous substring of length `k`.
You must solve this in O(N) time.

Example:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowels.

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet", and "ode" contain 2 vowels.
"""

def max_vowels(s: str, k: int) -> int:
    if len(s)<k or k<=0:
        return -1
    vowels= set('aeiou')
    count=sum(v in vowels for v in s[:k])
    max_count=count
    for i in range (k,len(s)):
        count+=(s[i] in vowels)-(s[i-k] in vowels)
        max_count=max(max_count,count)
    return max_count

if __name__ == "__main__":
    print(max_vowels("abciiidef", 3))  # Expected: 3
    print(max_vowels("leetcode", 3))   # Expected: 2
    print(max_vowels("xyz", 2))        # Expected: 0