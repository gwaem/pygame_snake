import sys, random

import pygame

from scripts.utils import *
from scripts.entities import PhysicsEntity, Entity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.last_move_time = pygame.time.get_ticks()

        self.movement = [0, 0]

        self.assets = {
            "player": pygame.transform.scale(
                load_image("entities/player/player.png"), (16, 16)
            ),
            "apple": pygame.transform.scale(load_image("entities/apple.png"), (16, 16)),
            "tile_0": pygame.transform.scale(load_image("tiles/tile_0.png"), (16, 16)),
            "tile_1": pygame.transform.scale(load_image("tiles/tile_1.png"), (16, 16)),
        }

        self.player = PhysicsEntity(self, "player", (5, 8), (16, 16))
        self.apple = Entity(
            self, "apple", (random.randint(0, 19), random.randint(0, 15)), (16, 16)
        )

        self.tilemap = Tilemap(self)

    def run(self):
        while True:
            self.current_time = pygame.time.get_ticks()
            self.display.fill((14, 219, 248))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_w, pygame.K_UP):
                        if self.movement[1] != 1:
                            self.movement = [0, -1]
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        if self.movement[1] != -1:
                            self.movement = [0, 1]
                    if event.key in (pygame.K_a, pygame.K_LEFT):
                        if self.movement[0] != 1:
                            self.movement = [-1, 0]
                    if event.key in (pygame.K_d, pygame.K_RIGHT):
                        if self.movement[0] != -1:
                            self.movement = [1, 0]
                    if event.key == pygame.K_ESCAPE:
                        terminate()

            self.tilemap.render(self.display)

            self.apple.render(self.display)

            if self.current_time - self.last_move_time >= 200:
                self.player.update(self.movement)
                self.last_move_time = self.current_time

            self.player.render(self.display)

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)


Game().run()
