import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_title('Main Sine Wave')

inset = ax.inset_axes([0.55, 0.55, 0.35, 0.35])
inset.plot(x, y)

inset.set_xlim(2, 4)
inset.set_title('Zoomed View')

plt.show()