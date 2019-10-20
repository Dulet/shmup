import pygame
from pygame.sprite import Sprite
import random
powerups = ['autofire', 'pierce', 'bullet', 'speed', "double", "triple"]
weights = [2, 2, 0, 2, 1, 0.7]

class Powerup(Sprite):

    def __init__(self, ai_settings, screen, images):
        super(Powerup, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = random.choices(powerups, weights, k=1)
        print(self.type)
        self.image = images.powerup_images[self.type[0]]
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