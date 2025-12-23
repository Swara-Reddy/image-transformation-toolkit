import numpy as np
import math

def apply_transformation(image, matrix):
    height, width = image.shape
    transformed = np.zeros_like(image)

    for x in range(height):
        for y in range(width):
            original_coords = np.array([x, y])
            new_coords = matrix @ original_coords

            nx, ny = int(new_coords[0]), int(new_coords[1])

            if 0 <= nx < height and 0 <= ny < width:
                transformed[nx, ny] = image[x, y]

    return transformed


def scale(image, sx, sy):
    scaling_matrix = np.array([
        [sx, 0],
        [0, sy]
    ])
    return apply_transformation(image, scaling_matrix)


def rotate(image, angle_degrees):
    angle = math.radians(angle_degrees)
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle),  math.cos(angle)]
    ])
    return apply_transformation(image, rotation_matrix)


def shear(image, shx, shy):
    shear_matrix = np.array([
        [1, shx],
        [shy, 1]
    ])
    return apply_transformation(image, shear_matrix)


def reflect(image):
    height, width = image.shape
    reflected = np.zeros_like(image)

    for x in range(height):
        for y in range(width):
            nx = height - 1 - x   # vertical reflection
            ny = y

            reflected[nx, ny] = image[x, y]

    return reflected

