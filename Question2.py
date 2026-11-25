from scipy.integrate import quad

def f(x):
    return x**2

area, error = quad(f, 0, 5)

print("Area under the curve =", area)