import pygame
import alien
import player
import attack
import variables
import random


class Game:
    screen = None
    aliens = []
    lost = False
    statusGame = False
    rockets = []
    win = False
    firstTry = True
    menu = True
    difficulty = 0
    backgroundColor = (0, 0, 0)
    firstWhile = True
    # timerExceeded = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 720))
        self.clock = pygame.time.Clock()
        done = self.statusGame
        hero = player.Player(self, 600 / 2, 720 - 20)
        generator = Generator(self)
        # timer = Timer(self)
        while not done:
            done = self.statusGame
            if len(self.aliens) == 0:
                self.menu = True
                self.win = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka doprava
                hero.x += 2 if hero.x < 720 - 20 else 0  # prava hranice

            for event in pygame.event.get():
                # timer.draw(self.timerExceeded)
                if event.type == pygame.QUIT:
                    self.statusGame = True
                    self.menu = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(attack.Rocket(self, hero.x, hero.y))

            pygame.display.update()
            self.clock.tick(60)
            if not self.firstTry:
                self.screen.fill(self.backgroundColor)
            if not self.menu:
                for alien in self.aliens:
                    alien.draw(self.difficulty)
                    alien.checkCollision(self)
                    if alien.y > 720:
                        self.win = False
                        self.menu = True
                if not self.lost:
                    hero.draw()
                for rocket in self.rockets:
                    rocket.draw(self)

            if self.menu:
                randomBackground = [variables.GREEN_BACKGROUND, variables.PURPLE_BACKGROUND, variables.RED_BACKGROUND, variables.BLUE_BACKGROUND, variables.ORANGE_BACKGROUND]
                if self.firstWhile:
                    self.screen.fill(random.choice(randomBackground))
                    self.firstWhile = False
                if self.win:
                    self.screen.fill(variables.GREEN_BACKGROUND)
                    self.displayText("GG! Thanks for playing", 260)
                    self.displaySubtitle("Relaunch project for replay", 360)

                elif self.firstTry:
                    self.displayText("Welcome", 220)
                    self.displaySubtitle("Select difficulty:", 320)
                    self.displaySubtitle("1: easy", 355)
                    self.displaySubtitle("2: normal", 390)
                    self.displaySubtitle("3: hard", 425)
                    self.displaySubtitle("4: impossible", 460)
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:  # sipka doleva
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


# class Timer:
#     def __init__(self, timer):
#         self.timer = timer
#
#     def draw(self, game):
#         timer = pygame.time.get_ticks() / 1000
#         if timer > 10:
#             game.timerExceeded = True


class Generator:
    def __init__(self, game):
        if game.difficulty == 4:
            margin = 20
            width = 10
        elif game.difficulty == 1:
            margin = 30
            width = 30
        else:
            margin = 30
            width = 30
        for x in range(margin, 600 - margin, width):
            for y in range(margin, int(600 / 2), width):
                game.aliens.append(alien.Alien(game, x, y))


game = Game()