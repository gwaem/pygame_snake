import sys

import pygame

from scripts import utils
from scripts.entities import PlayerEntity, FoodEntity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        # Screen initialization
        self.TILES_X = 20
        self.TILES_Y = 15
        self.TILE_SIZE = 32

        self.SCREEN_WIDTH = self.TILES_X * self.TILE_SIZE
        self.SCREEN_HEIGHT = self.TILES_Y * self.TILE_SIZE

        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH * 2, self.SCREEN_HEIGHT * 2)
        )
        self.display = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.last_move_time = pygame.time.get_ticks()

        self.movement = [1, 0]

        self.assets = {
            "player": utils.load_images("entities/player", self.TILE_SIZE),
            "apple": utils.load_image("entities/apple.png", self.TILE_SIZE),
            "tiles": utils.load_images("tiles", self.TILE_SIZE),
        }
        self.pickUpSound = pygame.mixer.Sound("data/sfx/pickup.wav")
        self.player = PlayerEntity(self)
        self.apple = FoodEntity(self, "apple", (16, 7))

        self.tilemap = Tilemap(self, self.TILE_SIZE)

    def run(self):
        while True:
            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_w, pygame.K_UP):
                        if self.movement[1] != 1:
                            self.movement = [0, -1]
                            self.player.rotate_head(self.movement)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        if self.movement[1] != -1:
                            self.movement = [0, 1]
                            self.player.rotate_head(self.movement)
                    if event.key in (pygame.K_a, pygame.K_LEFT):
                        if self.movement[0] != 1:
                            self.movement = [-1, 0]
                            self.player.rotate_head(self.movement)
                    if event.key in (pygame.K_d, pygame.K_RIGHT):
                        if self.movement[0] != -1:
                            self.movement = [1, 0]
                            self.player.rotate_head(self.movement)
                    if event.key == pygame.K_ESCAPE:
                        self.terminate()

            self.tilemap.render(self.display)

            if self.apple.pos == self.player.body[0]:
                self.player.update(self.movement, grow=True)
                self.apple.respawn()
                # self.pickUpSound.play()
            self.apple.render(self.display)

            if self.current_time - self.last_move_time >= 200:
                if self.movement != [0, 0]:
                    self.player.update(self.movement)
                    self.last_move_time = self.current_time
            self.player.render(self.display)

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)

    def terminate(self):
        """Terminate the program."""
        pygame.quit()
        sys.exit()


Game().run()
