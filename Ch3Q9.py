import numpy as np

vd = np.array([12, 5])
vw = np.array([3, -2])

va = vd + vw

print("Actual velocity:", va)
print("Magnitude:", np.linalg.norm(va))

unit = va / np.linalg.norm(va)
print("Unit vector:", unit)

angle = np.degrees(np.arccos(
    np.dot(vd, va) / (np.linalg.norm(vd) * np.linalg.norm(va))
))
print("Angle:", angle)