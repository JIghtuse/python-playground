import sys

import pygame

from bullet import Bullet


def process_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
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


def update_screen(settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.background_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
