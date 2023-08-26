"""DOGSTRING."""
import pygame
import math
import time
from button import Button
from model import Enemy
from random import randint
from character_testing import Test_Character

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
level_one_coordinates = [[40 * 17, 40 * 6], [40 * 21, 40 * 16]]
level_one_enemy = [[130, 80, level_one_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[0][1] + 20],
                   [160, 75, level_one_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[1][1]]]

airport_background = pygame.image.load("airport_background.png")
airport_background = pygame.transform.scale(airport_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_2_background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
map_2_background.fill((200, 30, 20))


img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")

tile_rects = []
# projectile_side
PJ_S = 80

enemy_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
enemy_projectile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


jamal = Test_Character(65, SCREEN_HEIGHT - 160, 1.5, 0)
player_group.add(jamal)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, map, screen, tile_size) -> None:
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size * 0.5, self.size * 0.5))
        self._rect = self.image.get_rect()
        # self.rect.topleft = (start_x - self.image.get_width(), start_y - self.image.get_height())
        self.image_mask = pygame.mask.from_surface(self.image)

        self.background = background
        self.map = map
        self.screen = screen
        self.tile_size = tile_size

        self.gravity = -9.81
        self._shoot = False
        self._angle = 0
        self._speed = 0

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
    def rect(self):
        return self._rect

    def change_angle(self, change_in_angle):
        self._angle += change_in_angle if 0 <= self._angle + change_in_angle <= 90 else 0
        pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def change_speed(self, change_in_speed):
        self._speed += change_in_speed if 0 <= self._speed + change_in_speed <= 150 else 0
        pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def draw_starting_point(self):
        # self.rect.x = self.start_x + 0.25 * self.size
        # self.rect.y = self.start_y + 0.25 * self.size
        self.rect.x = self.start_x
        self.rect.y = self.start_y
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
        coordinates = self.trajectory(1 / 10)
        for coords in coordinates:
            x = coords[0]
            y = coords[1]

            self.screen.blit(self.background, (0, 0))
            draw_tiles(self.map, self.tile_size)
            # draw_enemies(level_one_enemies)
            # pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
            # self.screen.blit(jamal.image, jamal.rect)
            player_group.draw(self.screen)
            enemy_group.draw(self.screen)

            self.screen.blit(self.image, (x, y))
            self.rect.x = x
            self.rect.y = y
            pygame.display.update()

            for tile in tile_rects:
                if self.rect.colliderect(tile):
                    time.sleep(0.5)
                    print("HIT")
                    return False
            # Use groupcollide() to detect collisions
            dead = False
            collisions = pygame.sprite.groupcollide(enemy_group, projectile_group, False, dead, pygame.sprite.collide_mask)

            # Handle collisions
            for enemy, projectiles in collisions.items():
                print("Character hit by projectiles:", len(projectiles))
                time.sleep(0.5)
                deduct_enemy_health(enemy)
                return False


class Enemy_Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, map, screen,
                 tile_size, angle, speed) -> None:
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size * 0.5,
                                                         self.size * 0.5))
        self._rect = self.image.get_rect()
        self.image_mask = pygame.mask.from_surface(self.image)

        self.background = background
        self.map = map
        self.screen = screen
        self.tile_size = tile_size

        self.gravity = -9.81
        self._shoot = False
        self._angle = angle
        self._speed = speed

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
    def rect(self):
        return self._rect

    def draw_starting_point(self):
        # self.rect.x = self.start_x + 0.25 * self.size
        # self.rect.y = self.start_y + 0.25 * self.size
        self.rect.x = self.start_x
        self.rect.y = self.start_y
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
        coordinates = self.trajectory(1 / 10)
        for coords in coordinates:
            x = coords[0]
            y = coords[1]

            self.screen.blit(self.background, (0, 0))
            draw_tiles(self.map, self.tile_size)
            # self.screen.blit(jamal.image, jamal.rect)
            player_group.draw(self.screen)
            enemy_group.draw(self.screen)

            self.screen.blit(self.image, (x, y))
            self.rect.x = x
            self.rect.y = y
            pygame.display.update()

            for tile in tile_rects:
                if self.rect.colliderect(tile):
                    time.sleep(0.5)
                    print("HIT")
                    return False
            # Use groupcollide() to detect collisions
            dead = False
            collisions = pygame.sprite.groupcollide(player_group, enemy_projectile_group,
                                                    False, dead, pygame.sprite.collide_mask)

            # Handle collisions
            for player, projectiles in collisions.items():
                print("Character hit by projectiles:", len(projectiles))
                time.sleep(0.5)
                deduct_player_health(player)
                return False


def deduct_player_health(player):
    global player_group
    damage = randint(50, 90)
    player.health -= damage

    print("health: ", player.health)

    if player.health <= 0:
        print("RIP")
        player.die()
        player_dead()


def deduct_enemy_health(enemy_hit):
    global enemy_group
    damage = randint(30, 90)
    old_shield = enemy_hit.shield
    enemy_hit.shield -= damage
    if enemy_hit.shield == 0:
        enemy_hit.health -= (damage - old_shield)

    print("health: ", enemy_hit.health)
    print("shield: ", enemy_hit.shield)

    if enemy_hit.health <= 0:
        print("RIP")
        enemy_hit.die()
        enemy_dead_check()


def enemy_dead_check():
    if len(enemy_group) == 0:
        jamal.level_points += 1
        print(jamal.level_points)


def player_dead():
    print("PLAYER IS DEAD")


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

    projectile = Projectile(projectile_starting_coords[0], projectile_starting_coords[1], "test.png", PJ_S, map_background, map_tiles, screen, tile_size)
    projectile_group.add(projectile)
    enemy_projectile = Enemy_Projectile(0, 0, "test.png", PJ_S, map_background, map_tiles, screen, tile_size, 0, 0)
    enemy_projectile_group.add(enemy_projectile)

    screen.blit(map_background, (0, 0))
    draw_tiles(map_tiles, tile_size, True)
    projectile.draw_starting_point()

    for enemy in enemy_group:
        enemy_projectile.start_x = enemy.rect.topleft[0] + 80
        enemy_projectile.start_y = enemy.rect.topleft[1] + 20
        enemy_projectile._angle = enemy.angle
        enemy_projectile._speed = enemy.speed
        enemy_projectile.draw_starting_point()
        enemy_projectile.draw_trajectory()

    # screen.blit(jamal.image, jamal.rect)
    player_group.draw(screen)
    # draw_enemies(level_one_enemies)
    enemy_group.draw(screen)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)
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
            shoot = projectile.draw_trajectory()
            screen.blit(map_background, (0, 0))
            draw_tiles(map_tiles, tile_size)
            projectile.draw_starting_point()
            enemy_projectile.draw_starting_point()
            # screen.blit(jamal.image, jamal.rect)
            player_group.draw(screen)
            # draw_enemies(level_one_enemies)
            enemy_group.draw(screen)

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
                                    40, 40, window, level_one_enemy[i][0],
                                    level_one_enemy[i][1])
                        enemy_group.add(level_one_enemies[i])

                    level_play(window, airport_background, map_1, 40, [(0 - (0.25 * PJ_S) + 90), (SCREEN_HEIGHT - (0.75 * PJ_S) - 120 - 30)])

                elif event.button == 1 and level_2_button.is_pressed():
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - (0.75 * PJ_S) - 60)])
        pygame.display.update()
    pygame.quit()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")

play_button = Button(SCREEN_WIDTH * 0.5, 200, 500, 200, "play.png", "Play")
#options_button = Button(100, 200, "tile2.png", "Options")

# jamal = Enemy(f"Enemy {2}", 100, 100, 25, 21, 21, 40, 40, window)
# print(jamal)
# enemy_group.add(jamal)

main_menu()
