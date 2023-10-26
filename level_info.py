import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

map_1_background = pygame.image.load("Assets/map1/map1_background.png")
map_1_background = pygame.transform.scale(map_1_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_2_background = pygame.image.load("Assets/map2/map2_background.png")
map_2_background = pygame.transform.scale(map_2_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


map_3_background = pygame.image.load("Assets/map3/map3_background.png")
map_3_background = pygame.transform.scale(map_3_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_4_background = pygame.image.load("Assets/map4/map4_background.png")
map_4_background = pygame.transform.scale(map_4_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_5_background = pygame.image.load("Assets/map5/map5_background.png")
map_5_background = pygame.transform.scale(map_5_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# map background, projectile starting coords
level_1_info = [airport_background, [40, (SCREEN_HEIGHT - 180)]]
level_2_info = [map_2_background, [100, 300]]
level_3_info = [map_3_background, [145, 580]]
level_4_info = [map_4_background, [100, 250]]
level_5_info = [map_5_background, [100, 420]]

level_info = [level_1_info, level_2_info, level_3_info, level_4_info, level_5_info]