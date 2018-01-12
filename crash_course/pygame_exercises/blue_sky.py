import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Blue Sky")

character = pygame.image.load('images/man-running.png')
character = pygame.transform.scale(character, (300, 300))
character_rect = character.get_rect()
screen_rect = screen.get_rect()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))
    screen.blit(character, character_rect)
    character_rect.centerx = screen_rect.centerx
    character_rect.centery = screen_rect.centery
    pygame.display.flip()
