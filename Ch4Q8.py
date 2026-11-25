import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig = plt.figure()

ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(x, x)

ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(x, x**2)

ax3 = fig.add_subplot(3, 1, 3)
ax3.plot(x, x**3)

plt.show()