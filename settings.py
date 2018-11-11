import random

class Settings():
    """A class to store settings"""

    def __init__(self):
        """here settings"""
        # screen settings
        self.screen_width = 600
        self.screen_height = 800

        # alien settings
        self.alien_speed = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.aliens_allowed = 20

        # background color
        self.bg_color = (0, 0, 15)

        # bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 1
        self.bullet_height = 3
        self.bullet_color = 10, 210, 92
        self.bullets_allowed = 5
        self.fire_cooldown = 0
        self.shoot_cooldown = 5
        self.autofire = False

        # level settings
        self.next_level = 1

        # score settings
        self.alien_points = 50

        # time settings
        self.frame_count = 0
        self.total_seconds = 0

        # ship settings
        self.ship_invulnerability = 200
        self.counter = 0
        self.ship_speed_factor = 10
        self.ship_limit = 3

        # stars settings
        self.max_stars_speed = 10
        self.stars_allowed = 100

        # powerup settings
        self.powerup_allowed = 1
        self.autofire_timer = 0
        self.pierce_timer = 0
        self.pierce = 0


    def default_settings(self):
        self.next_level = 1
        self.alien_points = 50
        self.alien_speed = 2
        self.aliens_allowed = 20
        self.alien_speed = 1
        self.frame_count = 0
        self.next_level = 1
        self.bullet_speed_factor = 10
        self.bullets_allowed = 5