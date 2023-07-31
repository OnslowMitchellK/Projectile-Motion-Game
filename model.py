from dataclasses import dataclass
import json
import pygame


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


enemy = Enemy("jamal", 100, 25)
print(enemy.health)