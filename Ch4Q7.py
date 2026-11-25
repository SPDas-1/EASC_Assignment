import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig = plt.figure()

functions = [x, x**2, x**3, np.sqrt(x)]

for i in range(4):
    ax = fig.add_subplot(2, 2, i+1)
    ax.plot(x, functions[i])

plt.show()