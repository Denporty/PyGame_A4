import os
import random

import pygame
import variables


class Malus:
    color = variables.BLACK_BACKGROUND

    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 20

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         self.color,
                         pygame.Rect(self.x, self.y, 16, 10))
        self.y += 3

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x - self.size and
                    self.y + self.size > rocket.y > self.y - self.size):
                if game.malus:
                    game.rockets.remove(rocket)
                    choiceMalus = random.choice([1, 2])
                    if choiceMalus == 1:
                        game.speedPlayerMalus = True
                        print('speedPlayerMalus')
                    if choiceMalus == 2:
                        game.speedRocketMalus = True
                        print('speedRocketMalus')
                    ouch = pygame.mixer.Sound(os.path.join('assets/malus.mp3'))
                    pygame.mixer.Sound.play(ouch)
                    pygame.mixer.music.play()
                    game.showMalusWording = True
                    game.malus = False
                self.color = variables.RED_BACKGROUND
