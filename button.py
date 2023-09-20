import pygame
pygame.init()

class Button:
    def __init__(self, x, y, text, width=300, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(text, True, font_colour)
        self.background_colour = background_colour
        self._rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.border_radius = border_radius
        self.outline = outline
        self.is_clickable = True

    def get_button_rect(self):
        return self._rect

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.background_colour, self._rect, self.outline, border_radius=self.border_radius)
        screen.blit(self.text, (self._rect.centerx - self.text.get_width() / 2, self._rect.centery - self.text.get_height() / 2))

    def is_pressed(self) -> bool:
        if self.is_clickable:
            pos = pygame.mouse.get_pos()
            return True if self._rect.collidepoint(pos[0], pos[1]) else False

    def toggle_clickable(self):
        self.is_clickable = False if self.is_clickable else True
<<<<<<< HEAD
    
    def lock_button(self, screen, image):
        loaded_image = pygame.image.load(image)
        transfromed_image = pygame.transform.scale(loaded_image, (self.width * 0.8, self.height * 0.8))
        image_rect = transfromed_image.get_rect()
        image_rect.center = (self._rect.centerx, self._rect.centery)
        screen.blit(transfromed_image, (image_rect.x, image_rect.y))
        

# class Collision_Button(Button):
#     def __init__(self, x, y, text, width=300, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
#         super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
#         pass

=======

    def lock_button(self, screen, image):
        loaded_image = pygame.image.load(image)
        transfromed_image = pygame.transform.scale(loaded_image, (self.width * 0.8, self.height * 0.8))
        image_rect = transfromed_image.get_rect()
        image_rect.center = (self._rect.centerx, self._rect.centery)
        screen.blit(transfromed_image, (image_rect.x, image_rect.y))


# class Collision_Button(Button):
#     def __init__(self, x, y, text, width=300, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
#         super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
#         pass
>>>>>>> origin/Ollie
