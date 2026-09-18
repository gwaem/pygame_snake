from scripts.utils import *


class Entity:
    def __init__(self, game, entity_type, pos, size):
        self.game = game
        self.entity_type = entity_type
        self.pos = list(pos)
        self.size = size

    def render(self, surface):
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets["apple"], pixel_pos)


class PlayerEntity(Entity):
    def __init__(self, game, entity_type, pos, size):
        super().__init__(game, entity_type, pos, size)

    def update(self, movement=(0, 0)):
        """Update the player position."""

        if movement[0] == 1 and self.pos[0] < (self.game.TILES_X - 1):
            self.pos[0] += movement[0]
        if movement[0] == -1 and self.pos[0] > 0:
            self.pos[0] += movement[0]
        if movement[1] == 1 and self.pos[1] < (self.game.TILES_Y - 1):
            self.pos[1] += movement[1]
        if movement[1] == -1 and self.pos[1] > 0:
            self.pos[1] += movement[1]

    def render(self, surface):
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets["player"]["player_head.png"], pixel_pos)
