def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    """Generate prime numbers between start and end (inclusive)."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get user input
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        print("Start should be less than or equal to end.")
    else:
        prime_numbers = generate_primes(start, end)
        print(f"Prime numbers between {start} and {end}:")
        print(prime_numbers)
except ValueError:
    print("Please enter valid integers.")
