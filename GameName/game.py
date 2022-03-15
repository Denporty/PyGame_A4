import pygame
import alien
import player
import attack


class Game:
    screen = None
    aliens = []
    wave = 0
    lost = False
    done = False
    rockets = []
    restart = False

    def __init__(self, width, height, wave):
        module_charge = pygame.init()
        print(module_charge)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False
        print(self.done)
        hero = player.Player(self, width / 2, height - 20)
        generator = Generator(self)
        timer = Timer(self)
        while not done:
            if len(self.aliens) == 0:
                self.displayText("Press ENTER to continue")
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LSHIFT]:  # sipka doleva
                    self.wave = self.wave + 1
                    print(self.wave)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka doprava
                hero.x += 2 if hero.x < width - 20 else 0  # prava hranice

            for event in pygame.event.get():
                timer.draw()
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(attack.Rocket(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            for alien in self.aliens:
                alien.draw(self.wave)
                alien.checkCollision(self)
                if alien.y > height:
                    self.lost = True
                    self.displayText("Game over")
            if not self.lost:
                hero.draw()
            for rocket in self.rockets:
                rocket.draw()

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
            game.displayText("Time exceeded ")


class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(alien.Alien(game, x, y))


if __name__ == '__main__':
    game = Game(600, 400, 0)
