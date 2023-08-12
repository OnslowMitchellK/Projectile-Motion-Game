import pygame
import math
import time
pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

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

TILE_SIZE = 20

img_1 = pygame.image.load("tile1.png")
img_2 = pygame.image.load("tile2.png")
img_1 = pygame.transform.scale(img_1, (TILE_SIZE, TILE_SIZE))
img_2 = pygame.transform.scale(img_2, (TILE_SIZE, TILE_SIZE))

tile_rect = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
tile_rects = []

class Projectile:
    def __init__(self, start_x, start_y, image, size, background, map) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self._projectile_rect = pygame.Rect(0, 0, 0.5 * self.size, 0.5 * self.size)
        self.background = background
        self.map = map

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
        window.blit(self.image, (self.start_x, self.start_y))
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

            window.blit(self.background, (0, 0))
            draw_tiles(self.map)
            window.blit(self.image, (x, y))
            self.projectile_rect.x = x + 0.25 * self.size
            self.projectile_rect.y = y + 0.25 * self.size
            pygame.display.update()

            for tile in tile_rects:
                if self.projectile_rect.colliderect(tile):
                    time.sleep(0.5)
                    return False

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
    pygame.display.update()

class Button:
    def __init__(self) -> None:
        pass


def menu():
    pass



def main(projectile: Projectile):
    current = True
    shoot = False

    window.blit(map_1_background, (0, 0))
    draw_tiles(map_1, True)
    projectile_one.draw_starting_point()

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
            shoot = projectile.draw_trajectory()
            window.blit(map_1_background, (0, 0))
            draw_tiles(map_1)
            projectile.draw_starting_point()
            pygame.display.update()

window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 0")
# projectile_side
PJ_S = 80
projectile_one = Projectile((0 - (0.25 * PJ_S)), (SCREEN_HEIGHT - (0.75 * PJ_S) - 60), pygame.image.load("test.png"), PJ_S, map_1_background, map_1)
main(projectile_one)
