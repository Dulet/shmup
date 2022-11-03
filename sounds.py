import pygame
VOLUME = 0.2

class Sounds():
    def __init__(self):
        self.shipshot = pygame.mixer.Sound('sounds/single.wav')
        pygame.mixer.Sound.set_volume(self.shipshot, VOLUME)
        self.shipshot2 = pygame.mixer.Sound('sounds/double.wav')
        pygame.mixer.Sound.set_volume(self.shipshot2, VOLUME)
        self.shipshot3 = pygame.mixer.Sound('sounds/triple.wav')
        pygame.mixer.Sound.set_volume(self.shipshot3, VOLUME)
        self.boom = pygame.mixer.Sound('sounds/boom2.wav')
        pygame.mixer.Sound.set_volume(self.boom, VOLUME)
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        pygame.mixer.Sound.set_volume(self.hit, VOLUME)
        self.extrabullet = pygame.mixer.Sound('sounds/bullet.wav')
        pygame.mixer.Sound.set_volume(self.extrabullet, VOLUME)