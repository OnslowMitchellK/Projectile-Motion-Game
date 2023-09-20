import pygame
import sys
from model import Enemy

pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 3), int(self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('test.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.initial_position = (x, y)  # Store the initial position
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

# Create sprite groups
character_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()

# Create characters and projectiles
# character = Character(700, 100)
# character_group.add(character)

projectile = Projectile(100, 70)
projectile_group.add(projectile)

jamal = Enemy(f"Enemy {2}", 100, 100, 25, 700, 100, 40, 40, screen)
character_group.add(jamal)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update projectile position
    projectile.rect.x += 1

    # Reset projectile if it goes off-screen
    if projectile.rect.right > screen.get_width():
        projectile.rect.topleft = projectile.initial_position

    # Use groupcollide() to detect collisions
    collisions = pygame.sprite.groupcollide(character_group, projectile_group, False, False, pygame.sprite.collide_mask)

    # Handle collisions
    for character, projectiles in collisions.items():
        print("Character hit by projectiles:", len(projectiles))
        projectile.rect.topleft = projectile.initial_position  # Reset projectile position

    # Clear the screen
    screen.fill((3, 50, 4))

    # Draw sprites
    character_group.draw(screen)
    screen.blit(projectile.mask_image, projectile.rect)
    pygame.draw.rect(screen, (255, 0, 0), projectile.rect, 2)
    jamal.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
