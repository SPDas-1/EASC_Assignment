import numpy as np

x = np.linspace(0, np.pi, 9)
a = x[::2]

print("sin:", np.sin(a))
print("sinh:", np.sinh(a))
print("cos:", np.cos(a))
print("cosh:", np.cosh(a))