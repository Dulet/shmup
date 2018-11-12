import sys
import pygame
import random
import time
from bullet import Bullet
from alien import Alien, Alien2
from star import Star
from powerup import Powerup
from sounds import Sounds

clock = pygame.time.Clock()
frame_rate = 60
start_time = 90


def check_events(ai_settings, screen, stats, play_button, ship, bullets, sounds, images):
    """responds to specific keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, sounds, images)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        pygame.mouse.set_visible(False)


def check_keydown_events(event, ai_settings, screen, ship, bullets, sounds, images):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_a:
        if ai_settings.autofire:
            ship.fire = True
        else:
            fire_bullet(ai_settings, screen, ship, bullets, sounds, images)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_a:
        ship.fire = False

def update_screen(ai_settings, screen, stats, sb, stars, ship, aliens, bullets, play_button, counter, powerups, sounds):
    """update images on screen and flip on the new screen"""
     # redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    sb.show_score()
    counter.show_score()
    counter.prep_score()
    ship.blitme()
    stars.draw(screen)
    aliens.draw(screen)
    powerups.draw(screen)
    pygame.display.flip()
    level_up(ai_settings)

def fire_bullet(ai_settings, screen, ship, bullets, sounds, images):
    if len(bullets) < ai_settings.bullets_allowed:
        sounds.fire.play()
        new_bullet = Bullet(ai_settings, screen, ship, images)
        bullets.add(new_bullet)



def update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats, sounds):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions (ai_settings, screen, ship, aliens, bullets, sb, stats, sounds)
#    if len(aliens) == 0:
#        level_end(ai_settings, screen, ship, aliens, bullets)



def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, sb, stats, sounds):
    if ai_settings.pierce == 0:
        hit = pygame.sprite.groupcollide(bullets, aliens, True, False)
    else:
        hit = pygame.sprite.groupcollide(bullets, aliens, False, False)
    for bullet, aliens in hit.items():
        for alien in aliens:
            alien.damage(1)
            if alien.health < 0:
                stats.score += alien.points
                sb.prep_score()
                sounds.boom.play()
            else:
                sounds.hit.play()



def create_powerup(ai_settings, screen, powerups, images):
    number_powerup_x = ai_settings.powerup_allowed
    for powerup_amount in range(number_powerup_x):
        if len(powerups) < number_powerup_x:
            if ai_settings.frame_count/60 >= ai_settings.powerup_cooldown:
                powerup = Powerup(ai_settings, screen, images)
                powerups.add(powerup)
                print("powerup spawned")
                ai_settings.powerup_cooldown += ai_settings.powerup_increase

def update_powerup(powerups, ai_settings):
    for powerup in powerups.copy():
        if powerup.rect.bottom >= ai_settings.screen_height:
            powerups.remove(powerup)


def update_stars(stars, ai_settings):
    for star in stars.copy():
        if star.rect.bottom >= ai_settings.screen_height:
            stars.remove(star)

def create_stars(ai_settings, screen, stars):
    number_stars_x = ai_settings.stars_allowed
    for star_amount in range(number_stars_x):
        if len(stars) < number_stars_x:
            star = Star(ai_settings, screen)
            stars.add(star)

def create_alien(ai_settings, screen, aliens, images):
    number_aliens_x = ai_settings.aliens_allowed
    for alien_amount in range(number_aliens_x):
        if len(aliens) < number_aliens_x:
            alien = Alien(ai_settings, screen, images)
            alien2 = Alien2(ai_settings, screen, images)
            aliens.add(alien)
            aliens.add(alien2)


def check_aliens_bottom (screen, aliens):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            aliens.remove(alien)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, images):
    create_alien(ai_settings, screen, aliens, images)
    aliens.update()
    if pygame.sprite.spritecollide(ship, aliens, False):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        print("ooh... ooohh.... *dies*")
    check_aliens_bottom(screen, aliens)


def update_timer(ai_settings):
    total_seconds = ai_settings.frame_count // frame_rate
    ai_settings.frame_count += 1
    clock.tick(frame_rate)
    return total_seconds

def powerup_check(ship, powerups, ai_settings, images):
    hits = pygame.sprite.spritecollide(ship, powerups, True)
    for hit in hits:

        if hit.type == 'autofire':
            if not ai_settings.autofire:
                print("autofire")
                ai_settings.autofire = True
                ai_settings.bullets_allowed *= 2
                ai_settings.autofire_timer = int(ai_settings.frame_count/60)

        if hit.type == 'pierce':
            print("pierce bullet")
            ai_settings.pierce = 1
            ai_settings.pierce_timer = int(ai_settings.frame_count/60)

        if hit.type == "bullet":
            print("extra bullet")
            ai_settings.bullets_allowed += 1

        if hit.type == "speed":
            print("extra bullet speed")
            ai_settings.bullet_speed_factor += 0.5

    if ai_settings.autofire:
        if int(ai_settings.frame_count / 60) - ai_settings.autofire_timer > 5:
            print("autofire ends")
            ai_settings.autofire = False
            ai_settings.bullets_allowed /= 2
            ship.fire = False

    if ai_settings.pierce == 1:
        if int(ai_settings.frame_count / 60) - ai_settings.pierce_timer > 5:
            print("pierce ends")
            ai_settings.pierce = 0

def level_up(ai_settings):
    ai_settings.meme = int(ai_settings.frame_count/1800)
    if ai_settings.meme == ai_settings.next_level:
        print("next level")
        ai_settings.alien_points += int((ai_settings.next_level**1.2))
        ai_settings.alien2_points += int((ai_settings.next_level ** 1.2))
        ai_settings.aliens_allowed += 5
        ai_settings.alien_speed += 0.20
        ai_settings.next_level = ai_settings.next_level + 1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        print("lives left:" + str(stats.ships_left))
        aliens.empty()
        bullets.empty()
        time.sleep(0.5)
        if ai_settings.ship_invulnerability > ai_settings.counter:
            ai_settings.counter += 1

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        stats.ships_left = ai_settings.ship_limit
        aliens.empty()
        bullets.empty()
        ai_settings.default_settings()
        print("game over, score: " + str(stats.score))
        stats.reset_stats = 0
    ship.center_ship()

