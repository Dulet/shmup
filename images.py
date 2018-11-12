import pygame


class Images():

    def __init__(self):
        self.bullet = pygame.image.load("images/laserblue.png")
        self.ship = pygame.image.load('images/ship2.png')
        self.alien = pygame.image.load("images/alienred.png")
        self.alien2 = pygame.image.load("images/alien2.png")
        self.powerup_images = {}
        self.powerup_images["speed"] = pygame.image.load("images/a.png")
        self.powerup_images["bullet"] = pygame.image.load("images/b.png")
        self.powerup_images["autofire"] = pygame.image.load('images/dogeup.png')
        self.powerup_images["pierce"] = pygame.image.load('images/ab.png')