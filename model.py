from dataclasses import dataclass
import pygame
from random import randint
LEVEL_ONE_ENEMY_NUM = 2
enemy_image = pygame.image.load("enemy.jpeg")


@dataclass
class Enemy(pygame.sprite.Sprite):
    """Enemy Class."""

    def __init__(self, name: str, health: int, shield: int,
                 damage: int, x: int, y: int, width: int, height: int, rect):
        """Enemy variables."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self._name: str = name
        self._health: int = health
        self._shield: int = shield
        self._damage: int = damage
        self._x: int = x
        self._y: int = y
        self._width: int = width
        self._height: int = height
        self.rect = rect

    @property
    def name(self) -> str:
        """Name getter."""
        return self._name

    @property
    def health(self) -> int:
        """Health getter."""
        return self._health

    @property
    def shield(self) -> int:
        """Shield getter."""
        return self._shield

    @property
    def damage(self) -> int:
        """Damage getter."""
        return self._damage

# print("Name: ", level_one_enemies[1].name)
# print("Health: ", level_one_enemies[1].health)
# print("Damage: ", level_one_enemies[1].damage)
# print("x Coordinate: ", level_one_enemies[1]._x)
# print("y Coordinate: ", level_one_enemies[1]._y)
# print("Width: ", level_one_enemies[1]._width)
# print("Height: ", level_one_enemies[1]._height)
