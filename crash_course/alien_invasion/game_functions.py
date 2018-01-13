import sys

import pygame

from alien import Alien
from bullet import Bullet


def process_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        try_fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def try_fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < settings.max_bullets_active:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def process_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def process_events(events, settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            process_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            process_keyup_events(event, ship)


def update_screen(settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.background_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


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


def create_fleet(settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    alien_rect = Alien(settings, screen).rect
    alien_width = alien_rect.width
    alien_height = alien_rect.height

    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_aliens_y = get_number_aliens_y(settings, alien_height, ship.rect.height)

    # Create the fleet of aliens
    for row in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            x = get_alien_x(alien_width, alien_number)
            y = get_alien_y(alien_height, row)
            alien = Alien(settings, screen, x, y)
            aliens.add(alien)
