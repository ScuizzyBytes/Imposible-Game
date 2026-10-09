import pygame

CELL = 25

def create_snakes(screen, snake_body):
    for x, y in  snake_body:
        pygame.draw.rect(screen, (0, 255, 0), (x + 1, y + 1, CELL - 2, CELL - 2))
    
