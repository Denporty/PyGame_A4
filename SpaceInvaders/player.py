import pygame
import variables


class Player:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         variables.WHITE_BACKGROUND,
                         pygame.Rect(self.x, self.y, 16, 10))
