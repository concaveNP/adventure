import pygame
from Settings import Settings
from Level import Level
from Player import Player


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):

        # Get the game settings
        self.settings = Settings()

        # Set up a level to load
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(file_name="tilemap/gold_castle.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]

        # Create a player object and set the level it is in
        self.player = Player(x=self.settings.INITIAL_PLAYER_POSITION__X, y=self.settings.INITIAL_PLAYER_POSITION__Y)
        self.player.currentLevel = self.currentLevel

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # Get keyboard input and move player accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    self.player.goUp()
                elif event.key == pygame.K_DOWN:
                    self.player.goDown()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()
                elif event.key == pygame.K_UP and self.player.changeY < 0:
                    self.player.stop()
                elif event.key == pygame.K_DOWN and self.player.changeY > 0:
                    self.player.stop()

        return False

    def run_logic(self):
        # Update player movement and collision logic
        self.player.update()

    # Draw level, player, overlay
    def draw(self, screen):
        screen.fill(self.settings.BACKGROUND)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        pygame.display.flip()
