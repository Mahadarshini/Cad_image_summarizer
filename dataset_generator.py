import cv2
import numpy as np
import os

# Create output folder
os.makedirs("dataset/pair001", exist_ok=True)

# White background
before = np.ones((600, 600, 3), dtype=np.uint8) * 255

# Draw outer plate
cv2.rectangle(before, (100, 100), (500, 500), (0, 0, 0), 3)

# Circular holes
cv2.circle(before, (180, 180), 25, (0, 0, 0), 3)
cv2.circle(before, (420, 180), 25, (0, 0, 0), 3)

# Rectangular slot
cv2.rectangle(before, (250, 300), (350, 340), (0, 0, 0), 3)

# Save before image
cv2.imwrite("dataset/pair001/before.png", before)

# Create after image
after = before.copy()

# Add a new circular hole
cv2.circle(after, (300, 430), 25, (0, 0, 0), 3)

# Save after image
cv2.imwrite("dataset/pair001/after.png", after)

print("Dataset created successfully!")