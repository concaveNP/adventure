
import pygame


class SpriteSheet(object):

    """Load the sprite sheet png"""
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {filename}")
            raise SystemExit(e)


    """Load a specific image from a specific rectangle."""
    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image
