import pygame.font

class Button:
    def __init__(self, settings, screen, message):
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepared only once
        self.prepare_message(message)

    def prepare_message(self, message):
        """Turn message into a rendered image and center text on the button"""
        self.message_image = self.font.render(message.upper(), True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self, screen):
        # Draw blank button and then draw message
        screen.fill(self.button_color, self.rect)
        screen.blit(self.message_image, self.message_image_rect)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))
    settings = []
    button = Button(settings, screen, "Play")
    while True:
        screen.fill((0, 0, 0))
        button.draw_button(screen)
        pygame.display.flip()
