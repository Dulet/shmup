import pygame
import random
import button
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship, images):
        """create a bullet"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position
        self.image = images.bullet
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                # ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.sound = pygame.mixer.Sound("sounds/lazer.wav")

        # store the bullet's position as decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # randomizes the bullet color each shot
        # self.color = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
        self.color = self.color

    def update(self):
        """move the bullet up the screen"""
        # update the decimal pos of bullet
        self.x -= self.speed_factor
        self.y -= self.speed_factor
        # update the rectangle pos
        self.rect.y = self.y
       # self.rect.x = self.x
        # randomizes the color during flight

        # speeds up the bullet during flight
        self.speed_factor += 0

    def draw_bullet(self):
        """draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)

