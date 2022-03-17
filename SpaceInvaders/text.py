import pygame
import variables


class Text:
    def __init__(self, game):
        self.game = game

    def displayText(self, text, height):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 50)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.game.screen.blit(textsurface, (25, height))

    def displaySubtitle(self, text, height):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.game.screen.blit(textsurface, (25, height))

    def displayBonusWording(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 30)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.game.screen.blit(textsurface, (25, 20))

    def displayMalusWording(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 30)
        textsurface = font.render(text, False, variables.BLACK_BACKGROUND)
        self.game.screen.blit(textsurface, (25, 60))

    def displayDashWording(self, text, color, height):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 30)
        textsurface = font.render(text, False, color)
        self.game.screen.blit(textsurface, (450, height))
