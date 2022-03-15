import pygame


class Alien:
    speed = 0

    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 20

    def draw(self, difficulty):
        pygame.draw.rect(self.game.screen,
                         (81, 43, 88),
                         pygame.Rect(self.x, self.y, self.size, self.size))
        if difficulty == 1:
            self.speed = 0.1
        elif difficulty == 2:
            self.speed = 0.25
        elif difficulty == 3:
            self.speed = 0.25
            self.size = 15
        elif difficulty == 4:
            self.speed = 0.25
            self.size = 10
        self.y += self.speed

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x - self.size and
                    self.y + self.size > rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)
