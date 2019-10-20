import game_stats as stats

class Settings():
    """A class to store settings"""

    def __init__(self):
        """here settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 800

        # alien settings
        self.alien_speed = 1.5
        self.fleet_direction = 1
        self.fleet_drop_speed = 5
        self.aliens_allowed = 15

        # alien1
        self.alien_health = 1
        self.alien_points = 50

        # alien2
        self.alien2_health = 3
        self.alien2_points = 75

        # background color
        self.bg_color = (0, 0, 15)

        # bullet level
        self.bullet_type = 1

        # bullet settings
        self.bullet1_damage = 1
        self.bullet2_damage = 2
        self.bullet3_damage = 3

        # bullet statistics
        self.bullets_allowed = 50
        self.bullet_speed_factor = 15

        # bullet aesthetics
        self.bullet_width = 1
        self.bullet_height = 3
        self.bullet_color = 10, 210, 92

        # autofire settings
        self.fire_cooldown = 10
        self.shoot_cooldown = 10
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
        self.ship_speed_factor = 14
        self.ship_limit = 2

        # stars settings
        self.max_stars_speed = 10
        self.stars_allowed = 100

        # powerup settings
        self.powerup_allowed = 3
        self.powerup_cooldown = 5
        self.powerup_increase = 8
        self.autofire_timer = 0
        self.pierce_timer = 0
        self.pierce = 0

    def default_settings(self):
        self.next_level = 1
        self.alien_speed = 1
        self.aliens_allowed = 20
        self.alien_speed = 1
        self.frame_count = 0
        self.bullet_type = 1
        self.next_level = 1
        self.bullet_speed_factor = 5
        self.bullets_allowed = 3
        self.alien_points = 50
        self.alien2_points = 75