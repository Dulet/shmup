import random

from pygame.sprite import Sprite
import pygame
RED = (255, 0, 0)
class BaseAlien(Sprite):
    """skeleton body hhehe"""
    def __init__(self, ai_settings, screen, images):
        super(BaseAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # load the god damn alien from the image
        self.image = images.alien
        self.rect = self.image.get_rect()

        # start new alien from top left of the screen

        if ai_settings.aliencount < 10:
            self.rect.x = ai_settings.screen_width/2 - 35
            self.rect.y = -ai_settings.screen_height+100

        if 10 <= ai_settings.aliencount <= 30:
            self.rect.y = -ai_settings.screen_height+100
            if ai_settings.distance%2 == 0:
                self.rect.x = (ai_settings.screen_width/2) - 35 - 20*ai_settings.distance
                print(self.rect.x, "minus")
                ai_settings.distance += 1
            else:
                self.rect.x = (ai_settings.screen_width/2) - 35 + 20* ai_settings.distance
                print(self.rect.x, "plus")
                ai_settings.distance += 1
        if ai_settings.aliencount > 30:
            self.rect.y = -ai_settings.screen_height + 100
            if ai_settings.distance == 0:
                self.rect.x = ai_settings.screen_width / 2 - 35
                self.rect.y = -ai_settings.screen_height + 100
            elif ai_settings.distance % 2 == 0:
                self.rect.x = (ai_settings.screen_width / 2) - 35 - 20 * ai_settings.distance
                print(self.rect.x, "minus")
                ai_settings.distance -= 1
            elif ai_settings.distance % 2 != 0:
                self.rect.x = (ai_settings.screen_width / 2) - 35 + 20 * ai_settings.distance
                print(self.rect.x, "plus")
                ai_settings.distance -= 1



            print(ai_settings.aliencount, "aliens: ")
        # else:
        #     self.rect.x = random.randint(35, ai_settings.screen_width-35)
        #     self.rect.y = random.randint(-4 * ai_settings.screen_height,
        #                                  -1 * ai_settings.screen_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.radius = 20
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

    def blitme(self, aliencount):
        """draw alien on screen"""
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

    def points(self):
        return self.points()

    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.kill()


class Alien(BaseAlien):
    def __init__(self, ai_settings, screen, images):
        super().__init__(ai_settings, screen, images)

        self.image = images.alien
        self.health = ai_settings.alien_health
        self.points = ai_settings.alien_points


class Alien2(BaseAlien):
    def __init__(self, ai_settings, screen, images):
        super().__init__(ai_settings, screen, images)

        self.image = images.alien2
        self.health = ai_settings.alien2_health
        self.points = ai_settings.alien2_points
