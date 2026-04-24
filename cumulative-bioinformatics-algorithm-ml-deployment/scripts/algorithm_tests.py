import time
import random

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < pivot]) + [x for x in arr if x == pivot] + quick_sort([x for x in arr if x > pivot])

# Timing Test
data_size = 5000
test_data = [random.uniform(0, 100) for _ in range(data_size)]

start = time.time()
sorted_data = quick_sort(test_data)
end = time.time()

print(f"Quick Sort on {data_size} biological markers took: {end - start:.5f} seconds.")
