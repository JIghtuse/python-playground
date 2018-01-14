import pygame
from pygame.sprite import Sprite, Group

SHIP_IMAGE_PATH = 'images/ship.png'
PROGRAM_NAME = 'Sideways shooter'

DISPLAY_MODE = 1920, 1080
BULLET_WIDTH = 30
BULLET_HEIGHT = 6

BACKGROUND_COLOR = 230, 230, 230
BULLET_COLOR = 60, 60, 60

SHIP_Y_SPEED = 5
BULLET_X_SPEED = 2


class Bullet(Sprite):
    def __init__(self, ship_rect):
        super().__init__()
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.rect.centerx = ship_rect.centerx
        self.rect.centery = ship_rect.centery
        self.rect.right = ship_rect.right

        self.x = float(self.rect.x)

    def draw(self, screen):
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)

    def update(self):
        self.x += BULLET_X_SPEED
        self.rect.x = self.x


class Ship:
    def __init__(self, screen):
        self.image = pygame.image.load(SHIP_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.moving_down = False
        self.moving_up = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top - SHIP_Y_SPEED > 0:
            self.rect.centery -= SHIP_Y_SPEED
        if self.moving_down and self.rect.bottom + SHIP_Y_SPEED < self.screen_rect.bottom:
            self.rect.centery += SHIP_Y_SPEED


class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_MODE)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(PROGRAM_NAME)
        self.ship = Ship(self.screen)
        self.running = False
        self.bullets = Group()

    def process_keydown(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def process_keyup(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def fire_bullet(self):
        self.bullets.add(Bullet(self.ship.rect))

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.process_keydown(event)
            elif event.type == pygame.KEYUP:
                self.process_keyup(event)

    def update(self):
        self.ship.update()
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for bullet in self.bullets.sprites():
            bullet.draw(self.screen)
        self.ship.draw(self.screen)

        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.process_events()
            self.update()
            self.draw()


shooter = SidewaysShooter()
shooter.run()
