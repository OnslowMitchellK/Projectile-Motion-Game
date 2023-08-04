from dataclasses import dataclass
import json
import pygame
from random import randint
LEVEL_ONE_ENEMY_NUM = 2
enemy_image = pygame.image.load("enemy.jpeg")


@dataclass
class Enemy():
    """Enemy Class."""

    def __init__(self, name: str, health: int,
                 damage: int, x: int, y: int, width: int, height: int):
        """Enemy variables"""
        self._name: str = name
        self._health: int = health
        self._damage: int = damage
        self._x: int = x
        self._y: int = y
        self._width: int = width
        self._height: int = height

    @property
    def name(self) -> str:
        """Name getter."""
        return self._name

    @property
    def health(self) -> int:
        """Health getter."""
        return self._health

    @property
    def damage(self) -> int:
        """Damage getter."""
        return self._damage


level_one_enemies = {}
for i in range(LEVEL_ONE_ENEMY_NUM):
    level_one_enemies[i] = Enemy(f"Enemy {i}", 100, 25,
                                 randint(0, 20), randint(0, 20), 40, 40)
