import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Define the function
def f(x):
    return x**2 + 4*x + 5


# (b) Find the minimum using SciPy
result = minimize_scalar(f)

x_min = result.x
y_min = result.fun

print("Function: f(x) = x^2 + 4x + 5")
print()
print("Minimum point:")
print("x =", round(x_min, 2))
print("Minimum value =", round(y_min, 2))


# (c) Generate x values using NumPy
x = np.linspace(-10, 5, 500)
y = f(x)


# (d) Visualize using Matplotlib
plt.plot(x, y, label="f(x)")
plt.scatter(x_min, y_min, color="red", s=80,
            label="Minimum Point")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function and Its Minimum")
plt.legend()
plt.grid(True)

plt.show()