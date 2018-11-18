import pygame

class Sounds():
    def __init__(self):
        self.shipshot = pygame.mixer.Sound('sounds/single.wav')
        self.shipshot2 = pygame.mixer.Sound('sounds/double.wav')
        self.shipshot3 = pygame.mixer.Sound('sounds/triple.wav')
        self.boom = pygame.mixer.Sound('sounds/boom2.wav')
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        self.extrabullet = pygame.mixer.Sound('sounds/bullet.wav')