import numpy as np

A = np.array([2, 1, 3])
B = np.array([1, -1, 2])
C = np.array([3, 2, -1])

print("A.B =", np.dot(A, B))

cross = np.cross(A, B)
print("A x B =", cross)

print("A.(B x C) =", np.dot(A, np.cross(B, C)))
print("(A x B).C =", np.dot(cross, C))

print("Identity verified:",
      np.dot(A, np.cross(B, C)) == np.dot(cross, C))