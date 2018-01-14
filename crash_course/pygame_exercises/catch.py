import random

import pygame

CHARACTER_IMAGE_PATH = 'images/man-running.png'
BALL_IMAGE_PATH = 'images/ball.png'
PROGRAM_NAME = 'Catch'

DISPLAY_MODE = 1920, 1080

BACKGROUND_COLOR = 230, 230, 230

CHARACTER_X_SPEED = 5
BALL_Y_SPEED = 2

MAX_FAIL_TIMES = 3


class Ball:
    def __init__(self, image, centerx, top):
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.top = top
        self.y = float(self.rect.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.y += BALL_Y_SPEED
        self.rect.y = self.y


class Character:
    def __init__(self, image, screen_rect):
        self.image = image
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect

        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.x = float(self.rect.x)

        self.moving_left = False
        self.moving_right = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left and self.rect.left - CHARACTER_X_SPEED > 0:
            self.x -= CHARACTER_X_SPEED
        if self.moving_right and self.rect.right + CHARACTER_X_SPEED < self.screen_rect.right:
            self.x += CHARACTER_X_SPEED
        self.rect.x = self.x


class Catch:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_MODE)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(PROGRAM_NAME)
        self.ball_image = pygame.image.load(BALL_IMAGE_PATH)
        self.running = False
        self.character_image = pygame.image.load(CHARACTER_IMAGE_PATH)
        self.character = Character(self.character_image, self.screen_rect)
        self.make_ball()
        self.fail_count = 0

    def process_keydown(self, event):
        if event.key == pygame.K_LEFT:
            self.character.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.character.moving_right = True

    def process_keyup(self, event):
        if event.key == pygame.K_LEFT:
            self.character.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.character.moving_right = False

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.process_keydown(event)
            elif event.type == pygame.KEYUP:
                self.process_keyup(event)

    def make_ball(self):
        ball_half_width = self.ball_image.get_rect().width / 2
        x = random.randint(ball_half_width, self.screen_rect.width - ball_half_width)
        self.ball = Ball(self.ball_image, x, self.screen_rect.top)

    def update(self):
        self.character.update()
        self.ball.update()
        if pygame.sprite.collide_rect(self.character, self.ball):
            self.make_ball()
        if self.ball.rect.top > self.screen_rect.bottom:
            self.make_ball()
            self.fail_count += 1
        if self.fail_count >= MAX_FAIL_TIMES:
            self.running = False

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.character.draw(self.screen)
        self.ball.draw(self.screen)

        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.process_events()
            self.update()
            self.draw()


catch_game = Catch()
catch_game.run()
