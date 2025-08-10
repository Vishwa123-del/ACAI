import random

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    num = random.randint(0, 10)
    fact = factorial(num)
    print(f"The number is: {num}")
    print(f"The factorial of {num} is: {fact}")

if __name__ == "__main__":
    main()
