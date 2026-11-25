import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(1, 10000, 1000)
y = x**2

ax.plot(x, y)

ax.set_xscale('log')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('y = x²')

plt.show()