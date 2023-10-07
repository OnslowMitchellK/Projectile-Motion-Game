##
# This youtubers guides were used in this program
# https://www.youtube.com/@CodingWithRuss

import pygame

# framerate
clock = pygame.time.Clock()
FPS = 60

pygame.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Projectile Motion gmae')

# Movement variables
moving_left = False
moving_right = False

# Colour
BG = (215, 142, 32)

def draw_bg():
    screen.fill(BG)

class Image_Coords:
    def __init__(self, relative_x, relative_y) -> None:
        self._x = relative_x
        self._y = relative_y
    
    def x(self) -> float:
        return self._x
    
    def y(self) -> float:
        return self._y


aziz_1 = Image_Coords(0, 0)
aziz_2 = Image_Coords(0, 0)
aziz_3 = Image_Coords(0, 20)
aziz_4 = Image_Coords(0, 10)
aziz_5 = Image_Coords(0, -10)
aziz_6 = Image_Coords(0, -20)
aziz_7 = Image_Coords(0, 0)
aziz_8 = Image_Coords(0, 0)

aziz_images: dict[str, Image_Coords] = {
    "Aziz 1.png": aziz_1,
    "Aziz 2.png": aziz_2,
    "Aziz 3.png": aziz_3,
    "Aziz 4.png": aziz_4,
    "Aziz 5.png": aziz_5,
    "Aziz 6.png": aziz_6,
    "Aziz 7.png": aziz_7,
    "Aziz 8.png": aziz_8
}



class Test_Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'test_slime.jpeg')
        # Rescaling the img of the character that appears on the screen
        self.scale = scale
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.level_points = 0
        self.super_points = 0
        self.damage = 40
        self.max_health = 100
        self._health = 100
        self.screen = screen
        self.shield = 0
        self.current_image = list(aziz_images.keys())[0]

    @property
    def health(self) -> int:
        """Health getter."""
        return self._health

    @health.setter
    def health(self, new_health) -> int:
        """Healther setter."""
        if new_health < 0:
            self._health = 0
        elif new_health > self.max_health:
            self._health = self.max_health
        else:
            self._health = new_health

    def change_image(self):
        is_image = False
        for image in aziz_images.keys():
            if image == list(aziz_images.keys())[-1]:
                self.current_image = list(aziz_images.keys())[0]
                break
            elif is_image:
                self.current_image = image
                break
            elif self.current_image == image:
                is_image = True

        dx = aziz_images[self.current_image].x()
        dy = aziz_images[self.current_image].y()

        self.x += dx
        self.y += dy

        img = pygame.image.load(self.current_image)
        self.image = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))

    def move(self, moving_left, moving_right):
        # reset movement
        dx = 0
        dy = 0

        # left or right movement
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    # def draw(self):
    #     screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def die(self):
        self.kill()

    def draw_health(self):
        green_percent = int(self.health / (self.max_health / 100))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.5 * self.image.get_height()), 100, 5))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.5 * self.image.get_height()), green_percent, 5))
        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.53 * self.image.get_height()), self.shield, 5))


# class Upgrade(pygame.sprite.Sprite):
# 	def __init__(self, char_type, x, y, scale):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.char_type = char_type
# 		img = pygame.image.load(f'Assets/{char_type}/arrow.png')
# 		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
# 		self.rect = self.image.get_rect()
# 		self.rect.center = (x, y)

# 	def draw(self):
# 		screen.blit(self.image, self.rect)


# # character spawn location
# player = Test_Character('player', 200, 200, 3, 5)
# upgrade = Upgrade('upgrade', 400, 400, 0.5)




# run = True
# while run:

# 	clock.tick(FPS)

# 	draw_bg()

# 	player.draw()

# 	player.move(moving_left, moving_right)

# 	for event in pygame.event.get():
# 		# quit game
# 		if event.type == pygame.QUIT:
# 			run = False
# 		# keyboard input
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_a:
# 				moving_left = True
# 			if event.key == pygame.K_d:
# 				moving_right = True
# 			if event.key == pygame.K_ESCAPE:
# 				run = False


# 		# keyboard input released
# 		if event.type == pygame.KEYUP:
# 			if event.key == pygame.K_a:
# 				moving_left = False
# 			if event.key == pygame.K_d:
# 				moving_right = False

# 		pygame.display.update()

# pygame.quit()