import game_functions as gf
import pygame
import pygame
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
        global speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if speed <= ai_settings.max_speed:
                speed *= ai_settings.ship_acceleration
            self.center += speed 
            print(speed)
        elif self.moving_left and self.rect.left > 0:
            if speed <= ai_settings.max_speed:
                speed *= ai_settings.ship_acceleration
            self.center -= speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            if speed <= ai_settings.max_speed:
                speed *= ai_settings.ship_acceleration
            self.rect.centery -= speed
        elif self.moving_down and self.screen_rect.bottom > self.rect.bottom:
            if speed <= ai_settings.max_speed:
                speed *= ai_settings.ship_acceleration
            self.rect.centery += speed
        else:
            speed = ai_settings.ship_speed_factor
        # autofire
        if self.fire and len(bullets) < ai_settings.bullets_allowed:
            if ai_settings.fire_cooldown == ai_settings.shoot_cooldown:
                ai_settings.fire_cooldown = 0
                gf.fire_bullet(ai_settings, screen, ship, bullets, sounds, images)
            else:
                ai_settings.fire_cooldown = ai_settings.fire_cooldown + 1


        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at the created location"""
        self.screen.blit(self.image, self.rect)
        pygame.draw.circle(self.image, (255, 0, 255), self.rect.center, 25)


