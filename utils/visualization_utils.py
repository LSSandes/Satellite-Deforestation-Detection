import cv2
import matplotlib.pyplot as plt

def plot_histograms(image, output_path):
    """Plot and save BGR and HSV histograms."""
    color = ('b', 'g', 'r')
    plt.figure(figsize=(12, 5))
    
    # BGR Histogram
    plt.subplot(1, 2, 1)
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
    plt.title("BGR Histogram")
    plt.xlabel("Pixel Intensity"); plt.ylabel("Count")
    
    # HSV Histogram
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    plt.subplot(1, 2, 2)
    for i, col in enumerate(['Hue', 'Saturation', 'Value']):
        hist = cv2.calcHist([hsv], [i], None, [256], [0, 256])
        plt.plot(hist, label=col)
    plt.legend(); plt.title("HSV Histogram")
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def display_and_save_results(original, segmented, coverage, output_path):
    """Show original and segmented images side by side, save to output."""
    plt.figure(figsize=(10, 5))
    plt.suptitle(f"Green Coverage: {coverage:.2f}%", fontsize=14)
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("Original Image"); plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
    plt.title("Segmented Vegetation"); plt.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
