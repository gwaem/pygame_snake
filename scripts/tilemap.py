import pygame


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tiles = []

        for y in range(self.game.TILES_Y):
            row = []
            for x in range(self.game.TILES_X):
                row.append(0)
            self.tiles.append(row)

    def render(self, surface):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if (x + y) % 2 == 0:
                    surface.blit(
                        self.game.assets["tiles"]["tile_0.png"],
                        (x * self.tile_size, y * self.tile_size),
                    )
                else:
                    surface.blit(
                        self.game.assets["tiles"]["tile_1.png"],
                        (x * self.tile_size, y * self.tile_size),
                    )
