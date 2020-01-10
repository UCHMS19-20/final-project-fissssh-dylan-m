import sys
import random
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))

XWING_IMG = pg.Surface((25, 38))
XWING_IMG.fill((90, 120, 150))
TIE_IMG = pg.Surface((40, 24))
TIE_IMG.fill((190, 60, 50))
BG_COLOR = pg.Color('gray15')


def main():
    clock = pg.time.Clock()
    # Surfaces/images have a `get_rect` method which 
    # returns a rect with the dimensions of the image.
    player_rect = XWING_IMG.get_rect()
    player_rect.center = (300, 400)
    change_x = 0
    change_y = 0
    enemies = []
    spawn_counter = 30

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    change_x = 5
                if event.key == pg.K_a:
                    change_x = -5
            if event.type == pg.KEYUP:
                if event.key == pg.K_d and change_x > 0:
                    change_x = 0
                if event.key == pg.K_a and change_x < 0:
                    change_x = 0

        # Spawn enemies if counter <= 0 then reset it.
        spawn_counter -= 1
        if spawn_counter <= 0:
            # Append an enemy rect. You can pass the position directly as an argument.
            enemies.append(TIE_IMG.get_rect(topleft=(random.randrange(600), 0)))
            spawn_counter = 30

        # Update player_rect and enemies.
        player_rect.x += change_x
        player_rect.y += change_y
        for enemy_rect in enemies:
            enemy_rect.y += 5
            # Collision detection with pygame.Rect.colliderect.
            if player_rect.colliderect(enemy_rect):
                print('Collision!')

        # Draw everything.
        screen.fill(BG_COLOR)
        for enemy_rect in enemies:
            screen.blit(TIE_IMG, enemy_rect)
        screen.blit(XWING_IMG, player_rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()