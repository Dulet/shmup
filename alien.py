import pygame
import random
from bullet import Bullet
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent alien, shocking huh?"""

    def __init__(self, ai_settings, screen):
        """let us begin making this hellish alien"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the god damn alien from the image
        self.image = pygame.image.load("images/alienred.png")
        self.rect = self.image.get_rect()

        # start new alien from top left of the screen
        self.rect.x = random.randint(35, ai_settings.screen_width-35)
        self.rect.y = random.randint(-4 * ai_settings.screen_height,
                                     -1 * ai_settings.screen_height)


        # store the aliens position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.health = 10

    def blitme(self):
        """draw alien on le screen"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
        # self.y += random.randint(self.ai_settings.alien_speed, 2*self.ai_settings.alien_speed)
        self.y += self.ai_settings.alien_speed
        self.rect.x = self.x
        self.rect.y = self.y
