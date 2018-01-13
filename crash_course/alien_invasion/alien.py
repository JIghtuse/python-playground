import pygame
from pygame.sprite import Sprite

ALIEN_IMAGE_PATH = 'images/alien.bmp'


class Alien(Sprite):
    """Single alien in the fleet"""

    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load(ALIEN_IMAGE_PATH)
        self.rect = self.image.get_rect()

        # Start each new alien near th etop left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
