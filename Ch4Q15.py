import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

y1 = (x-3)**2
y2 = -(x-2)**2 + 8

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')

plt.fill_between(x, y1, y2, where=(y2 >= y1),
                 color='yellow', alpha=0.5)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Between Two Curves')
plt.legend()

plt.show()