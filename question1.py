import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12],
                [13,14,15,16]])
print("Matrix:")
print(arr)
print("\nShape:", arr.shape)
print("Total sum:", arr.sum())
print("Row sums:", arr.sum(axis=1))
print("Column sums:", arr.sum(axis=0))
print("Transpose:")
print(arr.T)
rows, cols = arr.shape
if rows > 1 and cols > 1:
    top = arr[0, :]
    right = arr[1:rows-1, cols-1] if rows > 2 else np.array([])
    bottom = arr[rows-1, ::-1]
    left = arr[rows-2:0:-1, 0] if rows > 2 else np.array([])
    boundary = np.concatenate((top, right, bottom, left))
    print("Boundary elements in clockwise order:")
    print(boundary)
else:
    print("Boundary traversal not defined for this shape.")