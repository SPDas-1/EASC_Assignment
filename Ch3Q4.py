import numpy as np

img = np.random.randint(0, 256, (6, 6))

binary = (img >= 128).astype(int)

print("Binary Image:\n", binary)
print("Maximum:", np.max(img))
print("Minimum:", np.min(img))
print("Average:", np.mean(img))

print("Central 4x4:\n", img[1:5, 1:5])

bright = np.clip(img + 30, 0, 255)
print("Enhanced 6x6 Image:\n", bright)