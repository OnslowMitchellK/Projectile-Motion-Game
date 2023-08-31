"""DOGSTRING."""
import pygame
import math
import time
from button import Button
from model import Enemy
from random import randint, choice
from character_testing import Test_Character

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

map_1 = """00000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000003333300
0000000000000000000000000333330
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000000000000
00000000000000000000000000000000
33333333333333333333333333333333
33333333333333333333333333333333"""


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
level_one_coordinates = [[40 * 17, 40 * 6], [40 * 26, 40 * 15.05]]
level_one_enemy = [[130, 80, level_one_coordinates[0][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[0][1] + 20],
                   [170, 98, level_one_coordinates[1][0] + 80, SCREEN_HEIGHT -
                    level_one_coordinates[1][1]]]

airport_background = pygame.image.load("completed_airport_background.png")
airport_background = pygame.transform.scale(airport_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_2_background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
map_2_background.fill((200, 30, 20))


img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")
transparent_tile = pygame.image.load("transparent_tile.png")
font_directory = "C:/Fonts/Barriecito-Regular.ttf"
tile_rects = []
# projectile_side
PJ_S = 40

enemy_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
enemy_projectile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Main_Menu_Projectile:
    def __init__(self, image="test.png", possible_speeds = [-8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8]) -> None:
        self._image = pygame.image.load(image)
        size = randint(30, 50)
        self._image = pygame.transform.scale(self._image, (size, size))
        self._rect = self._image.get_rect()
        self._rect.x = randint(50, 300) if randint(1, 2) == 1 else randint(SCREEN_WIDTH - 300, SCREEN_WIDTH - 50)
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
    def __init__(self, start_x, start_y, image, size, background, map, screen, tile_size) -> None:
        super().__init__()
        self._start_x = start_x
        self._start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        # self._rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.image_mask = pygame.mask.from_surface(self.image)
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
    def start_x(self):
        return self._start_x
    
    @property
    def start_y(self):
        return self._start_y

    @property
    def shoot(self):
        return self._shoot

    @property
    def angle(self):
        return self._angle

    @property
    def speed(self):
        return self._speed

    # @property
    # def rect(self):
    #     return self._rect

    def change_angle(self, change_in_angle):
        self._angle = change_in_angle
        # self._angle += change_in_angle if 0 <= self._angle + change_in_angle <= 90 else 0
        # pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def change_speed(self, change_in_speed):
        self._speed = change_in_speed
        # self._speed += change_in_speed if 0 <= self._speed + change_in_speed <= 150 else 0
        # pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

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

    def draw_trajectory(self):
        coordinates = self.trajectory(1 / 10, self._start_x, self._start_y, self._angle, self._speed)
        run = True

        while run:
            for coords in coordinates:
                x = coords[0]
                y = coords[1]

                self.screen.blit(self.background, (0, 0))
                draw_tiles(self.map, self.tile_size)
                player_group.draw(self.screen)
                enemy_group.draw(self.screen)
                self.rect.centerx = x
                self.rect.centery = y
                self.screen.blit(self.image, (self.rect.x, self.rect.y))
                for enemy in enemy_group:
                    enemy.draw_health()
                current_player.draw_health()
                pygame.display.update()

                for tile in tile_rects:
                    if self.rect.colliderect(tile):
                        time.sleep(0.5)
                        run = False
                        break

                # Use groupcollide() to detect collisions
                collisions = pygame.sprite.groupcollide(enemy_group, projectile_group,
                                                        False, False, pygame.sprite.collide_mask)

                # Handle collisions
                for enemy, projectiles in collisions.items():
                    print("Character hit by projectiles:", len(projectiles))
                    time.sleep(0.5)
                    deduct_enemy_health(enemy)
                    return False
                if not run:
                    break
            break
        return


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
            # self.screen.blit(current_player.image, current_player.rect)
            player_group.draw(self.screen)
            enemy_group.draw(self.screen)
            for enemy in enemy_group:
                enemy.draw_health()
            current_player.draw_health()

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
            collisions = pygame.sprite.groupcollide(player_group, enemy_projectile_group,
                                                    False, False, pygame.sprite.collide_mask)

            # Handle collisions
            for player, projectiles in collisions.items():
                # print("Character hit by projectiles:", len(projectiles))
                time.sleep(0.5)
                deduct_player_health(player)
                return False


def deduct_player_health(player):
    global player_group
    damage = randint(50, 90)
    player.health -= damage

    print(" P health: ", player.health)

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
        current_player.level_points += 1
        print(current_player.level_points)


def player_dead():
    print("PLAYER IS DEAD")


def make_window(width: int, height:int, caption: str)  -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win


def draw_tiles(map, tile_size, first = False):
    scaled_img_1 = pygame.transform.scale(img_1, (tile_size, tile_size))
    scaled_img_2 = pygame.transform.scale(img_2, (tile_size, tile_size))
    scaled_transparent_tile = pygame.transform.scale(transparent_tile, (tile_size, tile_size))
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
            elif tile == "3":
                window.blit(scaled_transparent_tile, (x * tile_rect.width, y * tile_rect.height))
                if first:
                    if not duplicate:
                        tile_rects.append(tile_rect.copy())
            x += 1
        y += 1


def draw_enemies(enemy_level_list):
    for i in range(len(level_one_enemies)):
        level_one_enemies[i].draw()

def shoot_display(starting_coords, min_angle, max_angle):
    x_centre_s = starting_coords[0]
    y_centre_s = starting_coords[1]
    angles = [max_angle, min_angle]
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
    
    if min_angle == 0:
        if pos[1] > y_centre_s:
            draw = False
            angle = math.radians(min_angle)
    
    if max_angle == 90:
        if pos[0] < x_centre_s:
            draw = False
            angle = math.radians(max_angle)
    #         if pos[1] < y_centre_s:
    #             pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), (x_centre_s, pos[1]), 2)


    # if angle > min_angle and angle < max_angle and draw:
    #     pygame.draw.line(window, ((255, 255, 255,)), (x_centre_s, y_centre_s), pos, 2)

    # if pos[0] >= x_centre_s + ARC_WIDTH / 2:
    #     pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), (pos[0], y_centre_s), 2)
    # else:
    #     pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), (x_centre_s + ARC_WIDTH / 2, y_centre_s), 2)

    angle_text = font.render(f"{round(math.degrees(angle), 1)}°,", True, "white")
    window.blit(angle_text, (10, SCREEN_HEIGHT - 50))

    # pygame.draw.arc(window, ((0, 0, 0)), arc_rect, 0, angle, 10)
    # https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
    closest_angle = min(angles, key=lambda x:abs(x-math.degrees(angle)))
    speed = pos[0] / 5 if closest_angle == 0 else (y_centre_s - pos[1]) / 5
    speed = 0 if speed < 0 else speed
    speed_text = font.render(f"{speed} px/s", True, "white")
    window.blit(speed_text, (120, SCREEN_HEIGHT - 50))

    return [speed, math.degrees(angle)]


def enemy_shoot(enemy_projectile):
    rand_list = [0, randint(-20, 20)]
    for enemy in enemy_group:
        enemy_projectile.start_x = enemy.rect.topleft[0] + 80
        enemy_projectile.start_y = enemy.rect.topleft[1] + 20
        # enemy_projectile._angle = enemy.angle + rand_list[randint(0, 1)]
        enemy_projectile._speed = enemy.speed + rand_list[randint(0, 1)]
        enemy_projectile._angle = enemy.angle
        # enemy_projectile._speed = enemy.speed
        enemy_projectile.draw_starting_point()
        enemy_projectile.draw_trajectory()

def level_play(screen, map_background, map_tiles, tile_size, projectile_starting_coords, min_angle, max_angle):
    dot_distance = 6
    clock = pygame.time.Clock()
    current = True
    shoot = False

    projectile = Projectile(projectile_starting_coords[0], projectile_starting_coords[1], pygame.image.load("test.png"), PJ_S, map_background, map_tiles, screen, tile_size)
    projectile_group.add(projectile)
    enemy_projectile = Enemy_Projectile(0, 0, "test.png", PJ_S, map_background, map_tiles, screen, tile_size, 0, 0)
    enemy_projectile_group.add(enemy_projectile)

    screen.blit(map_background, (0, 0))
    draw_tiles(map_tiles, tile_size, True)
    projectile.draw_starting_point()
    player_group.draw(screen)
    for enemy in enemy_group:
        enemy.draw_health()
    current_player.draw_health()

    print("enemy group:", enemy_group)
    print("p projectile group:", projectile_group)
    print("e projectile group:", enemy_projectile_group)
    print("player group:", player_group)


    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_q:
                    current = False if current else True
                # if event.__dict__["key"] == pygame.K_SPACE:
                #     shoot = True
                #     break
            elif event.type == pygame.MOUSEBUTTONDOWN and not shoot:
                if event.button == 1:
                    shoot = True
                    break
                # if event.button == 4 and current:
                #     projectile.change_angle(5)
                # elif event.button == 5 and current:
                #     projectile.change_angle(-5)
                # elif event.button == 4 and not current:
                #     projectile.change_speed(5)
                # elif event.button == 5 and not current:
                #     projectile.change_speed(-5)
                

        screen.blit(map_background, (0, 0))
        draw_tiles(map_tiles, tile_size)
        player_group.draw(screen)
        enemy_group.draw(screen)
        for enemy in enemy_group:
            enemy.draw_health()
        current_player.draw_health()
        projectile.draw_starting_point()
        returned = shoot_display(projectile_starting_coords, min_angle, max_angle)
        coords = projectile.trajectory(1 / 3, projectile_starting_coords[0], projectile_starting_coords[1], returned[1], returned[0])
        for i in coords[:10]:
            if i[0] < SCREEN_WIDTH / dot_distance:
                pygame.draw.circle(window, "yellow", (i), 10)
        
        if shoot:
            projectile.change_speed(returned[0])
            projectile.change_angle(returned[1])
            projectile.draw_trajectory()
            projectile.draw_starting_point()
            shoot = False
            enemy_shoot(enemy_projectile)
        
        pygame.display.update()
    pygame.quit()


rects = [Main_Menu_Projectile() for x in range(100)]

def main_menu():
    TOLERANCE = 10
    main_menu_clock = pygame.time.Clock()
    window.fill((19, 50, 143))
    pygame.display.set_caption("Main Menu")

    play_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, "Play")
    options_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "Options")
    quit_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75, "Quit")

    play_button.draw(window)
    options_button.draw(window)
    quit_button.draw(window)
    buttons = [play_button, options_button, quit_button]

    run = True
    while run:
        main_menu_clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_button.is_pressed():
                    level_menu()
                elif event.button == 1 and options_button.is_pressed():
                    options_menu()
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
        

        play_button.draw(window)      
        options_button.draw(window)  
        quit_button.draw(window)
        pygame.display.update()



    pygame.quit()


def controls_menu():
    pygame.display.set_caption("Controls Menu")
    window.fill((10, 80, 180))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def options_menu():
    controls_button = Button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, "Controls")
    back_button = Button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.75, "Back")

    pygame.display.set_caption("Options Menu")
    window.fill((20, 90, 130))

    controls_button.draw(window)
    back_button.draw(window)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and controls_button.is_pressed():
                    controls_menu()
                elif event.button == 1 and back_button.is_pressed():
                    main_menu()

        pygame.display.update()
    pygame.quit()

def level_menu():
    level_1_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.25,"Level 1", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_2_button = Button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.25, "Level 2", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_3_button = Button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.25,"Level 3", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_4_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.25, "Level 4", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_5_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.5,"Level 5", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_6_button = Button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5, "Level 6", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_7_button = Button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.5,"Level 7", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_8_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.5, "Level 8", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_9_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.75,"Level 9", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    level_10_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.75, "Level 10", 100, 100, font_size=30, border_radius=20, background_colour=(190, 10, 180))
    back_button = Button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.75, "Back", 350, 100, font_size=50, border_radius=20, background_colour=(190, 10, 180))
    level_buttons = [level_1_button, level_2_button, level_3_button, level_4_button, level_5_button, level_6_button, level_7_button,
               level_8_button, level_9_button, level_10_button]
    

    pygame.display.set_caption("Level Menu")
    window.fill((90, 80, 40))
    
    for button in level_buttons:
        button.draw(window)
        button.lock_button(window, "lock.png")
        button.toggle_clickable()

    level_1_button.draw(window)
    level_1_button.toggle_clickable()
    back_button.draw(window)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and level_1_button.is_pressed():
                    pygame.display.set_caption("Level 1")
                    for i in range(len(level_one_coordinates)):
                        level_one_enemies[i] = Enemy(f"Enemy {2}", 100, 100, 25,
                                    level_one_coordinates[i][0],
                                    SCREEN_HEIGHT - level_one_coordinates[i][1],
                                    40, 40, window, level_one_enemy[i][0],
                                    level_one_enemy[i][1], 6)
                        enemy_group.add(level_one_enemies[i])

                    level_play(window, airport_background, map_1, 40, [20, (SCREEN_HEIGHT - 120)], 0, 90)

                elif event.button == 1 and level_2_button.is_pressed():
                    pygame.display.set_caption("Level 2")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_3_button.is_pressed():
                    pygame.display.set_caption("Level 3")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_4_button.is_pressed():
                    pygame.display.set_caption("Level 4")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_5_button.is_pressed():
                    pygame.display.set_caption("Level 5")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_6_button.is_pressed():
                    pygame.display.set_caption("Level 6")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_7_button.is_pressed():
                    pygame.display.set_caption("Level 7")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_8_button.is_pressed():
                    pygame.display.set_caption("Level 8")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_9_button.is_pressed():
                    pygame.display.set_caption("Level 9")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)

                elif event.button == 1 and level_10_button.is_pressed():
                    pygame.display.set_caption("Level 10")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)], 0, 90)
                
                elif event.button == 1 and back_button.is_pressed():
                    main_menu()

        pygame.display.update()
    pygame.quit()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")
current_player = Test_Character(65, SCREEN_HEIGHT - 160, 1.5, 0, window)
player_group.add(current_player)

main_menu()
