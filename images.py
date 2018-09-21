import pygame


class Images():

    def __init__(self):
        self.bullet = pygame.image.load("images/laserblue.png")
        self.ship = pygame.image.load('images/ship2.png')
        self.alien = pygame.image.load("images/alienred.png")
        self.powerup_images = {}
        self.powerup_images["autofire"] = pygame.image.load('images/dogeup.png')
        self.powerup_images["pierce"] = pygame.image.load('images/upgrade.png')