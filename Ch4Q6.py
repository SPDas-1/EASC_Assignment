import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])

x = np.linspace(0, 5, 100)
ax.plot(x, x**2)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('y=x²')

plt.show()