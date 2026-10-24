"""
Problem: Unique Inventory Count
You are given a SORTED array of product ID codes, `inventory`. 
Remove the duplicates in-place such that each unique product ID appears exactly once. 
The relative order of the elements should be kept the same.
Return the number of unique product IDs.

Constraints:
- You must do this in O(1) extra space.
- Do NOT use `list(set(inventory))`.

Example:
Input: inventory = [101, 101, 102, 103, 103, 103]
Output: 3
Explanation: The first 3 elements of inventory are modified to be [101, 102, 103]. 
(It does not matter what is left in the array beyond the first 3 elements).
"""

def get_unique_inventory(inventory: list[int]) -> int:
    # Build your O(1) space two-pointer logic here
    if not inventory:
        return 0
    insert_idx = 1
    for i in range(1,len(inventory)):
        if inventory[i]!=inventory[i-1]:
            inventory[insert_idx]=inventory[i]
            insert_idx+=1
    return insert_idx

if __name__ == "__main__":
    arr1 = [101, 101, 102, 103, 103, 103]
    k1 = get_unique_inventory(arr1)
    print(f"Unique count: {k1}, Modified Array Prefix: {arr1[:k1]}") 
    # Expected: Unique count: 3, Modified Array Prefix: [101, 102, 103]

    arr2 = [5, 5, 5, 5]
    k2 = get_unique_inventory(arr2)
    print(f"Unique count: {k2}, Modified Array Prefix: {arr2[:k2]}") 
    # Expected: Unique count: 1, Modified Array Prefix: [5]