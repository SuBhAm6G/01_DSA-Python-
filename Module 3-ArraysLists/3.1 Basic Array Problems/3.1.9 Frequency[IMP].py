"""
Problem: Most Popular Item
Given an array of integer product IDs representing recent sales, 
find and return the most frequently sold product ID (the mode).
If there is a tie (multiple products share the highest frequency), 
return the SMALLEST product ID among them.

Example:
Input: sales = [101, 103, 101, 102, 103, 105, 101, 103]
Frequencies: 101 -> 3, 103 -> 3, 102 -> 1, 105 -> 1
Output: 101 (Both 101 and 103 appear 3 times, but 101 is smaller)
"""
import collections
def most_popular_product(sales: list[int]) -> int:
    # Build your frequency map and tracking logic here
    freq = dict(collections.Counter(sales))
    max_items = []
    max_freq= max(freq.values())
    for key,val in freq.items():
        if val == max_freq:
            max_items.append(key)
    return min(max_items)

if __name__ == "__main__":
    print(most_popular_product([101, 103, 101, 102, 103, 105, 101, 103])) # Expected: 101
    print(most_popular_product([5, 5, 5, 2, 2, 2, 2]))                    # Expected: 2
    print(most_popular_product([99]))                                     # Expected: 99