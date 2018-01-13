import pygame
from pygame.sprite import Sprite

ALIEN_IMAGE_PATH = 'images/alien.bmp'


class Alien(Sprite):
    """Single alien in the fleet"""

    def __init__(self, settings, screen, x=0, y=0):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load(ALIEN_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
