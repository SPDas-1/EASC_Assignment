import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, x**2, 'r')
ax[0, 0].set_title('y=x²')

ax[0, 1].plot(x, 2*x+1, 'g')
ax[0, 1].set_title('y=2x+1')

ax[1, 0].plot(x, np.sin(x), 'b')
ax[1, 0].set_title('y=sin(x)')

ax[1, 1].plot(x, np.cos(x), 'm')
ax[1, 1].set_title('y=cos(x)')

for a in ax.flat:
    a.set_xlabel('X-axis')
    a.set_ylabel('Y-axis')
    a.grid()

plt.tight_layout()
plt.show()