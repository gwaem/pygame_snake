import sys
from pathlib import Path

import pygame

BASE_IMAGE_PATH = Path("data/images/")


def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH / path).convert()
    img.set_colorkey((255, 255, 255))
    return img


def tile_to_pixel(pos):
    pos = list(pos)
    new_pos = (pos[0] * 16), (pos[1] * 16)

    return new_pos


def terminate():
    pygame.quit()
    sys.exit()
