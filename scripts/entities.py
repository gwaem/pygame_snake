import random

from scripts.utils import tile_to_pixel


class PlayerEntity:
    def __init__(self, game):
        self.game = game

        # fmt: off
        self.body = [
            (5, 7), 
            (4, 7), 
            (3, 7), 
        ]
        # fmt: on

    def update(self, movement=(0, 0)):
        """Update the player position."""
        new_x_pos = self.body[0][0] + movement[0]
        new_y_pos = self.body[0][1] + movement[1]
        new_head_pos = (new_x_pos, new_y_pos)

        if (
            0 <= new_x_pos <= self.game.TILES_X - 1
            and 0 <= new_y_pos <= self.game.TILES_Y - 1
        ):
            old_body = self.body[:]
            self.body[0] = new_head_pos

            for i, pos in enumerate(old_body[:-1]):
                self.body[i + 1] = pos

    def render(self, surface):
        """Render the player on the screen."""
        for segment in self.body:
            pixel_pos = tile_to_pixel(segment, self.game.TILE_SIZE)

            if segment == self.body[0]:
                asset = self.game.assets["player"]["player_head.png"]
            elif segment == self.body[-1]:
                asset = self.game.assets["player"]["player_tail.png"]
            else:
                asset = self.game.assets["player"]["player_body.png"]

            surface.blit(asset, pixel_pos)


class FoodEntity:
    def __init__(self, game, food_type, pos):
        self.game = game
        self.food_type = food_type
        self.pos = tuple(pos)

    def respawn(self):
        """Update the food position."""
        new_x_pos = random.randint(0, self.game.TILES_X - 1)
        new_y_pos = random.randint(0, self.game.TILES_Y - 1)
        self.pos = (new_x_pos, new_y_pos)

    def render(self, surface):
        """Render the food on the screen."""
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets[self.food_type], pixel_pos)
