"""Module to represent a Dragon in the game"""


class Dragon:

    def __init__(self, game):
        self.image = None
        self.name = ''
        self.color = ''

        self.screen = game.screen

        # Start each piece off in the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
