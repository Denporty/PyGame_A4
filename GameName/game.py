import pygame
import alien
import player
import attack


class Game:
    screen = None
    aliens = []
    lost = False
    statusGame = False
    rockets = []
    win = False
    firstTry = True
    menu = True
    difficulty: 0

    def __init__(self):
        module_charge = pygame.init()
        print(module_charge)
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        done = self.statusGame
        hero = player.Player(self, 600 / 2, 400 - 20)
        generator = Generator(self)
        timer = Timer(self)
        while not done:
            print("done")
            done = self.statusGame
            if len(self.aliens) == 0:
                self.menu = True
                self.win = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka doprava
                hero.x += 2 if hero.x < 600 - 20 else 0  # prava hranice

            for event in pygame.event.get():
                timer.draw()
                if event.type == pygame.QUIT:
                    self.statusGame = True
                    self.menu = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(attack.Rocket(self, hero.x, hero.y))

            pygame.display.update()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            if not self.menu:
                for alien in self.aliens:
                    alien.draw(self.difficulty)
                    alien.checkCollision(self)
                    if alien.y > 400:
                        self.win = False
                        self.menu = True
                if not self.lost:
                    hero.draw()
                for rocket in self.rockets:
                    rocket.draw()

            if self.menu:
                print('restart')
                self.screen.fill((255, 255, 255))
                if self.win:
                    self.displayText("Thanks for playing")

                elif self.firstTry:
                    self.displayText("Press shift left for start")
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_LEFT]:  # sipka doleva
                        self.menu = False
                        self.statusGame = False
                        self.firstTry = False
                        self.difficulty = 1
                    if pressed[pygame.K_RIGHT]:
                        self.menu = False
                        self.statusGame = False
                        self.firstTry = False
                        self.difficulty = 2

                else:
                    self.displayText("Game Over")
                pygame.display.update()


    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


class Timer:
    def __init__(self, timer):
        self.timer = timer

    def draw(self):
        timer = pygame.time.get_ticks() / 1000
        if timer > 120:
            game.displayText("Press CTRL L for restart")
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LSHIFT]:
                game.statusGame = False


class Generator:
    def __init__(self, game):
        margin = 30
        width = 30
        for x in range(margin, 600 - margin, width):
            for y in range(margin, int(400 / 2), width):
                game.aliens.append(alien.Alien(game, x, y))


game = Game()
