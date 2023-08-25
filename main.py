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
level_one_coordinates = [[40 * 17, 40 * 2.95], [40 * 26, 40 * 13.05]]

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

class Main_Menu_Projectile:
    def __init__(self, image="test.png") -> None:
        self._image = pygame.image.load(image)
        size = randint(30, 40)
        self._image = pygame.transform.scale(self._image, (size, size))
        self._rect = self._image.get_rect()
        self._rect.x = randint(50, 300)
        self._rect.y = randint(50, SCREEN_HEIGHT - 50)
        self._dx = randint(3, 8)
        self._dy = randint(3, 8)

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


class Projectile:
    def __init__(self, start_x, start_y, image, size, background, map, screen, tile_size) -> None:
        self._start_x = start_x
        self._start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self._projectile_rect = pygame.Rect(0, 0, self.size, self.size)
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
        self.projectile_rect.x = self._start_x
        self.projectile_rect.y = self._start_y
        self.screen.blit(self.image, (self._start_x, self._start_y))
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
                draw_enemies(level_one_enemies)
                self.screen.blit(self.image, (x, y))
                self.projectile_rect.x = x
                self.projectile_rect.y = y
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


def level_play(screen, map_background, map_tiles, tile_size, projectile_starting_coords):
    clock = pygame.time.Clock()
    current = True
    shoot = False

    projectile = Projectile(projectile_starting_coords[0], projectile_starting_coords[1], pygame.image.load("test.png"), PJ_S, map_background, map_tiles, screen, tile_size)

    screen.blit(map_background, (0, 0))
    draw_tiles(map_tiles, tile_size, True)
    projectile.draw_starting_point()
    draw_enemies(level_one_enemies)

    x_centre_s = projectile_starting_coords[0] + 0.5 * PJ_S
    y_centre_s = projectile_starting_coords[1] + 0.5 * PJ_S
    ARC_WIDTH = 200
    arc_rect = pygame.Rect(0, 0, ARC_WIDTH, ARC_WIDTH)
    arc_rect.center = (x_centre_s, y_centre_s)
    angle_font = pygame.font.SysFont("C:/Fonts/Barriecito-Regular.ttf", 20)
    angle_text = angle_font.render("0°", True, "Green")
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
                

        screen.blit(map_background, (0, 0))
        draw_tiles(map_tiles, tile_size)
        draw_enemies(level_one_enemies)
        projectile.draw_starting_point()
        angle = math.atan2(SCREEN_HEIGHT - pygame.mouse.get_pos()[1] - (SCREEN_HEIGHT - y_centre_s), pygame.mouse.get_pos()[0] - (x_centre_s))
        pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), pygame.mouse.get_pos(), 2)
        if pygame.mouse.get_pos()[0] >= x_centre_s + ARC_WIDTH / 2:
            pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), (pygame.mouse.get_pos()[0], y_centre_s), 2)
        else:
            pygame.draw.line(window, ((255, 255, 255)), (x_centre_s, y_centre_s), (x_centre_s + ARC_WIDTH / 2, y_centre_s), 2)
        angle_text = angle_font.render(f"{round(math.degrees(angle), 1)}°", True, "Green")
        window.blit(angle_text, ((x_centre_s + ARC_WIDTH), y_centre_s - 20))
        pygame.draw.arc(window, ((0, 0, 0)), arc_rect, 0, angle, 10)


        if shoot:
            projectile.draw_trajectory()
            projectile.draw_starting_point()
            shoot = False
        
        pygame.display.update()
    pygame.quit()


projectile_rects = [Main_Menu_Projectile() for x in range(20)]

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
        for proj in projectile_rects:
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

default_controls = {

}

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
    level_1_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.25,"Level 1", 100, 100, font_size=30, border_radius=20)
    level_2_button = Button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.25, "Level 2", 100, 100, font_size=30, border_radius=20)
    level_3_button = Button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.25,"Level 3", 100, 100, font_size=30, border_radius=20)
    level_4_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.25, "Level 4", 100, 100, font_size=30, border_radius=20)
    level_5_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.5,"Level 5", 100, 100, font_size=30, border_radius=20)
    level_6_button = Button(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5, "Level 6", 100, 100, font_size=30, border_radius=20)
    level_7_button = Button(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.5,"Level 7", 100, 100, font_size=30, border_radius=20)
    level_8_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.5, "Level 8", 100, 100, font_size=30, border_radius=20)
    level_9_button = Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.75,"Level 9", 100, 100, font_size=30, border_radius=20)
    level_10_button = Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.75, "Level 10", 100, 100, font_size=30, border_radius=20)
    back_button = Button(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.75, "Back", 350, 100, font_size=50, border_radius=20)
    buttons = [level_1_button, level_2_button, level_3_button, level_4_button, level_5_button, level_6_button, level_7_button,
               level_8_button, level_9_button, level_10_button, back_button]
    pygame.display.set_caption("Level Menu")
    window.fill((90, 80, 40))
    
    for button in buttons:
        button.draw(window)

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
                                    40, 40, window)

                    level_play(window, airport_background, map_1, 40, [0, (SCREEN_HEIGHT - 120)])

                elif event.button == 1 and level_2_button.is_pressed():
                    pygame.display.set_caption("Level 2")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_3_button.is_pressed():
                    pygame.display.set_caption("Level 3")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_4_button.is_pressed():
                    pygame.display.set_caption("Level 4")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_5_button.is_pressed():
                    pygame.display.set_caption("Level 5")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_6_button.is_pressed():
                    pygame.display.set_caption("Level 6")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_7_button.is_pressed():
                    pygame.display.set_caption("Level 7")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_8_button.is_pressed():
                    pygame.display.set_caption("Level 8")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_9_button.is_pressed():
                    pygame.display.set_caption("Level 9")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])

                elif event.button == 1 and level_10_button.is_pressed():
                    pygame.display.set_caption("Level 10")
                    level_play(window, airport_background, map_2, 20, [(0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - 100)])
                
                elif event.button == 1 and back_button.is_pressed():
                    main_menu()

        pygame.display.update()
    pygame.quit()


window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")


main_menu()