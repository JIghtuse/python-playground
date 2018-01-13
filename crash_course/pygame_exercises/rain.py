import random
import sys

import pygame
from pygame.sprite import Group, Sprite

DISPLAY_MODE = 1920, 1080
BACKGROUND_COLOR = 0, 0, 0
RAINDROP_IMAGE_PATH = 'images/raindrop.png'


class Raindrop(Sprite):
    def __init__(self, raindrop_image, screen, x, y):
        super().__init__()
        self.image = raindrop_image
        self.screen = screen
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Rain:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.make_raindrops(self.screen)

    def get_number_of_raindrops_x(self, raindrop_x_spacing):
        space_available_x = self.screen_rect.width - raindrop_x_spacing * 2
        return space_available_x // (raindrop_x_spacing * 2)

    def get_number_of_raindrops_y(self, raindrop_y_spacing):
        space_available_y = self.screen_rect.width - raindrop_y_spacing * 2
        return space_available_y // (raindrop_y_spacing * 2)

    def make_raindrops(self, screen):
        raindrop_image = pygame.image.load(RAINDROP_IMAGE_PATH)
        raindrop_image = pygame.transform.scale(raindrop_image, (30, 30))

        raindrop_rect = raindrop_image.get_rect()

        raindrop_x_spacing = raindrop_rect.width * 2
        raindrop_y_spacing = raindrop_rect.height * 2

        number_of_raindrops_x = self.get_number_of_raindrops_x(raindrop_x_spacing)
        number_of_raindrops_y = self.get_number_of_raindrops_y(raindrop_y_spacing)

        self.raindrops = Group()
        for row_number in range(number_of_raindrops_y):
            for raindrop_number in range(number_of_raindrops_x):
                x = raindrop_x_spacing + raindrop_number * raindrop_x_spacing * 2
                y = raindrop_y_spacing + row_number * raindrop_y_spacing * 2
                # using random offsets to create a bit more realistic raindrop placing
                x += random.randint(-30, 30)
                y += random.randint(-30, 30)
                self.raindrops.add(Raindrop(raindrop_image, screen, x, y))

    def update(self):
        for raindrop in self.raindrops:
            raindrop.rect.y += 1
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top > self.screen_rect.bottom:
                self.raindrops.remove(raindrop)
        if not self.raindrops:
            self.make_raindrops(self.screen)

    def draw(self):
        for raindrop in self.raindrops.sprites():
            raindrop.blitme()

pygame.init()
screen = pygame.display.set_mode(DISPLAY_MODE)
rain = Rain(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    rain.update()
    rain.draw()
    pygame.display.flip()
