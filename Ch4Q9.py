import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, x**2)
ax[1, 1].plot(x, x**3)

plt.show()