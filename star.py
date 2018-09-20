import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):

    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/star3.png')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, ai_settings.screen_width)
        self.rect.y = random.randint(-4 * ai_settings.screen_height,
                                     -1 * ai_settings.screen_height)

        self.stars_speed = ai_settings.max_stars_speed

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = random.uniform(1, self.stars_speed)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y