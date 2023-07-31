from dataclasses import dataclass
import json
import pygame
from sys import os


@dataclass
class Enemy(pygame.sprite.Sprite):
    """Enemy Class."""

    def __init__(self):
        _name: str = "KAL"
        _health: int = 100
        _damage: int = 25
        # pygame.sprite.Sprite.__init__(self)
        # self.images = []

        # img = pygame.image.load(os.path.join('images', 'enemy.png')).convert()
        # self.images.append(img)
        # self.image = self.images[0]
        # self.rect = self.image.get_rect()

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


enemy = Enemy()
print(enemy.health)