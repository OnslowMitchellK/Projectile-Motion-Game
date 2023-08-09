import pygame
import math
import time
pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

map_1_small = """                                
                                
                                
                                
                                
                    1111        
                    0000        
                                
                           11111
                          100000
                         1000000
                        10000000
                       100000000
          111         1000000000
         100011      10000000000
11111111100000011111100000000000
00000000000000000000000000000000
00000000000000000000000000000000"""

map_1 = """                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                22222222        
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            2222
                                                           21111
                                                         2111111
                                                       211111111
                                                     22111111111
                                                  22211111111111
                                                 211111111111111
2222222222222222222222222222222222222222222222222111111111111111
1111111111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111111111"""

map_1_background = pygame.image.load("airport_background.png")
map_1_background = pygame.transform.scale(map_1_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")
img1 = pygame.transform.scale(img_1, (20, 20))
img2 = pygame.transform.scale(img_2, (20, 20))

PROJECTILE_SIDE = 80
projectile = pygame.image.load("test.png")
projectile = pygame.transform.scale(projectile, (PROJECTILE_SIDE, PROJECTILE_SIDE))
projectile_rect = None
tile_rect = pygame.Rect(0, 0, 20, 20)
tile_rects = []

def make_window(width: int, height:int, caption: str) -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win

def draw_tiles(map):
    game_map = map.split("\n")
    print(game_map[6])
    x = 0
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            tile_rect.x = x * 20
            tile_rect.y = y * 20
            if tile == "1":
                window.blit(img_1, (x * 20, y * 20))
                tile_rects.append(tile_rect.copy())
            elif tile == "2":
                window.blit(img_2, (x * 20, y * 20))
                tile_rects.append(tile_rect.copy())
            x += 1
        y += 1
    pygame.display.update()


def main():
    angle = 0
    speed = 0
    launch_time = 0
    gravity = -9.81
    current = True
    shoot = False
    quit = False

    start_x = (0 - (0.25 * PROJECTILE_SIDE))
    start_y = (SCREEN_HEIGHT - (0.75 * PROJECTILE_SIDE)) - 120

    x = start_x
    y = start_y
    projectile_rect = pygame.Rect(start_x + 0.25 * PROJECTILE_SIDE, start_y + 0.25 * PROJECTILE_SIDE, 40, 40)
    pygame.draw.rect(window, "pink", projectile_rect)
    window.blit(projectile, (x, y))
    draw_tiles(map_1)
    pygame.display.update()

    clock = pygame.time.Clock()

    while not quit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_q:
                    current = False if current else True
                if event.__dict__["key"] == pygame.K_SPACE:
                    shoot = True
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
                if event.button == 4 and current and angle < 90:
                    angle += 1
                elif event.button == 5 and current and angle > 1:
                    angle -= 1
                elif event.button == 4 and not current and speed < 150:
                    speed += 5
                elif event.button == 5 and not current and speed > 1:
                    speed -= 5
        
        if shoot:
            launch_time += (1 / 10)
            x = (start_x + (speed * math.cos(math.radians(angle)) * launch_time))
            y = (start_y - ((speed * math.sin(math.radians(angle)) * launch_time) + (0.5 * gravity * launch_time ** 2)))
            for tile in tile_rects:
                if y + 0.5 * projectile.get_height() >= SCREEN_HEIGHT or projectile_rect.colliderect(tile):
                    time.sleep(0.5)
                    launch_time = 0
                    shoot = False
                    x = start_x
                    y = start_y
                    break
            window.blit(map_1_background, (0, 0))
            projectile_rect.x = (x + 0.25 * PROJECTILE_SIDE)
            projectile_rect.y = (y + 0.25 * PROJECTILE_SIDE)
            draw_tiles(map_1)
            window.blit(projectile, (x, y))
            pygame.display.update()

        pygame.display.set_caption(f"Angle: {angle} Speed: {speed}")
    pygame.quit()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Map")
window.blit(map_1_background, (0, 0))
main()
    