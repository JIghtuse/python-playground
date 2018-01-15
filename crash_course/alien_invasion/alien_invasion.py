import sys
import time

import pygame
from pygame.sprite import Group

import game_stats
from button import Button
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien_fleet import AlienFleet

class AlienInvasion:
    def __init__(self):
        # Initialize pygame, settings, and screen object
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_mode)
        pygame.display.set_caption(self.settings.program_name)

        self.play_button = Button(self.settings, self.screen, "Play")

        # Create an instance to store game statistics
        self.stats = game_stats.GameStats(self.settings)

        # Make a ship, a group of bullets, and a group of aliens
        self.ship = Ship(self.settings, self.screen)
        self.bullets = Group()
        self.alien_fleet = AlienFleet(self.settings, self.screen, self.stats, self.ship)
        self.game_active = False

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        pygame.sprite.groupcollide(self.bullets, self.alien_fleet.aliens, True, True)

    def update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.background_color)

        # Redraw all bullets behind ship and aliens
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw_button(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def process_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.try_fire_bullet()
        elif event.key == pygame.K_q:
            self.sys.exit()

    def try_fire_bullet(self):
        """Fire a bullet if limit not reached yet"""
        if len(self.bullets) < self.settings.max_bullets_active:
            # Create a new bullet and add it to the bullets group
            new_bullet = Bullet(self.settings, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def process_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def process_events(self, events):
        """Respond to keypresses and mouse events"""
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
                # Starting new game if user presses play button
                if button_clicked and not self.game_active:
                    self.reset()
                    self.game_active = True
                    # Hide mouse cursor
                    pygame.mouse.set_visible(False)
            elif event.type == pygame.KEYDOWN:
                self.process_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.process_keyup_events(event)

    def reset(self):
        self.stats.reset_stats()
        self.reset_aliens_and_bullets()
        self.ship.center_ship()

    def reset_aliens_and_bullets(self):
        self.bullets.empty()
        self.alien_fleet.make_aliens()

    def hit(self):
        self.stats.ships_left -= 1
        self.reset_aliens_and_bullets()
        self.ship.center_ship()

        if self.stats.ships_left:
            time.sleep(0.5)

    def update_game_state(self):
        """Updates game state, returns True if game is still active"""
        # Returns whether
        self.ship.update()
        self.update_bullets()
        self.alien_fleet.update()
        if not self.alien_fleet:
            self.reset_aliens_and_bullets()
        if self.alien_fleet.ship_hit() or self.alien_fleet.reached_bottom():
            self.hit()
        if self.stats.ships_left == 0:
            pygame.mouse.set_visible(False)
            return False
        return True

    def run(self):
        # Start the main loop for the game
        while True:
            # Watch for keyboard and mouse events
            self.process_events(pygame.event.get())
            if self.game_active:
                self.game_active = self.update_game_state()
            self.update_screen()
