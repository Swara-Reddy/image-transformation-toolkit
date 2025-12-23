from src.load_image import load_grayscale_image
from src.transformations import scale, rotate, shear, reflect
from src.visualize import show_images

# Load image
image = load_grayscale_image("sample.jpg")

# Apply transformations
scaled_img = scale(image, 1.2, 1.2)
rotated_img = rotate(image, 30)
sheared_img = shear(image, 0.3, 0)
reflected_img = reflect(image)

# Visualize results
show_images(image, scaled_img, "Scaled Image")
show_images(image, rotated_img, "Rotated Image")
show_images(image, sheared_img, "Sheared Image")
show_images(image, reflected_img, "Reflected Image")
