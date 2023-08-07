import pygame
import sys
# from model import level_one_enemies, level_one_enemies[i].image
from model import Enemy
# from os import join

FPS = 60

pygame.init()

screen_width = 1280
screen_height = 720


LEVEL_ONE_ENEMY_NUM = 2
level_one_enemies = {}
for i in range(LEVEL_ONE_ENEMY_NUM):
    level_one_enemies[i] = Enemy(f"Enemy {i}", 100, 100, 25, screen_width - 100, screen_height - 100, 40, 40)

window = pygame.display.set_mode((screen_width, screen_height),
                                 pygame.RESIZABLE)
pygame.display.set_caption('Shooter')

background_image = pygame.image.load("background.jpg")
bg = pygame.transform.scale(background_image, [screen_width, screen_height])

FLOOR_HEIGHT = 100



"""
COLLISION TESTING.
"""
enemy_rect = level_one_enemies[i].image.get_rect()
x_speed, y_speed = 5,4


def bouncing_rect():
    global x_speed, y_speed, screen_width, screen_height
    enemy_rect.x += x_speed
    enemy_rect.y += y_speed

    if enemy_rect.right >= screen_width or enemy_rect.left <= 0:
        x_speed *= -1
    if enemy_rect.bottom >= screen_height - FLOOR_HEIGHT or enemy_rect.top <= 0:
        y_speed *= -1
    window.blit(level_one_enemies[i].image, enemy_rect)
    pygame.display.flip()
"""."""


def main(window):
    """Main."""
    global screen_width, screen_height
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Quit game.
            if event.type == pygame.QUIT:
                run = False
                break
        # window.blit(bg, [0, 0])
        # window.blit(level_one_enemies[i].image, [screen_width - level_one_enemies[i].image.get_width(), screen_height - level_one_enemies[i].image.get_height()])
        floor = pygame.Rect(0, screen_height - FLOOR_HEIGHT,
                    screen_width, FLOOR_HEIGHT)
        pygame.draw.rect(window, (255, 0, 255), floor)
        # window.blit(level_one_enemies[i].image, enemy_rect)
        # window.blit(level_one_enemies[0].image, level_one_enemies[0].rect)
        pygame.display.flip()
        print(window.get_width())
        screen_width = window.get_width()
        screen_height = window.get_height()
        bouncing_rect()

        # draw(window, background, bg_image)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)


# # Define floor parameters
# FLOOR_WIDTH, FLOOR_HEIGHT = screen_width, 100
# FLOOR_COLOR = (0, 128, 0)  # Green color (RGB)

# # Create the floor surface
# floor_surface = pygame.Surface((FLOOR_WIDTH, FLOOR_HEIGHT))
# floor_surface.fill(FLOOR_COLOR)

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Clear the screen
#     window.fill((255, 255, 255))  # White background color

#     # Draw the floor at the bottom-center of the screen
#     floor_x = (screen_width - FLOOR_WIDTH) // 2
#     floor_y = screen_height - FLOOR_HEIGHT
#     window.blit(floor_surface, (floor_x, floor_y))

#     # Update the display
#     pygame.display.flip()
