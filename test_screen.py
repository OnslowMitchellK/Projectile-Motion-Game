import pygame
import sys
from model import level_one_enemies, enemy_image
# from os import join

FPS = 60

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

background_image = pygame.image.load("background.jpg")
bg = pygame.transform.scale(background_image, [SCREEN_WIDTH, SCREEN_HEIGHT])

FLOOR_HEIGHT = 100
floor = pygame.Rect(0, SCREEN_HEIGHT - FLOOR_HEIGHT,
                    SCREEN_WIDTH, FLOOR_HEIGHT)
enemy_rect = enemy_image.get_rect()
x_speed, y_speed = 5,4


def bouncing_rect():
    global x_speed, y_speed
    enemy_rect.x += x_speed
    enemy_rect.y += y_speed

    if enemy_rect.right >= SCREEN_WIDTH or enemy_rect.left <= 0:
        x_speed *= -1
    if enemy_rect.bottom >= SCREEN_HEIGHT or enemy_rect.top <= 0:
        y_speed *= -1
    window.blit(enemy_image, enemy_rect)
    pygame.display.flip()


def main(window):
    """Main."""
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
        # window.blit(enemy_image, [SCREEN_WIDTH - enemy_image.get_width(), SCREEN_HEIGHT - enemy_image.get_height()])
        pygame.draw.rect(window, (255, 0, 255), floor)
        window.blit(enemy_image, enemy_rect)
        pygame.display.flip()

        bouncing_rect()

        # draw(window, background, bg_image)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)


# # Define floor parameters
# FLOOR_WIDTH, FLOOR_HEIGHT = SCREEN_WIDTH, 100
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
#     floor_x = (SCREEN_WIDTH - FLOOR_WIDTH) // 2
#     floor_y = SCREEN_HEIGHT - FLOOR_HEIGHT
#     window.blit(floor_surface, (floor_x, floor_y))

#     # Update the display
#     pygame.display.flip()
