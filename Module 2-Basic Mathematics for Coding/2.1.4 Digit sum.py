#[image copy 2.png]
def single_digit_root(n: int) -> int:
    # Build your mathematical logic here
    n = abs(n)
    total = n
    while (total // 10 != 0):
        total = 0
        while(n > 0):
            total += n % 10
            n = n // 10
        n = total
    return total

if __name__ == "__main__":
    print(single_digit_root(38))    # Expected: 2 (3+8=11, 1+1=2)
    print(single_digit_root(0))     # Expected: 0
    print(single_digit_root(-1234)) # Expected: 1 (1+2+3+4=10, 1+0=1)