import os

import pygame
import variables


class Alien:
    speed = 0
    color = variables.BLUE_BACKGROUND

    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 20

    def draw(self, difficulty):
        if difficulty == 1:
            self.speed = 0.25
            self.size = 25
        elif difficulty == 2:
            self.speed = 0.3
        elif difficulty == 3:
            self.speed = 0.35
            self.size = 15
        elif difficulty == 4:
            self.speed = 0.35
            self.size = 10
        pygame.draw.rect(self.game.screen,
                         self.color,
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += self.speed

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x - self.size and
                    self.y + self.size > rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)
                ouch = pygame.mixer.Sound(os.path.join('assets/destroy.mp3'))
                pygame.mixer.Sound.play(ouch)
                pygame.mixer.music.play(-1)
