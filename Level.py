import pytmx
from Layer import Layer


class Level(object):

    def __init__(self, file_name):
        # Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(file_name)

        # Create list of layers for map
        self.layers = []

        # Amount of level shift left/right
        self.levelShift = 0

        # Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(Layer(index=layer, map_object=self.mapObject))

    # Move layer left/right
    def shift_level(self, shift_x):
        self.levelShift += shift_x

        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shift_x

    # Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)
