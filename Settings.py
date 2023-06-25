class Settings:

    def __init__(self):

        # Screen size dimensions
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720

        # The title of the game shown in the containing window
        self.TITLE = "Adventure"

        # The rate at which the game loop process
        self.CLOCK_TICK_SPEED = 60

        # Initial play position
        self.INITIAL_PLAYER_POSITION__X = 200
        self.INITIAL_PLAYER_POSITION__Y = 200

        # Tiled map layer of tiles that you collide with
        self.MAP_COLLISION_LAYER = 1

        # Background color
        self.BACKGROUND = (170, 170, 170)
