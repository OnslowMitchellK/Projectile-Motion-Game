class Main_Menu_Projectile:
    def __init__(self, image="test.png") -> None:
        self._image = pygame.image.load(image)
        size = randint(30, 40)
        self._image = pygame.transform.scale(self._image, (size, size))
        self._rect = self._image.get_rect()
        self._rect.x = randint(50, 300)
        self._rect.y = randint(50, SCREEN_HEIGHT - 50)
        self._dx = randint(4, 5)
        self._dy = randint(4, 5)

    @property
    def image(self):
        return self._image
    
    @property
    def dx(self):
        return self._dx
    
    @property
    def dy(self):
        return self._dy
    
    @property
    def rect_left(self) -> float:
        return self._rect.left
    
    @property
    def rect_right(self) -> float:
        return self._rect.right
    
    @property
    def rect_top(self) -> float:
        return self._rect.top
    
    @property
    def rect_bottom(self) -> float:
        return self._rect.bottom
    
    @property
    def rect(self):
        return self._rect
   
    @property
    def rect_x(self):
        return self._rect.x
    
    @property
    def rect_y(self):
        return self._rect.y
   
    def plus_x(self):
        self._rect.x += self._dx

    def plus_y(self):
        self._rect.y += self._dy

    def multiply_x(self, num):
        self._dx *= num

    def multiply_y(self, num):
        self._dy *= num
   
    def draw(self, screen):
        screen.blit(self._image, (self._rect.x, self._rect.y))