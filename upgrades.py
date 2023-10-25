"""This is a file containing all the upgrades name, description and price."""

import pygame
from button import Plus_button

COST = 1

diamond_image = pygame.image.load("Assets/upgrades_images/diamond.png")
diamond_image = pygame.transform.scale(diamond_image, (20, 20))

coin_image = pygame.image.load("Assets/upgrades_images/coin.png")
coin_image = pygame.transform.scale(coin_image, (20, 20))


class Upgrade:
    def __init__(self, screen: pygame.Surface, x, y, image, title, cost, info_text, prices, levels=4, width=250, height=80, font_size=30, font="C:/Fonts/Barriecito-Regular.ttf", font_colour="white") -> None:
        self.screen = screen
        self.rect = pygame.Rect(0, 0, width, height)
        self.x = x
        self.y = y
        self.rect.center = (x, y)

        self.width = width
        self.height = height

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.font = pygame.font.SysFont(font, font_size)

        self.title = self.font.render(title, True, font_colour)
        self.cost = cost
        self.cost_list = [0 for i in range(cost)]

        self.levels = levels
        self.levels_list = [False for i in range(levels)]
        self.upgrade_circle = pygame.Rect(0, 0, 20, 20)

        self.plus_button = Plus_button(self.x + self.width / 2.8, self.y, "+", self.levels_list, 50, 50, font_size=50, font_colour="white", background_colour= "orange", border_radius=20)
        self.plus_button_outline = pygame.Rect(0, 0, 50, 50)
        self.plus_button_outline.center = (self.x + self.width / 2.8, self.y)

        self.info_font = pygame.font.SysFont(font, 12)
        self.info_text = self.info_font.render(info_text, True, "black")
        self.info_rect = pygame.Rect(0, 0, 200, 200)
        self.info_rect.center = (screen.get_width() / 2, screen.get_height() / 2)

        self.level_prices = prices

    def get_plus_button(self):
        return self.plus_button
    
    def display_info(self):
        pygame.draw.rect(self.screen, "white", self.info_rect)
        self.screen.blit(self.info_text, (self.screen.get_width() / 2, self.screen.get_height() / 2))

    def display_upgrade(self):
        self.screen.blit(self.title, (self.x - self.title.get_width() / 2, self.y - self.height * 0.8))
        pygame.draw.rect(self.screen, "#D4D4D4", self.rect, border_radius=30)
        self.screen.blit(self.image, (self.x - 120, self.y - self.image.get_height() / 2))
        self.display_dots()
        self.plus_button.draw(self.screen)
        pygame.draw.rect(self.screen, "#474747", self.plus_button_outline, 3, border_radius=20)
    
    def display_dots(self):
        count = 0
        for i in self.levels_list:
            self.upgrade_circle.center = ((self.x - 40  + 25 * count), self.y)
            colour = "red" if i else "grey"
            pygame.draw.rect(self.screen, colour, self.upgrade_circle, border_radius=10)
            pygame.draw.circle(self.screen, "#474747", ((self.x - 40  + 25 * count), self.y), 10, width=2)
            count += 1
    
    # def display_cost(self):
    #     count = 0
    #     for i in self.cost_list:
    #         self.screen.blit(coin_image, (self.x - 60  + 25 * count, self.y - 35))
    #         count += 1

    def display_cost(self):
        cost = self.get_price()
        if not cost:
            return
        count = 0
        for i in range(cost):
            self.screen.blit(coin_image, (self.x - 60  + 25 * count, self.y - 35))
            count += 1

    def get_level(self):
        return self.levels_list.count(1)

    def get_price(self):
        index = self.get_level()
        try:
            cost = self.level_prices[index]
        except Exception:
            return False
        return cost
    
    def deduct(self, level_points):
        new_points = level_points - self.get_price() if level_points - self.get_price() >= 0 else level_points
        bought = True if new_points != level_points else False
        return [bought, new_points]
    
    def reset_level(self):
        for i in range(len(self.levels_list)):
            self.levels_list[i] = 0


class Super_upgrade(Upgrade):
    def __init__(self, screen: pygame.Surface, x, y, image, title, cost, info_text, prices, levels=4, width=250, height=80, font_size=30, font="C:/Fonts/Barriecito-Regular.ttf", font_colour="white") -> None:
        super().__init__(screen, x, y, image, title, cost, info_text, prices, levels, width, height, font_size, font, font_colour)
        pass

    def display_cost(self):
        cost = self.get_price()
        if not cost:
            return
        count = 0
        for i in range(cost):
            self.screen.blit(diamond_image, (self.x - 60  + 25 * count, self.y - 35))
            count += 1