import pygame
from random import randrange


class Timer:
    def __init__(self, timer):
        self.timer = timer

    def draw(self, game):
        if not game.menu:
            timer = pygame.time.get_ticks() / 1000
            if timer > 10:
                game.bonusSpawn = True
            if timer > randrange(5, 15):
                game.malusSpawn = True
