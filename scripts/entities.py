import random

from scripts.utils import *


class Entity:
    def __init__(self, game, entity_type, pos):
        self.game = game
        self.entity_type = entity_type
        self.pos = list(pos)

    def render(self, surface):
        """Render the entity on a surface."""
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets[self.entity_type], pixel_pos)


class PlayerEntity(Entity):
    def __init__(self, game, pos):
        super().__init__(game, "player", pos)

    def update(self, movement=(0, 0)):
        """Update the player position."""
        new_x_pos = self.pos[0] + movement[0]
        new_y_pos = self.pos[1] + movement[1]

        # Check if new position is within the screen borders.
        if 0 <= new_x_pos <= self.game.TILES_X - 1:
            self.pos[0] = new_x_pos
        if 0 <= new_y_pos <= self.game.TILES_Y - 1:
            self.pos[1] = new_y_pos

    def render(self, surface):
        """Render the player entity on a surface."""
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets[self.entity_type]["player_head.png"], pixel_pos)


class AppleEntity(Entity):
    def __init__(self, game, pos):
        super().__init__(game, "apple", pos)

    def update(self):
        """Update the apple position."""
        self.pos[0] = random.randint(0, self.game.TILES_X - 1)
        self.pos[1] = random.randint(0, self.game.TILES_Y - 1)
