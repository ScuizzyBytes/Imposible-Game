import pygame

from cubes import create_cubes
from create_snake import create_snakes

pygame.init()

CELL = 25
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imposible Game")

dx, dy = CELL, 0

running = True

snake_body = [(100, 100)]

clock = pygame.time.Clock()
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -CELL
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, CELL
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL, 0 
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL, 0

    head_x, head_y = snake_body[0]
    new_head = (head_x + dx, head_y + dy)
    snake_body.insert(0, new_head)     

    screen.fill((100, 100, 100))

    create_cubes(screen)

    create_snakes(screen, snake_body)

    pygame.display.flip()

    clock.tick(8)

pygame.QUIT()
