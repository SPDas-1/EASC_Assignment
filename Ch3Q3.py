import numpy as np

t = np.random.uniform(20, 40, (8, 7))

avg = np.mean(t, axis=1)
print("Average:", avg)
print("Maximum:", np.max(t, axis=1))
print("Minimum:", np.min(t, axis=1))
print("Highest average location:", np.argmax(avg) + 1)
print("Readings above 35:", np.sum(t > 35))