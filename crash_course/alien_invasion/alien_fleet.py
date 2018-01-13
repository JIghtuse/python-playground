import pygame
from pygame.sprite import Group

from alien import Alien


def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    return available_space_x // (2 * alien_width)


def get_number_aliens_y(settings, alien_height, ship_height):
    """Determine the number of aliens that fit in a column"""
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    return available_space_y // (2 * alien_height)


def get_alien_x(alien_width, alien_number):
    """Gets x position where alien should be placed"""
    return alien_width + 2 * alien_width * alien_number


def get_alien_y(alien_height, row_number):
    """Gets y position where alien should be placed"""
    return alien_height + 2 * alien_height * row_number


class AlienFleet:
    def __init__(self, settings, screen, ship):
        self.move_direction = 1
        self.screen = screen
        self.settings = settings
        self.ship_height = ship.rect.height

        alien_rect = Alien(settings, screen, 0, 0, self.move_direction).rect
        self.alien_width = alien_rect.width
        self.alien_height = alien_rect.height

        self.aliens = Group()

        self.make_aliens()

    def __bool__(self):
        return bool(self.aliens)

    def make_aliens(self):
        # Create an alien and find the number of aliens in a row
        number_aliens_x = get_number_aliens_x(self.settings, self.alien_width)
        number_aliens_y = get_number_aliens_y(self.settings, self.alien_height, self.ship_height)

        # Create the fleet of aliens
        for row in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                x = get_alien_x(self.alien_width, alien_number)
                y = get_alien_y(self.alien_height, row)
                alien = Alien(self.settings, self.screen, x, y, self.move_direction)
                self.aliens.add(alien)

    def update(self):
        """Update the positions of all aliens in the fleet"""
        if any(alien.is_at_the_edge() for alien in self.aliens):
            # We should change fleet direction and drop it down
            self.move_direction *= -1
            for alien in self.aliens:
                alien.move_direction = self.move_direction
                alien.rect.y += self.settings.alien_speed_y
        self.aliens.update()

    def draw(self):
        self.aliens.draw(self.screen)
