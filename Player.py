import pygame
from SpriteSheet import SpriteSheet
from Settings import Settings


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Get the game settings
        self.settings = Settings()

        # Load the sprite sheet of frames for this player
        self.sprites = SpriteSheet("images/adventure.png")

        self.still = self.sprites.image_at((5, 24, 12, 31))

        self.image = self.still

        # Set player position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set speed and direction
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"

        # Boolean to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()

        # Players current level, set after object initialized in game constructor
        self.currentLevel = None

    def update(self):
        # Update player position by change
        self.rect.x += self.changeX

        # Get tiles in collision layer that player is now touching
        tile_hit_list = pygame.sprite.spritecollide(self,
                                                    self.currentLevel.layers[self.settings.MAP_COLLISION_LAYER].tiles,
                                                    False)

        # Move player to correct side of that block
        for tile in tile_hit_list:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right

        # Update player position by change
        self.rect.y += self.changeY

        # Get tiles in collision layer that player is now touching
        tile_hit_list = pygame.sprite.spritecollide(self,
                                                    self.currentLevel.layers[self.settings.MAP_COLLISION_LAYER].tiles,
                                                    False)

        # Move player to correct side of that block
        for tile in tile_hit_list:
            if self.changeY > 0:
                self.rect.bottom = tile.rect.top
            else:
                self.rect.top = tile.rect.bottom

        # When correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 4:
                self.runningFrame = 0
            else:
                self.runningFrame += 1

    # Move right
    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 3

    # Move left
    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -3

    def goUp(self):
        self.direction = "up"
        self.running = True
        self.changeY = -3

    def goDown(self):
        self.direction = "down"
        self.running = True
        self.changeY = 3

    # Stop moving
    def stop(self):
        self.running = False
        self.changeX = 0
        self.changeY = 0

    # Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)
