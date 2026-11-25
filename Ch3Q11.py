import numpy as np

F = np.array([50, 30, -20])
d = np.array([4, 6, 3])

print("Force magnitude:", np.linalg.norm(F))

W = np.dot(F, d)
print("Work done:", W, "J")

print("Positive work" if W > 0 else "Negative work")

angle = np.degrees(np.arccos(
    W / (np.linalg.norm(F) * np.linalg.norm(d))
))
print("Angle:", angle)