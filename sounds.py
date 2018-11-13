import pygame

class Sounds():
    def __init__(self):

        self.fire = pygame.mixer.Sound('sounds/6.wav')
        self.boom = pygame.mixer.Sound('sounds/boom.wav')
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        self.extrabullet = pygame.mixer.Sound('sounds/bullet.wav')