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
        self._rect = pygame.Rect(x, y, width, height)
        self._rect.center = (x, y)
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


class Lockable_button(Button):
    def __init__(self, x, y, text, width=100, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
        super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
        pass

    def toggle_clickable(self):
        self.is_clickable = False if self.is_clickable else True
    
    def lock_button(self, screen, image):
        loaded_image = pygame.image.load(image)
        transfromed_image = pygame.transform.scale(loaded_image, (self.width * 0.8, self.height * 0.8))
        image_rect = transfromed_image.get_rect()
        image_rect.center = (self._rect.centerx, self._rect.centery)
        screen.blit(transfromed_image, (image_rect.x, image_rect.y))

class Upgrades_button(Lockable_button):
    def __init__(self, x, y, upgrade_image, upgrade_dict, text=None, width=300, height=150, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
        super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
        self.image = pygame.image.load(upgrade_image)
        self.name = list(upgrade_dict.keys())[0]
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(self.name, True, font_colour)
        self.description = upgrade_dict[self.name][0]
        self.price = upgrade_dict[self.name][1]
        self.mini_description = upgrade_dict[self.name][2]
        self.mini_font = pygame.font.SysFont(font, int(font_size / 2))
        self.mini_text = self.mini_font.render(self.mini_description, True, "red")
        self.price_font = pygame.font.SysFont(font, int(font_size / 2))
        self.price_text = self.price_font.render(f"${self.price}", True, "red")
        
    
    def display(self, screen):
        pygame.draw.rect(screen, self.background_colour, self._rect, self.outline, border_radius=self.border_radius)
        screen.blit(self.text, (self._rect.centerx - self.text.get_width() / 2, self._rect.centery - self.text.get_height() / 2))
        screen.blit(self.mini_text, (self._rect.centerx - self.mini_text.get_width() / 2, self._rect.centery + self.mini_text.get_height() * 1.3))
        screen.blit(self.price_text, (self._rect.centerx - self.price_text.get_width() / 2, self._rect.centery + self.price_text.get_height() * 3))
    
    def confirm_purchase(self, screen: pygame.Surface):
        rect = pygame.Rect(0, 0, 300, 300)
        rect.center = (640, self.y)
        pygame.draw.rect(screen, "white", rect)

# class Super_upgrades_button(Upgrades_button):
#     def __init__(self, x, y, upgrade_image, upgrade_dict, text=None, width=300, height=150, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
#         super().__init__(x, y, upgrade_image, upgrade_dict, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
#         pass

class Plus_button(Button):
    def __init__(self, x, y, text, levels_list, width=300, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
        super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
        self.levels_list = levels_list

    def add_level(self):
        count = 0
        for i in self.levels_list:
            if not i:
                self.levels_list[count] = True
                break
            count += 1
        return self.levels_list


class Level_completed_button(Button):
    def __init__(self, x, y, image, text="None", font="C:/Fonts/CroissantOne-Regular.ttf", font_size=20, font_colour=(255, 255, 255), width=50, height=50, background_colour=(252, 177, 3), outline=0, border_radius=25) -> None:
        super().__init__(x, y, text, width, height, font, font_size, font_colour,background_colour, outline, border_radius)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width * 0.6, height * 0.6))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, self._rect, self.outline, border_radius=self.border_radius)
        screen.blit(self.image, self.image_rect.topleft)

# class Collision_Button(Button):
#     def __init__(self, x, y, text, width=300, height=100, font="C:/Fonts/Barriecito-Regular.ttf", font_size=100, font_colour=(255, 255, 255), background_colour=(0, 0, 0), outline=0, border_radius=0) -> None:
#         super().__init__(x, y, text, width, height, font, font_size, font_colour, background_colour, outline, border_radius)
#         pass

