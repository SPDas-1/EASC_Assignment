import numpy as np

F = np.array([10, 20, 30])
r = np.array([2, 3, 1])
d = np.array([3, 1, 2])

torque = np.cross(r, F)
print("Torque magnitude:", np.linalg.norm(torque))

work = np.dot(F, d)
print("Work done:", work, "J")

angle = np.degrees(np.arccos(
    np.dot(F, d) / (np.linalg.norm(F) * np.linalg.norm(d))
))
print("Angle:", angle)

print("Work is positive" if work > 0 else "Work is negative")