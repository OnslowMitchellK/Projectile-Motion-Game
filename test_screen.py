import pygame
import os
from os import join

FPS = 60

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


def get_background(background_name):
    image = pygame.image.load(join("assets", "Background", background_name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(SCREEN_WIDTH // width + 1):
	    for j in range(SCREEN_HEIGHT // height + 1):
		    pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
	    window.blit(bg_image, tile)
	
    pygame.display.update()


def main(screen):
	clock = pygame.time.Clock()
    background, bg_image = get_background("background.jpg")

	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
				break
		
        draw(window, background, bg_image)
	pygame.quit()
	quit()


if __name__ == "__main__":
	main(window)