import random

import pygame
import variables


class Bonus:
    color = variables.GOLD_BACKGROUND

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
                if game.bonus:
                    game.rockets.remove(rocket)
                self.color = variables.RED_BACKGROUND
                if game.bonus:
                    choiceBonus = random.choice([1, 2, 3])
                    if choiceBonus == 1:
                        game.goTopBonus = True
                    elif choiceBonus == 2:
                        game.bigRocketBonus = True
                    elif choiceBonus == 3:
                        game.speedRocketBonus = True
                    game.showBonusWording = True
                    game.bonus = False
