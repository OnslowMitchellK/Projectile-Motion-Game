import pygame
import sys
# from os import join

FPS = 60

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

# background_image = pygame.image.load("background.jpg")

# def get_background(background_name):
#     image = pygame.image.load(join("assets", "Background", background_name))
#     _, _, width, height = image.get_rect()
#     tiles = []
#     for i in range(SCREEN_WIDTH // width + 1):
# 	    for j in range(SCREEN_HEIGHT // height + 1):
# 		    pos = (i * width, j * height)
#             tiles.append(pos)
#     return tiles, image


# def draw(window, background, bg_image):
#     for tile in background:
# 	    window.blit(bg_image, tile)
	
#     pygame.display.update()


# def main(screen):
# 	clock = pygame.time.Clock()
#     # background, bg_image = get_background("background.jpg")

# 	run = True
# 	while run:
# 		clock.tick(FPS)
# 		for event in pygame.event.get():
# 			#quit game
# 			if event.type == pygame.QUIT:
# 				run = False
# 				break
# 		screen.blit(background_image, [0, 0])
# 		pygame.display.flip()
		
#         # draw(window, background, bg_image)
# 	pygame.quit()
# 	quit()


# if __name__ == "__main__":
# 	main(window)


# Define floor parameters
FLOOR_WIDTH, FLOOR_HEIGHT = SCREEN_WIDTH, 100
FLOOR_COLOR = (0, 128, 0)  # Green color (RGB)

# Create the floor surface
floor_surface = pygame.Surface((FLOOR_WIDTH, FLOOR_HEIGHT))
floor_surface.fill(FLOOR_COLOR)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    window.fill((255, 255, 255))  # White background color

    # Draw the floor at the bottom-center of the screen
    floor_x = (SCREEN_WIDTH - FLOOR_WIDTH) // 2
    floor_y = SCREEN_HEIGHT - FLOOR_HEIGHT
    window.blit(floor_surface, (floor_x, floor_y))

    # Update the display
    pygame.display.flip()