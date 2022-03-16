import os

import pygame
import generator
import player
import attack
import variables
import random
from random import randrange
import bonus
import timer
import malus


class Game:
    screen = None
    aliens = []
    lost = False
    statusGame = False
    rockets = []
    doublerockets = []
    win = False
    firstTry = True
    menu = True
    difficulty = 0
    backgroundColor = (0, 0, 0)
    firstWhile = True
    goTopBonus = False
    bigRocketBonus = False
    speedRocketBonus = False
    bonusSpawn = False
    bonus = True
    showBonusWording = False
    malusSpawn = False
    malus = True
    speedPlayerMalus = False
    speedRocketMalus = False
    doubleRocketBonus = False
    winSound = False
    dashEnableLeft = True
    dashEnableRight = True
    i = 0

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 720))
        self.clock = pygame.time.Clock()
        done = self.statusGame
        hero = player.Player(self, 600 / 2, 720 - 20)
        bonusAppear = bonus.Bonus(self, randrange(600), 0)
        malusAppear = malus.Malus(self, randrange(600), 0)
        generator.Generator(self)
        pygame.mixer.init()
        pygame.mixer.music.load('assets/space-invaders.mp3')
        pygame.mixer.music.play(-1)
        while not done:
            self.clock.tick(60)
            done = self.statusGame
            if len(self.aliens) == 0:
                self.menu = True
                self.win = True
                if self.winSound:
                    victory = pygame.mixer.Sound(os.path.join('assets/victory.mp3'))
                    pygame.mixer.Sound.play(victory)
                    pygame.mixer.music.play()
                    self.clock.tick(0)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                if not self.speedPlayerMalus:
                    hero.x -= 2 if hero.x > 20 else 0
                else:
                    hero.x -= 1.8 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                if not self.speedPlayerMalus:
                    hero.x += 2 if hero.x < 600 - 20 else 0
                else:
                    hero.x += 1.5 if hero.x < 600 - 20 else 0
            if self.dashEnableRight:
                if pressed[pygame.K_d]:
                    hero.x = hero.x + 100 if hero.x > 20 else 0
                    self.dashEnableRight = False
            if self.dashEnableLeft:
                if pressed[pygame.K_q]:
                    hero.x = hero.x - 100 if hero.x < 600 - 20 else 0
                    self.dashEnableLeft = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.statusGame = True
                    self.menu = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost and not self.menu:
                    self.rockets.append(attack.Rocket(self, hero.x, hero.y))
                    ouch = pygame.mixer.Sound(os.path.join('assets/rocket.mp3'))
                    pygame.mixer.Sound.play(ouch)
                    pygame.mixer.music.play()
                    if self.doubleRocketBonus:
                        self.rockets.append(attack.Rocket(self, hero.x + 6, hero.y))

            pygame.display.update()
            if not self.firstTry:
                self.screen.fill(self.backgroundColor)
            if not self.menu:
                for alien in self.aliens:
                    alien.draw(self.difficulty)
                    alien.checkCollision(self)
                    if self.goTopBonus:
                        if self.i < len(self.aliens):
                            alien.y = alien.y - 30
                            self.i = self.i + 1
                        else:
                            self.i = 0
                            self.goTopBonus = False
                    if alien.y > 720:
                        pygame.mixer.music.load('assets/game-over.mp3')
                        pygame.mixer.music.play()
                        self.win = False
                        self.menu = True
                if not self.lost:
                    wait = timer.Timer(self)
                    wait.draw(self)
                    hero.draw()
                for rocket in self.rockets:
                    rocket.draw()
                if self.malusSpawn:
                    malusAppear.draw()
                    if malus:
                        malusAppear.checkCollision(self)
                if self.bonusSpawn:
                    bonusAppear.draw()
                    if bonus:
                        bonusAppear.checkCollision(self)
                if self.showBonusWording:
                    if self.bigRocketBonus:
                        self.displayBonusWording("Big rockets")
                    elif self.speedRocketBonus:
                        self.displayBonusWording("Rockets speed")
                    elif self.doubleRocketBonus:
                        self.displayBonusWording("Double rockets")
                    else:
                        self.displayBonusWording("Invaders go back")

            if self.menu:
                randomBackground = [variables.GREEN_BACKGROUND, variables.PURPLE_BACKGROUND, variables.RED_BACKGROUND,
                                    variables.BLUE_BACKGROUND, variables.ORANGE_BACKGROUND]
                if self.firstWhile:
                    self.screen.fill(random.choice(randomBackground))
                    self.firstWhile = False
                if self.win:
                    self.screen.fill(variables.GREEN_BACKGROUND)
                    self.displayText("GG! Thanks for playing", 260)
                    self.displaySubtitle("Relaunch project for replay", 360)
                    self.winSound = True

                elif self.firstTry:
                    self.displayText("Welcome", 220)
                    self.displaySubtitle("Select difficulty:", 320)
                    self.displaySubtitle("1: easy", 355)
                    self.displaySubtitle("2: normal", 390)
                    self.displaySubtitle("3: hard", 425)
                    self.displaySubtitle("4: impossible", 460)
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:
                        self.menu = False
                        self.firstTry = False
                        self.difficulty = 1
                        self.backgroundColor = variables.GREEN_BACKGROUND
                    if pressed[pygame.K_2]:
                        self.menu = False
                        self.firstTry = False
                        self.difficulty = 2
                        self.backgroundColor = variables.ORANGE_BACKGROUND
                    if pressed[pygame.K_3]:
                        self.menu = False
                        self.firstTry = False
                        self.difficulty = 3
                        self.backgroundColor = variables.RED_BACKGROUND
                    if pressed[pygame.K_4]:
                        self.menu = False
                        self.firstTry = False
                        self.difficulty = 4
                        self.backgroundColor = variables.PURPLE_BACKGROUND

                else:
                    self.screen.fill(variables.RED_BACKGROUND)
                    self.displayText("Game Over", 220)
                    self.displaySubtitle("The invaders have got you", 320)
                    self.displaySubtitle("Relaunch project for replay", 355)
                pygame.display.update()

    def displayText(self, text, height):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 50)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.screen.blit(textsurface, (25, height))

    def displaySubtitle(self, text, height):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.screen.blit(textsurface, (25, height))

    def displayBonusWording(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('impact', 30)
        textsurface = font.render(text, False, variables.WHITE_BACKGROUND)
        self.screen.blit(textsurface, (25, 20))


game = Game()
