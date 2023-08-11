import pygame
import math
import time
from model import Enemy
LEVEL_ONE_ENEMY_NUM = 2
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


level_one_enemies = {}
for i in range(LEVEL_ONE_ENEMY_NUM):
    level_one_enemies[i] = Enemy(f"Enemy {i}", 100, 100, 25, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 40, 40)

pygame.init()

def make_window(width: int, height:int, caption: str) -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win

def main():
    PROJECTILE_SIDE = 100
    angle = 0
    speed = 0
    launch_time = 0
    gravity = -9.81
    current = True
    shoot = False
    quit = False

    window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed 0")

    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((255, 255, 255))

    projectile = pygame.image.load("test.png")
    projectile = pygame.transform.scale(projectile, (PROJECTILE_SIDE, PROJECTILE_SIDE))

    start_x = (0 - (0.25 * PROJECTILE_SIDE))
    start_y = (SCREEN_HEIGHT - (0.75 * PROJECTILE_SIDE))

    x = start_x
    y = start_y

    clock = pygame.time.Clock()

    while not quit:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_q:
                    current = False if current else True
                if event.__dict__["key"] == pygame.K_SPACE:
                    shoot = True
                    break
                #if event.__dict__["key"] == pygame.K_w:
                    #angle += 5
                #elif event.__dict__["key"] == pygame.K_a:
                    #speed -= 5
                #elif event.__dict__["key"] == pygame.K_s:
                    #angle -= 5
                #elif event.__dict__["key"] == pygame.K_d:
                    #speed += 5
            elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
                if event.button == 4 and current and angle < 90:
                    angle += 1
                elif event.button == 5 and current and angle > 1:
                    angle -= 1
                elif event.button == 4 and not current and speed < 100:
                    speed += 5
                elif event.button == 5 and not current and speed > 1:
                    speed -= 5
        
        if shoot:
            launch_time += (1 / 20)
            x = (start_x + (speed * math.cos(math.radians(angle)) * launch_time))
            y = (start_y - ((speed * math.sin(math.radians(angle)) * launch_time) + (0.5 * gravity * launch_time ** 2)))
            if y + 0.5 * projectile.get_height() >= SCREEN_HEIGHT:
                time.sleep(0.5)
                launch_time = 0
                shoot = False
                x = start_x
                y = start_y

        pygame.display.set_caption(f"Angle: {angle} Speed: {speed}")
        window.blit(background, (0, 0))
        window.blit(projectile, (x, y))
        window.blit(level_one_enemies[0].image, [SCREEN_WIDTH - level_one_enemies[0].image.get_width(), SCREEN_HEIGHT - level_one_enemies[0].image.get_height()])
        pygame.display.update()

    pygame.quit()


main()