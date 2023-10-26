import pygame
LEVEL_ONE_ENEMY_NUM = 2
enemy_image = pygame.image.load("Assets/player_enemy_images/enemy.jpeg")


class Enemy(pygame.sprite.Sprite):
    """Enemy Class."""

    def __init__(self, name: str, health: int, shield: int,
                 x: int, y: int, width: int, height: int,
                 screen, angle: int, speed: int, level: int):
        """Enemy variables."""
        super().__init__()
        self.image = pygame.image.load('Assets/player_enemy_images/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 3), int(self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.alive_image = pygame.image.load('Assets/player_enemy_images/enemy.png').convert_alpha()
        self.dead_image = pygame.image.load('animations/enemy_animation/Enemy 1/Enemywhite.png').convert_alpha()
        self.shoot_animations = [pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_1.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_2.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_3.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_4.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_5.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_6.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_7.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_8.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_9.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3))), pygame.transform.scale(pygame.image.load('animations/enemy_animation/Enemy 1/ellipse_10.png').convert_alpha(), (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3)))]
        self.dead_image = pygame.transform.scale(self.dead_image, (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3)))
        self.alive_image = pygame.transform.scale(self.alive_image, (int(self.alive_image.get_width() * 3), int(self.alive_image.get_height() * 3)))
        self.x = x
        self.y = y
        self._name: str = name
        self.level = level
        self.max_health = health * (1 + (self.level - 1 ** 2) * 0.1)
        self._health: int = health * (1 + (self.level - 1 ** 2) * 0.1)
        self._shield: int = shield
        self.damage: int = 12.5 + int(self.level * 5)
        self._width: int = width
        self._height: int = height
        self.screen = screen
        self.angle = angle
        self.speed = speed

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