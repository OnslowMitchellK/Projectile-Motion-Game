from dataclasses import dataclass
import json
import pygame
LEVEL_ONE_ENEMY_NUM = 2


@dataclass
class Enemy():
    """Enemy Class."""

    def __init__(self, name: str, health: int, damage: int):
        self._name: str = name
        self._health: int = health
        self._damage: int = damage

    @property
    def name(self) -> str:
        """Name getter."""
        return self._name
    
    @property
    def health(self) -> str:
        """Health getter."""
        return self._health

    @property
    def damage(self) -> str:
        """Damage getter."""
        return self._damage

level_one_enemies = {}
for i in range(LEVEL_ONE_ENEMY_NUM):
    level_one_enemies[i] = Enemy(f"Enemy {i}", 100, 25)
enemy = Enemy("jamal", 100, 25)
print(level_one_enemies[1].name)