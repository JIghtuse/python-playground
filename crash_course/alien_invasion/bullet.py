import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullet fired from the ship"""

    def __init__(self, settings, speed_y, screen, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_y = speed_y
        self.direction = -1

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y += self.direction * self.speed_y
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
