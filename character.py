##
# This youtubers guides were used in this program
# https://www.youtube.com/@CodingWithRuss

import pygame

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
aziz_3 = Image_Coords(0, 40)
aziz_4 = Image_Coords(0, 20)
aziz_5 = Image_Coords(0, -20)
aziz_6 = Image_Coords(0, -40)
aziz_7 = Image_Coords(0, 0)
aziz_8 = Image_Coords(0, 0)

file = "animations/Aziz Animations/"

aziz_images: dict[str, Image_Coords] = {
    f"{file}Aziz 1.png": aziz_1,
    f"{file}Aziz 2.png": aziz_2,
    f"{file}Aziz 3.png": aziz_3,
    f"{file}Aziz 4.png": aziz_4,
    f"{file}Aziz 5.png": aziz_5,
    f"{file}Aziz 6.png": aziz_6,
    f"{file}Aziz 7.png": aziz_7,
    f"{file}Aziz 8.png": aziz_8
}



class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'{file}Aziz 1.png')
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
    
    def get_image(self):
        return f"{self.current_image}"


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

        img = pygame.image.load(self.current_image)
        self.image = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))

    def die(self):
        self.kill()

    def draw_health(self):
        green_percent = int(self.health / (self.max_health / 100))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.5 * self.image.get_height()), 100, 5))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.5 * self.image.get_height()), green_percent, 5))
        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x - (self.image.get_width()/3), self.y - (0.53 * self.image.get_height()), self.shield, 5))

