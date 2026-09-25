import random

import pygame

from scripts.utils import tile_to_pixel


class PlayerEntity:
    def __init__(self, game):
        self.game = game
        self.head_asset = self.game.assets["player"]["player_head.png"]
        self.body_asset = self.game.assets["player"]["player_body.png"]
        self.tail_asset = self.game.assets["player"]["player_tail.png"]
        self.current_head = self.head_asset

        # fmt: off
        self.body = [
            (5, 7), 
            (4, 7), 
            (3, 7),
        ]
        # fmt: on

    def update(self, movement=(0, 0), grow=False):
        """Update the player position."""
        old_body = self.body[:]

        new_x_pos = self.body[0][0] + movement[0]
        new_y_pos = self.body[0][1] + movement[1]
        new_head_pos = (new_x_pos, new_y_pos)

        if (
            0 <= new_x_pos <= self.game.TILES_X - 1
            and 0 <= new_y_pos <= self.game.TILES_Y - 1
        ):
            if new_head_pos not in old_body:
                self.body[0] = new_head_pos

                if grow is True:
                    self.body.append(old_body[-1])

                for i, pos in enumerate(old_body[:-1]):
                    self.body[i + 1] = pos
            else:
                return True

    def rotate_head(self, movement=(0, 0)):
        if movement == [0, -1]:
            self.current_head = pygame.transform.rotate(self.head_asset, 90)
        elif movement == [0, 1]:
            self.current_head = pygame.transform.rotate(self.head_asset, 270)
        elif movement == [-1, 0]:
            self.current_head = pygame.transform.rotate(self.head_asset, 180)
        else:
            self.current_head = self.head_asset

    def render(self, surface):
        for i, segment in enumerate(self.body):
            pixel_pos = tile_to_pixel(segment, self.game.TILE_SIZE)

            if i == 0:
                asset = self.current_head
            elif i == len(self.body) - 1:
                asset = self.tail_asset
            else:
                asset = self.body_asset

            surface.blit(asset, pixel_pos)


class FoodEntity:
    def __init__(self, game, food_type, pos):
        self.game = game
        self.food_type = food_type
        self.pos = tuple(pos)

    def respawn(self):
        """Update the food position."""
        while True:
            new_x_pos = random.randint(0, self.game.TILES_X - 1)
            new_y_pos = random.randint(0, self.game.TILES_Y - 1)
            new_pos = (new_x_pos, new_y_pos)
            if new_pos not in self.game.player.body:
                break

        self.pos = new_pos

    def render(self, surface):
        pixel_pos = tile_to_pixel(self.pos, self.game.TILE_SIZE)
        surface.blit(self.game.assets[self.food_type], pixel_pos)
