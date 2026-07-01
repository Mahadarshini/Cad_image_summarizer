import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load images
before = cv2.imread("dataset/pair001/before.png")
after = cv2.imread("dataset/pair001/after.png")

# Convert to grayscale
gray_before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
gray_after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# Compute SSIM
score, diff = ssim(gray_before, gray_after, full=True)
diff = (diff * 255).astype("uint8")

print(f"SSIM Score: {score:.4f}")

# Threshold the difference image
thresh = cv2.threshold(
    diff,
    0,
    255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
)[1]

# Remove tiny noise
kernel = np.ones((3, 3), np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

changed_area = 0

for contour in contours:

    area = cv2.contourArea(contour)

    if area < 30:
        continue

    changed_area += area

    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(
        after,
        (x, y),
        (x+w, y+h),
        (0, 0, 255),
        2
    )

# Percentage changed
total_area = before.shape[0] * before.shape[1]
percentage = (changed_area / total_area) * 100

print(f"Changed Area : {changed_area:.2f}")
print(f"Changed % : {percentage:.2f}%")

# Save outputs
cv2.imwrite("outputs/difference_mask.png", thresh)
cv2.imwrite("outputs/highlighted_changes.png", after)

print("Done!")