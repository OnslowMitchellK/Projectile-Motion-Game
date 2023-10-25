"""DOGSTRING."""
import pygame
import math
import time
from button import Button, Lockable_button, Upgrades_button, Level_completed_button
from model import Enemy
from random import randint, choice
from character import Character
from upgrades import *
from instructions import text
from level_info import level_info
import json
from map_model import Map_Masks

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

def make_window(width: int, height:int, caption: str)  -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win

window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")

map_obj_2 = Map_Masks(pygame.image.load('Assets/map2/map2_objects.png').convert_alpha())
map_obj_3 = Map_Masks(pygame.image.load('Assets/map3/map_3_obj.png').convert_alpha())
map_obj_4 = Map_Masks(pygame.image.load('Assets/map4/map_4_obj.png').convert_alpha())
map_obj_5 = Map_Masks(pygame.image.load('Assets/map5/map_5_obj.png').convert_alpha())
map_obj_3.image = pygame.transform.scale(map_obj_3.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_object_list = [0, 1, map_obj_2, map_obj_3, map_obj_4, map_obj_5]
map_group = pygame.sprite.Group()


player_coords = {1: (65, SCREEN_HEIGHT - 160), 2: (100, 300), 3: (145, 580), 4: (65, 250), 5: (100, 420)}


level_one_enemies = {}
level_one_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_one_enemy = [[130, 80, level_one_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[0][1] + 20],
                   [170, 98, level_one_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[1][1]]]
level_two_enemies = {}
level_two_coordinates = [[SCREEN_WIDTH - 550, 450], [SCREEN_WIDTH - 200, 230]]
level_two_enemy = [[130, 82, level_two_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_two_coordinates[0][1] + 20],
                   [130, 110, level_two_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_two_coordinates[1][1]]]
level_three_enemies = {}
level_three_coordinates = [[SCREEN_WIDTH - 500, 150], [SCREEN_WIDTH - 300, 360], [SCREEN_WIDTH - 120, 470]]
level_three_enemy = [[130, 85, level_three_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_three_coordinates[0][1] + 20],
                    [150, 85, level_three_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_three_coordinates[1][1] + 20],
                   [180, 129, level_three_coordinates[2][0] + 80, SCREEN_HEIGHT -
                    level_three_coordinates[2][1]]]
level_four_enemies = {}
level_four_coordinates = [[SCREEN_WIDTH - 700, 500], [SCREEN_WIDTH - 300, 340], [SCREEN_WIDTH - 100, 600]]
level_four_enemy = [[130, 80, level_four_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_four_coordinates[0][1] + 20],
                    [110, 130, level_four_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_four_coordinates[1][1] + 20],
                   [140, 104, level_four_coordinates[2][0] + 80, SCREEN_HEIGHT -
                    level_four_coordinates[2][1]]]
level_five_enemies = {}
level_five_coordinates = [[SCREEN_WIDTH - 890, 180], [SCREEN_WIDTH - 435, 600], [1040, 602]]
level_five_enemy = [[110, 80, level_five_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_five_coordinates[0][1] + 20],
                    [170, 95, level_five_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_five_coordinates[1][1]],
                   [160, 98, level_five_coordinates[2][0] + 80, SCREEN_HEIGHT -
                    level_five_coordinates[2][1]]]
level_six_enemies = {}
level_six_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_six_enemy = [[130, 80, level_six_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_six_coordinates[0][1] + 20],
                   [170, 98, level_six_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_six_coordinates[1][1]]]
level_seven_enemies = {}
level_seven_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_seven_enemy = [[130, 80, level_seven_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_seven_coordinates[0][1] + 20],
                   [170, 98, level_seven_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_seven_coordinates[1][1]]]
level_eight_enemies = {}
level_eight_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_eight_enemy = [[130, 80, level_eight_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_eight_coordinates[0][1] + 20],
                   [170, 98, level_eight_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_eight_coordinates[1][1]]]
level_nine_enemies = {}
level_nine_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_nine_enemy = [[130, 80, level_nine_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_nine_coordinates[0][1] + 20],
                   [170, 98, level_nine_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_nine_coordinates[1][1]]]
level_ten_enemies = {}
level_ten_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_ten_enemy = [[130, 80, level_ten_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_ten_coordinates[0][1] + 20],
                   [170, 98, level_ten_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_ten_coordinates[1][1]]]


font_directory = "C:/Fonts/Barriecito-Regular.ttf"
tile_rects = []
# projectile_side
PJ_S = 40

enemy_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
enemy_projectile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Main_Menu_Projectile:
    def __init__(self, image="Assets/player_enemy_images/proj.png", possible_speeds = [-8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8]) -> None:
        self._image = pygame.image.load(image)
        size = randint(30, 50)
        self._image = pygame.transform.scale(self._image, (size, size))
        self._rect = self._image.get_rect()
        self._rect.x = randint(50, SCREEN_WIDTH - 50)
        self._rect.y = randint(50, SCREEN_HEIGHT - 50)
        self._dx = choice(possible_speeds)
        self._dy = choice(possible_speeds)

    @property
    def image(self):
        return self._image
   
    @property
    def dx(self):
        return self._dx
   
    @property
    def dy(self):
        return self._dy
   
    @property
    def rect_left(self) -> float:
        return self._rect.left
   
    @property
    def rect_right(self) -> float:
        return self._rect.right
   
    @property
    def rect_top(self) -> float:
        return self._rect.top
   
    @property
    def rect_bottom(self) -> float:
        return self._rect.bottom
   
    @property
    def rect(self):
        return self._rect
   
    @property
    def rect_x(self):
        return self._rect.x
   
    @property
    def rect_y(self):
        return self._rect.y
   
    def plus_x(self):
        self._rect.x += self._dx

    def plus_y(self):
        self._rect.y += self._dy

    def multiply_x(self, num):
        self._dx *= num

    def multiply_y(self, num):
        self._dy *= num
   
    def draw(self, screen):
        screen.blit(self._image, (self._rect.x, self._rect.y))


class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, screen) -> None:
        super().__init__()
        self._start_x = start_x
        self._start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.image_mask = pygame.mask.from_surface(self.image)
        self.background = background
        self.map = map
        self.screen = screen

        self.gravity = -9.81
        self._shoot = False
        self._angle = 0
        self._speed = 0
        self.speeds = []
   
    @property
    def start_x(self):
        return self._start_x
    
    @start_x.setter
    def start_x(self, new_start_x) -> int:
        self._start_x = new_start_x
   
    @property
    def start_y(self):
        return self._start_y

    @start_y.setter
    def start_y(self, new_start_y) -> int:
        self._start_y = new_start_y

    @property
    def shoot(self):
        return self._shoot

    @property
    def angle(self):
        return self._angle

    @property
    def speed(self):
        return self._speed


    def change_angle(self, change_in_angle):
        self._angle = change_in_angle

    def change_speed(self, change_in_speed):
        self._speed = change_in_speed

    def change_size(self, factor):
        self.image = pygame.transform.scale(self.image, (self.size * factor, self.size * factor))
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def draw_starting_point(self):
        self.rect.centerx = self._start_x
        self.rect.centery = self._start_y
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
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

    def draw_trajectory(self, stop_x=0, stop_y=0, double_jump=False, halt=False):
        pressed = False
        jumped = False
        coordinates = self.trajectory(1 / 10, self._start_x, self._start_y, self._angle, self._speed)

        if upgrade_2.get_level() >= 1 and stop_x != 0 and not double_jump:
            coordinates = self.trajectory(1 / 10, stop_x, stop_y, 0, 0)
            pressed = True
        elif upgrade_3.get_level() >= 2 and stop_x != 0 and double_jump:
            coordinates = self.trajectory(1 / 10, stop_x, stop_y, self.angle, self.speed)
            jumped = True
        
        if upgrade_2.get_level() == 0:
            pressed = True
        run = True
        clock = pygame.time.Clock()

        while run:
            for coords in coordinates:
                clock.tick(60)
                x = coords[0]
                y = coords[1]

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.__dict__["key"] == pygame.K_1 and upgrade_3.get_level() >= 1:
                            self.change_size(2)
                            break
                        elif event.__dict__["key"] == pygame.K_SPACE and not pressed and not double_jump:
                            return [x, y]
                        elif event.__dict__["key"] == pygame.K_2 and upgrade_3.get_level() >= 2 and not jumped and not halt:
                            self.draw_trajectory(x, y, True)
                            return

                
                

                self.screen.blit(self.background, (0, 0))
                map_group.draw(self.screen)
                player_group.draw(self.screen)
                enemy_group.draw(self.screen)

                self.rect.centerx = x
                self.rect.centery = y
                self.screen.blit(self.image, (self.rect.x, self.rect.y))
                for enemy in enemy_group:
                    enemy.draw_health()
                current_player.draw_health()
                pygame.display.update()

                if (self.rect.centerx > SCREEN_WIDTH + 200 or
                    self.rect.centery > SCREEN_HEIGHT + 200):
                    time.sleep(0.5)
                    run = False
                    break
                
                map_collisions = pygame.sprite.groupcollide(map_group, projectile_group,
                                                        False, False, pygame.sprite.collide_mask)
                # Handle collisions
                for map, projectiles in map_collisions.items():
                    time.sleep(0.5)
                    return False

                # Use groupcollide() to detect collisions
                collisions = pygame.sprite.groupcollide(enemy_group, projectile_group,
                                                        False, False, pygame.sprite.collide_mask)

                # Handle collisions
                for enemy, projectiles in collisions.items():
                    time.sleep(0.5)
                    deduct_enemy_health(enemy)
                    return False
                if not run:
                    break
            break
        return


class Enemy_Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, screen,
                 angle, speed) -> None:
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
        clock = pygame.time.Clock()
        for coords in coordinates:
            clock.tick(60)
            x = coords[0]
            y = coords[1]

            self.screen.blit(self.background, (0, 0))
            map_group.draw(self.screen)
            player_group.draw(self.screen)
            enemy_group.draw(self.screen)
            for enemy in enemy_group:
                enemy.draw_health()
            current_player.draw_health()

            self.screen.blit(self.image, (x, y))
            self.rect.x = x
            self.rect.y = y
            pygame.display.update()

            if self.rect.centerx < -200:
                time.sleep(0.5)
                return False

            map_collisions = pygame.sprite.groupcollide(map_group, enemy_projectile_group,
                                                    False, False, pygame.sprite.collide_mask)
            # Handle collisions
            for map, projectiles in map_collisions.items():
                time.sleep(0.5)
                return False

            # Use groupcollide() to detect collisions
            collisions = None
            collisions = pygame.sprite.groupcollide(player_group, enemy_projectile_group,
                                                    False, False, pygame.sprite.collide_mask)
            # Handle collisions
            for player, projectiles in collisions.items():
                time.sleep(0.5)
                deduct_player_health(player)
                return False
    


make_enemy = []

def loop_enemies():
    global make_enemy
    make_enemy = []
    for i in range(len(level_one_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_one_coordinates[i][0],
                    SCREEN_HEIGHT - level_one_coordinates[i][1],
                    40, 40, window, level_one_enemy[i][0],
                    level_one_enemy[i][1], 1))
    for i in range(len(level_two_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_two_coordinates[i][0],
                    SCREEN_HEIGHT - level_two_coordinates[i][1],
                    40, 40, window, level_two_enemy[i][0],
                    level_two_enemy[i][1], 2))
    for i in range(len(level_three_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_three_coordinates[i][0],
                    SCREEN_HEIGHT - level_three_coordinates[i][1],
                    40, 40, window, level_three_enemy[i][0],
                    level_three_enemy[i][1], 3))
    for i in range(len(level_four_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_four_coordinates[i][0],
                    SCREEN_HEIGHT - level_four_coordinates[i][1],
                    40, 40, window, level_four_enemy[i][0],
                    level_four_enemy[i][1], 4))
    for i in range(len(level_five_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_five_coordinates[i][0],
                    SCREEN_HEIGHT - level_five_coordinates[i][1],
                    40, 40, window, level_five_enemy[i][0],
                    level_five_enemy[i][1], 5))
    for i in range(len(level_six_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_six_coordinates[i][0],
                    SCREEN_HEIGHT - level_six_coordinates[i][1],
                    40, 40, window, level_six_enemy[i][0],
                    level_six_enemy[i][1], 6))
    for i in range(len(level_seven_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_seven_coordinates[i][0],
                    SCREEN_HEIGHT - level_seven_coordinates[i][1],
                    40, 40, window, level_seven_enemy[i][0],
                    level_seven_enemy[i][1], 7))
    for i in range(len(level_eight_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_eight_coordinates[i][0],
                    SCREEN_HEIGHT - level_eight_coordinates[i][1],
                    40, 40, window, level_eight_enemy[i][0],
                    level_eight_enemy[i][1], 8))
    for i in range(len(level_nine_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_nine_coordinates[i][0],
                    SCREEN_HEIGHT - level_nine_coordinates[i][1],
                    40, 40, window, level_nine_enemy[i][0],
                    level_nine_enemy[i][1], 9))
    for i in range(len(level_ten_coordinates)):
        make_enemy.append(Enemy(f"Enemy {2}", 100, 100,
                    level_ten_coordinates[i][0],
                    SCREEN_HEIGHT - level_ten_coordinates[i][1],
                    40, 40, window, level_ten_enemy[i][0],
                    level_ten_enemy[i][1], 10))


def deduct_player_health(player):
    global enemy_group
    for i in enemy_group:
        damage = i.damage
    level = i.level
    old_shield = player.shield
    player.shield -= damage
    if player.shield <= 0:
        player.shield = 0
        player.health -= (damage - old_shield)

    if player.health <= 0:
        print("RIP")
        player.die()
        player_dead(level)


def deduct_enemy_health(enemy_hit):
    global player_group
    for i in player_group:
        damage = i.damage + 200
    # Damage upgrade.
    try:
        damage += (upgrade_5.get_level() * 20)
    except:
        pass
    crit_chance = upgrade_8.get_level()
    ran = randint(1, 8)
    if ran <= crit_chance:
        damage = damage + (damage * 0.5)
    if current_player.health < current_player.max_health:
        current_player.health = current_player.health + (upgrade_9.get_level() * 3)
    old_shield = enemy_hit.shield
    enemy_hit.shield -= damage
    if enemy_hit.shield == 0:
        enemy_hit.health -= (damage - old_shield)
    if enemy_hit.health <= 0:
        print("RIP")
        for i in range(13):
            if (i % 2) != 0 and i < 8:
                enemy_hit.image = enemy_hit.dead_image
                enemy_group.draw(window)
                pygame.display.update()
                pygame.time.wait(250)
            elif (i % 2) == 0 and i < 8:
                enemy_hit.image = enemy_hit.alive_image
                enemy_group.draw(window)
                pygame.display.update()
                pygame.time.wait(250)
            elif i == 9:
                enemy_hit.die()
        enemy_dead_check(enemy_hit.level)

locked_levels = [2, 3, 4, 5, 6, 7, 8, 9, 10]
def enemy_dead_check(level):
    if len(enemy_group) == 0:
        try:
            locked_levels.remove(level + 1)
        except Exception:
            pass
        level_finished(True, level)


def player_dead():
    print("PLAYER IS DEAD")
    enemy_group.sprites()[0].level
    level_finished(False, enemy_group.sprites()[0].level)

def draw_enemies(enemy_level_list):
    for i in range(len(level_one_enemies)):
        level_one_enemies[i].draw()

def shoot_display(starting_coords):
    x_centre_s = starting_coords[0]
    y_centre_s = starting_coords[1]
    draw = True

    pos = pygame.mouse.get_pos()

    ARC_WIDTH = 100
    arc_rect = pygame.Rect(0, 0, ARC_WIDTH, ARC_WIDTH)
    arc_rect.center = (x_centre_s, y_centre_s)

    font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 50)
    angle_text = font.render("0°", True, "white")
    speed_text = font.render("0 px/s", True, "white")

    angle = math.atan2(SCREEN_HEIGHT - pos[1] - (SCREEN_HEIGHT - y_centre_s), pos[0] - (x_centre_s))
    angle += 2 * math.pi if angle < 0 else 0
   
    angle_text = font.render(f"{round(math.degrees(angle), 1)}°,", True, "white")
    window.blit(angle_text, (10, SCREEN_HEIGHT - 50))
    speed = pos[0] / 15 + (SCREEN_HEIGHT - pos[1]) / 8
    speed = 0 if speed < 0 else speed
    speed_text = font.render(f"{round(speed, 2)} px/s", True, "white")
    window.blit(speed_text, (120, SCREEN_HEIGHT - 50))

    return [speed, math.degrees(angle)]


def enemy_shoot(enemy_projectile, background):
    for enemy in enemy_group:
        rand_list = [0, randint(-80, 80)]
        for i in range(upgrade_7.get_level()):
            rand_list.append(randint(-80, 80))
            rand_list.append(randint(-80, 80))
            rand_list.append(0)
        enemy_projectile.start_x = enemy.rect.topleft[0] + 80
        enemy_projectile.start_y = enemy.rect.topleft[1] + 20
        enemy_projectile._speed = enemy.speed + rand_list[randint(0, len(rand_list) - 1)]
        print(enemy_projectile._speed)
        enemy_projectile._angle = enemy.angle
        for i in range(len(enemy.shoot_animations)):
            window.blit(background, (0, 0))
            map_group.draw(window)
            player_group.draw(window)
            current_player.draw_health()
            enemy.image = enemy.shoot_animations[i]
            enemy_group.draw(window)
            pygame.display.update()
            pygame.time.wait(50)
        window.blit(background, (0, 0))
        map_group.draw(window)
        player_group.draw(window)
        current_player.draw_health()
        enemy.image = enemy.alive_image
        enemy_group.draw(window)
        enemy_projectile.draw_starting_point()
        enemy_projectile.draw_trajectory()


def level_play(info):
    global current_player, enemy_group
    screen = window
    map_background = info[0]
    projectile_starting_coords = info[1]
    # min_angle = info[4]
    # max_angle = info[5]

    dot_distance = 6
    clock = pygame.time.Clock()
    current = True
    shoot = False

    if len(player_group) == 0:
        current_player = Character(65, SCREEN_HEIGHT - 160, 3, 0, window)
        player_group.add(current_player)

    try:
        current_player.max_health = 100 + (upgrade_4.get_level() * 25)
        current_player.health = 100 + (upgrade_4.get_level() * 25)
    except:
        current_player.health = 100
    try:
        current_player.shield = (upgrade_6.get_level() * 25)
    except:
        current_player.shield = 0
    projectile_group.empty()
    projectile = Projectile(projectile_starting_coords[0], projectile_starting_coords[1], pygame.image.load("Assets/player_enemy_images/proj.png"), PJ_S, map_background, screen)
    projectile_group.add(projectile)
    enemy_projectile = Enemy_Projectile(0, 0, "Assets/player_enemy_images/proj.png", PJ_S, map_background,screen, 0, 0)
    enemy_projectile_group.empty()
    enemy_projectile_group.add(enemy_projectile)

    screen.blit(map_background, (0, 0))
    map_group.draw(screen)
    projectile.draw_starting_point()
    player_group.draw(screen)
    for enemy in enemy_group:
        enemy.draw_health()
    current_player.draw_health()

    trajectory_level = upgrade_1.get_level()

    exit_button = Button(50, 25, "Exit", 100, 50, font_size=40)

    image_counter = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                save_file()
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_q:
                    current = False if current else True
            elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
                if event.button == 1 and exit_button.is_pressed():
                    enemy_group.empty()
                    main_menu()
                elif event.button == 1:
                    shoot = True
                    break
        
        image_counter += 1
        screen.blit(map_background, (0, 0))

        if image_counter % 6 == 0:
            current_player.change_image()
            image_counter = 0

        map_group.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        for enemy in enemy_group:
            enemy.draw_health()
        current_player.draw_health()
        # projectile.draw_starting_point()
        returned = shoot_display(projectile_starting_coords)
        coords = projectile.trajectory(1 / 3, projectile_starting_coords[0], projectile_starting_coords[1], returned[1], returned[0])
        y_coords = [x[1] for x in coords]
        y_max = min(y_coords)
        max_coords = [coords[y_coords.index(y_max)][0], y_max]

        match trajectory_level:
            case 0:
                """No trajectory display"""
                pass
            case 1:
                """10 dots across a eigth of the screen"""
                dot_distance = 8
                for i in coords[:10]:
                    if i[0] < SCREEN_WIDTH / dot_distance:
                        pygame.draw.circle(window, "yellow", (i), 10)
            case 2:
                """20 dots across a quarter of the screen"""
                dot_distance = 5
                for i in coords[:20]:
                    if i[0] < SCREEN_WIDTH / dot_distance:
                        pygame.draw.circle(window, "yellow", (i), 10)
            case 3:
                """30 dots 1/3 across screen and shows max height"""
                dot_distance = 3
                for i in coords[:30]:
                    if i[0] < SCREEN_WIDTH / dot_distance:
                        pygame.draw.circle(window, "yellow", (i), 10)
                pygame.draw.circle(window, "blue", (max_coords), 10)
       
        if shoot and current_player.get_image() == "animations/Aziz Animations/Aziz 4.png":
            while current_player.get_image() != "animations/Aziz Animations/Aziz 1.png":
                current_player.change_image()

            projectile.change_speed(returned[0])
            projectile.change_angle(returned[1])
            stop_coords = projectile.draw_trajectory()
            try:
                projectile.draw_trajectory(stop_coords[0], stop_coords[1], halt=True)
            except:
                pass

            projectile.change_size(1)
            shoot = False
            enemy_shoot(enemy_projectile, map_background)
        
        exit_button.draw(window)

        pygame.display.update()
    pygame.quit()



def level_finished(won: bool, current_level):
    global current_player
    background = pygame.Rect(0, 0, 400, 200)
    background.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.draw.rect(window, "black", background, border_radius=10)

    str_text = "Level Cleared" if won else "Level Failed"
    font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 50)
    text = font.render(str_text, True, "white")
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.4)

    diamond_text = font.render(f"+1", True, "white")
    coin_text = font.render(f"+3", True, "white")

    diamond = pygame.transform.scale(diamond_image, (40, 40))
    coin = pygame.transform.scale(coin_image, (40, 40))

    window.blit(text, text_rect.topleft)
    if won:
        window.blit(diamond, (SCREEN_WIDTH * 0.5 - 100, SCREEN_HEIGHT * 0.47))
        window.blit(diamond_text, (SCREEN_WIDTH * 0.5 - 50, SCREEN_HEIGHT * 0.48))
        window.blit(coin, (SCREEN_WIDTH * 0.5 + 10, SCREEN_HEIGHT * 0.47))
        window.blit(coin_text, (SCREEN_WIDTH * 0.5 + 60, SCREEN_HEIGHT * 0.48))
        current_player.super_points += 1
        current_player.level_points += 3

    main_menu_button = Level_completed_button(SCREEN_WIDTH * .395, SCREEN_HEIGHT * .6, "Assets/level_finished_images/home.png")
    upgrades_menu_button = Level_completed_button(SCREEN_WIDTH * .465, SCREEN_HEIGHT * .6, "Assets/level_finished_images/upgrades.png")
    retry_button = Level_completed_button(SCREEN_WIDTH * .535, SCREEN_HEIGHT * .6, "Assets/level_finished_images/retry.png")
    next_level_button = Level_completed_button(SCREEN_WIDTH * .606, SCREEN_HEIGHT * .6, "Assets/level_finished_images/next_level.png")

    buttons = [main_menu_button, upgrades_menu_button, retry_button, next_level_button]

    for button in buttons:
        button.draw(window)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                save_file()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and main_menu_button.is_pressed():
                    main_menu()
                elif event.button == 1 and upgrades_menu_button.is_pressed():
                    upgrades_window()
                elif event.button == 1 and retry_button.is_pressed():
                    enemy_group.empty()
                    map_group.empty()
                    map_group.add(map_object_list[current_level])
                    loop_enemies()
                    if len(player_group) == 0:
                        current_player = Character(player_coords[current_level][0],
                                                        player_coords[current_level][1], 3, 0, window)
                        player_group.add(current_player)
                    for i in make_enemy: 
                        if i.level == current_level:
                            enemy_group.add(i)
                    level_play(level_info[current_level - 1])
                elif event.button == 1 and next_level_button.is_pressed():
                    if won or (current_level + 1) not in locked_levels:
                        map_group.empty()
                        loop_enemies()
                        if len(player_group) == 0:
                            current_player = Character(65, SCREEN_HEIGHT - 160, 3, 0, window)
                            player_group.add(current_player)
                        for i in make_enemy:
                            if i.level == current_level + 1:
                                enemy_group.add(i)
                        map_group.add(map_object_list[current_level + 1])
                        current_player.x = player_coords[current_level + 1][0]
                        current_player.y = player_coords[current_level + 1][1]
                        current_player.rect.center = player_coords[current_level + 1]
                        level_play(level_info[current_level])

        pygame.display.update()
    pygame.quit()


rects = [Main_Menu_Projectile() for x in range(100)]

UPGRADES_WIDTH = SCREEN_WIDTH
UPGRADES_HEIGHT = SCREEN_HEIGHT

upgrade_1 = Super_upgrade(window, UPGRADES_WIDTH / 6, UPGRADES_HEIGHT / 4, "Assets/upgrades_images/cannon.png", "Upgrade Trajection Display", 5, "Info", [2, 1, 1], 3)

upgrade_2 = Super_upgrade(window, UPGRADES_WIDTH / 6, UPGRADES_HEIGHT / 4 * 2, "Assets/upgrades_images/cannon.png", "Projectile Halt", 5, "Info", [1], 1)

upgrade_3 = Super_upgrade(window, UPGRADES_WIDTH / 6, UPGRADES_HEIGHT / 4 * 3, "Assets/upgrades_images/cannon.png", "Projectile Upgrades", 2, "Info", [3, 1], 2)

upgrade_4 = Upgrade(window, UPGRADES_WIDTH / 2, UPGRADES_HEIGHT / 4, "Assets/upgrades_images/cannon.png", "Increase Health", 3, "Info", [1, 4, 1, 1])

upgrade_5 = Upgrade(window, UPGRADES_WIDTH / 2, UPGRADES_HEIGHT / 4 * 2, "Assets/upgrades_images/cannon.png", "Increase Damage", 4, "Info", [1, 1, 5, 1])

upgrade_6 = Upgrade(window, UPGRADES_WIDTH / 2, UPGRADES_HEIGHT / 4 * 3, "Assets/upgrades_images/cannon.png", "Increase Shield", 1, "Info", [1, 1, 1, 1])

upgrade_7 = Upgrade(window, UPGRADES_WIDTH / 6 * 5, UPGRADES_HEIGHT / 4, "Assets/upgrades_images/cannon.png", "Increase Evasion", 5, "Info", [1, 1, 1, 1])

upgrade_8 = Upgrade(window, UPGRADES_WIDTH / 6 * 5, UPGRADES_HEIGHT / 4 * 2, "Assets/upgrades_images/cannon.png", "Increase Critical Hit Chance", 5, "Info", [2, 1, 1, 1])

upgrade_9 = Upgrade(window, UPGRADES_WIDTH / 6 * 5, UPGRADES_HEIGHT / 4 * 3, "Assets/upgrades_images/cannon.png", "Upgrade Lifesteal", 5, "Info", [1, 5, 1, 1])

upgrades: list[Upgrade] = [upgrade_1, upgrade_2, upgrade_3, upgrade_4, upgrade_5, upgrade_6, upgrade_7, upgrade_8, upgrade_9]

def upgrades_window():
    pygame.display.set_caption("Upgrades Window")
    window = pygame.display.set_mode((UPGRADES_WIDTH, UPGRADES_HEIGHT))
    window.fill((10, 80, 180))

    plus_buttons = [x.get_plus_button() for x in upgrades]
    info_buttons = [x.get_info_button() for x in upgrades]

    main_menu_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 70, "Main Menu", font_size=60)
    main_menu_button.draw(window)

    for upgrade in upgrades:
        upgrade.display_cost()
    
    diamond_amount = current_player.super_points
    coin_amount = current_player.level_points

    font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 100)


    diamond_text = font.render(f": {diamond_amount}", True, "white")
    coin_text = font.render(f": {coin_amount}", True, "white")

    big_diamond = pygame.transform.scale(diamond_image, (80, 80))
    big_coin = pygame.transform.scale(coin_image, (80, 80))


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                save_file()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and main_menu_button.is_pressed():
                        main_menu()
                for plus in plus_buttons:
                    if event.button == 1 and plus.is_pressed():
                        index = plus_buttons.index(plus)
                        super = True if index <= 2 else False
                        returned = upgrades[index].deduct(current_player.super_points) if super else upgrades[index].deduct(current_player.level_points)
                        if super:
                            already_done = True if diamond_amount != current_player.super_points else False
                        else:
                            already_done = True if coin_amount != current_player.level_points else False

                        if returned[0] and not already_done:
                            plus.add_level()

                            if super:
                                current_player.super_points = returned[1]
                                diamond_amount = current_player.super_points
                                diamond_text = font.render(f": {current_player.super_points}", True, "white")

                            else:
                                current_player.level_points = returned[1]
                                coin_amount = current_player.level_points
                                coin_text = font.render(f": {current_player.level_points}", True, "white")

                        upgrades[index].display_dots()
                for info in info_buttons:
                    if event.button == 1 and info.is_pressed():
                        index = info_buttons.index(info)
                        upgrades[index].display_info()
        
        window.fill((10, 80, 190))

        window.blit(big_diamond, (40, 20))
        window.blit(diamond_text, (120, 30))
        window.blit(big_coin, (270, 20))
        window.blit(coin_text, (350, 30))
        main_menu_button.draw(window)

        for upgrade in upgrades:
            upgrade.display_upgrade()
            upgrade.display_dots()
            upgrade.display_cost()
                       


        pygame.display.update()
    pygame.quit()

# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
def blit_text(surface:pygame.Surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def instructions_menu():
    pygame.display.set_caption("Instructions Menu")
    window.fill((190, 50, 180))
    font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 20)
    blit_text(window, text, (0, 0), font)

    back_button = Button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.9, "Main Menu", font_size=60)
    back_button.draw(window)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                save_file()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and back_button.is_pressed():
                    main_menu()


        pygame.display.update()
    pygame.quit()

def main_menu():
    TOLERANCE = 10
    main_menu_clock = pygame.time.Clock()
    window.fill((19, 50, 143))
    pygame.display.set_caption("Main Menu")

    play_button = Button(SCREEN_WIDTH / 5 * 2.5, SCREEN_HEIGHT / 3, "Play")
    instructions_button = Button(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 3, "Instructions", font_size=60)
    upgrades_button = Button(SCREEN_WIDTH / 5 * 4, SCREEN_HEIGHT / 3, "Upgrades", font_size=60)
    clear_button = Button(SCREEN_WIDTH / 5 * 1.75, SCREEN_HEIGHT / 3 * 2, "Clear Save", font_size=60)
    quit_button = Button(SCREEN_WIDTH / 5 * 3.25, SCREEN_HEIGHT / 3 * 2, "Quit")

    play_button.draw(window)
    clear_button.draw(window)
    instructions_button.draw(window)
    upgrades_button.draw(window)
    quit_button.draw(window)
    buttons = [play_button, instructions_button, upgrades_button, clear_button, quit_button]

    run = True
    while run:
        main_menu_clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                save_file()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_button.is_pressed():
                    level_menu()
                elif event.button == 1 and instructions_button.is_pressed():
                    instructions_menu()
                elif event.button == 1 and upgrades_button.is_pressed():
                    upgrades_window()
                elif event.button == 1 and clear_button.is_pressed():
                    clear_save()
                elif event.button == 1 and quit_button.is_pressed():
                    pygame.quit()
        window.fill((19, 50, 143))
        for proj in rects:
            proj.plus_x()
            proj.plus_y()
            if proj.rect_right >= SCREEN_WIDTH and proj.dx > 0:
                proj.multiply_x(-1)
            elif proj.rect_left <= 0 and proj.dx < 0:
                proj.multiply_x(-1)
            elif proj.rect_bottom >= SCREEN_HEIGHT and proj.dy > 0:
                proj.multiply_y(-1)
            elif proj.rect_top <= 0 and proj.dy < 0:
                proj.multiply_y(-1)
            for button in buttons:
                if proj.rect.colliderect(button.get_button_rect()):
                    if abs(proj.rect_top - button.get_button_rect().bottom) < TOLERANCE and proj.dy < 0:
                        proj.multiply_y(-1)
                        break
                    elif abs(proj.rect_bottom - button.get_button_rect().top) < TOLERANCE and proj.dy > 0:
                        proj.multiply_y(-1)
                        break
                    elif abs(proj.rect_right - button.get_button_rect().left) < TOLERANCE and proj.dx > 0:
                        proj.multiply_x(-1)
                        break
                    elif abs(proj.rect_left - button.get_button_rect().right) < TOLERANCE and proj.dx < 0:
                        proj.multiply_x(-1)
                        break
            proj.draw(window)
       

        for button in buttons:
            button.draw(window)
        pygame.display.update()



    pygame.quit()


def clear_save():
    global locked_levels
    CLEAR_WIDTH = 600
    CLEAR_HEIGHT = 300

    pygame.display.set_caption("Clear Save")
    pygame.display.set_mode((CLEAR_WIDTH, CLEAR_HEIGHT))
    window.fill((20, 90, 130))

    font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 30)
    confirmation_text_pt_1 = font.render("Are you sure you want to clear your save?", True, "white") 
    confirmation_text_pt_2 = font.render("Note this will clear all your progress and cannot be reversed", True, "white")

    yes_button = Button(CLEAR_WIDTH * 0.5 - 50, CLEAR_HEIGHT * 0.5 + 50, "Yes", 80, 40, font_size=60)
    no_button = Button(CLEAR_WIDTH * 0.5 + 50, CLEAR_HEIGHT * 0.5 + 50, "No", 80, 40, font_size=60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and yes_button.is_pressed():
                    with open("save.json", "w") as save:
                        save.truncate()
                    current_player.level_points = 0
                    current_player.super_points = 0
                    locked_levels = [2, 3, 4, 5, 6, 7, 8, 9, 10]
                    for upgrade in upgrades:
                        upgrade.reset_level()


                    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    main_menu()
                elif event.button == 1 and no_button.is_pressed():
                    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    main_menu()

        window.blit(confirmation_text_pt_1, (90, 40))
        window.blit(confirmation_text_pt_2, (8, 80))
        yes_button.draw(window)
        no_button.draw(window)

        pygame.display.update()
    pygame.quit()

def level_menu():
    global current_player
    map_group.empty()
    level_1_button = Lockable_button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.25,"Level 1", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_2_button = Lockable_button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.25, "Level 2", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_3_button = Lockable_button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.25,"Level 3", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_4_button = Lockable_button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.25, "Level 4", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_5_button = Lockable_button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.5,"Level 5", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_6_button = Lockable_button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5, "Level 6", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_7_button = Lockable_button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.5,"Level 7", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_8_button = Lockable_button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.5, "Level 8", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_9_button = Lockable_button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.75,"Level 9", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_10_button = Lockable_button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.75, "Level 10", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    back_button = Lockable_button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.75, "Main Menu", 350, 100, font_size=50, border_radius=20, background_colour=(190, 10, 180))
   
    level_buttons = {1 : level_1_button, 2 : level_2_button, 3 : level_3_button,
                     4 : level_4_button, 5 : level_5_button, 6 : level_6_button,
                     7 : level_7_button, 8 : level_8_button, 9 : level_9_button,
                     10 : level_10_button}
   

    pygame.display.set_caption("Level Menu")
    window.fill((90, 80, 40))

    i = 1
    for button in level_buttons:
        level_buttons[i].draw(window)
        print(button)
        if i in locked_levels:
            level_buttons[i].lock_button(window, "Assets/level_finished_images/lock.png")
            level_buttons[i].toggle_clickable()
        i += 1
        

    back_button.draw(window)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                enemy_group.empty()
                if len(player_group) == 0:
                    current_player = Character(65, SCREEN_HEIGHT - 160, 3, 0, window)
                    player_group.add(current_player)
                if event.button == 1 and level_1_button.is_pressed():
                    pygame.display.set_caption("Level 1")
                    for i in range(len(level_one_coordinates)):
                        level_one_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_one_coordinates[i][0],
                                    SCREEN_HEIGHT - level_one_coordinates[i][1],
                                    40, 40, window, level_one_enemy[i][0],
                                    level_one_enemy[i][1], 1)
                        enemy_group.add(level_one_enemies[i])
                    current_player.x = player_coords[1][0]
                    current_player.y = player_coords[1][1]
                    current_player.rect.center = player_coords[1]
                    level_play(level_info[0])

                elif event.button == 1 and level_2_button.is_pressed():
                    pygame.display.set_caption("Level 2")
                    for i in range(len(level_two_coordinates)):
                        level_two_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_two_coordinates[i][0],
                                    SCREEN_HEIGHT - level_two_coordinates[i][1],
                                    40, 40, window, level_two_enemy[i][0],
                                    level_two_enemy[i][1], 2)
                        enemy_group.add(level_two_enemies[i])
                    map_group.add(map_object_list[2])
                    current_player.x = player_coords[2][0]
                    current_player.y = player_coords[2][1]
                    current_player.rect.center = player_coords[2]
                    level_play(level_info[1])

                elif event.button == 1 and level_3_button.is_pressed():
                    pygame.display.set_caption("Level 3")
                    for i in range(len(level_three_coordinates)):
                        level_three_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_three_coordinates[i][0],
                                    SCREEN_HEIGHT - level_three_coordinates[i][1],
                                    40, 40, window, level_three_enemy[i][0],
                                    level_three_enemy[i][1], 3)
                        enemy_group.add(level_three_enemies[i])
                    map_group.add(map_object_list[3])
                    current_player.x = player_coords[3][0]
                    current_player.y = player_coords[3][1]
                    current_player.rect.center = player_coords[3]
                    level_play(level_info[2])

                elif event.button == 1 and level_4_button.is_pressed():
                    pygame.display.set_caption("Level 4")
                    for i in range(len(level_four_coordinates)):
                        level_four_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_four_coordinates[i][0],
                                    SCREEN_HEIGHT - level_four_coordinates[i][1],
                                    40, 40, window, level_four_enemy[i][0],
                                    level_four_enemy[i][1], 4)
                        enemy_group.add(level_four_enemies[i])
                    map_group.add(map_object_list[4])
                    current_player.x = player_coords[4][0]
                    current_player.y = player_coords[4][1]
                    current_player.rect.center = player_coords[4]
                    level_play(level_info[3])

                elif event.button == 1 and level_5_button.is_pressed():
                    pygame.display.set_caption("Level 5")
                    for i in range(len(level_five_coordinates)):
                        level_five_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_five_coordinates[i][0],
                                    SCREEN_HEIGHT - level_five_coordinates[i][1],
                                    40, 40, window, level_five_enemy[i][0],
                                    level_five_enemy[i][1], 5)
                        enemy_group.add(level_five_enemies[i])
                    map_group.add(map_object_list[5])
                    current_player.x = player_coords[5][0]
                    current_player.y = player_coords[5][1]
                    current_player.rect.center = player_coords[5]
                    level_play(level_info[4])

                elif event.button == 1 and level_6_button.is_pressed():
                    pygame.display.set_caption("Level 6")
                    for i in range(len(level_six_coordinates)):
                        level_six_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_six_coordinates[i][0],
                                    SCREEN_HEIGHT - level_six_coordinates[i][1],
                                    40, 40, window, level_six_enemy[i][0],
                                    level_six_enemy[i][1], 6)
                        enemy_group.add(level_six_enemies[i])
                    map_group.add(map_object_list[6])
                    level_play(level_info[5])

                elif event.button == 1 and level_7_button.is_pressed():
                    pygame.display.set_caption("Level 7")
                    for i in range(len(level_seven_coordinates)):
                        level_seven_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_seven_coordinates[i][0],
                                    SCREEN_HEIGHT - level_seven_coordinates[i][1],
                                    40, 40, window, level_seven_enemy[i][0],
                                    level_seven_enemy[i][1], 7)
                        enemy_group.add(level_seven_enemies[i])
                    map_group.add(map_object_list[7])
                    level_play(level_info[6])

                elif event.button == 1 and level_8_button.is_pressed():
                    pygame.display.set_caption("Level 8")
                    for i in range(len(level_eight_coordinates)):
                        level_eight_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_eight_coordinates[i][0],
                                    SCREEN_HEIGHT - level_eight_coordinates[i][1],
                                    40, 40, window, level_eight_enemy[i][0],
                                    level_eight_enemy[i][1], 8)
                        enemy_group.add(level_eight_enemies[i])
                    map_group.add(map_object_list[8])
                    level_play(level_info[7])

                elif event.button == 1 and level_9_button.is_pressed():
                    pygame.display.set_caption("Level 9")
                    for i in range(len(level_nine_coordinates)):
                        level_nine_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_nine_coordinates[i][0],
                                    SCREEN_HEIGHT - level_nine_coordinates[i][1],
                                    40, 40, window, level_nine_enemy[i][0],
                                    level_nine_enemy[i][1], 9)
                        enemy_group.add(level_nine_enemies[i])
                    map_group.add(map_object_list[9])
                    level_play(level_info[8])

                elif event.button == 1 and level_10_button.is_pressed():
                    pygame.display.set_caption("Level 10")
                    for i in range(len(level_ten_coordinates)):
                        level_ten_enemies[i] = Enemy(f"Enemy {2}", 100, 100,
                                    level_ten_coordinates[i][0],
                                    SCREEN_HEIGHT - level_ten_coordinates[i][1],
                                    40, 40, window, level_ten_enemy[i][0],
                                    level_ten_enemy[i][1], 10)
                        enemy_group.add(level_ten_enemies[i])
                    map_group.add(map_object_list[10])
                    level_play(level_info[9])

                elif event.button == 1 and back_button.is_pressed():
                    main_menu()

        pygame.display.update()
    pygame.quit()

def save_file():
    open_file = open("save.json", 'w')
    save_upgrades = {}
    for i in range(len(upgrades)):
        save_upgrades[i + 1] = upgrades[i].levels_list
    save_dict = {'1': [save_upgrades, locked_levels, current_player.level_points, current_player.super_points]}
    json.dump(save_dict, open_file)

def upload_save():
    global locked_levels
    try:
        open_f = open('save.json')
        data = json.load(open_f)
        locked_levels = data['1'][1]
        count = 1
        for i in upgrades:
            i.levels_list = data['1'][0][f"{count}"]
            i.plus_button.levels_list = i.levels_list
            count += 1
        current_player.level_points = data['1'][2]
        current_player.super_points = data['1'][3]

        #current_player.super_points = 200
        #current_player.level_points = 200
    except:
        pass


current_player = Character(65, SCREEN_HEIGHT - 160, 3, 0, window)
player_group.add(current_player)

upload_save()
main_menu()