import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

map_1 = """00000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000003333300
0000000000000000000000000333330
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000003333300
00000000000000000000000000000000
00000000000000000000000000000000
33333333333333333333333333333333
33333333333333333333333333333333"""


map_22 = """                                                                

                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                         22222222222222222222222                
                          111111111111111111111                
                            11111111111111111                  
                              1111111111111                    
                                111111111                          
                                111111111                
                                111111111                    
                               1111111111                      
                               1111111111                      
                               111111111                      
                               111111111                        
           22222222222         111111111                    2222
           11111111111           11111111                  21111
           11111111111          111111111                2211111
           11111111111         1111111111              221111111
           11111111111         11111111              22111111111
           11111111111         111111111          22211111111111
           11111111111         1111111111        211111111111111
2222222222211111111111222222222211111111122222222111111111111111
1111111111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111111111"""

map_3 = ""

airport_background = pygame.image.load("completed_airport_background.png")
airport_background = pygame.transform.scale(airport_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_2_background = pygame.image.load("map2_background.png")
map_2_background = pygame.transform.scale(map_2_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


map_3_background = pygame.image.load("map3_background.png")
map_3_background = pygame.transform.scale(map_3_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

map_4_background = pygame.image.load("map4_background.png")
map_4_background = pygame.transform.scale(map_4_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# screen, map background, map tiles, tile size, rpojectile starting coords, min angle, max angle
level_1_info = [airport_background, map_1, 40, [65, SCREEN_HEIGHT - 160], 0, 90]
level_2_info = [map_2_background, map_3, 20, [100, 300], 30, 90]
level_3_info = [map_3_background, map_3, 20, [145, 580], 30, 90]
level_4_info = [map_4_background, map_3, 20, [100, 250], 30, 90]
level_5_info = []
level_6_info = []
level_7_info = []
level_8_info = []
level_9_info = []
level_10_info = []

level_info = [level_1_info, level_2_info, level_3_info, level_4_info, level_5_info, level_6_info, level_7_info, level_8_info, level_9_info, level_10_info]