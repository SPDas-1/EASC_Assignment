import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

plt.plot(x, x**2, label='y=x²', color='red', linewidth=3)
plt.plot(x, 3*x, label='y=3x', color='green', linewidth=2)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Two Functions')
plt.show()