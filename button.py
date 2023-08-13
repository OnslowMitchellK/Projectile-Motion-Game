import pygame
import time
pygame.init()

class Button:
    def __init__(self, x, y, width, height, image: pygame.Surface, text) -> None:
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.text = text
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #pygame.draw.rect(screen, "Yellow", self.rect)

    def is_pressed(self) -> bool:
        pos = pygame.mouse.get_pos()
        return True if self.rect.collidepoint(pos[0], pos[1]) else False