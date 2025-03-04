import time
import os
import numpy as np
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor
from skimage.measure import shannon_entropy  # entropy is now called shannon_entropy
from skimage.filters import sobel, prewitt, hessian, gabor
from skimage.morphology import disk
from scipy import ndimage as nd


## The sequential version
import glob
import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt
import matplotlib.pyplot as plt
image = yes_images[0]

import time
from tqdm import tqdm


def read_images(images_path):
    """
    Reads all images from a specified path using OpenCV.

    Parameters:
        - images_path (str): The path to the directory containing the images.
    Returns:
        - images (list): A list of images read from the directory.
    """
    images = []
    for file_path in images_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
                images.append(image)
    return images


# Define the path to the dataset
dataset_path = '../data/brain_tumor_dataset/'

# List all image files in the 'yes' and 'no' directories
yes_images = glob.glob(dataset_path + 'yes/*.jpg')
no_images = glob.glob(dataset_path + 'no/*.jpg')

yes_images = read_images(yes_images)
no_images = read_images(no_images)

print(f"Number of 'yes' images: {len(yes_images)}")
print(f"Number of 'no' images: {len(no_images)}")



# Apply filters
entropy_img = entropy(image, disk(2))
gaussian_img = nd.gaussian_filter(image, sigma=1)
sobel_img = sobel(image)
gabor_img = gabor(image, frequency=0.9)[1]
hessian_img = hessian(image, sigmas=range(1, 100, 1))
prewitt_img = prewitt(image)

# Store the original and filtered images in a dictionary
filtered_images = {
    'Original': image,
    'Entropy': entropy_img,
    'Gaussian': gaussian_img,
    'Sobel': sobel_img,
    'Gabor': gabor_img,
    'Hessian': hessian_img,
    'Prewitt': prewitt_img
}

# Display each filtered image
plt.figure(figsize=(18, 3))
for i, (filter_name, filtered_image) in enumerate(filtered_images.items()):
        plt.subplot(1, len(filtered_images), i + 1)
        plt.imshow(filtered_image, cmap='gray')
        plt.title(filter_name)
        plt.axis('off')
plt.show()




# Function to process a single image
def process_single_image(image):
    return {
        'Original': image,
        'Entropy': entropy(image, disk(2)),
        'Gaussian': nd.gaussian_filter(image, sigma=1),
        'Sobel': sobel(image),
        'Gabor': gabor(image, frequency=0.9)[1],
        'Hessian': hessian(image, sigmas=[1, 5, 10]),  # Reduced range
        'Prewitt': prewitt(image)
    }

num_workers =os.cpu_count()
# Function to process images in parallel
def process_images_parallel(images):
    processed_images = []
    num_workers = os.cpu_count()  # Use all available CPU cores

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for result in tqdm(executor.map(process_single_image, images[:5]), total=5):
            processed_images.append(result)

    return processed_images

# Example usage
start_time = time.time()
yes_inputs = process_images_parallel(yes_images)
no_inputs = process_images_parallel(no_images)
end_time = time.time()

execution_time_par = end_time - start_time

