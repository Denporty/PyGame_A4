import alien

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