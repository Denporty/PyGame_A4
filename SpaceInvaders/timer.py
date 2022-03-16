import pygame

class Timer:
    def __init__(self, timer):
        self.timer = timer

    def draw(self, game):
        timer = pygame.time.get_ticks() / 1000
        if timer > 10:
            game.bonusSpawn = True