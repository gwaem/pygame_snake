import os

import pygame

BASE_IMAGE_PATH = "data/images/"


def load_image(path, tile_size):
    """Load a single image file from the data folder."""
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (tile_size, tile_size))
    return img


def load_images(path, tile_size):
    """Load multiple image files from the data folder as a sorted dictionary."""
    images = {}
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images[img_name] = load_image(path + "/" + img_name, tile_size)
    return images


def tile_to_pixel(pos, tile_size):
    """Take a tile position and transform it into a pixel position."""
    pos = list(pos)
    new_pos = (pos[0] * tile_size), (pos[1] * tile_size)
    return new_pos
