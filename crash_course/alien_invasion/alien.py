import pygame
from pygame.sprite import Sprite

ALIEN_IMAGE_PATH = 'images/alien.bmp'


class Alien(Sprite):
    """Single alien in the fleet"""

    def __init__(self, settings, speed_x, screen, x, y, move_direction):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.speed_x = speed_x

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load(ALIEN_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_direction = move_direction

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def is_at_the_edge(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        """Move the alien right"""
        self.x += self.speed_x * self.move_direction
        self.rect.x = self.x
