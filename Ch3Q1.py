import numpy as np

theta = np.linspace(0, 360, 9)
V = 230 * np.sin(np.radians(theta))

print("Angles:", theta)
print("Voltage:", V)