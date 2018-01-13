import pygame

class Ship:

    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.x_speed = settings.ship_x_speed

        # Load the ship image and get its rect
        image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bototm center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update the ship's position based on movement speed"""
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.x_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.x_speed

        # Update rect object from self.center
        self.rect.centerx = self.centerx

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.centerx = float(self.screen_rect.centerx)
        self.rect.centerx = self.screen_rect.centerx