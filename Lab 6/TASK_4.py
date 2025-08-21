def sum_to_n(n):
    """Calculate the sum of the first n natural numbers without using a loop."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * (n + 1) // 2  # Integer division for clean result

n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers is: {sum_to_n(n)}")

# Example usage:
print(sum_to_n(10))
