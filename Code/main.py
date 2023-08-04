##
# This youtubers guides were used for this program
# https://www.youtube.com/@CodingWithRuss

import pygame
FPS = 60

pygame.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


class Test_Character(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('Assets/test_slime.jpeg')
		# Rescaling the img of the character that appears on the screen
		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self):
		window.blit(self.image, self.rect)



player = Test_Character(200, 200, 5)
player2 = Test_Character(600, 600, 5)



run = True
while run:

	
	player.draw()
	player2.draw()

	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()

pygame.quit()
