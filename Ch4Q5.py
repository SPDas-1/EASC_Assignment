import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y)
plt.annotate('(2,4)', xy=(2,4))
plt.show()