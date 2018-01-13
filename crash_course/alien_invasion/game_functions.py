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


def update_screen(settings, screen, ship, alien_fleet, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.background_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien_fleet.draw()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets, aliens):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens
    # If so, get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
