import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad

print("SCIENTIFIC COMPUTING MODULES")
print("============================")

# 1. Vector calculations using NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\n1. Vector Calculations - NumPy")
print("Vector A:", a)
print("Vector B:", b)
print("A + B:", a + b)


# 2. Symbolic differentiation using SymPy
x = sp.symbols('x')

f = x**3 + 2*x**2 + x

derivative = sp.diff(f, x)

print("\n2. Symbolic Differentiation - SymPy")
print("Function:", f)
print("Derivative:", derivative)


# 3. Numerical integration using SciPy
def function(x):
    return x**2

area, error = quad(function, 0, 5)

print("\n3. Numerical Integration - SciPy")
print("Function: f(x) = x^2")
print("Limits: 0 to 5")
print("Area:", area)


# 4. Graphical representation using Matplotlib
x_values = np.linspace(0, 5, 100)
y_values = x_values**2

plt.figure()
plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graphical Representation of f(x) = x²")
plt.grid()
plt.show()


# 5. 3D visualization using Matplotlib
x_3d = np.linspace(-5, 5, 50)
y_3d = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x_3d, y_3d)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Surface Visualization")

plt.show()