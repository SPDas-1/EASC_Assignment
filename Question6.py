import numpy as np
import matplotlib.pyplot as plt

# Input measurements
data = list(map(float, input("Enter measurements separated by spaces: ").split()))

# NumPy calculations
mean = np.mean(data)
std_dev = np.std(data)

# Display results
print("\nScientific Computing Results")
print("----------------------------")
print("Measurements:", data)
print("Mean =", mean)
print("Standard Deviation =", std_dev)

# Matplotlib visualization
plt.plot(data, marker='o')
plt.xlabel("Measurement Number")
plt.ylabel("Value")
plt.title("Measurement Data")
plt.grid(True)
plt.show()