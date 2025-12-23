import matplotlib.pyplot as plt

def show_images(original, transformed, title):
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(title)
    plt.imshow(transformed, cmap="gray")
    plt.axis("off")

    plt.show()
