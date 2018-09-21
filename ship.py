import pygame
from bullet import Bullet  #used when you want to autofire
import time #autofire

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

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False # autofire

    def update(self, bullets, ai_settings, screen, ship, sounds, images):
        """update the ship movement depending on keypress"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.screen_rect.bottom > self.rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor + 0.5
        #autofire
        if self.fire and len(bullets) < ai_settings.bullets_allowed:
            if ai_settings.fire_cooldown == ai_settings.shoot_cooldown:
                ai_settings.fire_cooldown = 0
                new_bullet = Bullet(ai_settings, screen, ship, images)
                bullets.add(new_bullet)
                sounds.fire.play()
            else:
                ai_settings.fire_cooldown = ai_settings.fire_cooldown + 1


        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at the created location"""
        self.screen.blit(self.image, self.rect)


