import math
import pygame
import time

pygame.init()

win = pygame.display.set_mode((1000, 500))
background = pygame.Surface((1000, 500))
background.fill((255, 255, 255))
pygame.display.set_caption("Test projectile")
win.fill((255, 255, 255))

FPS = 60

img = pygame.image.load("test.png")
img = pygame.transform.scale(img, (40, 40))

class Projectile:
    def __init__(self, type: str, width: int, height: int, gravity: float) -> None:
        self._type = type
        self._width = width
        self._height = height
        self._gravity = gravity

    @property
    def type(self):
        return self._type

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
    @property
    def gravity(self):
        return self._gravity

    def player_launch(self, angle: float, power: float):
        self.horz_init_vel = power * math.cos(angle)
        self.vert_init_vel = power * math.sin(angle)
        self.time_to_max = (0 - self.horz_init_vel) / self._gravity

    def horz_distance(self, time):
        return (self.horz_init_vel * time)

    def vert_distance(self, time):
        return (self.vert_init_vel * time) + (0.5 * self._gravity * time ** 2)

    def draw(self):
        launch_time = 0
        run = True
        while run:
            if test.vert_distance(launch_time) < 0:
                break
            win.blit(background, (0, 0))
            win.blit(img, ((-20 + test.horz_distance(launch_time)), (480 - test.vert_distance(launch_time))))
            time.sleep(0.01)
            launch_time += (1 / FPS)
            pygame.display.update()

test = Projectile("Cannon", 200, 200, -9.81)
test.player_launch(math.pi/6, 100)
test.draw()
