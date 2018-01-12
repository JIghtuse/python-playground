import sys

import pygame

DISPLAY_MODE = 1920, 1080
PROGRAM_NAME = "Printing Keys"
BACKGROUND_COLOR = 255, 255, 255

pygame.init()

screen = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption(PROGRAM_NAME)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)

    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
