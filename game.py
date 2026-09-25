import sys

import pygame

from scripts import utils
from scripts.entities import PlayerEntity, FoodEntity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        self.TILES_X = 20
        self.TILES_Y = 15
        self.TILE_SIZE = 32
        self.SCREEN_WIDTH = self.TILES_X * self.TILE_SIZE
        self.SCREEN_HEIGHT = self.TILES_Y * self.TILE_SIZE
        self.TEXTCOLOR = (0, 0, 0)
        self.BACKGROUNDCOLOR = (255, 255, 255)
        self.FPS = 60

        # Set up pygame and window
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH * 2, self.SCREEN_HEIGHT * 2)
        )
        self.display = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Set up Movement.
        self.last_move_time = pygame.time.get_ticks()
        self.movement = [1, 0]

        # Set up fonts.
        self.font = pygame.font.SysFont(None, 48)

        # Set up images.
        self.assets = {
            "player": utils.load_images("entities/player", self.TILE_SIZE),
            "apple": utils.load_image("entities/apple.png", self.TILE_SIZE),
            "tiles": utils.load_images("tiles", self.TILE_SIZE),
        }

        # Set up sounds.
        self.pickUpSound = pygame.mixer.Sound("data/sfx/pickup.wav")

        # Set up entities.
        self.player = PlayerEntity(self)
        self.apple = FoodEntity(self, "apple", (16, 7))

        # Set up tilemap.
        self.tilemap = Tilemap(self, self.TILE_SIZE)

        self.top_score = 0

    def run(self):
        # Show the "Start" screen.
        self.display.fill(self.BACKGROUNDCOLOR)
        self.draw_text(
            "Snake",
            self.font,
            self.display,
            (self.SCREEN_WIDTH / 3),
            (self.SCREEN_HEIGHT / 3),
        )
        self.draw_text(
            "Press a key to start.",
            self.font,
            self.display,
            (self.SCREEN_WIDTH / 3) - 30,
            (self.SCREEN_HEIGHT / 3) + 50,
        )
        self.screen.blit(
            pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
        )
        pygame.display.update()
        self.wait_for_player_to_press_key()

        while True:
            self.score = 0
            self.player = PlayerEntity(self)
            self.apple = FoodEntity(self, "apple", (16, 7))
            self.movement = [1, 0]
            self.last_move_time = pygame.time.get_ticks()
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

                # Respawn the apple after being eaten
                if self.apple.pos == self.player.body[0]:
                    self.player.update(self.movement, grow=True)
                    self.apple.respawn()
                    # self.pickUpSound.play()
                    self.score += 5
                self.apple.render(self.display)

                # Move the player after a given period.
                if self.current_time - self.last_move_time >= 200:
                    if self.movement != [0, 0]:
                        game_over = self.player.update(self.movement)

                        if game_over is True:
                            if self.score > self.top_score:
                                self.top_score = self.score
                            break
                        self.last_move_time = self.current_time
                self.player.render(self.display)

                self.draw_text(f"Score:{self.score}", self.font, self.display, 10, 0)
                self.draw_text(
                    f"Top Score:{self.top_score}", self.font, self.display, 200, 0
                )

                self.screen.blit(
                    pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
                )
                pygame.display.update()
                self.clock.tick(self.FPS)

            # Show the "Game Over" screen.
            self.display.fill(self.BACKGROUNDCOLOR)
            self.draw_text(
                "GAME OVER",
                self.font,
                self.display,
                (self.SCREEN_WIDTH / 3),
                (self.SCREEN_HEIGHT / 3),
            )
            self.draw_text(
                "Press a key to play again.",
                self.font,
                self.display,
                (self.SCREEN_WIDTH / 3) - 80,
                (self.SCREEN_HEIGHT / 3) + 50,
            )
            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.wait_for_player_to_press_key()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def draw_text(self, text, font, surface, x, y):
        textobj = font.render(text, 1, self.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def wait_for_player_to_press_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Pressing ESC quits.
                        self.terminate()
                    return


Game().run()
