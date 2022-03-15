import pygame
import variables


class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self, game):
        if game.difficulty == 1:
            pygame.draw.rect(self.game.screen,
                             variables.BLUE_BACKGROUND,
                             pygame.Rect(self.x, self.y, 8, 16))
            self.y += -2
        elif game.difficulty == 4:
            pygame.draw.rect(self.game.screen,
                             variables.WHITE_BACKGROUND,
                             pygame.Rect(self.x, self.y, 2, 4))
            self.y += -2
        else:
            pygame.draw.rect(self.game.screen,
                             variables.BLUE_BACKGROUND,
                             pygame.Rect(self.x, self.y, 2, 4))
            self.y += -2
