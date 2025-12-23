import numpy as np
from PIL import Image

def load_grayscale_image(path):
    """
    Loads an image and converts it to a grayscale matrix
    """
    image = Image.open(path).convert("L")
    image_array = np.array(image)
    return image_array
