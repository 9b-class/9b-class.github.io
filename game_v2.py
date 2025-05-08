import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
zero = 0
FPS = 60
scale = 10
speed = scale / 10
player_color = (255, 0, 0)
player_rect = pygame.Rect(310 + scale, 210 + scale, 1 * scale, 1 * scale)

map_width = 37 * scale + scale
map_height = 25 * scale + scale
map_color = (0, 102, 0)
map_rect = pygame.Rect(305, 205, map_width, map_height)

obstacle_color = (0, 0, 255)
fill_color = (0, 0, 0)


obstacle = [[1, 25, 0, 0],
            [6, 1, 0, 0],
            [16, 1, 8, 0],
            [8, 1, 29, 0],
            [1, 25, 37-1, 0],
            [5, 1, 0, 24],
            [7, 1, 9, 24],
            [6, 1, 20, 24],
            [7, 1, 30, 24],
            [3, 9, 4, 8],
            [3, 5, 4, 17],
            [2.5, 1, 4.5, 22],
            [3, 5, 9, 3],
            [3,5, 9, 10],
            [3, 5, 9, 17],
            [3, 5, 14, 3],
            [3, 5, 14, 10],
            [3, 5, 14, 17],
            [3, 5, 19, 3],
            [3, 5, 19, 10], 
            [3, 5, 19, 17],
            [3, 5, 24, 3],
            [3, 5, 24, 10],
            [3, 5, 24, 17],
            [3, 5, 29, 3],
            [3, 5, 29, 10],
            [3, 5, 29, 17],
            [2, 15, 34, 5],
            [0.5, 1.5, 13, 3.5],
            [0.5, 1.5, 13, 6],
            [0.5, 1.5, 18, 3.5],
            [0.5, 1.5, 18, 6],
            [0.5, 1.5, 23, 3.5],
            [0.5, 1.5, 23, 6],
            [0.5, 1.5, 28, 3.5],
            [0.5, 1.5, 28, 6],
            [0.5, 1.5, 33, 3.5],
            [0.5, 1.5, 33, 6],
            [0.5, 1.5, 13, 10.5],
            [0.5, 1.5, 13, 13],
            [0.5, 1.5, 18, 10.5],
            [0.5, 1.5, 18, 13],
            [0.5, 1.5, 23, 10.5],
            [0.5, 1.5, 23, 13],
            [0.5, 1.5, 28, 10.5],
            [0.5, 1.5, 28, 13],
            [0.5, 1.5, 33, 10.5],
            [0.5, 1.5, 33, 13],
            [0.5, 1.5, 13, 17.5],
            [0.5, 1.5, 13, 20],
            [0.5, 1.5, 18, 17.5],
            [0.5, 1.5, 18, 20],
            [0.5, 1.5, 23, 17.5],
            [0.5, 1.5, 23, 20],
            [0.5, 1.5, 28, 17.5],
            [0.5, 1.5, 28, 20],
            [0.5, 1.5, 33, 17.5],
            [0.5, 1.5, 33, 20]

            
            ]

pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    def can_move(dx, dy):
        new_rect = player_rect.move(dx,dy)
        return not any(new_rect.colliderect(obstacle_func(rect)) for rect in range(len(obstacle)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map_rect.y < player_rect.y and can_move(0, -speed):
        map_rect.y += speed
    if keys[pygame.K_s] and map_rect.y > -map_height + player_rect.height + player_rect.y and can_move(0, speed):
        map_rect.y -= speed
    if keys[pygame.K_a] and map_rect.x < player_rect.x and can_move(-speed, 0):
        map_rect.x += speed
    if keys[pygame.K_d] and map_rect.x > -map_width + player_rect.width + player_rect.x and can_move(speed, 0):
        map_rect.x -= speed
    
    def obstacle_func(qatar):
        return pygame.Rect(map_rect.x + obstacle[qatar][2] * scale, map_rect.y + obstacle[qatar][3] * scale, obstacle[qatar][0] * scale, obstacle[qatar][1] * scale)
    
    screen.fill(fill_color)
    pygame.draw.rect(screen, map_color, map_rect)
    pygame.draw.rect(screen, player_color, player_rect)
    for rect in range(len(obstacle)):
        pygame.draw.rect(screen, obstacle_color, obstacle_func(rect))

    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()