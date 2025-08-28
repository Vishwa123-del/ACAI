items = [3, "apple", 1, "banana", 2]
numbers = sorted([i for i in items if isinstance(i, int)])
strings = sorted([i for i in items if isinstance(i, str)])
print(numbers + strings)
