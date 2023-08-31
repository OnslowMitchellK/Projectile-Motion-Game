import pygame
from random import randint
LEVEL_ONE_ENEMY_NUM = 2
enemy_image = pygame.image.load("enemy.jpeg")


class Enemy(pygame.sprite.Sprite):
    """Enemy Class."""

    def __init__(self, name: str, health: int, shield: int,
                 damage: int, x: int, y: int, width: int, height: int,
                 screen, angle: int, speed: int, level: int):
        """Enemy variables."""
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 3), int(self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image_mask = pygame.mask.from_surface(self.image)

        self.x = x
        self.y = y
        self._name: str = name
        self.level = level - 1
        self.max_health = health * (1 + (self.level ** 2) * 0.02)
        self._health: int = health * (1 + (self.level ** 2) * 0.02)
        self._shield: int = shield
        self._damage: int = damage
        self._width: int = width
        self._height: int = height
        self.screen = screen
        self.angle = angle
        self.speed = speed

    # @property
    # def name(self) -> str:
    #     """Name getter."""
    #     return self._name

    @property
    def health(self) -> int:
        """Health getter."""
        return self._health

    @health.setter
    def health(self, new_health) -> int:
        """Healther setter."""
        if new_health < 0:
            self._health = 0
        else:
            self._health = new_health

    @property
    def shield(self) -> int:
        """Shield getter."""
        return self._shield

    @shield.setter
    def shield(self, new_shield) -> int:
        """Healther setter."""
        if new_shield < 0:
            self._shield = 0
        else:
            self._shield = new_shield

    # @property
    # def damage(self) -> int:
    #     """Damage getter."""
    #     return self._damage

    def draw(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

    def die(self):
        self.kill()

    def draw_health(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y - (0.125 * self.image.get_height()), 100, 5))
        green_percent = int(self.health / (self.max_health / 100))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.x, self.y - (0.125 * self.image.get_height()), green_percent, 5))
        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x, self.y - (0.175 * self.image.get_height()), self.shield, 5))
# print("Name: ", level_one_enemies[1].name)
# print("Health: ", level_one_enemies[1].health)
# print("Damage: ", level_one_enemies[1].damage)
# print("x Coordinate: ", level_one_enemies[1]._x)
# print("y Coordinate: ", level_one_enemies[1]._y)
# print("Width: ", level_one_enemies[1]._width)
# print("Height: ", level_one_enemies[1]._height)
