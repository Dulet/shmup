import pygame


class Images():

    def __init__(self):
        self.bullet = pygame.image.load("images/bullet1.png")
        self.bullet1 = pygame.image.load("images/bullet2.png")
        self.bullet2 = pygame.image.load("images/bullet3.png")
        self.bullet21 = pygame.image.load("images/bullet32.png")
        self.bullet22 = pygame.image.load("images/bullet33.png")
        self.ship = pygame.image.load('images/ship.png')
        self.alien = pygame.image.load("images/alieneasy2.1.png")
        self.alien2 = pygame.image.load("images/alien2.1.png")
        self.star = pygame.image.load("images/star3.png")
        self.powerup_images = {}
        self.powerup_images["speed"] = pygame.image.load("images/bulletspeed.png")
        self.powerup_images["bullet"] = pygame.image.load("images/bullet.png")
        self.powerup_images["autofire"] = pygame.image.load('images/autofire.png')
        self.powerup_images["pierce"] = pygame.image.load('images/pierce.png')
        self.powerup_images["double"] = pygame.image.load("images/double.png")
        self.powerup_images["triple"] = pygame.image.load("images/triple.png")

    def default(self):
        self.bullet = pygame.image.load("images/bullet1.png")
        self.bullet1 = pygame.image.load("images/bullet2.png")
        self.bullet2 = pygame.image.load("images/bullet3.png")
        self.bullet21 = pygame.image.load("images/bullet32.png")
        self.bullet22 = pygame.image.load("images/bullet33.png")

    def pierce(self):
        self.bullet = pygame.image.load("images/laserred.png")
        self.bullet1 = pygame.image.load("images/laserred.png")
        self.bullet2 = pygame.image.load("images/laserred.png")
        self.bullet21 = pygame.image.load("images/laserred1.png")
        self.bullet22 = pygame.image.load("images/laserred2.png")