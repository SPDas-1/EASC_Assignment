import numpy as np

marks = np.random.normal(8, 5, (50, 3))

print("Marks:\n", marks)

max_pos = np.unravel_index(np.argmax(marks), marks.shape)
min_pos = np.unravel_index(np.argmin(marks), marks.shape)

print("Maximum:", marks[max_pos], "Location:", max_pos)
print("Minimum:", marks[min_pos], "Location:", min_pos)

print("Variance:", np.var(marks))
print("Standard deviation:", np.std(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))