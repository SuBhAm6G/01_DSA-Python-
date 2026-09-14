"""
Problem: Square of Sum vs Sum of Squares
Find the absolute difference between the square of the sum of the first N natural numbers 
and the sum of the squares of the first N natural numbers.
You must solve this in O(1) time and O(1) space. (No loops allowed).

Example: N = 10
Square of the sum = (1 + 2 + ... + 10)^2 = 55^2 = 3025
Sum of the squares = 1^2 + 2^2 + ... + 10^2 = 385
Difference = 3025 - 385 = 2640
"""

def difference_of_sums(n: int) -> int:
    # Build your O(1) logic here using both mathematical formulas
    if n<=0:
        return 0
    return ((n*(n+1))//2)**2 - (n * (n+1) * (2*n +1))//6

if __name__ == "__main__":
    print(difference_of_sums(10))  # Expected: 2640
    print(difference_of_sums(3))   # Expected: 22  (36 - 14)