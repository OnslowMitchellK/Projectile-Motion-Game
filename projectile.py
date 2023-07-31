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
