"""DOGSTRING."""
import pygame
import math
import time
from button import Button
from model import Enemy
from random import randint

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

map_1 = """                                
                               
                               
                               
                               
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

map_2 = """                                                                
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
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

level_one_enemies = {}
level_one_coordinates = [[40 * 17, 40 * 4], [40 * 23, 40 * 14]]

airport_background = pygame.image.load("airport_background.png")
airport_background = pygame.transform.scale(airport_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_2_background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
map_2_background.fill((200, 30, 20))


img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")

tile_rects = []
# projectile_side
PJ_S = 80

class Projectile:
    def __init__(self, start_x, start_y, image, size, background, map, screen, tile_size) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self._projectile_rect = pygame.Rect(0, 0, 0.5 * self.size, 0.5 * self.size)
        self.background = background
        self.map = map
        self.screen = screen
        self.tile_size = tile_size

        self.gravity = -9.81
        self._shoot = False
        self._angle = 0
        self._speed = 0
        self.speeds = []

    @property
    def shoot(self):
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

    def trajectory(self, change_in_time, start_x, start_y, angle, speed):
        coordinates = []
        launch_time = 0
        y = self.start_y
        while y + (0.5 * self.size) <= SCREEN_HEIGHT:
            launch_time += change_in_time
            x = (start_x + (speed * math.cos(math.radians(angle)) * launch_time))
            y = (start_y - ((speed * math.sin(math.radians(angle)) * launch_time) + (0.5 * self.gravity * launch_time ** 2)))
            coordinates.append([x, y])
        return coordinates

    def draw_trajectory(self):
        coordinates = self.trajectory(1 / 10, self.start_x, self.start_y, self._angle, self._speed)
        run = True

        while run:
            for coords in coordinates:
                x = coords[0]
                y = coords[1]

                self.screen.blit(self.background, (0, 0))
                draw_tiles(self.map, self.tile_size)
                draw_enemies(level_one_enemies)
                self.screen.blit(self.image, (x, y))
                self.projectile_rect.x = x + 0.25 * self.size
                self.projectile_rect.y = y + 0.25 * self.size
                pygame.display.update()

                for tile in tile_rects:
                    if self.projectile_rect.colliderect(tile):
                        time.sleep(0.5)
                        run = False
                        break

                for i in range(len(level_one_enemies)):
                    if self.projectile_rect.colliderect(level_one_enemies[i]):
                        time.sleep(0.5)
                        deduct_health(level_one_enemies[i])
                        run = False
                        break
                if not run:
                    break
            break
        return


def deduct_health(enemy_hit):
    damage = randint(30, 90)
    old_shield = enemy_hit.shield
    enemy_hit.shield -= damage
    if enemy_hit.shield == 0:
        enemy_hit.health -= (damage - old_shield)

    if enemy_hit.health <= 0:
        print("RIP")

    print("health: ", enemy_hit.health)
    print("shield: ", enemy_hit.shield)



def make_window(width: int, height:int, caption: str)  -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win


def draw_tiles(map, tile_size, first = False):
    scaled_img_1 = pygame.transform.scale(img_1, (tile_size, tile_size))
    scaled_img_2 = pygame.transform.scale(img_2, (tile_size, tile_size))
    tile_rect = pygame.Rect(0, 0, tile_size, tile_size)
    game_map = map.split("\n")
    x = 0
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if first:
                duplicate = False
                tile_rect.x = x * tile_size
                tile_rect.y = y * tile_size
                if tile_rect.copy() in tile_rects:
                    duplicate = True
            if tile == "1":
                window.blit(scaled_img_1, (x * tile_rect.width, y * tile_rect.height))
                if first:
                    if not duplicate:
                        tile_rects.append(tile_rect.copy())
            elif tile == "2":
                window.blit(scaled_img_2, (x * tile_rect.width, y * tile_rect.height))
                if first:
                    if not duplicate:
                        tile_rects.append(tile_rect.copy())
            x += 1
        y += 1


def draw_enemies(enemy_level_list):
    for i in range(len(level_one_enemies)):
        level_one_enemies[i].draw()


def level_play(screen, map_background, map_tiles, tile_size, projectile_starting_coords):
    current = True
    shoot = False

    projectile = Projectile(projectile_starting_coords[0], projectile_starting_coords[1], pygame.image.load("test.png"), PJ_S, map_background, map_tiles, screen, tile_size)

    screen.blit(map_background, (0, 0))
    draw_tiles(map_tiles, tile_size, True)
    projectile.draw_starting_point()
    draw_enemies(level_one_enemies)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
            projectile.draw_trajectory()
            screen.blit(map_background, (0, 0))
            draw_tiles(map_tiles, tile_size)
            projectile.draw_starting_point()
            draw_enemies(level_one_enemies)
            shoot = False

        pygame.display.update()
    pygame.quit()


def main_menu():
    window.fill((40, 90, 150))
    pygame.display.set_caption("Main Menu")
    play_button.draw(window)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_button.is_pressed():
                    level_menu()
        pygame.display.update()
    pygame.quit()

def level_menu():
    level_1_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.33, 200, 100, "level_1.png", "Level 1")
    level_2_button = Button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.33, 200, 100, "level_2.png", "Level 2")

    pygame.display.set_caption("Level Menu")
    window.fill((90, 80, 40))

    level_1_button.draw(window)
    level_2_button.draw(window)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and level_1_button.is_pressed():
                    for i in range(len(level_one_coordinates)):
                        level_one_enemies[i] = Enemy(f"Enemy {2}", 100, 100, 25,
                                    level_one_coordinates[i][0],
                                    SCREEN_HEIGHT - level_one_coordinates[i][1],
                                    40, 40, window)

                    level_play(window, airport_background, map_1, 40, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - (0.75 * PJ_S) - 120)])

                elif event.button == 1 and level_2_button.is_pressed():
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - (0.75 * PJ_S) - 60)])
        pygame.display.update()
    pygame.quit()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")

play_button = Button(SCREEN_WIDTH * 0.5, 200, 500, 200, "play.png", "Play")
#options_button = Button(100, 200, "tile2.png", "Options")

main_menu()