import pygame
from Tile import Tile


class Layer(object):
    def __init__(self, index, map_object):
        # Layer index from tiled map
        self.index = index

        # Create group of tiles for this layer
        self.tiles = pygame.sprite.Group()

        # Reference map object
        self.mapObject = map_object

        # Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(Tile(image=img, x=(x * self.mapObject.tilewidth), y=(y * self.mapObject.tileheight)))

    # Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)
