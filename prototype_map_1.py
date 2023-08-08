import pygame
pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

map_1 = """W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW
W  A W WWWWWAW  WAWW  W AA     W
AAAWWW          WWWAAAWW     WWW"""

img_1 = pygame.image.load("test.png")
img_2 = pygame.image.load("cannon.png")


def make_window(width: int, height:int, caption: str) -> pygame.Surface:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return win

def draw_tiles(map):
    game_map = map.split("\n")
    x = 0
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == "W":
                window.blit(img_1, (x * 40, y * 40))
            elif tile == "A":
                window.blit(img_2, (x * 40, y * 40))
            x += 1
        y += 1
                
        


def main():
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == pygame.K_SPACE:
                    draw_tiles(map_1)

    pygame.quit()
    

window = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Map")
main()
    