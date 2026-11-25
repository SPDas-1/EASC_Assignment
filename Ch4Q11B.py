import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot([1, 2, 3], [1, 4, 9])
ax2.plot([1, 2, 3], [2, 4, 6])
ax3.plot([1, 2, 3], [1, 8, 27])
ax4.plot([1, 2, 3], [3, 6, 9])

plt.show()