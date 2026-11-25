import numpy as np

A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 1, 4]])

B = np.array([10, 15, 20])

print("Determinant:", np.linalg.det(A))
print("Inverse:\n", np.linalg.inv(A))

X = np.linalg.solve(A, B)

print("Solution:", X)
print("Verification:", A @ X)