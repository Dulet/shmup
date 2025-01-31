import pygame
from pygame.sprite import Sprite

class BulletBase(Sprite):
    """a class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship, images):
        """create a bullet"""
        super(BulletBase, self).__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position
        self.image = images.bullet
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
        #                         ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #self.rect2.centerx = ship.rect.centerx + 50
        #self.rect2.top = ship.rect.top

        # store the bullet's position as decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #self.x1 = float(self.rect2.x)
        #self.y1 = float(self.rect2.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # randomizes the bullet color each shot
        # self.color = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
        # self.color = self.color

        self.damage = ai_settings.bullet1_damage

    def update(self):
        """move the bullet up the screen"""
        # update the decimal pos of bullet
        self.x -= self.speed_factor
        self.y -= self.speed_factor
        #self.x1 -= self.speed_factor
        #self.y1 -= self.speed_factor

        # update the rectangle pos
        self.rect.y = self.y

        # used to move vertically
        #self.rect.x = self.x

        # speeds up the bullet during flight
        self.speed_factor += 0

    def draw_bullet(self):
        """draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)
                           #(self.image, self.rect2)), doreturn = 1)


class Bullet(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)


class Bullet21(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)
        self.rect.centerx -= 10
        self.image = images.bullet1


class Bullet22(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)
        self.rect.centerx += 10
        self.image = images.bullet1


class Bullet31(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)
        self.image = images.bullet2
        # print(self.rect.centerx)


class Bullet32(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)
        self.rect.x -= self.speed_factor
        self.image = images.bullet21
        # print(self.rect.centerx)

    def update(self):
        super().update()
        self.rect.x -= self.speed_factor*0.2


class Bullet33(BulletBase):
    def __init__(self, ai_settings, screen, ship, images):
        super().__init__(ai_settings, screen, ship, images)
        self.rect.x += self.speed_factor
        self.image = images.bullet22
        # print(self.rect.centerx)

    def update(self):
        super().update()
        self.rect.x += self.speed_factor*0.2