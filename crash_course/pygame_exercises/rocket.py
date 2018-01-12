import sys

import pygame

DISPLAY_MODE = 1920, 1080
PROGRAM_NAME = "Rocket"
BACKGROUND_COLOR = 200, 200, 255
ROCKET_IMAGE_PATH = 'images/rocket.png'

class Rocket:
    def __init__(self, screen):
        self.rocket = pygame.image.load(ROCKET_IMAGE_PATH)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rocket_rect = self.rocket.get_rect()
        self.rocket_rect.centerx = self.screen_rect.centerx
        self.rocket_rect.centery = self.screen_rect.centery
        self.x = float(self.rocket_rect.centerx)
        self.y = float(self.rocket_rect.centery)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 4.5

    def update(self):
        if self.moving_left and self.rocket_rect.left > 0:
            self.x -= self.speed
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_up and self.rocket_rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rocket_rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rocket_rect.centerx = self.x
        self.rocket_rect.centery = self.y

    def draw(self):
        screen.blit(self.rocket, self.rocket_rect)


pygame.init()

screen = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption(PROGRAM_NAME)

rocket = Rocket(screen)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

    rocket.update()

    screen.fill(BACKGROUND_COLOR)
    rocket.draw()
    pygame.display.flip()
