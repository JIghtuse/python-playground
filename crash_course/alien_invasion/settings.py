class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize game settings"""
        self.program_name = "Alien Invasion"

        # Screen settings
        self.screen_width = 1920
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # Ship settings
        self.ship_x_speed = 1.5

        # Bullet settings
        self.bullet_y_speed = 2
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = 60, 60, 60
        self.max_bullets_active = 3

        # Alien settings
        self.alien_speed_x = 1
        self.alien_speed_y = 10
