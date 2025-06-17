import numpy as np
np.random.seed(0)
arr = np.random.uniform(0, 100, 10)
arr = np.round(arr, 2)
print("Original array of floats:")
print(arr)
sorted_arr = np.sort(arr)
alternate = []
i, j = 0, len(sorted_arr) - 1
while i <= j:
    alternate.append(sorted_arr[i])
    if i != j:
        alternate.append(sorted_arr[j])
    i += 1
    j -= 1
alternate = np.array(alternate)
print("\nSorted array (ascending):")
print(sorted_arr)
print("Alternate sorted array (min, max, ...):")
print(alternate)
