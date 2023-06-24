import pygame
import Game
import Settings


def main():

    # Pull in the settings for overall game setup
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    pygame.display.set_caption(settings.title)
    clock = pygame.time.Clock()
    done = False
    game = Game()

    # Main game loop for event processing
    while not done:
        done = game.process_events()
        game.run_logic()
        game.draw(screen)
        clock.tick(settings.clock_tick_speed)

    pygame.quit()


main()
