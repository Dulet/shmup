import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from counter import Counter
from sounds import Sounds
from images import Images
import game_functions as gf


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def run_game():
    # create a screen and launch the game
    pygame.mixer.pre_init(44100, -16, 16, 2048)
    pygame.mixer.init()
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    # make a ship, bullet, alien
    sounds = Sounds()
    images = Images()
    bullets = Group()
    aliens = Group()
    stars = Group()
    powerups = Group()
    ship = Ship(ai_settings, screen, images)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    counter = Counter(ai_settings, screen, stats)

    # create a fleet
    if stats.game_active:
        gf.create_stars(ai_settings, screen, stars)
        gf.create_powerup(ai_settings, screen, powerups)

    # main game loop

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, sounds, images)
        gf.update_screen(ai_settings, screen, stats, sb, stars, ship, aliens, bullets,
                         play_button, counter, powerups, sounds)
        if stats.game_active:
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats, sounds)
            gf.create_stars(ai_settings, screen, stars)
            gf.create_powerup(ai_settings, screen, powerups, images)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, images)
            gf.update_stars(stars, ai_settings)
            gf.update_powerup(powerups, ai_settings)
            gf.update_timer(ai_settings)
            gf.powerup_check(ship, powerups, ai_settings, images, sounds)
            bullets.update()
            stars.update()
            powerups.update()
            aliens.update()
            ship.update(bullets, ai_settings, screen, ship, sounds, images)
            screen.fill(ai_settings.bg_color)
            # screen.blit(BackGround.image, BackGround.rect)

run_game()
