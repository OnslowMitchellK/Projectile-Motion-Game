# import pygame
# import math
# import time
# from model import Enemy
# from random import randint
# pygame.init()

# BLACK = (0, 0, 0)
# SCREEN_HEIGHT = 720
# SCREEN_WIDTH = 1280
# LEVEL_ONE_ENEMY_NUM = 2
# level_one_enemies = {}


# map_1_small = """                                
                                
                                
                                
                                
#                     2222        
#                     1111        
                                
#                            22222
#                           211111
#                          2111111
#                         21111111
#                        211111111
#           222         2111111111
#          211122      21111111111
# 22222222211111122222211111111111
# 11111111111111111111111111111111
# 11111111111111111111111111111111"""

# map_1 = """                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
#                          22222222222222222222222                
#                           111111111111111111111                 
#                             11111111111111111                   
#                               1111111111111                     
#                                 111111111                       
#                                 111111111                       
#                                 111111111                       
#                                1111111111                       
#                                1111111111                       
#                                111111111                       
#                                111111111                        
#            22222222222         111111111                    2222
#            11111111111           11111111                  21111
#            11111111111          111111111                2211111
#            11111111111         1111111111              221111111
#            11111111111         11111111              22111111111
#            11111111111         111111111          22211111111111
#            11111111111         1111111111         21111111111111
# 2222222222211111111111222222222211111111122222222111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111"""

# map_1_background = pygame.image.load("airport_background.png")
# map_1_background = pygame.transform.scale(map_1_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# TILE_SIZE = 20

# img_1 = pygame.image.load("tile1.png")
# img_2 = pygame.image.load("tile2.png")
# img_1 = pygame.transform.scale(img_1, (TILE_SIZE, TILE_SIZE))
# img_2 = pygame.transform.scale(img_2, (TILE_SIZE, TILE_SIZE))

# PROJECTILE_SIDE = 80
# projectile = pygame.image.load("test.png")
# projectile = pygame.transform.scale(projectile, (PROJECTILE_SIDE, PROJECTILE_SIDE))
# projectile_rect = None
# tile_rect = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
# tile_rects = []

# def make_window(width: int, height:int, caption: str)  -> pygame.Surface:
#     win = pygame.display.set_mode((width, height))
#     pygame.display.set_caption(caption)
#     return win

# def draw_tiles(map):
#     game_map = map.split("\n")
#     x = 0
#     y = 0
#     for row in game_map:
#         x = 0
#         for tile in row:
#             duplicate = False
#             tile_rect.x = x * TILE_SIZE
#             tile_rect.y = y * TILE_SIZE
#             if tile_rect.copy() in tile_rects:
#                 duplicate = True
#             if tile == "1":
#                 window.blit(img_1, (x * TILE_SIZE, y * TILE_SIZE))
#                 if not duplicate:
#                     tile_rects.append(tile_rect.copy())
#             elif tile == "2":
#                 window.blit(img_2, (x * TILE_SIZE, y * TILE_SIZE))
#                 if not duplicate:
#                     tile_rects.append(tile_rect.copy())
#             x += 1
#         y += 1
#     pygame.display.update()


# def level_one():
#     for i in range(LEVEL_ONE_ENEMY_NUM):
#         ran_x = randint(0, 600)
#         ran_y = randint(0, 400)
#         level_one_enemies[i] = Enemy(f"Enemy {i}", 100, 100, 25,
#                                      ran_x, ran_y,
#                                      40, 40, window)
#         level_one_enemies[i].draw()


# def main():
#     angle = 0
#     speed = 0
#     launch_time = 0
#     gravity = -9.81
#     current = True
#     shoot = False
#     quit = False

#     start_x = (0 - (0.25 * PROJECTILE_SIDE))
#     start_y = (SCREEN_HEIGHT - (0.75 * PROJECTILE_SIDE)) - 120

#     x = start_x
#     y = start_y
#     projectile_rect = pygame.Rect(start_x + 0.25 * PROJECTILE_SIDE, start_y + 0.25 * PROJECTILE_SIDE, 40, 40)
#     window.blit(projectile, (x, y))
#     draw_tiles(map_1)

#     level_one()

#     pygame.display.update()

#     clock = pygame.time.Clock()

#     while not quit:
#         clock.tick(60)
#         window.fill(BLACK)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 quit = True
#             elif event.type == pygame.KEYDOWN:
#                 if event.__dict__["key"] == pygame.K_q:
#                     current = False if current else True
#                 if event.__dict__["key"] == pygame.K_SPACE:
#                     shoot = True
#                     break
#             elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
#                 if event.button == 4 and current and angle < 90:
#                     angle += 1
#                 elif event.button == 5 and current and angle > 1:
#                     angle -= 1
#                 elif event.button == 4 and not current and speed < 150:
#                     speed += 5
#                 elif event.button == 5 and not current and speed > 1:
#                     speed -= 5

#         if shoot:
#             launch_time += (1 / 5)
#             x = (start_x + (speed * math.cos(math.radians(angle)) * launch_time))
#             y = (start_y - ((speed * math.sin(math.radians(angle)) * launch_time) + (0.5 * gravity * launch_time ** 2)))
#             for tile in tile_rects:
#                 if y + 0.5 * projectile.get_height() >= SCREEN_HEIGHT or projectile_rect.colliderect(tile):
#                     time.sleep(0.5)
#                     launch_time = 0
#                     shoot = False
#                     x = start_x
#                     y = start_y
#                     break
#             for i in range(len(level_one_enemies)):
#                 if projectile_rect.colliderect(level_one_enemies[i]):
#                     time.sleep(0.5)
#                     launch_time = 0
#                     shoot = False
#                     x = start_x
#                     y = start_y
#                     break
#             window.blit(map_1_background, (0, 0))
#             projectile_rect.x = (x + 0.25 * PROJECTILE_SIDE)
#             projectile_rect.y = (y + 0.25 * PROJECTILE_SIDE)
#             draw_tiles(map_1)
#             # window.blit(level_one_enemies[i].image, [0, 0])

#             for i in range(len(level_one_enemies)):
#                 level_one_enemies[i].draw()

#             window.blit(projectile, (x, y))
#             pygame.display.update()
#         pygame.display.set_caption(f"Angle: {angle} Speed: {speed}")

#     pygame.quit()


# window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Map")
# window.blit(map_1_background, (0, 0))

# main()


import pygame
import math
import time
from model import Enemy
from random import randint

pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
BLACK = (0, 0, 0)

map_1_small = """                                
                                
                                
                                
                                
                    2222        
                    1111        
                                
                           22222
                          211111
                         2111111
                        21111111
                       211111111
          222         2111111111
         211122      21111111111
22222222211111122222211111111111
11111111111111111111111111111111
11111111111111111111111111111111"""

map_1 = """                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                         22222222222222222222222                
                          111111111111111111111                 
                            11111111111111111                   
                              1111111111111                     
                                111111111                       
                                111111111                       
                                111111111                       
                               1111111111                       
                               1111111111                       
                               111111111                       
                               111111111                        
           22222222222         111111111                    2222
           11111111111           11111111                  21111
           11111111111          111111111                2211111
           11111111111         1111111111              221111111
           11111111111         11111111              22111111111
           11111111111         111111111          22211111111111
           11111111111         1111111111        211111111111111
2222222222211111111111222222222211111111122222222111111111111111
1111111111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111111111"""

map_1_background = pygame.image.load("airport_background.png")
map_1_background = pygame.transform.scale(map_1_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

level_one_enemies = {}

TILE_SIZE = 20

img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")
img_1 = pygame.transform.scale(img_1, (TILE_SIZE, TILE_SIZE))
img_2 = pygame.transform.scale(img_2, (TILE_SIZE, TILE_SIZE))

tile_rect = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
tile_rects = []

class Projectile:
    def __init__(self, start_x, start_y, image, size, background, map, screen) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self._projectile_rect = pygame.Rect(0, 0, 0.5 * self.size, 0.5 * self.size)
        self.background = background
        self.map = map
        self.screen = screen

        self.gravity = -9.81
        self._shoot = False
        self._angle = 0
        self._speed = 0
    
    @property
    def shoot(self) -> bool:
        return self._shoot

    @property
    def angle(self):
        return self._angle

    @property
    def speed(self):
        return self._speed

    @property
    def projectile_rect(self):
        return self._projectile_rect
    
    def change_angle(self, change_in_angle):
        self._angle += change_in_angle if 0 <= self._angle + change_in_angle <= 90 else 0
        pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def change_speed(self, change_in_speed):
        self._speed += change_in_speed if 0 <= self._speed + change_in_speed <= 150 else 0
        pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def draw_starting_point(self):
        self.projectile_rect.x = self.start_x + 0.25 * self.size
        self.projectile_rect.y = self.start_y + 0.25 * self.size
        self.screen.blit(self.image, (self.start_x, self.start_y))
        pygame.display.update()

    def trajectory(self, change_in_time):
        coordinates = []
        launch_time = 0
        y = self.start_y
        while y + (0.5 * self.size) <= SCREEN_HEIGHT:
            launch_time += change_in_time
            x = (self.start_x + (self._speed * math.cos(math.radians(self._angle)) * launch_time))
            y = (self.start_y - ((self._speed * math.sin(math.radians(self._angle)) * launch_time) + (0.5 * self.gravity * launch_time ** 2)))
            coordinates.append([x, y])
        return coordinates

    def draw_trajectory(self):
        coordinates = self.trajectory(1 / 5)
        for coords in coordinates:
            time.sleep(1 / 100)
            x = coords[0]
            y = coords[1]

            self.screen.fill(BLACK)
            self.screen.blit(self.background, (0, 0))
            draw_tiles(self.map)
            draw_enemies(level_one_enemies)
            self.screen.blit(self.image, (x, y))
            self.projectile_rect.x = x + 0.25 * self.size
            self.projectile_rect.y = y + 0.25 * self.size
            pygame.display.update()

            for tile in tile_rects:
                if self.projectile_rect.colliderect(tile):
                    time.sleep(0.5)
                    return False
            for i in range(len(level_one_enemies)):
                if self.projectile_rect.colliderect(level_one_enemies[i]):
                    time.sleep(0.5)
                    deduct_health(level_one_enemies[i])
                    return False


def deduct_health(enemy_hit):
    damage = randint(30, 90)
    enemy_hit.shield -= damage
    if enemy_hit.shield == 0:
        enemy_hit.health -= damage

    if enemy_hit.health <= 0:
        print("RIP")
    
    print("health: ", enemy_hit.health)
    print("shield: ", enemy_hit.shield)



def make_window(width: int, height:int, caption: str)  -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win


def draw_tiles(map, first = False):
    game_map = map.split("\n")
    x = 0
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if first:
                duplicate = False
                tile_rect.x = x * TILE_SIZE
                tile_rect.y = y * TILE_SIZE
                if tile_rect.copy() in tile_rects:
                    duplicate = True
            if tile == "1":
                window.blit(img_1, (x * TILE_SIZE, y * TILE_SIZE))
                if first:
                    if not duplicate:
                        tile_rects.append(tile_rect.copy())
            elif tile == "2":
                window.blit(img_2, (x * TILE_SIZE, y * TILE_SIZE))
                if first:
                    if not duplicate:
                        tile_rects.append(tile_rect.copy())
            x += 1
        y += 1


def draw_enemies(enemy_level_list):
    for i in range(len(level_one_enemies)):
        level_one_enemies[i].draw()


def level_play(screen, projectile: Projectile, map_background, map_tiles):
    current = True
    shoot = False

    screen.blit(map_background, (0, 0))
    draw_tiles(map_tiles, True)
    projectile.draw_starting_point()
    draw_enemies(level_one_enemies)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_q:
                    current = False if current else True
                if event.__dict__["key"] == pygame.K_SPACE:
                    shoot = True
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
                if event.button == 4 and current:
                    projectile.change_angle(5)
                elif event.button == 5 and current:
                    projectile.change_angle(-5)
                elif event.button == 4 and not current:
                    projectile.change_speed(5)
                elif event.button == 5 and not current:
                    projectile.change_speed(-5)
        if shoot:
            screen.fill(BLACK)
            shoot = projectile.draw_trajectory()
            screen.blit(map_background, (0, 0))
            draw_tiles(map_tiles)
            projectile.draw_starting_point()
            draw_enemies(level_one_enemies)

        pygame.display.update()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 0")

level_one_enemies[0] = Enemy(f"Enemy {1}", 100, 100, 25,
                                600, 400,
                                40, 40, window)
level_one_enemies[1] = Enemy(f"Enemy {2}", 100, 100, 25,
                                400, 400,
                                40, 40, window)

# projectile_side
PJ_S = 80
projectile_one = Projectile((0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - (0.75 * PJ_S) - 60), pygame.image.load("test.png"), PJ_S, map_1_background, map_1, window)
level_play(window, projectile_one, map_1_background, map_1)