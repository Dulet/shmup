import game_functions as gf
import pygame
import math

RED = (255, 0, 0)
class Ship:

    def __init__(self, ai_settings, screen, images):
        """get a ship and set its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get the rectangle of it
        self.image = images.ship
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # draw the ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.radius = 25

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False # autofire if true

        # Ship speed attributes
        self.current_speed = ai_settings.ship_speed_factor # Current speed
        self.base_speed = ai_settings.ship_speed_factor # Base speed
        self.max_speed = ai_settings.max_speed # Max speed
        self.acceleration = ai_settings.ship_acceleration # Acceleration

    def update(self, bullets, ai_settings, screen, ship, sounds, images):
        """update the ship movement depending on keypress"""
        moving_any = self.moving_right or self.moving_left or self.moving_up or self.moving_down

        if moving_any:
            # accelerate if current speed is less than max speed
            if self.current_speed < self.max_speed:
                self.current_speed *= self.acceleration
                if self.current_speed > self.max_speed: # cap at max speed
                    self.current_speed = self.max_speed
        else:
            self.current_speed = self.base_speed

        dx = 0
        dy = 0

        if self.moving_right:
            dx += self.current_speed
        if self.moving_left:
            dx -= self.current_speed
        if self.moving_up:
            dy -= self.current_speed
        if self.moving_down:
            dy += self.current_speed

        if dx != 0 and dy != 0:
            diagonal_factor = math.sqrt(2)
            dx /= diagonal_factor
            dy /= diagonal_factor

        self.x += dx
        self.y += dy

        if self.x < self.rect.width / 2:
            self.x = self.rect.width / 2
        elif self.x > self.screen_rect.width - self.rect.width / 2:
            self.x = self.screen_rect.width - self.rect.width / 2

        if self.y < self.rect.height / 2:
            self.y = self.rect.height / 2
        elif self.y > self.screen_rect.height - self.rect.height / 2:
            self.y = self.screen_rect.height - self.rect.height / 2

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

        if self.fire and len(bullets) < ai_settings.bullets_allowed:
            if ai_settings.fire_cooldown == ai_settings.shoot_cooldown:
                ai_settings.fire_cooldown = 0
                gf.fire_bullet(ai_settings, screen, ship, bullets, sounds, images)
            else:
                ai_settings.fire_cooldown = ai_settings.fire_cooldown + 1

    def center_ship(self):
        """Center the ship on the screen."""
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.bottom - self.rect.height / 2 #
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def blitme(self):
        """draw the ship at the created location"""
        self.screen.blit(self.image, self.rect)
        # debugging
        pygame.draw.circle(self.image, (255, 0, 255), self.rect.center, 25)