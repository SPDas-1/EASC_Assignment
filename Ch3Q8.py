import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("Dot product:", np.dot(A, B))
print("Cross product:", np.cross(A, B))
print("Dyadic product:\n", np.outer(A, B))