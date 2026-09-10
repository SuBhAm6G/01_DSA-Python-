def count_digits(n: int) -> int:
    if n == 0:
        return 1
        
    n = abs(n)
    count = 0  # Blank 1: Initialize your tracking state
    
    while n > 0:   # Blank 2: What is the condition to keep the loop alive?
        n = n // 10      # Blank 3: Perform the operation to chop the last digit
        count += 1      # Blank 4: Update your state
        
    return count   # Blank 5: What is the final output?


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(f"Number of digits: {count_digits(number)}")

#[image.png]

def has_even_digits(n: int) -> bool:
    # Build your logic here without using str()
    digit_count = count_digits(n)  
    return digit_count % 2 == 0

if __name__ == "__main__":
    print(has_even_digits(4567))  # Expected: True (4 digits)
    print(has_even_digits(8))     # Expected: False (1 digit)
    print(has_even_digits(0))     # Expected: False (1 digit)
    print(has_even_digits(-99))   # Expected: True (2 digits)