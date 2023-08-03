import math
import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
win.fill((255, 255, 255))

class Projectile:
    def __init__(self, type: str, width: int, height: int, ) -> None:
        self._type = type
        self._width = width
        self._height = height

    @property
    def type(self):
        return self._type

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def player_launch(self, angle: float, power: float, gravity: float):
        horz_init_vel = power * math.cos(angle)
        vert_init_vel = power * math.sin(angle)
        print(horz_init_vel, vert_init_vel)
        time_to_max = (0 - horz_init_vel) / gravity
        print(time_to_max)
        vert_dist = (0 - vert_init_vel) / (2 * gravity)
        print(vert_dist)
    
    def draw(self):
        pygame.draw.circle(win, (0, 200, 200), (20, 40), 10)

test = Projectile("Cannon", 200, 200)
test.player_launch(math.pi/6, 40, -9.81)
test.draw()