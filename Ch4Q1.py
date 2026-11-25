import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.set_facecolor('lightyellow')

ax = fig.add_subplot(111)
ax.set_facecolor('lightblue')

x = np.linspace(-5, 5, 100)
ax.plot(x, x**2)

plt.show()