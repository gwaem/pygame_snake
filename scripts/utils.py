import sys, os
from pathlib import Path

import pygame

BASE_IMAGE_PATH = Path("data/images/")


def load_image(path, tile_size):
    img = pygame.image.load(BASE_IMAGE_PATH / path).convert()
    img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (tile_size, tile_size))
    return img


def load_images(path, tile_size):
    images = {}
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH / path)):
        images[img_name] = load_image(path + "/" + img_name, tile_size)
    return images


def tile_to_pixel(pos, tile_size):
    pos = list(pos)
    new_pos = (pos[0] * tile_size), (pos[1] * tile_size)

    return new_pos


def terminate():
    pygame.quit()
    sys.exit()
