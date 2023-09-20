import pygame, math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, map, screen, tile_size) -> None:
        super().__init__()
        self._start_x = start_x
        self._start_y = start_y
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        # self._rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.image_mask = pygame.mask.from_surface(self.image)
        self.background = background
        self.map = map
        self.screen = screen
        self.tile_size = tile_size

        self.gravity = -9.81
        self._shoot = False
        self._angle = 0
        self._speed = 0
        self.speeds = []
    
    @property
    def start_x(self):
        return self._start_x
    
    @property
    def start_y(self):
        return self._start_y

    @property
    def shoot(self):
        return self._shoot

    @property
    def angle(self):
        return self._angle

    @property
    def speed(self):
        return self._speed

    # @property
    # def rect(self):
    #     return self._rect

    def change_angle(self, change_in_angle):
        self._angle = change_in_angle
        # self._angle += change_in_angle if 0 <= self._angle + change_in_angle <= 90 else 0
        # pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def change_speed(self, change_in_speed):
        self._speed = change_in_speed
        # self._speed += change_in_speed if 0 <= self._speed + change_in_speed <= 150 else 0
        # pygame.display.set_caption(f"Angle: {self._angle} Speed: {self._speed}")

    def draw_starting_point(self):
        self.rect.centerx = self._start_x
        self.rect.centery = self._start_y
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()
 
    def trajectory(self, change_in_time, start_x, start_y, angle, speed):
        coordinates = []
        launch_time = 0
        y = self.start_y
        while y + (0.5 * self.size) <= SCREEN_HEIGHT:
            launch_time += change_in_time
            x = (start_x + (speed * math.cos(math.radians(angle)) * launch_time))
            y = (start_y - ((speed * math.sin(math.radians(angle)) * launch_time) + (0.5 * self.gravity * launch_time ** 2)))
            coordinates.append([x, y])
        return coordinates

    def draw_trajectory(self):
        coordinates = self.trajectory(1 / 10, self._start_x, self._start_y, self._angle, self._speed)
        run = True

        while run:
            for coords in coordinates:
                x = coords[0]
                y = coords[1]

                self.screen.blit(self.background, (0, 0))
                draw_tiles(self.map, self.tile_size)
                player_group.draw(self.screen)
                enemy_group.draw(self.screen)
                self.rect.centerx = x
                self.rect.centery = y
                self.screen.blit(self.image, (self.rect.x, self.rect.y))
                for enemy in enemy_group:
                    enemy.draw_health()
                current_player.draw_health()
                pygame.display.update()

                for tile in tile_rects:
                    if self.rect.colliderect(tile):
                        time.sleep(0.5)
                        run = False
                        break
                if (self.rect.centerx > SCREEN_WIDTH + 200 or
                    self.rect.centery > SCREEN_HEIGHT + 200):
                    time.sleep(0.5)
                    run = False
                    break

                # Use groupcollide() to detect collisions
                collisions = pygame.sprite.groupcollide(enemy_group, projectile_group,
                                                        False, False, pygame.sprite.collide_mask)

                # Handle collisions
                for enemy, projectiles in collisions.items():
                    print("Character hit by projectiles:", len(projectiles))
                    time.sleep(0.5)
                    deduct_enemy_health(enemy)
                    return False
                if not run:
                    break
            break
        return


class Enemy_Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, size, background, map, screen,
                 tile_size, angle, speed) -> None:
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.size = size
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size * 0.5,
                                                         self.size * 0.5))
        self._rect = self.image.get_rect()
        self.image_mask = pygame.mask.from_surface(self.image)

        self.background = background
        self.map = map
        self.screen = screen
        self.tile_size = tile_size

        self.gravity = -9.81
        self._shoot = False
        self._angle = angle
        self._speed = speed

    @property
    def shoot(self):
        return self._shoot

    @property
    def angle(self):
        return self._angle

    @property
    def speed(self):
        return self._speed

    @property
    def rect(self):
        return self._rect

    def draw_starting_point(self):
        # self.rect.x = self.start_x + 0.25 * self.size
        # self.rect.y = self.start_y + 0.25 * self.size
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.screen.blit(self.image, (self.start_x, self.start_y))
        pygame.display.update()

    def trajectory(self, change_in_time):
        coordinates = []
        launch_time = 0
        y = self.start_y
        while y + (0.5 * self.size) <= SCREEN_HEIGHT:
            launch_time += change_in_time
            x = (self.start_x + (self._speed * math.cos(math.radians(self._angle)) * launch_time))
            y = (self.start_y - ((self._speed * math.sin(math.radians(self._angle)) * launch_time) + (0.5 * self.gravity * launch_time ** 2)))
            coordinates.append([x, y])
        return coordinates

    def draw_trajectory(self):
        coordinates = self.trajectory(1 / 10)
        for coords in coordinates:
            x = coords[0]
            y = coords[1]

            self.screen.blit(self.background, (0, 0))
            draw_tiles(self.map, self.tile_size)
            # self.screen.blit(current_player.image, current_player.rect)
            player_group.draw(self.screen)
            enemy_group.draw(self.screen)
            for enemy in enemy_group:
                enemy.draw_health()
            current_player.draw_health()

            self.screen.blit(self.image, (x, y))
            self.rect.x = x
            self.rect.y = y
            pygame.display.update()

            for tile in tile_rects:
                if self.rect.colliderect(tile):
                    time.sleep(0.5)
                    print("HIT")
                    return False
            # Use groupcollide() to detect collisions
            collisions = pygame.sprite.groupcollide(player_group, enemy_projectile_group,
                                                    False, False, pygame.sprite.collide_mask)

            # Handle collisions
            for player, projectiles in collisions.items():
                # print("Character hit by projectiles:", len(projectiles))
                time.sleep(0.5)
                deduct_player_health(player)
                return False