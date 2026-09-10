#[image copy.png]
def reverse_and_double(n: int) -> int:
    # Build your mathematical logic here
    is_neg = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n = n // 10
    return -reversed_num*2 if is_neg else reversed_num*2

if __name__ == "__main__":
    print(reverse_and_double(123))   # Expected: 642 (321 * 2)
    print(reverse_and_double(-45))   # Expected: -108 (-54 * 2)
    print(reverse_and_double(120))   # Expected: 42 (021 -> 21 * 2)