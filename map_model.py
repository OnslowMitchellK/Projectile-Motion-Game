import pygame


class Map_Masks(pygame.sprite.Sprite):
    """Enemy Class."""

    def __init__(self, image: str):
        """Enemy variables."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()