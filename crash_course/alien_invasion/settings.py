class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize game settings"""
        self.program_name = "Alien Invasion"

        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_mode = self.screen_width, self.screen_height
        self.background_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_x = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_y = 2.0
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = 60, 60, 60
        self.max_bullets_active = 3

        # Alien settings
        self.alien_speed_x = 1.0
        self.alien_speed_y = 10.0
        self.max_aliens_x = 10
        self.max_aliens_y = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.5
