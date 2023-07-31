import math

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

    def player_launch(self, angle: float, power: float):
        horz_init_vel = power * math.cos(angle)
        vert_init_vel = power * math.sin(angle)
        print(horz_init_vel, vert_init_vel)

test = Projectile("Cannon", 200, 200)
test.player_launch(math.pi, 4)