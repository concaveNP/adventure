import pygame
from Game import Game
from Settings import Settings


def main():

    # Pull in the settings for overall game setup
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    done = False
    game = Game()

    # Main game loop for event processing
    while not done:
        done = game.process_events()
        game.run_logic()
        game.draw(screen)
        clock.tick(settings.CLOCK_TICK_SPEED)

    pygame.quit()


main()
