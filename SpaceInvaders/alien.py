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
        self.life = 2

    def draw(self, difficulty):
        if difficulty == 1:
            self.speed = 0.15
            self.size = 25
        elif difficulty == 2:
            self.speed = 0.15
        elif difficulty == 3:
            self.speed = 0.17
        elif difficulty == 4:
            self.speed = 0.20
            self.size = 15
        pygame.draw.rect(self.game.screen,
                         self.color,
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += self.speed

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x - self.size and
                    self.y + self.size > rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                if self.life > 1:
                    self.life = self.life - 1
                    if game.difficulty == 3:
                        self.color = variables.ORANGE_BACKGROUND
                    else:
                        self.color = variables.RED_BACKGROUND
                else:
                    game.aliens.remove(self)
                ouch = pygame.mixer.Sound(os.path.join('assets/destroy.mp3'))
                pygame.mixer.Sound.play(ouch)
                pygame.mixer.music.play(-1)
