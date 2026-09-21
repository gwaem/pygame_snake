class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size

    def render(self, surface):
        # Render the tilemap on screen.
        for y in range(self.game.TILES_Y):
            for x in range(self.game.TILES_X):
                if (x + y) % 2 == 0:
                    tile = self.game.assets["tiles"]["tile_0.png"]
                else:
                    tile = self.game.assets["tiles"]["tile_1.png"]

                surface.blit(
                    tile,
                    (x * self.tile_size, y * self.tile_size),
                )
