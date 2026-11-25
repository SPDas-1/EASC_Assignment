import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 1].plot([1, 2, 3], [2, 4, 6])
ax[1, 0].plot([1, 2, 3], [1, 8, 27])
ax[1, 1].plot([1, 2, 3], [3, 6, 9])

plt.show()