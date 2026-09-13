"""
Problem: Sign Counter
Given a list of integers, return a dictionary containing the exact count 
of how many numbers are 'positive', 'negative', and 'zero'.

Example:
Input: arr = [-4, 0, 5, -2, 0, 0, 8]
Output: {'positive': 2, 'negative': 2, 'zero': 3}
"""

def count_signs(arr: list[int]) -> dict:
    # Build your logic here
    res = {'positive': 0, 'negative': 0, 'zero': 0}
    for x in arr:
        if x > 0:
            res['positive'] += 1
        elif x < 0:
            res['negative'] += 1
        else:
            res['zero'] += 1

    return res


if __name__ == "__main__":
    print(count_signs([-4, 0, 5, -2, 0, 0, 8])) 
    # Expected: {'positive': 2, 'negative': 2, 'zero': 3}
    
    print(count_signs([1, 2, 3]))               
    # Expected: {'positive': 3, 'negative': 0, 'zero': 0}