import cv2
import os
from utils.color_utils import segment_vegetation, calculate_green_coverage
from utils.visualization_utils import plot_histograms, display_and_save_results

# Input and output folders
INPUT_DIR = "input"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process each image in input folder
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"\nProcessing: {filename}")
        img_path = os.path.join(INPUT_DIR, filename)
        image = cv2.imread(img_path)

        # Segmentation
        segmented, mask = segment_vegetation(image)

        # Coverage calculation
        coverage = calculate_green_coverage(mask)
        print(f"Green Coverage: {coverage:.2f}%")

        # Save histogram
        hist_output = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}_histogram.png")
        plot_histograms(image, hist_output)

        # Display + save segmented result
        result_output = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}_segmented.png")
        display_and_save_results(image, segmented, coverage, result_output)

print("\nProcessing complete! Segmented images and histograms saved in 'output/' folder.")
