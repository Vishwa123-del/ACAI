
def quicksort_first_pivot(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return quicksort_first_pivot(left) + [pivot] + quicksort_first_pivot(right)
def quicksort_random_pivot(arr):
    import random
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random_pivot(left) + middle + quicksort_random_pivot(right)
def quicksort_median_of_three(arr):
    if len(arr) <= 1:
        return arr
    # Select median of first, middle, and last elements
    first, middle, last = arr[0], arr[len(arr)//2], arr[-1]
    candidates = sorted([first, middle, last])
    pivot = candidates[1]
    # Remove the pivot from array to avoid duplicates in partitioning
    arr = [x for x in arr if x != pivot]
    left = [x for x in arr if x < pivot]
    middle_list = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_median_of_three(left) + middle_list + quicksort_median_of_three(right)


def quicksort_hoare_partition(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = hoare_partition(arr, low, high)
        quicksort_hoare_partition(arr, low, pi)
        quicksort_hoare_partition(arr, pi + 1, high)
    
    return arr


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]


# Test array
test_array = [90, 12, 77, 23, 5, 41, 68]

print("=" * 60)
print("QUICK SORT IMPLEMENTATION & COMPARISON")
print("=" * 60)
print(f"\nOriginal Array: {test_array}")

# Test different pivot selection strategies
print("\n1. First Pivot Strategy:")
result1 = quicksort_first_pivot(test_array.copy())
print(f"   Sorted: {result1}")

print("\n2. Random Pivot Strategy:")
result2 = quicksort_random_pivot(test_array.copy())
print(f"   Sorted: {result2}")

print("\n3. Median-of-Three Strategy:")
result3 = quicksort_median_of_three(test_array.copy())
print(f"   Sorted: {result3}")

print("\n4. Hoare Partition (In-place) Strategy:")
test_copy = test_array.copy()
result4 = quicksort_hoare_partition(test_copy)
print(f"   Sorted: {result4}")

print("\n" + "=" * 60)
print("PIVOT SELECTION STRATEGIES EXPLAINED")
print("=" * 60)
explanations = """
1. FIRST PIVOT (Simple but naive):
    - Uses the first element as pivot
    - Time: O(n²) worst case on sorted data
    - Space: O(n) for recursion stack
    - Pro: Simple implementation
    - Con: Bad performance on pre-sorted arrays

2. RANDOM PIVOT (Good average case):
    - Randomly selects a pivot element
    - Time: O(n log n) average case with high probability
    - Space: O(n) for recursion stack
    - Pro: Avoids worst-case on sorted data
    - Con: Non-deterministic, requires randomization

3. MEDIAN-OF-THREE (Balanced partitions):
    - Selects median of first, middle, last elements
    - Time: O(n log n) average case, O(n²) worst case
    - Space: O(n) for recursion stack
    - Pro: Better partition balance, deterministic
    - Con: Slightly more complex calculation

4. HOARE PARTITION (In-place, efficient):
    - Uses two-pointer approach for partitioning
    - Time: O(n log n) average case
    - Space: O(log n) only for recursion stack
    - Pro: In-place sorting, cache-friendly
    - Con: More complex logic, modifies original array

RECOMMENDATION:
For production use, the Median-of-Three or Hoare partition
strategies provide the best balance of simplicity and efficiency.
Random pivot is excellent for competitive programming.
"""

print(explanations)
