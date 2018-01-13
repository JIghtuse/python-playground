import pygame
from pygame.sprite import Group

import game_functions
from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.program_name)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    game_functions.create_fleet(settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        game_functions.process_events(pygame.event.get(), settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(settings, screen, ship, aliens, bullets)

run_game()
