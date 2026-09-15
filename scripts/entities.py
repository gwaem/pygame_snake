import pygame

from scripts.utils import *


class Entity:
    def __init__(self, game, entity_type, pos, size):
        self.game = game
        self.entity_type = entity_type
        self.pos = list(pos)
        self.size = size

    def render(self, surface):
        pixel_pos = tile_to_pixel(self.pos)
        surface.blit(self.game.assets["apple"], pixel_pos)


class PhysicsEntity(Entity):
    def __init__(self, game, entity_type, pos, size):
        super().__init__(game, entity_type, pos, size)

    def update(self, movement=(0, 0)):
        """Update the player position."""

        if movement[0] == 1 and self.pos[0] < 19:
            self.pos[0] += movement[0]
        if movement[0] == -1 and self.pos[0] > 0:
            self.pos[0] += movement[0]
        if movement[1] == 1 and self.pos[1] < 14:
            self.pos[1] += movement[1]
        if movement[1] == -1 and self.pos[1] > 0:
            self.pos[1] += movement[1]

    def render(self, surface):
        pixel_pos = tile_to_pixel(self.pos)
        surface.blit(self.game.assets["player"], pixel_pos)
