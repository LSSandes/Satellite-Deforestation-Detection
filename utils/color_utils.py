import cv2
import numpy as np

def segment_vegetation(image):
    """Segment vegetation using HSV color thresholds."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 25, 25])   # Adjust if needed
    upper_green = np.array([86, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    segmented = cv2.bitwise_and(image, image, mask=mask)
    return segmented, mask

def calculate_green_coverage(mask):
    """Calculate green pixel percentage."""
    green_pixels = np.count_nonzero(mask)
    total_pixels = mask.size
    coverage = (green_pixels / total_pixels) * 100
    return coverage
