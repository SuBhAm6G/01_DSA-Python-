"""
Problem: Find the Dropped Packet
You receive a stream of integer packet IDs. There are exactly N packets expected, 
numbered from 0 to N. One packet was dropped.
Return the ID of the dropped packet.
Constraint: You MUST use the Bitwise XOR approach. Do not use sum().

Example:
Input: packets = [3, 0, 1] 
(N = 3, so expected IDs are 0, 1, 2, 3. The number 2 is missing).
Output: 2
"""

def find_dropped_packet(packets: list[int]) -> int:
    # Build your O(N) time, O(1) space XOR logic here
    missing = len(packets)
    for i,num in enumerate(packets):
        missing ^= i^num
    return missing

if __name__ == "__main__":
    print(find_dropped_packet([3, 0, 1]))                   # Expected: 2
    print(find_dropped_packet([0, 1, 2, 3, 4, 5, 6, 7, 9])) # Expected: 8
    print(find_dropped_packet([0]))                         # Expected: 1