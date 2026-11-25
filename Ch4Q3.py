import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.3, 500)

y1 = np.sin(x)
y3 = np.sin(3*x)/3
y5 = np.sin(5*x)/5
y7 = np.sin(7*x)/7

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y3, label='sin(3x)/3')
plt.plot(x, y5, label='sin(5x)/5')
plt.plot(x, y7, label='sin(7x)/7')

plt.plot(x, y1+y3+y5+y7, 'k', linewidth=3, label='Sum')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.legend()
plt.show()