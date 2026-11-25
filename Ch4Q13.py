import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x) + np.random.normal(0, 0.2, 500)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.plot(x, y)
ax.set_title('Noisy Sine Signal')

inset = ax.inset_axes([0.55, 0.55, 0.35, 0.35])
inset.plot(x, y)

inset.set_xlim(2, 4)
inset.set_title('Enlarged View')

plt.show()