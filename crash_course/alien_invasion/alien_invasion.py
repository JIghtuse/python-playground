import pygame
from pygame.sprite import Group

import game_functions
from settings import Settings
from ship import Ship
from alien_fleet import AlienFleet

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.program_name)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(settings, screen)
    bullets = Group()
    alien_fleet = AlienFleet(settings, screen, ship)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        game_functions.process_events(pygame.event.get(), settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets, alien_fleet.aliens)
        alien_fleet.update()
        game_functions.update_screen(settings, screen, ship, alien_fleet, bullets)

run_game()
