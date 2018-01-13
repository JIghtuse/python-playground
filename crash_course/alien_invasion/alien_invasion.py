import pygame
from pygame.sprite import Group

import game_functions
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.program_name)

    # Make a ship
    ship = Ship(settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Make an alien
    alien = Alien(settings, screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        game_functions.process_events(pygame.event.get(), settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(settings, screen, ship, alien, bullets)

run_game()
