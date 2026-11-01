"""
LeafCare AI - Dataset Analysis and Visualization Module
Analyzes image dimensions and displays sample disease images across train/test/validation splits.
"""

import os
import random
from PIL import Image
import matplotlib.pyplot as plt

# Base directory of the repository
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Main dataset folder: check environment variable, default path, or relative folder
DEFAULT_CANDIDATES = [
    os.getenv("LEAF_DATASET_PATH", ""),
    os.path.join(BASE_DIR, "image data"),
    os.path.join(BASE_DIR, "leaf-disease-dataset-combination"),
    r"C:\Users\Shagun\OneDrive\Desktop\leaf disease project\image data"
]

DATASET_PATH = next((p for p in DEFAULT_CANDIDATES if p and os.path.isdir(p)), os.path.join(BASE_DIR, "image data"))

folders = ["train", "test", "validation"]


def analyze_folder(folder_path):
    """
    Scans a dataset directory, counting valid images and computing
    minimum, maximum, and average image resolutions.

    Args:
        folder_path (str): Path to folder containing image files/subdirectories.
    """
    sizes = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(root, file)
                try:
                    with Image.open(img_path) as img:
                        sizes.append(img.size)
                except Exception:
                    continue

    if sizes:
        min_size = min(sizes)
        max_size = max(sizes)
        avg_width = sum([s[0] for s in sizes]) / len(sizes)
        avg_height = sum([s[1] for s in sizes]) / len(sizes)

        print(f"\n[Folder] {folder_path}")
        print(f"Total Images: {len(sizes)}")
        print(f"Minimum Size: {min_size}")
        print(f"Maximum Size: {max_size}")
        print(f"Average Size: ({int(avg_width)}, {int(avg_height)})")
    else:
        print(f"No images found in {folder_path}")


def show_random_images(folder_path):
    """
    Samples and plots a 3x3 grid of 9 random leaf images from a split folder,
    annotating each image with its parent folder disease class label.

    Args:
        folder_path (str): Path to folder containing class-separated images.
    """
    all_images = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                all_images.append(os.path.join(root, file))

    if not all_images:
        print(f"No images available to display from {folder_path}")
        return

    sample_size = min(9, len(all_images))
    random_images = random.sample(all_images, sample_size)

    plt.figure(figsize=(10, 10))

    for i, img_path in enumerate(random_images):
        img = Image.open(img_path)
        disease = os.path.basename(os.path.dirname(img_path))

        plt.subplot(3, 3, i + 1)
        plt.imshow(img)
        plt.title(disease, fontsize=9)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"LeafCare AI - Scanning dataset at: {DATASET_PATH}")
    for folder in folders:
        target_split = os.path.join(DATASET_PATH, folder)
        if os.path.isdir(target_split):
            analyze_folder(target_split)
        else:
            print(f"Split directory not found: {target_split}")

    train_path = os.path.join(DATASET_PATH, "train")
    if os.path.isdir(train_path):
        show_random_images(train_path)
